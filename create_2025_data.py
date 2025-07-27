#!/usr/bin/env python3
"""
ベストプレープロ野球2025年選手データ生成メインスクリプト
"""

import pandas as pd
import numpy as np
import re
from pathlib import Path

# データディレクトリの設定
DATA_DIR = Path(__file__).parent / "result"
OUTPUT_DIR = Path(__file__).parent / "data"

class PlayerDataGenerator:
    """選手データ生成クラス"""
    
    def __init__(self):
        self.data_2025 = self.load_2025_data()
        self.data_2024 = self.load_2024_data()
        self.reference_conversion = self.analyze_1999_2000_conversion()
        
    def load_2025_data(self):
        """2025年成績データを読み込み"""
        return {
            'batting': pd.read_csv(DATA_DIR / "npb_2025_batting_stats.csv", encoding="utf-8"),
            'pitching': pd.read_csv(DATA_DIR / "npb_2025_pitching_stats.csv", encoding="utf-8"),
            'fielding': pd.read_csv(DATA_DIR / "npb_2025_fielding_stats.csv", encoding="utf-8")
        }
    
    def load_2024_data(self):
        """2024年成績データを読み込み"""
        return {
            'batting': pd.read_csv(DATA_DIR / "npb_2024_batting_stats.csv", encoding="utf-8"),
            'pitching': pd.read_csv(DATA_DIR / "npb_2024_pitching_stats.csv", encoding="utf-8"),
            'fielding': pd.read_csv(DATA_DIR / "npb_2024_fielding_stats.csv", encoding="utf-8")
        }
    
    def analyze_1999_2000_conversion(self):
        """1999→2000年の変換パターンを分析（参考用）"""
        # 1999年データ
        batters_1999 = pd.read_csv(DATA_DIR / "npb_1999_batter.txt", sep="\t", encoding="utf-8")
        pitchers_1999 = pd.read_csv(DATA_DIR / "npb_1999_pitcher.txt", sep="\t", encoding="utf-8")
        
        # 2000年データからサンプル選手を抽出して比較パターンを作成
        sample_conversions = {
            # 打率から打撃指数への変換例
            'avg_to_batting_index': {
                0.369: 290,  # ローズ → 高打撃指数
                0.330: 270,  # 関川 → 中打撃指数
                0.315: 310,  # 高橋由伸 → 高打撃指数
                0.300: 280,  # 平均的
            },
            # HR数から長打力への変換例
            'hr_to_power': {
                37: 'A',   # ローズ
                34: 'A',   # 高橋由伸
                20: 'C',   # 中程度
                5: 'E',    # 低い
            }
        }
        
        return sample_conversions
    
    def calculate_batter_abilities(self, player_stats_2025, player_stats_2024=None):
        """野手の能力値を計算"""
        abilities = {}
        
        # 基本データ取得（NaN処理含む）
        avg_2025 = player_stats_2025.get('打率', 0.0)
        if pd.isna(avg_2025):
            avg_2025 = 0.0
        hr_2025 = player_stats_2025.get('本塁打', 0)
        if pd.isna(hr_2025):
            hr_2025 = 0
        rbi_2025 = player_stats_2025.get('打点', 0)
        if pd.isna(rbi_2025):
            rbi_2025 = 0
        sb_2025 = player_stats_2025.get('盗塁', 0)
        if pd.isna(sb_2025):
            sb_2025 = 0
        bb_2025 = player_stats_2025.get('四球', 0)
        if pd.isna(bb_2025):
            bb_2025 = 0
        so_2025 = player_stats_2025.get('三振', 0)
        if pd.isna(so_2025):
            so_2025 = 0
        
        # 打撃指数計算 (220-350, 平均270)
        base_index = 270
        if avg_2025 > 0.300:
            abilities['batting_index'] = min(350, base_index + int((avg_2025 - 0.270) * 300))
        elif avg_2025 > 0.250:
            abilities['batting_index'] = base_index + int((avg_2025 - 0.270) * 200)
        else:
            abilities['batting_index'] = max(220, base_index + int((avg_2025 - 0.270) * 200))
        
        # 長打力 (S/A/B/C/D/E)
        if hr_2025 >= 25:
            abilities['power'] = 'S'
        elif hr_2025 >= 20:
            abilities['power'] = 'A'
        elif hr_2025 >= 15:
            abilities['power'] = 'B'
        elif hr_2025 >= 10:
            abilities['power'] = 'C'
        elif hr_2025 >= 5:
            abilities['power'] = 'D'
        else:
            abilities['power'] = 'E'
        
        # 好打（バットコントロール）
        if avg_2025 >= 0.320:
            abilities['contact'] = 'S'
        elif avg_2025 >= 0.300:
            abilities['contact'] = 'A'
        elif avg_2025 >= 0.280:
            abilities['contact'] = 'B'
        elif avg_2025 >= 0.260:
            abilities['contact'] = 'C'
        elif avg_2025 >= 0.240:
            abilities['contact'] = 'D'
        else:
            abilities['contact'] = 'E'
        
        # 脚力（盗塁数ベース）
        if sb_2025 >= 20:
            abilities['speed'] = 'A'
        elif sb_2025 >= 15:
            abilities['speed'] = 'B'
        elif sb_2025 >= 10:
            abilities['speed'] = 'C'
        elif sb_2025 >= 5:
            abilities['speed'] = 'D'
        else:
            abilities['speed'] = 'E'
        
        # 選球眼（四球数ベース）
        if bb_2025 >= 60:
            abilities['discipline'] = 'A'
        elif bb_2025 >= 40:
            abilities['discipline'] = 'B'
        elif bb_2025 >= 25:
            abilities['discipline'] = 'C'
        elif bb_2025 >= 15:
            abilities['discipline'] = 'D'
        else:
            abilities['discipline'] = 'E'
        
        # その他の能力はデフォルト値
        abilities['arm'] = 'C'  # 肩（守備データから後で調整）
        abilities['experience'] = 'C'  # 実績
        abilities['stamina'] = 'C'  # スタミナ
        abilities['clutch'] = 0  # 信頼度
        abilities['vs_left'] = 0  # 対左
        
        return abilities
    
    def calculate_pitcher_abilities(self, player_stats_2025, player_stats_2024=None):
        """投手の能力値を計算"""
        abilities = {}
        
        # 基本データ取得（NaN処理含む）
        era_2025 = player_stats_2025.get('防御率', 4.00)
        if pd.isna(era_2025):
            era_2025 = 4.00
        wins_2025 = player_stats_2025.get('勝利', 0)
        if pd.isna(wins_2025):
            wins_2025 = 0
        saves_2025 = player_stats_2025.get('セ｜ブ', 0)
        if pd.isna(saves_2025):
            saves_2025 = 0
        strikeouts_2025 = player_stats_2025.get('三振', 0)
        if pd.isna(strikeouts_2025):
            strikeouts_2025 = 0
        walks_2025 = player_stats_2025.get('四球', 0)
        if pd.isna(walks_2025):
            walks_2025 = 0
        innings_2025 = player_stats_2025.get('投球回', 0)
        if pd.isna(innings_2025):
            innings_2025 = 0
        
        # 切れ（奪三振率ベース）
        if innings_2025 > 0:
            k_rate = (strikeouts_2025 / innings_2025) * 9
            if k_rate >= 10.0:
                abilities['stuff'] = 'S'
            elif k_rate >= 8.5:
                abilities['stuff'] = 'A'
            elif k_rate >= 7.0:
                abilities['stuff'] = 'B'
            elif k_rate >= 6.0:
                abilities['stuff'] = 'C'
            elif k_rate >= 5.0:
                abilities['stuff'] = 'D'
            else:
                abilities['stuff'] = 'E'
        else:
            abilities['stuff'] = 'C'
        
        # 制球（与四球率ベース）
        if innings_2025 > 0:
            bb_rate = (walks_2025 / innings_2025) * 9
            if bb_rate <= 2.0:
                abilities['control'] = 'A'
            elif bb_rate <= 3.0:
                abilities['control'] = 'B'
            elif bb_rate <= 4.0:
                abilities['control'] = 'C'
            elif bb_rate <= 5.0:
                abilities['control'] = 'D'
            else:
                abilities['control'] = 'E'
        else:
            abilities['control'] = 'C'
        
        # 安定性（防御率ベース）
        if era_2025 <= 2.50:
            abilities['stability'] = 'A'
        elif era_2025 <= 3.50:
            abilities['stability'] = 'B'
        elif era_2025 <= 4.50:
            abilities['stability'] = 'C'
        elif era_2025 <= 5.50:
            abilities['stability'] = 'D'
        else:
            abilities['stability'] = 'E'
        
        # 球速（平均的な設定、実際のデータが無いので推定）
        if strikeouts_2025 >= 100:
            abilities['velocity'] = 148  # 快速球
        elif strikeouts_2025 >= 80:
            abilities['velocity'] = 144
        elif strikeouts_2025 >= 60:
            abilities['velocity'] = 140
        elif strikeouts_2025 >= 40:
            abilities['velocity'] = 136
        else:
            abilities['velocity'] = 132
        
        # その他のデフォルト能力
        abilities['movement'] = 'C'  # 球質
        abilities['technique'] = 'C'  # 技術
        abilities['stamina'] = 'C'  # スタミナ
        abilities['recovery'] = 24  # 回復（平均値）
        
        return abilities
    
    def determine_player_type(self, player_stats):
        """選手タイプを決定"""
        # 野手のスプレー/パワータイプ
        hr = player_stats.get('本塁打', 0)
        doubles = player_stats.get('二塁打', 0)
        avg = player_stats.get('打率', 0.0)
        
        if hr >= 15 or (hr >= 10 and doubles <= 15):
            return 'P'  # パワーヒッター
        else:
            return 'S'  # スプレーヒッター
    
    def determine_batting_side(self, player_name):
        """打席を推定（実際のデータが無いのでランダムまたはデフォルト）"""
        # 実際の実装では選手データベースを参照
        # ここでは簡易的にランダム
        sides = ['R', 'L', 'B']
        return np.random.choice(sides, p=[0.7, 0.25, 0.05])  # 右打者多め
    
    def generate_team_data(self):
        """全チームのデータを生成"""
        print("2025年選手データ生成開始...")
        
        # チームごとに処理
        teams = self.data_2025['batting']['球団'].unique()
        all_team_data = {}
        
        for team in teams:
            if pd.isna(team):
                continue
                
            print(f"\n=== {team} ===")
            team_data = self.generate_single_team_data(team)
            all_team_data[team] = team_data
        
        return all_team_data
    
    def generate_single_team_data(self, team_name):
        """単一チームのデータを生成"""
        # そのチームの選手データを抽出
        team_batters = self.data_2025['batting'][
            self.data_2025['batting']['球団'] == team_name
        ]
        team_pitchers = self.data_2025['pitching'][
            self.data_2025['pitching']['球団'] == team_name
        ]
        
        team_data = {
            'batters': [],
            'pitchers': []
        }
        
        # 野手データ生成
        for _, batter in team_batters.iterrows():
            player_name = batter['選　手']
            if pd.isna(player_name) or player_name.startswith('【'):
                continue
                
            abilities = self.calculate_batter_abilities(batter)
            player_type = self.determine_player_type(batter)
            batting_side = self.determine_batting_side(player_name)
            
            player_data = {
                'name': player_name.strip('*'),
                'batting_side': batting_side,
                'type': player_type,
                'abilities': abilities
            }
            team_data['batters'].append(player_data)
            
        # 投手データ生成  
        for _, pitcher in team_pitchers.iterrows():
            player_name = pitcher['投　手']
            if pd.isna(player_name) or player_name.startswith('【'):
                continue
                
            abilities = self.calculate_pitcher_abilities(pitcher)
            
            player_data = {
                'name': player_name.strip('*'),
                'abilities': abilities
            }
            team_data['pitchers'].append(player_data)
        
        print(f"野手: {len(team_data['batters'])}名, 投手: {len(team_data['pitchers'])}名")
        return team_data
    
    def export_team_data_format(self, all_teams, output_file="teamdata_2025.txt"):
        """teamdata_2000.txt形式でデータを出力"""
        output_path = OUTPUT_DIR / output_file
        
        # チーム名マッピング（日本語→略称）
        team_mapping = {
            '読売ジャイアンツ': {'name': 'ヨミウリジャイアンツ', 'symbol': 'giants', 'uniform': 'G_h G_v'},
            '阪神タイガース': {'name': 'ハンシンタイガース', 'symbol': 'tigers', 'uniform': 'T_h T_v'},
            '横浜DeNAベイスターズ': {'name': 'ヨコハマベイスターズ', 'symbol': 'baystars', 'uniform': 'Y_h Y_v'},
            '広島東洋カープ': {'name': 'ヒロシマカープ', 'symbol': 'carp', 'uniform': 'C_h C_v'},
            '東京ヤクルトスワローズ': {'name': 'ヤクルトスワローズ', 'symbol': 'swallows', 'uniform': 'S_h S_v'},
            '中日ドラゴンズ': {'name': 'チュウニチドラゴンズ', 'symbol': 'dragons', 'uniform': 'D_h D_v'},
            '福岡ソフトバンクホークス': {'name': 'ソフトバンクホークス', 'symbol': 'hawks', 'uniform': 'H_h H_v'},
            '北海道日本ハムファイターズ': {'name': 'ニッポンハムファイターズ', 'symbol': 'fighters', 'uniform': 'F_h F_v'},
            '千葉ロッテマリーンズ': {'name': 'ロッテマリーンズ', 'symbol': 'marines', 'uniform': 'M_h M_v'},
            '東北楽天ゴールデンイーグルス': {'name': 'ラクテンイーグルス', 'symbol': 'eagles', 'uniform': 'E_h E_v'},
            'オリックス・バファローズ': {'name': 'オリックスバファローズ', 'symbol': 'buffaloes', 'uniform': 'B_h B_v'},
            '埼玉西武ライオンズ': {'name': 'セイブライオンズ', 'symbol': 'lions', 'uniform': 'L_h L_v'},
        }
        
        with open(output_path, 'w', encoding='cp932', errors='ignore') as f:
            f.write(";--------------------------------------------------------------------\n")
            f.write("; 2025年ベストプレープロ野球選手データ\n")
            f.write("; 自動生成版\n")
            f.write("\n")
            
            for team_name, team_data in all_teams.items():
                if team_name not in team_mapping:
                    continue
                    
                team_info = team_mapping[team_name]
                
                f.write(";--------------------------------------------------------------------\n")
                f.write(f"; チーム名                  略称         記    BGM\n")
                f.write(f"  {team_info['name']:<20} {team_info['symbol']:<10} {team_info['symbol'][0]} {team_info['symbol']}\n")
                f.write("\n")
                f.write("; UNIFORM                   SYMBOL       BGM\n")
                f.write(f"  {team_info['uniform']:<20} {team_info['symbol']:<10} {team_info['symbol']}\n")
                f.write("\n")
                f.write("; 特徴             打 走 守 機 盗 足 絡 守 幸\n")
                f.write("  平均             0  0  0  0  0  0  0  0  0\n")
                f.write("\n")
                f.write("; 選手             打 打 C 1 2 3 S O 肩 脚 眼 実 ス 好 長 信 対 打撃\n")
                
                # 野手データ出力
                for i, batter in enumerate(team_data['batters'][:25], 1):  # 最大25名
                    name = batter['name'][:8]  # 名前は8文字まで
                    batting_side = batter['batting_side']
                    player_type = batter['type']
                    abilities = batter['abilities']
                    
                    # 守備位置（仮想的に設定）
                    positions = ['-', '-', '-', '-', '-', '-']  # C,1,2,3,S,O
                    
                    f.write(f"{i:2d} {name:<15} {batting_side}  {player_type}  "
                           f"{' '.join(positions)}  "
                           f"{abilities['arm']}  {abilities['speed']}  {abilities['discipline']}  "
                           f"{abilities['experience']}  {abilities['stamina']}  "
                           f"{abilities['contact']}  {abilities['power']}  "
                           f"{abilities['clutch']:+2d} {abilities['vs_left']:+2d}  "
                           f"{abilities['batting_index']}\n")
                
                f.write("\n")
                f.write("; 投手             投 型 球速 切 制 安 球 技 ス  回 年俸\n")
                
                # 投手データ出力
                for pitcher in team_data['pitchers']:
                    name = pitcher['name'][:8]
                    abilities = pitcher['abilities']
                    
                    # 投手タイプ（簡易設定）
                    pitcher_type = 'R'
                    pitcher_grade = 'C'
                    
                    f.write(f"P {name:<15} {pitcher_type}  {pitcher_grade}   "
                           f"{abilities['velocity']:3d}  "
                           f"{abilities['stuff']}  {abilities['control']}  {abilities['stability']}  "
                           f"{abilities['movement']}  {abilities['technique']}  {abilities['stamina']}  "
                           f"{abilities['recovery']:2d}  200\n")
                
                f.write("\n")
        
        print(f"データファイル出力完了: {output_path}")
        return output_path

def main():
    """メイン処理"""
    generator = PlayerDataGenerator()
    all_teams = generator.generate_team_data()
    
    print(f"\n生成完了: {len(all_teams)}チーム")
    
    # データファイル出力
    output_file = generator.export_team_data_format(all_teams)
    
    # サンプル出力
    for team_name, team_data in list(all_teams.items())[:2]:
        print(f"\n=== {team_name} サンプル ===")
        if team_data['batters']:
            batter = team_data['batters'][0]
            print(f"野手例: {batter['name']} ({batter['batting_side']}/{batter['type']}) "
                  f"打撃指数={batter['abilities']['batting_index']}")
        if team_data['pitchers']:
            pitcher = team_data['pitchers'][0]
            print(f"投手例: {pitcher['name']} "
                  f"球速={pitcher['abilities']['velocity']}")
    
    print(f"\n2025年選手データファイル: {output_file}")
    return output_file

if __name__ == "__main__":
    main()