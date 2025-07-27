#!/usr/bin/env python3
"""
ベストプレープロ野球2025年選手データ生成
データ分析・変換スクリプト
"""

import pandas as pd
import numpy as np
import re
from pathlib import Path

# データディレクトリの設定
DATA_DIR = Path(__file__).parent / "result"
OUTPUT_DIR = Path(__file__).parent / "data"

def load_1999_data():
    """1999年成績データを読み込み（参考用）"""
    # 野手データ
    batters_1999 = pd.read_csv(
        DATA_DIR / "npb_1999_batter.txt", 
        sep="\t", 
        encoding="utf-8"
    )
    
    # 投手データ  
    pitchers_1999 = pd.read_csv(
        DATA_DIR / "npb_1999_pitcher.txt",
        sep="\t",
        encoding="utf-8"
    )
    
    print("=== 1999年データ構造 ===")
    print("野手カラム:", batters_1999.columns.tolist())
    print("投手カラム:", pitchers_1999.columns.tolist())
    print(f"野手数: {len(batters_1999)}, 投手数: {len(pitchers_1999)}")
    
    return batters_1999, pitchers_1999

def load_2024_2025_data():
    """2024年・2025年成績データを読み込み"""
    # 2025年データ
    batting_2025 = pd.read_csv(DATA_DIR / "npb_2025_batting_stats.csv", encoding="utf-8")
    pitching_2025 = pd.read_csv(DATA_DIR / "npb_2025_pitching_stats.csv", encoding="utf-8")
    fielding_2025 = pd.read_csv(DATA_DIR / "npb_2025_fielding_stats.csv", encoding="utf-8")
    
    # 2024年データ
    batting_2024 = pd.read_csv(DATA_DIR / "npb_2024_batting_stats.csv", encoding="utf-8")
    pitching_2024 = pd.read_csv(DATA_DIR / "npb_2024_pitching_stats.csv", encoding="utf-8")
    fielding_2024 = pd.read_csv(DATA_DIR / "npb_2024_fielding_stats.csv", encoding="utf-8")
    
    print("=== 2024-2025年データ構造 ===")
    print("2025年打撃:", batting_2025.columns.tolist())
    print("2025年投手:", pitching_2025.columns.tolist())
    print("2025年守備:", fielding_2025.columns.tolist())
    
    return {
        '2025': {'batting': batting_2025, 'pitching': pitching_2025, 'fielding': fielding_2025},
        '2024': {'batting': batting_2024, 'pitching': pitching_2024, 'fielding': fielding_2024}
    }

def analyze_2000_data():
    """2000年のチームデータ形式を分析"""
    # 複数のエンコーディングを試行
    encodings = ['shift_jis', 'cp932', 'utf-8', 'euc-jp']
    content = None
    
    for encoding in encodings:
        try:
            with open(OUTPUT_DIR / "teamdata_2000.txt", "r", encoding=encoding) as f:
                content = f.read()
            print(f"エンコーディング {encoding} で読み込み成功")
            break
        except UnicodeDecodeError:
            continue
    
    if content is None:
        # バイナリモードで読んで問題箇所を特定
        with open(OUTPUT_DIR / "teamdata_2000.txt", "rb") as f:
            raw_content = f.read()
        print("エンコーディング自動判定を試行")
        content = raw_content.decode('utf-8', errors='ignore')
    
    print("=== 2000年データ形式分析 ===")
    
    # チーム区切りを探す
    teams = content.split(';--------------------------------------------------------------------')
    print(f"チーム数: {len(teams) - 1}")  # 最初の空行を除く
    
    # 野手データのパターンを分析
    lines = content.split('\n')
    player_lines = [line for line in lines if line and not line.startswith(';') and not line.startswith(' ')]
    
    # サンプル野手行を分析
    batter_samples = []
    pitcher_samples = []
    
    for line in player_lines[:20]:  # 最初の20行をサンプル
        if line.startswith('P '):
            pitcher_samples.append(line)
        elif len(line.split()) > 10:  # 野手っぽい行
            batter_samples.append(line)
    
    print("野手データサンプル:")
    for sample in batter_samples[:3]:
        print(f"  {sample}")
    
    print("投手データサンプル:")  
    for sample in pitcher_samples[:3]:
        print(f"  {sample}")
    
    return content

def main():
    """メイン分析処理"""
    print("ベストプレープロ野球 データ分析開始")
    print("=" * 50)
    
    # 各年代のデータを読み込み・分析
    batters_1999, pitchers_1999 = load_1999_data()
    data_2024_2025 = load_2024_2025_data()
    teamdata_2000 = analyze_2000_data()
    
    # 基本統計
    print("\n=== 基本統計 ===")
    print("1999年野手平均打率:", batters_1999['打率'].mean())
    print("1999年野手平均HR:", batters_1999['本塁打'].mean())
    print("2025年野手平均打率:", data_2024_2025['2025']['batting']['打率'].mean())
    
    print("\n分析完了")

if __name__ == "__main__":
    main()