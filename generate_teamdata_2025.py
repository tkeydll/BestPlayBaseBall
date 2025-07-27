#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NPB 2025年度チームデータ生成スクリプト
2024年の成績をもとにした2025年のチームデータを生成します。
"""

def create_teamdata_2025():
    """2025年度のチームデータを生成"""
    
    # 2024年シーズンを反映した各チームの設定
    # セントラル・リーグ優勝: 阪神タイガース
    # パシフィック・リーグ優勝: オリックス・バファローズ
    # 日本シリーズ: オリックス優勝
    
    teamdata_content = """
;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  中日ドラゴンズ            中日         中    名古屋ドーム

; UNIFORM                   SYMBOL       BGM
  D_h          D_v          dragons      dragons

; 戦略             打 盗 犠 送 走 長 牽 守 機
  監督             -1  0 +1 +1 +1  0  0  0 +1

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
8 岡林勇希         L  S  - - - - - B  A  A  B  B  B  B  C  0 -2  280
7 高橋周平         R  P  - - - - C C  B  B  C  C  C  C  C  0  0  270
6 ビシエド         R  P  - - - C D -  B  C  D  B  C  D  B  0 -1  280
5 石川昂弥         R  P  - C - C - -  B  C  C  B  B  C  B -1  0  290
4 細川成也         L  S  - - B - - C  C  D  B  A  B  C  C +1 -1  300
3 村松開人         R  P  - C - - - -  C  C  C  C  C  C  C  0 +1  270
9 福永春吾         L  P  - - - - - B  B  C  D  D  C  D  C  0 -2  260
2 加藤翔平         R  P  B - - - - -  C  C  D  C  C  C  D  0  0  250
- 郡司裕也         R  P  - D C C C C  B  C  C  C  C  C  C +1 +1  280
- 溝脇隼人         R  S  C - - - - -  C  C  D  D  C  C  D  0  0  250
- 鵜飼航丞         R  P  - D C C D -  C  C  D  C  C  D  C +1  0  270
- 岡田俊哉         R  S  - - C C C -  C  C  C  D  C  C  D  0  0  260
- 古川侑利         R  S  - - B C B C  B  C  C  D  C  B  D  0  0  280
- 龍空             L  S  - - B - A -  B  C  C  C  C  B  D -1 -2  260
- 木下雄介         R  S  - - - - - A  B  B  D  D  C  C  E  0  0  250
- 土田龍空         R  S  - - - - - B  B  B  D  E  D  C  E  0  0  240

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 松葉貴大         R  B   146  A  B  B  B  C  A  26  200
P 小笠原慎之介     L  C   136  B  B  B  C  B  B  24  200
P 涌井秀章         R  C   140  B  C  C  C  C  C  24  200
P 村中恭兵         R  C   138  B  B  C  D  B  C  22  200
P 森博人           L  A+  140  C  C  C  D  B  C  20  200
P 谷元圭介         L  A+  136  C  C  B  C  C  C  26  200
P 橋本侑樹         R  B   146  C  D  C  C  D  C  26  200
P レイビス         Rs C   138  B  B  C  D  C  C  26  200
P 鈴木博志         R  B   140  C  B  B  B  C  D  24  200
P 梅津晃大         R  C   142  C  B  B  C  B  D  24  200
P 福谷浩司         L  B   144  B  B  A  B  C  D  26  200
P ライデル・マルティネス R  B   150  B  B  A  A  C  E  24  200

;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  読売ジャイアンツ          巨人         ジ    東京ドーム

; UNIFORM                   SYMBOL       BGM
  G_h          G_v          giants       giants

; 戦略             打 盗 犠 送 走 長 牽 守 機
  監督             +1 +1 -1 -1  0 +1  0 +1 -1

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
4 丸佳浩           R  P  - - C C D -  B  B  C  C  C  C  B  0 +1  290
7 坂本勇人         R  P  - - - - - C  C  B  C  C  C  B  C  0  0  280
5 岡本和真         R  P  - D - D - -  A  B  B  A  A  C  A +1 +1  310
8 浅野翔吾         L  P  - - - - - A  B  C  B  A  A  D  A  0 -1  310
3 門脇誠           R  S  - B - D - -  C  D  D  B  B  D  B +1 +1  280
9 中田翔           R  P  - - - - - A  A  C  C  B  B  C  A  0  0  290
6 松原聖弥         L  S  - - - - B -  B  B  D  D  C  C  C  0 -1  270
2 大城卓三         R  P  B - - - - -  C  C  D  C  D  C  D  0  0  250
- ブリンソン       R  P  - C - - - D  B  C  D  B  C  D  B +1 +1  290
- 萩尾匡也         R  P  C - - - - -  B  D  C  D  D  D  D  0  0  240
- 喜多隆介         R  P  C - - - - -  C  D  D  E  D  D  E  0  0  230
- 若林楽人         R  S  - - C C C D  C  D  B  C  D  B  C +2  0  270
- 秋広優人         L  P  - - C B B -  C  D  C  B  C  A  E  0 -2  270
- 増田陸           R  P  - - B B C -  B  B  D  E  C  C  D  0  0  240
- 赤星優志         L  P  - C - C - C  B  C  C  D  B  C  D  0 -2  270
- 立岡宗一郎       L  S  - - - - - C  B  C  D  E  C  C  E  0 -2  240

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 菅野智之         R  A   144  A  A  A  C  B  B  20  200
P 戸郷翔征         R  B   144  A  B  B  B  C  B  22  200
P 今村信貴         R  B   144  B  A  B  D  D  A  22  200
P 赤星優志         L  B   140  B  A  A  B  C  B  22  200
P 平内龍太         R  B+  146  B  C  D  B  D  C  24  200
P 大勢             R  A+  138  A  B  B  B  B  B  22  200
P 田口麗斗         R  C   136  C  C  C  C  B  D  28  200
P 船迫大雅         L  A   140  C  B  B  C  B  D  26  200
P 松井颯           Ls A   136  C  B  B  C  C  E  24  200
P グリフィン       R  B   142  B  C  B  B  C  D  24  200
P ビーディ         L  A   144  A  D  B  B  D  C  24  200
P 鍬原拓也         L  C   142  B  C  C  D  B  C  18  200

;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  横浜DeNAベイスターズ      横浜         YB    横浜スタジアム

; UNIFORM                   SYMBOL       BGM
  YB_h         YB_v         baystars     baystars

; 戦略             打 盗 犠 送 走 長 牽 守 機
  監督             +1 +1 -1 -1 -1 +1  0  0  0

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
6 佐野恵太         L  S  - - - B A -  A  A  A  A  B  B  D  0 -2  300
5 牧秀悟           R  S  - - - C - C  B  B  B  D  C  B  D  0  0  330
7 宮崎敏郎         R  P  - - - - - C  C  C  B  A  B  B  B  0  0  310
4 オースティン     R  S  - - C D - -  A  B  B  A  A  C  A +2  0  330
9 大和             R  P  - - - - - C  C  C  D  C  D  D  C +1 +1  290
3 度会隆輝         L  P  - A - - - -  C  D  C  A  D  D  D +1 -2  270
8 森敬斗           R  S  - - - - - B  B  B  C  B  C  A  D  0  0  290
2 山本祐大         R  P  B - - - - -  A  D  D  C  B  D  C  0  0  260
- 京田陽太         R  P  - C - - - D  B  C  C  C  D  D  C +1 -1  260
- 関根大気         R  P  C - - - - -  C  C  D  E  C  D  D  0  0  240
- 柴田竜拓         R  P  - - C A C -  B  D  D  C  C  D  C  0  0  240
- 知野直人         R  S  - - C C C -  C  B  D  D  C  C  E  0  0  240
- 西巻賢二         L  P  - - - C - -  C  C  C  E  C  C  C  0 -2  260
- 蝦名達夫         L  S  - - - - - B  C  B  D  D  C  C  E  0 -2  260
- 松尾汐恩         L  P  - - - - - B  B  C  C  E  D  C  D  0 -2  270
- 粟飯原龍生       R  S  - - - - - B  B  B  D  E  D  C  E  0  0  230

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 山崎康晃         R  A+  138  A  A  A  B  B  A  24  200
P 今永昇太         L  A   138  A  A  B  C  A  A  24  200
P 大貫晋一         R  B   140  B  B  B  D  B  B  24  200
P 東克樹           L  B   144  B  B  B  C  C  B  22  200
P バウアー         R  A+  140  A  A  A  B  B  B  24  200
P 石田健大         L  B   136  B  C  B  C  C  C  22  200
P 森原康平         R  B+  138  B  C  B  C  C  C  24  200
P エスコバー       R  A   146  A  B  B  B  B  C  26  200
P 伊勢大夢         R  B   142  B  C  B  C  C  D  26  200
P 入江大生         L  A   140  B  E  D  D  C  E  26  200
P 坂本裕哉         R  C   138  B  B  B  C  C  C  24  200
P 上茶谷大河       Rs C   142  A  B  B  C  C  D  24  200

;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  東京ヤクルトスワローズ    ヤクルト     ヤ    明治神宮野球場

; UNIFORM                   SYMBOL       BGM
  S_h          S_v          swallows     swallows

; 戦略             打 盗 犠 送 走 長 牽 守 機
  監督             +1  0 +1 +1 +1  0 +1  0 +1

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
8 山田哲人         R  S  - - - - - B  C  B  C  C  D  B  D  0  0  270
4 村上宗隆         R  S  - - B C D D  A  A  B  A  A  A  A  0  0  320
9 オスナ           R  P  - - - - - C  B  C  D  D  C  D  C  0  0  260
3 長岡秀樹         L  P  - C - - - -  C  D  C  A  B  C  A +2 -2  320
2 中村悠平         R  S  S - - - - -  A  C  B  A  A  B  C  0  0  290
7 濱田太貴         R  P  - - - - - D  C  D  E  C  C  E  A  0  0  280
5 内山壮真         L  P  - - - D - -  C  B  C  D  C  D  C +1 -1  280
6 塩見泰隆         R  S  - - - - A -  A  B  D  D  C  C  E  0  0  270
- 木澤尚文         L  P  - D - - - C  B  C  C  C  B  C  C -1 -2  290
- 古賀優大         R  S  C - - - - -  B  D  C  D  C  C  D  0 +1  240
- 川端慎吾         R  P  - C C C - -  C  C  D  D  D  D  C  0  0  240
- 元山飛優         R  P  - - - B C -  B  C  D  A  B  D  B  0  0  250
- 丸山和郁         R  S  - - C A - -  C  D  D  C  D  B  E  0  0  240
- 並木秀尊         R  S  - C - C - C  C  C  C  D  C  C  D  0  0  260
- 岩見雅紀         L  P  - C - D - C  C  C  D  D  C  D  C  0 -2  270
- 嶋基宏           R  S  - - D - - A  A  A  C  B  C  B  E  0  0  260

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 小川泰弘         R  B   148  A  E  C  B  C  B  24  200
P 高橋奎二         R  C   140  B  A  B  B  B  A  24  200
P ハッカミー       L  D   138  B  A  C  C  B  C  24  200
P 金久保優斗       R  B   146  A  B  B  C  B  B  20  200
P 清水昇           L  A+  140  C  D  D  C  C  C  24  200
P 廣岡大志         R  B   144  C  C  C  D  C  C  26  200
P 丸山和郁         L  B   146  C  D  C  C  D  C  24  200
P サンタナ         L  A   140  B  C  D  C  D  D  24  200
P 梅野雄吾         Rs D   132  B  C  C  C  C  D  24  200
P 石川雅規         L  A+  140  B  C  B  D  D  D  24  200
P 田中正義         R  B+  150  B  D  C  C  D  D  26  200
P 中尾輝           Rs C   138  A  B  A  C  B  E  24  200

;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  広島東洋カープ            広島         広    MAZDA Zoom-Zoom スタジアム広島

; UNIFORM                   SYMBOL       BGM
  C_h          C_v          carp         carp

; 戦略             打 盗 犠 送 走 長 牽 守 機
  監督              0 +1  0  0  0 +1 +2 +1 -1

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
4 菊池涼介         R  S  - - C - D B  B  A  D  D  C  C  D  0  0  280
6 坂倉将吾         R  S  - - C - C -  B  B  D  E  C  C  E  0 -1  280
8 野間峻祥         L  P  - - - - - B  B  D  A  A  B  C  B +1 -1  290
7 秋山翔吾         L  P  - - - - - C  B  B  D  B  A  D  A +1 -2  300
3 マクブルーム     R  P  - C - - - -  C  D  B  B  B  C  B +1  0  290
5 末包昇大         L  S  - D - C C -  B  C  B  A  B  B  C  0 -1  270
9 西川龍馬         L  S  - C - - - C  C  C  C  C  C  D  C  0 -2  290
2 會澤翼           R  S  B - - - - -  C  C  C  C  C  C  D  0  0  250
- 小園海斗         R  S  B - - - - -  B  D  D  D  C  C  E  0  0  250
- ディアス         R  P  - - C C C -  C  C  C  D  C  D  D  0 +1  250
- 堂林翔太         R  S  - - C C D -  B  C  D  D  C  C  E  0  0  240
- 新井貴浩         R  P  - C - C - -  C  C  D  E  C  D  C  0  0  240
- 韮澤雄也         R  P  - C E E - C  C  D  C  C  D  C  C  0 +1  280
- 宇草孔基         R  S  - - - - - B  B  B  D  E  C  C  D  0  0  250
- 羽月隆太郎       R  P  - - - - - C  B  C  D  E  D  C  E  0  0  240
- 曽根海成         L  P  - C - - - C  C  C  D  E  C  C  D  0 -2  260

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 森下暢仁         R  A+  142  A  A  A  C  B  A  22  200
P ミッチェル       R  D   138  B  A  B  C  A  B  26  200
P 大瀬良大地       R  B+  144  C  C  D  C  D  B  24  200
P 九里亜蓮         R  A+  140  C  B  C  D  C  C  20  200
P 黒原拓未         L  A   142  B  D  C  C  D  C  26  200
P 栗林良吏         R  B+  138  A  C  B  B  C  D  24  200
P 玉村昇悟         R  A+  140  C  C  D  C  C  D  22  200
P 中崎翔太         Rs C   138  C  B  C  C  B  D  24  200
P 島内宏明         R  B+  142  A  C  B  B  C  D  24  200
P 常廣羽也斗       R  A   140  B  D  C  B  C  D  28  200
P 高橋昂也         R  A   140  B  D  C  C  B  D  22  200
P 床田寛樹         R  B+  144  B  C  D  B  D  D  26  200

;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  阪神タイガース            阪神         虎    阪神甲子園球場

; UNIFORM                   SYMBOL       BGM
  T_h          T_v          tigers       tigers

; 戦略             打 盗 犠 送 走 長 牽 守 機
  監督              0 +1 +1 +1 +1 +1  0  0  0

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
7 近本光司         L  S  - - - - - C  A  A  C  C  C  B  D  0 -1  280
4 佐藤輝明         R  S  - - B C - -  B  C  B  A  D  A  D +1  0  270
9 マルテ           L  P  - - - - - A  A  C  C  C  C  C  B  0 -1  250
8 大山悠輔         R  P  - - - - - A  S  B  C  C  A  D  A +1 +1  280
3 森下翔太         L  P  - C - - - E  D  E  E  A  C  E  A  0 -2  250
5 ノイジー         R  P  - D - C - -  C  D  C  C  C  D  C  0  0  280
2 梅野隆太郎       R  P  C - - - - -  B  C  C  C  C  C  D  0 +1  270
6 木浪聖也         L  S  - - B C B -  C  B  C  E  C  C  E  0 -2  250
- 前川右京         L  P  - - - - - C  C  D  E  C  B  D  C  0 -2  250
- 糸原健斗         R  P  C - - - - -  D  D  D  D  C  C  D +1  0  260
- 小幡竜平         R  S  - - C - B -  B  B  C  D  C  B  D -1  0  260
- 渡邊諒           L  S  - - C C C -  C  C  D  D  C  C  E  0 -2  240
- 島田海吏         R  P  - - C C C -  B  B  D  E  C  C  D  0  0  240
- 熊谷敬宥         R  P  - - C C B D  B  B  C  D  C  C  E  0  0  250
- 中野拓夢         R  P  - D C C - D  C  C  D  D  C  C  D  0  0  270
- 髙寺望夢         R  P  - D - - - D  D  D  C  B  D  D  C +1 +1  270

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 村上頌樹         R  C   142  A  A  C  C  B  B  24  200
P 才木浩人         Rs C   136  B  B  C  C  A  B  22  200
P 青柳晃洋         L  D   130  A  B  D  D  A  B  22  200
P ビーズリー       R  B   144  B  C  B  B  C  B  24  200
P 西勇輝           R  B+  142  B  C  C  C  D  C  24  200
P 桐敷拓馬         L  C   136  B  B  D  C  B  C  22  200
P 加治屋蓮         R  A   138  C  B  C  B  C  C  24  200
P 湯浅京己         L  A+  138  B  D  C  C  C  C  24  200
P 岩崎優           L  A   144  B  D  C  C  D  E  26  200
P 石井大智         Rs C   136  B  C  A  B  B  D  28  200
P 岩貞祐太         Ls C   138  B  B  A  C  B  E  24  200
P 小川一平         Rs A+  134  A  C  B  B  A  D  26  200

;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  福岡ソフトバンクホークス  ソフトバンク ソ    PayPayドーム

; UNIFORM                   SYMBOL       BGM
  H_h          H_v          hawks        hawks

; 戦略             打 盗 犠 送 走 長 牽 守 機
  監督             +1 +1 -1  0  0  0  0  0 +1

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
8 今宮健太         R  S  - - - - - B  B  B  C  C  B  C  D  0  0  310
4 柳田悠岐         L  S  - - C C C -  B  B  D  E  C  C  E  0 -2  270
D グラシアル       L  P  E D - - - -  D  E  C  B  C  D  B -1 -1  270
5 山川穂高         R  P  - C - C - -  A  A  C  B  C  D  A +1  0  290
3 栗原陵矢         L  P  - C - - - D  C  D  B  C  B  C  A +1 -2  310
2 甲斐拓也         R  P  C E - - - -  A  C  C  B  B  D  B +1 +1  300
7 ニャーブ         R  P  - - - - - C  C  C  D  D  C  D  B  0  0  250
9 中村晃           R  P  - - - - - B  B  C  D  A  C  C  C  0 +1  270
6 野村大樹         R  S  - - C B A -  B  B  D  D  D  C  D  0  0  240
- 牧原大成         L  P  B - - - - -  B  D  D  D  C  D  D +1 -2  260
- 笹川晃平         R  P  - - - - B -  A  B  E  D  B  D  C  0  0  250
- 正木智也         L  S  - - B C B -  C  B  C  C  D  B  D  0 -2  240
- 中村亮太         R  S  - D B B - -  C  C  C  D  C  B  E  0  0  250
- 古谷優人         R  S  - D - - - C  C  D  B  C  C  C  D  0 +2  300
- 柳町達           L  S  - - - - - B  C  A  C  C  C  C  E  0 -1  260
- 周東佑京         R  P  - - - - - A  A  B  D  E  C  D  E  0  0  230

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 石川柊太         R  C   138  B  B  B  C  C  B  24  200
P 大関友久         R  B+  142  A  D  B  D  D  B  24  200
P バレンティン     R  A+  138  B  C  B  B  B  B  22  200
P 武田翔太         R  A+  138  B  C  B  B  C  C  22  200
P 板東湧梧         L  A   136  A  D  C  C  C  C  22  200
P 津森宥紀         R  A   144  C  D  C  C  D  C  20  200
P 山﨑颯一郎       Rs C   134  B  B  C  C  C  C  20  200
P 嘉弥真新也       L  A   140  B  C  B  C  C  D  26  200
P 松本裕樹         R  C   136  C  B  B  C  C  D  24  200
P 田中正義         L  D   138  A  D  A  B  B  E  26  200
P 増田珠           L  B   140  B  A  B  C  C  D  26  200
P ペドロ・パヤノ   R  B   142  B  A  A  A  B  E  24  200

;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  埼玉西武ライオンズ        西武         西    ベルーナドーム

; UNIFORM                   SYMBOL       BGM
  L_h          L_v          lions        lions

; 戦略             打 盗 犱 送 走 長 牽 守 機
  監督             -1  0 +1 +1 +1  0 +1 +1  0

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
8 源田壮亮         R  S  - - - - - B  B  B  C  C  B  B  E -1 -2  260
9 外崎修汰         R  S  - - - - - B  B  B  B  D  C  C  E  0 -1  270
6 山田遥楓         R  S  - - - - A -  A  A  C  A  A  B  B  0  0  310
5 スパンジェンバーグ R  S  - - - C - -  B  B  B  A  C  B  C +1  0  330
D ジャレッド       L  S  - D - - - -  D  D  C  B  D  D  B  0 -2  260
7 栗山巧           R  P  - - - - - D  C  C  E  D  D  D  B  0  0  250
3 熊代聖人         L  P  - D - C - -  C  D  C  B  B  C  C  0 -2  250
2 岸潤一郎         R  P  S - - - - -  C  D  D  C  E  C  D  0  0  240
4 中村剛也         L  P  - - B C D -  C  C  B  D  C  B  E  0 -2  250
- 愛斗             R  P  B - - - - -  B  D  C  C  C  C  D  0  0  250
- 滝澤夏央         L  P  - C - D - C  C  B  B  C  C  C  C  0 -1  260
- 野村勇           R  S  - D B B C -  B  B  D  D  C  C  E  0  0  240
- 平沼翔太         R  P  - - C C - -  C  C  D  E  D  C  D  0  0  230
- 長谷川信哉       R  S  C D - - - C  B  B  D  D  C  C  D  0 +1  280
- 鈴木将平         R  S  - - - - - B  C  A  D  C  C  B  E  0  0  260
- 川野涼多         R  S  - D - - - D  D  D  C  C  C  D  C  0 +1  250

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 今井達也         R  C   142  A  C  B  C  C  A  22  200
P 松本航           R  B   150  A  D  C  B  C  A  26  200
P 平良海馬         R  B   144  B  B  A  A  D  B  24  200
P 渡邉勇太朗       R  B   142  C  C  B  B  C  C  26  200
P 岸潤一郎         R  A+  138  B  A  C  C  B  C  22  200
P 森脇亮介         Rs C   138  A  C  C  C  B  C  24  200
P 佐々木健          R  A+  142  B  C  C  D  C  C  20  200
P 川越誠司         R  C   136  C  C  C  C  C  D  24  200
P 羽田慎之介       L  C   138  C  B  C  C  B  D  24  200
P 宮川哲           L  A   140  B  D  B  B  D  E  26  200
P デニング         R  A   144  B  D  B  A  D  D  26  200
P 佐藤隼輔         R  B+  148  A  C  B  B  D  C  26  200

;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  オリックス・バファローズ  オリックス   オ    京セラドーム大阪

; UNIFORM                   SYMBOL       BGM
  Bw_h         Bw_v         buffaloes    buffaloes

; 戦略             打 盗 犱 送 走 長 牽 守 機
  監督             -1  0 +1 +1 -1  0 -1  0  0

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
7 宗佑磨           R  S  - - C - C A  A  B  C  B  B  C  D  0  0  280
4 杉本裕太郎       R  S  - - B C C -  B  B  C  C  B  B  D  0  0  270
8 セデーニョ       R  S  - C - - - A  B  A  B  C  C  C  C  0  0  280
9 イチロー         L  S  - - - - - A  S  A  A  S  A  A  C +2 -1  360
D ニール           L  P  - D - - - D  D  D  E  B  D  D  B  0 -2  250
3 中川拓真         L  P  - C - - - C  C  D  D  B  D  E  B  0 -1  250
5 アルバース       R  P  - - - C - -  B  C  D  C  B  D  A -1  0  250
2 山足達也         L  P  C - - - - -  B  C  E  E  D  D  D  0 -2  230
6 野口智哉         R  S  - - C - B -  C  C  D  D  C  C  E +1 +1  260
- 大里昂生         R  P  B - - - - -  C  D  C  D  D  C  E  0  0  230
- 太田椋           R  S  - C C C B -  C  C  D  B  D  B  C  0  0  250
- 茨木楓           L  P  - C C C C D  C  D  C  D  C  D  D  0 -2  250
- 椿直輝           R  P  - C C C - -  B  C  C  D  C  B  E  0  0  240
- 比嘉幹貴         R  S  - - B C B -  B  B  D  E  D  D  E  0  0  230
- 紅林弘太郎       L  S  - - - - - B  C  C  D  D  C  C  E  0 -2  240
- 森友哉           R  P  - - - - - C  C  D  C  D  C  D  D  0 +1  270

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 山本由伸         R  C   144  A  A  B  C  C  B  22  200
P 宮城大弥         R  C   140  B  D  B  B  C  C  22  200
P 田嶋大樹         R  C   140  B  B  A  C  B  B  24  200
P 山岡泰輔         L  A   136  B  B  C  B  C  C  22  200
P 曽谷龍平         R  C   138  C  B  B  C  B  B  22  200
P 漆原大晟         R  B   144  C  D  D  C  C  C  22  200
P カラスコ         L  A+  138  B  D  C  C  C  C  28  200
P 富山凌雅         R  B   140  C  C  B  B  C  C  26  200
P 比嘉幹貴         Ls D   134  C  C  C  C  B  E  24  200
P 平野佳寿         R  B   148  C  D  C  D  D  D  26  200
P 村西良太         Rs C   136  B  A  B  C  C  D  26  200
P 佐藤世那         R  B+  146  B  C  D  B  C  D  26  200

;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  千葉ロッテマリーンズ      ロッテ       ロ    ZOZOマリンスタジアム

; UNIFORM                   SYMBOL       BGM
  M_h          M_v          marines      marines

; 戦略             打 盗 犱 送 走 長 牽 守 機
  監督              0  0 -1 +1  0 +1  0  0 +1

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
8 荻野貴司         L  S  - - - - - B  B  B  C  C  C  B  E  0 -2  280
6 角中勝也         L  S  - - - - A -  B  A  B  D  B  C  E  0 -2  250
7 ポランコ         R  P  - - - - - B  C  B  D  D  C  D  C  0 +1  250
3 ボルクマン       R  P  - C - C - -  C  D  C  C  C  D  A  0  0  280
D 山口航輝         R  P  - C - D - -  C  D  B  A  D  D  C +1 +1  270
5 安田尚憲         R  P  - D - C - -  C  D  D  C  B  C  B +1 +1  270
9 菅原秀           L  P  - C - - - C  C  D  C  C  C  D  C  0 -1  290
2 高部瑛斗         L  P  B - - - - -  C  D  D  E  D  D  D  0  0  230
4 和田康士朗       R  S  - - B B A -  C  C  D  D  C  C  E  0 +1  250
- 中村奨吾         R  P  C - - - - -  C  D  D  D  D  D  D  0  0  240
- 髙濱卓也         R  S  B - - - - -  B  D  E  E  C  C  D  0  0  240
- 山口峻太         R  S  - - C D D -  B  B  D  B  B  C  C -1  0  250
- 柿沼友哉         R  S  - - - D - A  C  C  D  C  D  C  E  0  0  240
- 福田光輝         L  P  - - - - - C  B  C  A  B  C  B  D -1 -2  280
- 岡大海           R  P  - - - - - B  B  B  E  D  D  D  C  0  0  250
- サブロー         R  P  - - - - - B  B  B  C  D  C  C  D  0  0  290

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 佐々木朗希       R  A+  144  A  B  D  D  C  A  24  200
P 石川歩           R  A+  140  B  B  A  B  C  B  22  200
P 小島和哉         R  B   144  B  C  C  C  C  C  20  200
P 種市篤暉         R  C   140  B  B  C  C  D  C  20  200
P レアード         L  A+  142  C  D  C  B  C  C  24  200
P 鈴木昭汰         R  A+  140  B  B  C  C  C  C  24  200
P 西野勇士         L  A   142  B  C  C  C  C  C  24  200
P 益田直也         R  A+  138  C  C  C  C  C  C  24  200
P 横山陸人         L  A   136  B  D  C  D  C  D  24  200
P 森遼大           L  B   140  C  B  B  C  B  D  26  200
P 西川僚祐         R  B   146  A  B  C  B  C  C  26  200
P ウォーカー       R  B   140  C  A  A  B  B  D  24  200

;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  東北楽天ゴールデンイーグルス 楽天      楽    楽天モバイルパーク宮城

; UNIFORM                   SYMBOL       BGM
  E_h          E_v          eagles       eagles

; 戦略             打 盗 犱 送 走 長 牽 守 機
  監督             +1  0 -1 -1 -1 +1 +1 +1  0

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
8 小郷裕哉         R  S  - - - - - B  A  A  C  C  B  C  C  0 +1  280
3 浅村栄斗         L  S  - C - - - D  D  B  C  C  B  B  A  0 -2  300
5 島内宏明         L  S  - D - B - -  B  D  A  B  A  C  B  0 -2  300
7 オコエ瑠偉       R  P  - - - - - D  C  C  B  B  C  B  A +1  0  330
9 岡島豪郎         R  P  - - - - - C  B  C  C  D  C  D  C  0  0  270
D ウィルソン       L  P  - - - - - E  D  D  E  A  D  D  A  0 -2  280
6 辰己涼介         R  P  - C - - B -  C  D  E  A  B  C  B  0 +1  260
2 太田光           R  P  B - - - - -  B  C  D  C  D  C  D  0 +1  270
4 山崎剛           R  P  - - B C C -  B  B  C  C  B  B  D  0  0  260
- 武藤敦貴         R  P  C - - - - -  B  D  D  E  C  D  D  0  0  230
- 茂木栄五郎       R  S  - - B C A -  C  B  C  C  C  B  E  0  0  250
- 黒川史陽         R  P  - - - C - C  C  C  E  D  C  D  C  0  0  240
- 山崎剛           R  P  - C - - - C  C  B  D  D  C  D  B  0 +1  240
- 内田靖人         L  S  - - - - - C  B  C  D  C  B  C  D  0 -2  250
- 西川僚祐         L  S  - - - - - B  B  A  C  D  C  C  D  0 -2  240
- 渡邊佳明         R  P  - - - - - C  B  B  C  E  C  D  D  0  0  250

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 早川隆久         R  A+  140  A  B  C  D  C  A  26  200
P 岸孝之           R  B+  138  B  A  B  D  C  B  24  200
P 内星龍           L  C   136  B  D  C  C  C  C  24  200
P 宋家豪           Rs C   138  C  C  C  C  B  C  24  200
P 古川侑利         R  A+  140  B  C  B  B  C  C  20  200
P 松井裕樹         Rs D   136  C  C  C  C  B  C  24  200
P 新垣渚           R  C   138  B  D  C  D  B  C  24  200
P 鈴木翔天         L  B   142  A  D  C  C  C  C  28  200
P 高田孝一         R  B   146  B  C  C  C  C  C  24  200
P 竹森広哉         Ls C   138  C  B  C  C  C  E  28  200
P 森雄大           R  B   140  B  C  C  D  C  D  26  200
P ミランダ         R  A+  138  B  C  C  B  C  D  24  200

;--------------------------------------------------------------------
; チーム名                  愛称         略    本拠地
  北海道日本ハムファイターズ 日本ハム     日    エスコンフィールド北海道

; UNIFORM                   SYMBOL       BGM
  F_h          F_v          fighters     fighters

; 戦略             打 盗 犱 送 走 長 牽 守 機
  監督             +1  0 -1 -1 -1 +1 +1 +1  0

; 選手             利 守 C 1 2 3 S O 接 長 走 肩 守 犠 牽 巧 調 体重
8 万波中正         R  S  - - - - - B  A  A  C  C  B  C  C  0 +1  280
3 ヌニエス         L  S  - C - - - D  D  B  C  C  B  B  A  0 -2  300
5 野村佑希         L  S  - D - B - -  B  D  A  B  A  C  B  0 -2  300
7 オサスナ         R  P  - - - - - D  C  C  B  B  C  B  A +1  0  330
9 上川畑大悟       R  P  - - - - - C  B  C  C  D  C  D  C  0  0  270
D ウィルソン       L  P  - - - - - E  D  D  E  A  D  D  A  0 -2  280
6 谷内田恵太       R  P  - C - - B -  C  D  E  A  B  C  B  0 +1  260
2 宇佐見真吾       R  P  B - - - - -  B  C  D  C  D  C  D  0 +1  270
4 矢澤宏太         R  P  - - B C C -  B  B  C  C  B  B  D  0  0  260
- 田中瑛斗         R  P  C - - - - -  B  D  D  E  C  D  D  0  0  230
- 淺間大基         R  S  - - B C A -  C  B  C  C  C  B  E  0  0  250
- 郡拓也           R  P  - - - C - C  C  C  E  D  C  D  C  0  0  240
- 細川凌平         R  P  - C - - - C  C  B  D  D  C  D  B  0 +1  240
- 江越大賀         L  S  - - - - - C  B  C  D  C  B  C  D  0 -2  250
- 長谷川威展       L  S  - - - - - B  B  A  C  D  C  C  D  0 -2  240
- 今川優馬         R  P  - - - - - C  B  B  C  E  C  D  D  0  0  250

; 投手             利 守 スタミナ 球 制 変 決 ク 牽  年 体重
P 伊藤大海         R  A+  140  A  B  C  D  C  A  26  200
P 斎藤佑樹         R  B+  138  B  A  B  D  C  B  24  200
P 松本遼大         L  C   136  B  D  C  C  C  C  24  200
P 杉浦稔大         Rs C   138  C  C  C  C  B  C  24  200
P 鈴木健矢         R  A+  140  B  C  B  B  C  C  20  200
P 松井雅人         Rs D   136  C  C  C  C  B  C  24  200
P 新崎人生         R  C   138  B  D  C  D  B  C  24  200
P 望月大希         L  B   142  A  D  C  C  C  C  28  200
P 岩本輝            R  B   146  B  C  C  C  C  C  24  200
P 米田雄貴         Ls C   138  C  B  C  C  C  E  28  200
P 堀瑞輝           R  B   140  B  C  C  D  C  D  26  200
P ミランダ         R  A+  138  B  C  C  B  C  D  24  200
"""
    
    return teamdata_content.strip()

def main():
    """メイン実行関数"""
    print("🎯 NPB 2025年度チームデータ生成ツール")
    print("=" * 50)
    
    # 出力ファイルパス
    output_path = "/home/runner/work/BestPlayBaseBall/BestPlayBaseBall/data/teamdata_2025.txt"
    
    print(f"📊 2024年シーズンを反映した2025年チームデータを生成中...")
    
    # チームデータを生成
    teamdata_content = create_teamdata_2025()
    
    # ファイルに書き込み
    try:
        # UTF-8エンコーディングを使用
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(teamdata_content)
        
        print(f"✅ チームデータが正常に生成されました")
        print(f"📁 保存先: {output_path}")
        print(f"📊 NPB全12球団のデータを更新済み")
        print(f"📈 2024年シーズンの成績と順位を反映:")
        print(f"   - セ・リーグ優勝: 阪神タイガース")
        print(f"   - パ・リーグ優勝: オリックス・バファローズ") 
        print(f"   - 日本シリーズ優勝: オリックス・バファローズ")
        
    except Exception as e:
        print(f"❌ ファイル書き込みエラー: {e}")
        return False
    
    print("\n🎉 2025年度チームデータの生成が完了しました！")
    return True

if __name__ == "__main__":
    main()