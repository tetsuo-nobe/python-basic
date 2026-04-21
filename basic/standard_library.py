'''
Python の基本
標準ライブラリの例（os, time, pprint, json, random）
'''

import os
import time
import pprint
import json
import random

# --- 例 1: os --- カレントディレクトリ（現在の作業フォルダ）を取得する

current_dir = os.getcwd()
print("現在のディレクトリ: " + current_dir)

# カレントディレクトリ内のファイル一覧を取得する
file_list = os.listdir(current_dir)
print("ファイル一覧:")
print(file_list)

# --- 例 2: time --- 処理の経過時間を計測する

start = time.time()

# 2秒間処理を停止する
print("2秒間待機します...")
time.sleep(2)

end = time.time()
elapsed = end - start
print(f"経過時間: {elapsed:.2f} 秒")

# --- 例 3: pprint --- 辞書型データを見やすく表示する

item = {
    '商品名': 'りんご',
    'カテゴリ': '果物',
    '単価': 150,
    '仕入先': {
        '仕入先コード': 1001,
        '仕入先名': '田中商店'
    },
    '関連商品': ['みかん', 'バナナ', 'スイカ']
}

# print だと1行にまとめて表示される
print("--- print の場合 ---")
print(item)

# pprint だと見やすく整形して表示される
print("--- pprint の場合 ---")
pprint.pprint(item)

# --- 例 4: json --- 辞書型データを JSON 文字列に変換する

# 辞書型 → JSON 文字列に変換（日本語が文字化けしないように ensure_ascii=False を指定）
json_str = json.dumps(item, ensure_ascii=False, indent=2)
print("--- JSON 文字列 ---")
print(json_str)

# JSON 文字列 → 辞書型に変換
restored_item = json.loads(json_str)
print("--- JSON から復元した辞書型データ ---")
print(restored_item['商品名'])

# --- 例 5: random --- ランダムな値を生成する

# 1 から 10 までのランダムな整数を生成
random_num = random.randint(1, 10)
print(f"ランダムな数値: {random_num}")

# リストからランダムに1つ選ぶ
fruits = ['りんご', 'バナナ', 'さくらんぼ', 'みかん', 'スイカ']
chosen = random.choice(fruits)
print(f"ランダムに選ばれた果物: {chosen}")

# リストの順番をランダムに並び替える
random.shuffle(fruits)
print(f"シャッフル後: {fruits}")
