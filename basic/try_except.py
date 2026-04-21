'''
Python の基本
try except の例（エラー処理）
'''

# --- 例 1: 数値の変換エラーをキャッチする ---

# 数値に変換できない文字列
value = "abc"

# try の中でエラーが発生すると except に処理が移る
try:
    num = int(value)
    print(num)
except:
    print("数値に変換できませんでした。")

# --- 例 2: ゼロ除算のエラーをキャッチする ---

num1 = 10
num2 = 0

try:
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("0 で割ることはできません。")

# --- 例 3: リストの範囲外アクセスをキャッチする ---

fruits = ['りんご', 'バナナ', 'さくらんぼ']

try:
    print(fruits[5])
except IndexError:
    print("リストの範囲外です。")

# --- 例 4: 辞書に存在しないキーへのアクセスをキャッチする ---

item = {
    '商品名': 'りんご',
    '単価': 150,
}

try:
    print(item['カテゴリ'])
except KeyError:
    print("指定したキーは辞書に存在しません。")

# --- 例 5: try, except, finally を組み合わせる ---
# finally の中の処理は、エラーが発生してもしなくても必ず実行される

num1 = 10
num2 = 0

try:
    result = num1 / num2
    print(f"計算結果は {result} です。")
except ZeroDivisionError:
    print("0 で割ることはできません。")
finally:
    print("計算処理を終了します。")

# --- 例 6: except でエラー名を指定するケース、指定しないケース、finally を組み合わせる ---

value = "abc"
num2 = 0

try:
    num1 = int(value)
    result = num1 / num2
    print(f"計算結果は {result} です。")
except ZeroDivisionError:
    # 特定のエラーをキャッチする（ゼロ除算）
    print("0 で割ることはできません。")
except:
    # 上の except に該当しないエラーはすべてここでキャッチされる
    print("予期しないエラーが発生しました。")
finally:
    # エラーの有無に関わらず必ず実行される
    print("すべての処理を終了します。")
