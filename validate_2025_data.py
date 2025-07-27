#!/usr/bin/env python3
"""
2025年選手データ検証スクリプト
生成されたデータの品質と整合性をチェック
"""

import re
from pathlib import Path

def validate_teamdata_file(filepath):
    """teamdataファイルの検証"""
    print(f"=== {filepath.name} 検証開始 ===")
    
    with open(filepath, 'r', encoding='cp932', errors='ignore') as f:
        content = f.read()
    
    # 基本統計
    lines = content.split('\n')
    total_lines = len(lines)
    
    # チーム数カウント
    team_sections = content.count(';--------------------------------------------------------------------')
    team_count = team_sections - 1  # ヘッダー分を除く
    
    # 選手数カウント
    batter_lines = [line for line in lines if re.match(r'^\s*\d+\s+\w', line)]
    pitcher_lines = [line for line in lines if re.match(r'^P\s+\w', line)]
    
    print(f"総行数: {total_lines}")
    print(f"チーム数: {team_count}")
    print(f"野手数: {len(batter_lines)}")
    print(f"投手数: {len(pitcher_lines)}")
    
    # 能力値範囲チェック
    batting_indices = []
    velocities = []
    
    for line in batter_lines:
        parts = line.split()
        if len(parts) >= 18:
            try:
                batting_index = int(parts[-1])
                batting_indices.append(batting_index)
            except:
                pass
    
    for line in pitcher_lines:
        parts = line.split()
        if len(parts) >= 11:
            try:
                velocity = int(parts[3])
                velocities.append(velocity)
            except:
                pass
    
    if batting_indices:
        print(f"打撃指数範囲: {min(batting_indices)} - {max(batting_indices)}")
        print(f"打撃指数平均: {sum(batting_indices) / len(batting_indices):.1f}")
    
    if velocities:
        print(f"球速範囲: {min(velocities)} - {max(velocities)}")
        print(f"球速平均: {sum(velocities) / len(velocities):.1f}")
    
    # エラーチェック
    errors = []
    
    # 打撃指数チェック（220-350の範囲）
    invalid_indices = [idx for idx in batting_indices if idx < 220 or idx > 350]
    if invalid_indices:
        errors.append(f"範囲外打撃指数: {len(invalid_indices)}件")
    
    # 球速チェック（128-158の範囲）
    invalid_velocities = [vel for vel in velocities if vel < 128 or vel > 158]
    if invalid_velocities:
        errors.append(f"範囲外球速: {len(invalid_velocities)}件")
    
    # 結果出力
    if errors:
        print("⚠️  エラー:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("✅ データ検証: 問題なし")
    
    print()
    return len(errors) == 0

def compare_with_reference():
    """参考データとの比較"""
    print("=== 2000年参考データとの比較 ===")
    
    data_dir = Path(__file__).parent / "data"
    ref_file = data_dir / "teamdata_2000.txt"
    new_file = data_dir / "teamdata_2025_final.txt"
    
    if not ref_file.exists():
        print("参考ファイルが見つかりません")
        return
    
    # ファイルサイズ比較
    ref_size = ref_file.stat().st_size
    new_size = new_file.stat().st_size
    
    print(f"2000年ファイルサイズ: {ref_size:,} bytes")
    print(f"2025年ファイルサイズ: {new_size:,} bytes")
    print(f"サイズ比: {new_size / ref_size:.2f}倍")
    print()

def main():
    """メイン検証処理"""
    print("2025年選手データ検証開始")
    print("=" * 50)
    
    data_dir = Path(__file__).parent / "data"
    
    # 各ファイルを検証
    files_to_check = [
        "teamdata_2025.txt",
        "teamdata_2025_final.txt"
    ]
    
    all_valid = True
    for filename in files_to_check:
        filepath = data_dir / filename
        if filepath.exists():
            is_valid = validate_teamdata_file(filepath)
            all_valid = all_valid and is_valid
        else:
            print(f"⚠️  ファイルが見つかりません: {filename}")
            all_valid = False
    
    # 参考データとの比較
    compare_with_reference()
    
    # 最終結果
    print("=" * 50)
    if all_valid:
        print("🎉 全ての検証が完了しました！")
        print("2025年選手データの生成が成功しました。")
        print()
        print("📁 生成されたファイル:")
        for filename in files_to_check:
            filepath = data_dir / filename
            if filepath.exists():
                print(f"  - {filename}")
        print()
        print("🎮 ベストプレープロ野球での使用準備完了！")
    else:
        print("❌ 検証でエラーが検出されました。")
        print("データを確認して修正してください。")

if __name__ == "__main__":
    main()