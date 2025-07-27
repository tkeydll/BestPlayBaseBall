#!/usr/bin/env python3
"""
2025年選手データの品質向上スクリプト
より詳細な能力値算出とリアルな設定を適用
"""

import pandas as pd
import numpy as np
from pathlib import Path

class EnhancedPlayerDataGenerator:
    """強化版選手データ生成クラス"""
    
    def __init__(self):
        self.data_2025 = self.load_2025_data()
        self.data_2024 = self.load_2024_data()
        
        # 実在選手の打席・投手タイプ辞書（一部例）
        self.player_batting_sides = {
            '村上宗隆': 'L', '山田哲人': 'R', '塩見泰隆': 'L', '大山悠輔': 'R',
            '佐藤輝明': 'L', '近本光司': 'L', '森下翔太': 'R', '岡本和真': 'R',
            '門脇誠': 'R', '秋広優人': 'R', '松井雅人': 'R', 'オスナ': 'R',
            'バウアー': 'R', '村上頌樹': 'L', '森下暢仁': 'R', '大瀬良大地': 'R'
        }
        
        self.pitcher_types = {
            'バウアー': {'hand': 'R', 'grade': 'A+'}, 
            '森下暢仁': {'hand': 'R', 'grade': 'A'},
            '大瀬良大地': {'hand': 'R', 'grade': 'B+'},
            '村上頌樹': {'hand': 'L', 'grade': 'B'},
            '青柳晃洋': {'hand': 'L', 'grade': 'B+'},
            '藤浪晋太郎': {'hand': 'R', 'grade': 'B'},
        }
    
    def load_2025_data(self):
        """2025年成績データを読み込み"""
        data_dir = Path(__file__).parent / "result"
        return {
            'batting': pd.read_csv(data_dir / "npb_2025_batting_stats.csv", encoding="utf-8"),
            'pitching': pd.read_csv(data_dir / "npb_2025_pitching_stats.csv", encoding="utf-8"),
            'fielding': pd.read_csv(data_dir / "npb_2025_fielding_stats.csv", encoding="utf-8")
        }
    
    def load_2024_data(self):
        """2024年成績データを読み込み"""
        data_dir = Path(__file__).parent / "result"
        return {
            'batting': pd.read_csv(data_dir / "npb_2024_batting_stats.csv", encoding="utf-8"),
            'pitching': pd.read_csv(data_dir / "npb_2024_pitching_stats.csv", encoding="utf-8"),
            'fielding': pd.read_csv(data_dir / "npb_2024_fielding_stats.csv", encoding="utf-8")
        }
    
    def enhanced_batter_abilities(self, player_stats_2025, player_name):
        """強化版野手能力算出"""
        abilities = {}
        
        # 基本データ（NaN処理含む）
        def safe_get(val, default=0):
            if pd.isna(val):
                return default
            if isinstance(val, str):
                try:
                    return float(val) if '.' in val else int(val)
                except:
                    return default
            return val
        
        avg_2025 = safe_get(player_stats_2025.get('打率', 0.0), 0.0)
        hr_2025 = safe_get(player_stats_2025.get('本塁打', 0), 0)
        rbi_2025 = safe_get(player_stats_2025.get('打点', 0), 0)
        sb_2025 = safe_get(player_stats_2025.get('盗塁', 0), 0)
        bb_2025 = safe_get(player_stats_2025.get('四球', 0), 0)
        so_2025 = safe_get(player_stats_2025.get('三振', 0), 0)
        games_2025 = safe_get(player_stats_2025.get('試合', 0), 0)
        pa_2025 = safe_get(player_stats_2025.get('打席', 0), 0)
        
        # より精密な打撃指数計算
        base_index = 270
        
        if avg_2025 >= 0.350:
            abilities['batting_index'] = 350
        elif avg_2025 >= 0.320:
            abilities['batting_index'] = 320 + int((avg_2025 - 0.320) * 1000)
        elif avg_2025 >= 0.300:
            abilities['batting_index'] = 300 + int((avg_2025 - 0.300) * 1000)
        elif avg_2025 >= 0.280:
            abilities['batting_index'] = 280 + int((avg_2025 - 0.280) * 1000)
        elif avg_2025 >= 0.250:
            abilities['batting_index'] = 250 + int((avg_2025 - 0.250) * 1000)
        else:
            abilities['batting_index'] = max(220, 220 + int((avg_2025 - 0.220) * 1000))
        
        # 丸め処理（10の倍数）
        abilities['batting_index'] = round(abilities['batting_index'] / 10) * 10
        abilities['batting_index'] = max(220, min(350, abilities['batting_index']))
        
        # 長打力（HR + RBI + 出場機会を考慮）
        power_score = hr_2025 * 2 + (rbi_2025 / max(games_2025, 1)) * 10
        if power_score >= 50:
            abilities['power'] = 'S'
        elif power_score >= 35:
            abilities['power'] = 'A'
        elif power_score >= 25:
            abilities['power'] = 'B'
        elif power_score >= 15:
            abilities['power'] = 'C'
        elif power_score >= 8:
            abilities['power'] = 'D'
        else:
            abilities['power'] = 'E'
        
        # バットコントロール（三振率を考慮）
        contact_rate = 1.0 - (so_2025 / max(pa_2025, 1)) if pa_2025 > 0 else 0.7
        if contact_rate >= 0.90:
            abilities['contact'] = 'S'
        elif contact_rate >= 0.85:
            abilities['contact'] = 'A'
        elif contact_rate >= 0.80:
            abilities['contact'] = 'B'
        elif contact_rate >= 0.75:
            abilities['contact'] = 'C'
        elif contact_rate >= 0.70:
            abilities['contact'] = 'D'
        else:
            abilities['contact'] = 'E'
        
        # 脚力（盗塁数と出場数考慮）
        speed_score = sb_2025 + (sb_2025 / max(games_2025, 1)) * 5
        if speed_score >= 25:
            abilities['speed'] = 'S'
        elif speed_score >= 18:
            abilities['speed'] = 'A'
        elif speed_score >= 12:
            abilities['speed'] = 'B'
        elif speed_score >= 6:
            abilities['speed'] = 'C'
        elif speed_score >= 3:
            abilities['speed'] = 'D'
        else:
            abilities['speed'] = 'E'
        
        # 選球眼（四球率）
        discipline_rate = bb_2025 / max(pa_2025, 1) if pa_2025 > 0 else 0.05
        if discipline_rate >= 0.15:
            abilities['discipline'] = 'A'
        elif discipline_rate >= 0.12:
            abilities['discipline'] = 'B'
        elif discipline_rate >= 0.08:
            abilities['discipline'] = 'C'
        elif discipline_rate >= 0.05:
            abilities['discipline'] = 'D'
        else:
            abilities['discipline'] = 'E'
        
        # 実績（出場数・安定性）
        if games_2025 >= 120:
            abilities['experience'] = 'A'
        elif games_2025 >= 100:
            abilities['experience'] = 'B'
        elif games_2025 >= 80:
            abilities['experience'] = 'C'
        elif games_2025 >= 50:
            abilities['experience'] = 'D'
        else:
            abilities['experience'] = 'E'
        
        # デフォルト値
        abilities['arm'] = 'C'
        abilities['stamina'] = 'C'
        abilities['clutch'] = 0
        abilities['vs_left'] = 0
        
        # 特別な選手の調整
        if '村上宗隆' in player_name:
            abilities['power'] = 'S'
            abilities['batting_index'] = max(abilities['batting_index'], 320)
            abilities['clutch'] = 2
        elif '山田哲人' in player_name:
            abilities['power'] = 'A'
            abilities['speed'] = 'A'
            abilities['experience'] = 'S'
        elif '岡本和真' in player_name:
            abilities['power'] = 'S'
            abilities['batting_index'] = max(abilities['batting_index'], 310)
        
        return abilities
    
    def enhanced_pitcher_abilities(self, player_stats_2025, player_name):
        """強化版投手能力算出"""
        abilities = {}
        
        def safe_get(val, default=0):
            if pd.isna(val):
                return default
            if isinstance(val, str):
                try:
                    return float(val) if '.' in val else int(val)
                except:
                    return default
            return val
        
        era_2025 = safe_get(player_stats_2025.get('防御率', 4.00), 4.00)
        wins_2025 = safe_get(player_stats_2025.get('勝利', 0), 0)
        saves_2025 = safe_get(player_stats_2025.get('セ｜ブ', 0), 0)
        strikeouts_2025 = safe_get(player_stats_2025.get('三振', 0), 0)
        walks_2025 = safe_get(player_stats_2025.get('四球', 0), 0)
        innings_2025 = safe_get(player_stats_2025.get('投球回', 0), 0)
        games_2025 = safe_get(player_stats_2025.get('登板', 0), 0)
        
        # 切れ（奪三振率）
        k_per_9 = (strikeouts_2025 / max(innings_2025, 1)) * 9 if innings_2025 > 0 else 6.0
        if k_per_9 >= 11.0:
            abilities['stuff'] = 'S'
        elif k_per_9 >= 9.5:
            abilities['stuff'] = 'A'
        elif k_per_9 >= 8.0:
            abilities['stuff'] = 'B'
        elif k_per_9 >= 6.5:
            abilities['stuff'] = 'C'
        elif k_per_9 >= 5.0:
            abilities['stuff'] = 'D'
        else:
            abilities['stuff'] = 'E'
        
        # 制球（与四球率）
        bb_per_9 = (walks_2025 / max(innings_2025, 1)) * 9 if innings_2025 > 0 else 4.0
        if bb_per_9 <= 1.5:
            abilities['control'] = 'S'
        elif bb_per_9 <= 2.5:
            abilities['control'] = 'A'
        elif bb_per_9 <= 3.5:
            abilities['control'] = 'B'
        elif bb_per_9 <= 4.5:
            abilities['control'] = 'C'
        elif bb_per_9 <= 5.5:
            abilities['control'] = 'D'
        else:
            abilities['control'] = 'E'
        
        # 安定性（防御率）
        if era_2025 <= 2.00:
            abilities['stability'] = 'S'
        elif era_2025 <= 2.75:
            abilities['stability'] = 'A'
        elif era_2025 <= 3.50:
            abilities['stability'] = 'B'
        elif era_2025 <= 4.25:
            abilities['stability'] = 'C'
        elif era_2025 <= 5.00:
            abilities['stability'] = 'D'
        else:
            abilities['stability'] = 'E'
        
        # スタミナ（イニング数と登板数から算出）
        workload = innings_2025 + games_2025 * 0.5
        if workload >= 180:
            abilities['stamina'] = 'A'
        elif workload >= 140:
            abilities['stamina'] = 'B'
        elif workload >= 100:
            abilities['stamina'] = 'C'
        elif workload >= 60:
            abilities['stamina'] = 'D'
        else:
            abilities['stamina'] = 'E'
        
        # 球速（奪三振数と防御率から推定）
        velocity_base = 140
        if k_per_9 >= 10.0:
            velocity_base = 150
        elif k_per_9 >= 8.5:
            velocity_base = 146
        elif k_per_9 >= 7.0:
            velocity_base = 142
        elif k_per_9 >= 5.5:
            velocity_base = 138
        else:
            velocity_base = 134
        
        # 防御率による調整
        if era_2025 <= 2.50:
            velocity_base += 4
        elif era_2025 >= 5.00:
            velocity_base -= 4
        
        abilities['velocity'] = min(158, max(128, velocity_base))
        abilities['velocity'] = (abilities['velocity'] // 2) * 2  # 2の倍数に丸め
        
        # デフォルト能力
        abilities['movement'] = 'C'
        abilities['technique'] = 'C'
        abilities['recovery'] = 24
        
        # 特別な投手の調整
        if 'バウアー' in player_name:
            abilities['stuff'] = 'S'
            abilities['velocity'] = 154
            abilities['technique'] = 'A'
        elif '森下暢仁' in player_name:
            abilities['stuff'] = 'A'
            abilities['velocity'] = 148
            abilities['stability'] = 'A'
        elif '大瀬良大地' in player_name:
            abilities['control'] = 'A'
            abilities['technique'] = 'A'
        
        return abilities
    
    def get_pitcher_type(self, player_name):
        """投手タイプを取得"""
        if player_name in self.pitcher_types:
            return self.pitcher_types[player_name]
        
        # デフォルト設定
        return {'hand': 'R', 'grade': 'C'}
    
    def get_batting_side(self, player_name):
        """打席を取得"""
        # 実際の選手データから取得
        clean_name = player_name.strip('*')
        if clean_name in self.player_batting_sides:
            return self.player_batting_sides[clean_name]
        
        # デフォルト（右打者が多い）
        return np.random.choice(['R', 'L', 'B'], p=[0.75, 0.22, 0.03])
    
    def process_team_enhanced(self, team_name):
        """チーム単位で強化データ生成"""
        print(f"処理中: {team_name}")
        
        # 打者データ
        team_batters = self.data_2025['batting'][
            self.data_2025['batting']['球団'] == team_name
        ]
        
        # 投手データ  
        team_pitchers = self.data_2025['pitching'][
            self.data_2025['pitching']['球団'] == team_name
        ]
        
        processed_data = {'batters': [], 'pitchers': []}
        
        # 野手処理
        for _, batter in team_batters.iterrows():
            player_name = str(batter['選　手'])
            if pd.isna(batter['選　手']) or player_name.startswith('【'):
                continue
            
            abilities = self.enhanced_batter_abilities(batter, player_name)
            batting_side = self.get_batting_side(player_name)
            
            # タイプ決定（より詳細）
            hr = abilities.get('power', 'E')
            player_type = 'P' if hr in ['S', 'A'] else 'S'
            
            processed_data['batters'].append({
                'name': player_name.strip('*'),
                'batting_side': batting_side,
                'type': player_type,
                'abilities': abilities
            })
        
        # 投手処理
        for _, pitcher in team_pitchers.iterrows():
            player_name = str(pitcher['投　手'])
            if pd.isna(pitcher['投　手']) or player_name.startswith('【'):
                continue
            
            abilities = self.enhanced_pitcher_abilities(pitcher, player_name)
            pitcher_type_info = self.get_pitcher_type(player_name)
            
            processed_data['pitchers'].append({
                'name': player_name.strip('*'),
                'hand': pitcher_type_info['hand'],
                'grade': pitcher_type_info['grade'],
                'abilities': abilities
            })
        
        return processed_data

def main():
    """強化版データ生成メイン処理"""
    print("2025年選手データ強化版生成開始...")
    
    generator = EnhancedPlayerDataGenerator()
    
    # 全チーム処理
    teams = generator.data_2025['batting']['球団'].unique()
    all_enhanced_data = {}
    
    for team in teams:
        if pd.isna(team):
            continue
        team_data = generator.process_team_enhanced(team)
        all_enhanced_data[team] = team_data
        print(f"  {team}: 野手{len(team_data['batters'])}名, 投手{len(team_data['pitchers'])}名")
    
    print("\n強化版データ生成完了!")
    return all_enhanced_data

if __name__ == "__main__":
    enhanced_data = main()
    
    # サンプル表示
    for team_name, data in list(enhanced_data.items())[:2]:
        print(f"\n=== {team_name} 強化版サンプル ===")
        if data['batters']:
            player = data['batters'][0]
            print(f"野手: {player['name']} ({player['batting_side']}/{player['type']}) "
                  f"指数={player['abilities']['batting_index']} "
                  f"長打={player['abilities']['power']}")
        if data['pitchers']:
            player = data['pitchers'][0]
            print(f"投手: {player['name']} ({player['hand']}/{player['grade']}) "
                  f"球速={player['abilities']['velocity']} "
                  f"切れ={player['abilities']['stuff']}")