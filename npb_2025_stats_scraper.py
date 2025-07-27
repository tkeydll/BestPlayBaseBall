#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NPB 2025年度球団別個人成績取得スクリプト
セリーグ・パリーグ全12球団の打撃・投手・守備成績をCSVで保存
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
from urllib.parse import urljoin

# NPBの球団コードとチーム名のマッピング
TEAMS = {
    # セントラル・リーグ
    'g': '読売ジャイアンツ',
    't': '阪神タイガース', 
    'db': '横浜DeNAベイスターズ',
    'c': '広島東洋カープ',
    's': '東京ヤクルトスワローズ',
    'd': '中日ドラゴンズ',
    # パシフィック・リーグ
    'h': '福岡ソフトバンクホークス',
    'f': '北海道日本ハムファイターズ',
    'm': '千葉ロッテマリーンズ',
    'e': '東北楽天ゴールデンイーグルス',
    'b': 'オリックス・バファローズ',
    'l': '埼玉西武ライオンズ'
}

# 成績の種類
STATS_TYPES = {
    'bat': '打撃成績',
    'pit': '投手成績', 
    'fld': '守備成績'
}

BASE_URL = 'https://npb.jp/bis/2025/stats/'

def get_page_content(url):
    """Webページのコンテンツを取得"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"❌ ページ取得エラー: {url} - {e}")
        return None

def parse_stats_table(html_content, team_name, stats_type):
    """統計テーブルを解析してDataFrameに変換"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # データ行を検索（<tr>タグを直接探す）
    rows = []
    all_trs = soup.find_all('tr')
    
    # ヘッダー候補を探す（複数パターンを試す）
    headers = []
    header_found = False
    
    for tr in all_trs:
        cells = tr.find_all(['td', 'th'])
        if not cells:
            continue
            
        row_data = [cell.get_text(strip=True) for cell in cells]
        
        # ヘッダー行を特定（選手名が含まれていない行）
        if not header_found and len(row_data) > 5:
            # ヘッダー候補を設定
            if not headers:
                # 統計項目名が含まれているかチェック
                if any(item in str(row_data) for item in ['打率', '本塁打', '防御率', '勝', '守備率', '失策']):
                    headers = row_data
                    header_found = True
                    continue
                elif '選手名' in str(row_data) or '打席' in str(row_data) or '試合' in str(row_data):
                    headers = row_data
                    header_found = True
                    continue
        
        # データ行の処理（ヘッダーが見つかった後）
        if header_found and len(row_data) >= 5:
            # 選手データと思われる行を追加（空行や区切り行をスキップ）
            if row_data[0] and not all(cell == '' or cell == '-' for cell in row_data):
                rows.append(row_data)
    
    # ヘッダーが見つからない場合、デフォルトヘッダーを使用
    if not headers:
        if stats_type == 'bat':
            headers = ['選手名', '試合', '打席', '打数', '得点', '安打', '二塁打', '三塁打', '本塁打', 
                      '塁打', '打点', '盗塁', '盗塁死', '犠打', '犠飛', '四球', '敬遠', '死球', 
                      '三振', '併殺打', '打率', '長打率', '出塁率']
        elif stats_type == 'pit':
            headers = ['選手名', '試合', '勝', '敗', 'セーブ', 'ホールド', '完投', '完封', '無四球', 
                      '投球回', '打者', '被安打', '被本塁打', '与四球', '敬遠', '与死球', '奪三振', 
                      '暴投', 'ボーク', '失点', '自責点', '防御率', 'WHIP', '被打率']
        else:  # fld
            headers = ['選手名', '試合', 'イニング', '守備機会', '刺殺', '補殺', '失策', '併殺', 
                      '守備率', 'RF', 'PB', 'SB', 'CS', '盗塁阻止率']
    
    if not rows:
        print(f"⚠️ {team_name}の{STATS_TYPES[stats_type]}データが見つかりませんでした")
        return None
    
    # 行の長さを調整（ヘッダーと合わせる）
    max_cols = max(len(headers), max(len(row) for row in rows) if rows else 0)
    
    # ヘッダーの長さを調整
    while len(headers) < max_cols:
        headers.append(f'列{len(headers)+1}')
    
    # データ行の長さを調整
    adjusted_rows = []
    for row in rows:
        while len(row) < len(headers):
            row.append('')
        adjusted_rows.append(row[:len(headers)])  # 余分な列を削除
    
    if not adjusted_rows:
        print(f"⚠️ {team_name}の{STATS_TYPES[stats_type]}データが見つかりませんでした")
        return None
    
    # DataFrameを作成
    df = pd.DataFrame(adjusted_rows, columns=headers)
    df['球団'] = team_name
    df['成績種別'] = STATS_TYPES[stats_type]
    
    return df

def scrape_all_teams():
    """全12球団の成績を取得"""
    all_data = {
        'batting': [],
        'pitching': [],
        'fielding': []
    }
    
    print("🚀 NPB 2025年度球団別個人成績の取得を開始するよ〜")
    print(f"📊 対象: {len(TEAMS)}球団 × {len(STATS_TYPES)}種類 = {len(TEAMS) * len(STATS_TYPES)}ページ")
    
    for team_code, team_name in TEAMS.items():
        print(f"\n⚾ {team_name}の成績を取得中...")
        
        for stats_code, stats_name in STATS_TYPES.items():
            # URLを構築（例: idb1_g.html for 巨人の打撃成績）
            if stats_code == 'bat':
                url_pattern = f'idb1_{team_code}.html'
            elif stats_code == 'pit':
                url_pattern = f'idp1_{team_code}.html'
            else:  # fld
                url_pattern = f'idf1_{team_code}.html'
            
            url = urljoin(BASE_URL, url_pattern)
            print(f"  📈 {stats_name}: {url}")
            
            # ページ取得
            html_content = get_page_content(url)
            if html_content:
                # データ解析
                df = parse_stats_table(html_content, team_name, stats_code)
                if df is not None and not df.empty:
                    if stats_code == 'bat':
                        all_data['batting'].append(df)
                    elif stats_code == 'pit':
                        all_data['pitching'].append(df)
                    else:  # fld
                        all_data['fielding'].append(df)
                    print(f"    ✅ {len(df)}選手のデータを取得")
                else:
                    print(f"    ❌ データの取得に失敗")
            
            # サーバーに負荷をかけないよう待機
            time.sleep(1)
    
    return all_data

def save_to_csv(all_data):
    """取得したデータをCSVファイルに保存"""
    output_dir = "c:\\Users\\tkeyd\\git\\BestPlayBaseBall\\result"
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\n💾 CSVファイルの保存開始...")
    
    for stats_type, data_list in all_data.items():
        if data_list:
            # 全データを結合
            combined_df = pd.concat(data_list, ignore_index=True)
            
            # ファイル名を設定
            filename = f"npb_2025_{stats_type}_stats.csv"
            filepath = os.path.join(output_dir, filename)
            
            # CSV保存
            combined_df.to_csv(filepath, index=False, encoding='utf-8-sig')
            
            print(f"  📁 {filename}: {len(combined_df)}行のデータを保存")
            print(f"    パス: {filepath}")
        else:
            print(f"  ⚠️ {stats_type}のデータが見つかりませんでした")

def main():
    """メイン実行関数"""
    print("🎯 NPB 2025年度球団別個人成績取得ツール")
    print("=" * 50)
    
    # 全球団の成績を取得
    all_data = scrape_all_teams()
    
    # CSVファイルに保存
    save_to_csv(all_data)
    
    print("\n🎉 全ての処理が完了しました！")
    print("📊 取得されたCSVファイルをresultフォルダで確認してね〜")

if __name__ == "__main__":
    main()
