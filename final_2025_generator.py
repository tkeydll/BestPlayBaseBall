#!/usr/bin/env python3
"""
最終版 2025年選手データ生成・出力スクリプト
強化された能力値計算とリアルな選手データ
"""

from enhance_2025_data import EnhancedPlayerDataGenerator
import pandas as pd
from pathlib import Path

class Final2025DataExporter:
    """最終版2025年データ出力クラス"""
    
    def __init__(self):
        self.generator = EnhancedPlayerDataGenerator()
        self.output_dir = Path(__file__).parent / "data"
        
        # チーム名マッピング
        self.team_mapping = {
            '読売ジャイアンツ': {
                'name': 'ヨミウリジャイアンツ', 
                'symbol': 'giants', 
                'uniform': 'G_h G_v',
                'characteristics': [0, 0, 1, 1, 0, 0, 0, 0, 1]
            },
            '阪神タイガース': {
                'name': 'ハンシンタイガース', 
                'symbol': 'tigers', 
                'uniform': 'T_h T_v',
                'characteristics': [1, 0, 0, 0, 1, 0, 1, 0, 0]
            },
            '横浜DeNAベイスターズ': {
                'name': 'ヨコハマベイスターズ', 
                'symbol': 'baystars', 
                'uniform': 'Y_h Y_v',
                'characteristics': [0, 1, 0, 1, 0, 1, 0, 0, 0]
            },
            '広島東洋カープ': {
                'name': 'ヒロシマカープ', 
                'symbol': 'carp', 
                'uniform': 'C_h C_v',
                'characteristics': [0, 0, 0, 0, 0, 0, 1, 1, 1]
            },
            '東京ヤクルトスワローズ': {
                'name': 'ヤクルトスワローズ', 
                'symbol': 'swallows', 
                'uniform': 'S_h S_v',
                'characteristics': [1, 0, 1, 1, 1, 0, 1, 0, 1]
            },
            '中日ドラゴンズ': {
                'name': 'チュウニチドラゴンズ', 
                'symbol': 'dragons', 
                'uniform': 'D_h D_v',
                'characteristics': [-1, 0, 1, 1, 1, 0, 0, 0, 1]
            },
            '福岡ソフトバンクホークス': {
                'name': 'ソフトバンクホークス', 
                'symbol': 'hawks', 
                'uniform': 'H_h H_v',
                'characteristics': [1, 1, 1, 1, 1, 1, 0, 0, 1]
            },
            '北海道日本ハムファイターズ': {
                'name': 'ニッポンハムファイターズ', 
                'symbol': 'fighters', 
                'uniform': 'F_h F_v',
                'characteristics': [0, 1, 0, 0, 1, 0, 0, 1, 0]
            },
            '千葉ロッテマリーンズ': {
                'name': 'ロッテマリーンズ', 
                'symbol': 'marines', 
                'uniform': 'M_h M_v',
                'characteristics': [0, 0, 0, 1, 0, 1, 1, 0, 0]
            },
            '東北楽天ゴールデンイーグルス': {
                'name': 'ラクテンイーグルス', 
                'symbol': 'eagles', 
                'uniform': 'E_h E_v',
                'characteristics': [0, 0, 1, 0, 0, 0, 0, 0, 1]
            },
            'オリックス・バファローズ': {
                'name': 'オリックスバファローズ', 
                'symbol': 'buffaloes', 
                'uniform': 'B_h B_v',
                'characteristics': [1, 1, 0, 0, 1, 0, 0, 0, 0]
            },
            '埼玉西武ライオンズ': {
                'name': 'セイブライオンズ', 
                'symbol': 'lions', 
                'uniform': 'L_h L_v',
                'characteristics': [0, 0, 0, 0, 0, 1, 0, 1, 0]
            }
        }
    
    def determine_fielding_positions(self, player_name, team_name):
        """選手の守備位置を決定（仮想的な設定）"""
        # 実際には選手データベースから取得すべきだが、ここでは簡易設定
        positions = ['-', '-', '-', '-', '-', '-']  # C,1,2,3,S,O
        
        # 捕手っぽい名前
        if any(x in player_name for x in ['大城', '古賀', '炭谷', '甲斐', '森', '梅野']):
            positions[0] = 'A'  # 捕手
        # 内野手っぽい名前の場合の処理...
        # （実装を簡略化）
        
        return positions
    
    def calculate_vs_left_ability(self, batting_side, player_name):
        """対左投手能力を計算"""
        if batting_side == 'L':
            return -1  # 左打者は左投手苦手
        elif batting_side == 'R':
            return 0   # 右打者は普通
        else:
            return 0   # 両打者
    
    def export_final_teamdata(self, output_filename="teamdata_2025_final.txt"):
        """最終版teamdataファイルを出力"""
        print("最終版2025年選手データ出力開始...")
        
        # 全チームデータ生成
        teams = self.generator.data_2025['batting']['球団'].unique()
        all_team_data = {}
        
        for team in teams:
            if pd.isna(team):
                continue
            team_data = self.generator.process_team_enhanced(team)
            all_team_data[team] = team_data
        
        # ファイル出力
        output_path = self.output_dir / output_filename
        
        with open(output_path, 'w', encoding='cp932', errors='ignore') as f:
            self._write_header(f)
            
            for team_name, team_data in all_team_data.items():
                if team_name not in self.team_mapping:
                    continue
                
                self._write_team_section(f, team_name, team_data)
        
        print(f"最終版データファイル出力完了: {output_path}")
        return output_path
    
    def _write_header(self, f):
        """ファイルヘッダーを書き込み"""
        f.write(";--------------------------------------------------------------------\n")
        f.write("; ベストプレープロ野球2025年選手データ\n")
        f.write("; 2024-2025年実績データベース自動生成版\n")
        f.write("; Generated by BestPlayBaseBall Data Generator\n")
        f.write("\n")
    
    def _write_team_section(self, f, team_name, team_data):
        """チームセクションを書き込み"""
        team_info = self.team_mapping[team_name]
        
        f.write(";--------------------------------------------------------------------\n")
        f.write(f"; チーム名                  略称         記    BGM\n")
        f.write(f"  {team_info['name']:<20} {team_info['symbol']:<10} {team_info['symbol'][0]:<3} {team_info['symbol']}\n")
        f.write("\n")
        f.write("; UNIFORM                   SYMBOL       BGM\n")
        f.write(f"  {team_info['uniform']:<20} {team_info['symbol']:<10} {team_info['symbol']}\n")
        f.write("\n")
        
        # チーム特徴
        chars = team_info['characteristics']
        char_labels = ['打', '走', '守', '機', '盗', '足', '絡', '守', '幸']
        f.write("; 特徴             打 走 守 機 盗 足 絡 守 幸\n")
        char_str = "  " + team_info['name'][:8].ljust(15)
        for char in chars:
            char_str += f"{char:+2d} "
        f.write(char_str + "\n\n")
        
        # 野手データ
        f.write("; 選手             打 打 C 1 2 3 S O 肩 脚 眼 実 ス 好 長 信 対 打撃\n")
        
        for i, batter in enumerate(team_data['batters'][:25], 1):  # 最大25名
            name = batter['name'][:8]
            batting_side = batter['batting_side']
            player_type = batter['type']
            abilities = batter['abilities']
            
            # 守備位置（簡易設定）
            positions = self.determine_fielding_positions(name, team_name)
            
            # 対左計算
            vs_left = self.calculate_vs_left_ability(batting_side, name)
            
            # 特別な選手への信頼度設定
            clutch = abilities.get('clutch', 0)
            if any(star in name for star in ['村上宗隆', '山田哲人', '岡本和真', '大山悠輔']):
                clutch = 2
            elif any(good in name for good in ['秋広', '森下', '近本']):
                clutch = 1
            
            f.write(f"{i:2d} {name:<15} {batting_side}  {player_type}  "
                   f"{' '.join(positions)}  "
                   f"{abilities['arm']}  {abilities['speed']}  {abilities['discipline']}  "
                   f"{abilities['experience']}  {abilities['stamina']}  "
                   f"{abilities['contact']}  {abilities['power']}  "
                   f"{clutch:+2d} {vs_left:+2d}  "
                   f"{abilities['batting_index']}\n")
        
        f.write("\n")
        
        # 投手データ
        f.write("; 投手             投 型 球速 切 制 安 球 技 ス  回 年俸\n")
        
        for pitcher in team_data['pitchers']:
            name = pitcher['name'][:8]
            hand = pitcher['hand']
            grade = pitcher['grade']
            abilities = pitcher['abilities']
            
            f.write(f"P {name:<15} {hand}  {grade}   "
                   f"{abilities['velocity']:3d}  "
                   f"{abilities['stuff']}  {abilities['control']}  {abilities['stability']}  "
                   f"{abilities['movement']}  {abilities['technique']}  {abilities['stamina']}  "
                   f"{abilities['recovery']:2d}  200\n")
        
        f.write("\n")

def main():
    """メイン処理"""
    exporter = Final2025DataExporter()
    output_file = exporter.export_final_teamdata()
    
    print(f"\n=== 2025年選手データ生成完了 ===")
    print(f"出力ファイル: {output_file}")
    print("ベストプレープロ野球での使用準備完了！")
    
    return output_file

if __name__ == "__main__":
    main()