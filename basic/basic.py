# # は行単位のコメント

"""
ダブルコーテーション 3つに囲まれた行はすべてコメント
(シングルコーテーションでも OK)
"""

# message という変数に Hello! という文字列を代入
hello_message = "Hello! "  
print(hello_message)

# 文字列は シングルコーテーションで囲んでもいいが、統一するのがのぞましい
world_message = 'World!'  
print(world_message)

# Pythonではインデントを揃える必要があります。
# よって1文字ずれている下記はエラーになります。
# print(hello_message)

# 文字列の連結
your_name = "John"
print(hello_message + your_name)
print(f"{hello_message}{your_name}")

# 数値型の変数の定義
english_score = 80

# 文字列に変換
english_score_string = str(english_score)

# 下記は 81 になります。
print(english_score + 1)

#下記はエラーになります。
#print(english_score_string + 1)

# 四則演算
num1 = 10
num2 = 2
num3 = num1 + num2
print(f"{num1} に {num2} を足すと {num3} です。")

num3 = num1 * num2
print(f"{num1} に {num2} を掛けると {num3} です。")

num3 = num1 - num2
print(f"{num1} から {num2} を引くと {num3} です。")

num3 = num1 / num2
print(f"{num1} を {num2} で割ると {num3} です。")

num3 = num1 % num2
print(f"{num1} を {num2} で割った余りは {num3} です。")

# list 型では複数の値をまとめて保持できます。
product_list = [
    "keyboard",
    "mouse",
    "monitor"
]

print(product_list[0])
print(product_list[1])
print(product_list[2])

# list型の最後尾に値を追加
product_list.append("headphone")
print(product_list[3])

# 他のファイルの変数をインポートして使用する
# ファイル名のみ指定するパターン
import external
print(external.my_num_value)
print(external.my_str_value)

# ファイル名と変数名を明示的に指定するパターン
from external import my_num_value, my_str_value
print(my_num_value)
print(my_str_value)

# ファイル名と変数名を明示的に指定して変数に別名をつけて使用するパターン
from external import my_num_value as my_num, my_str_value as my_str
print(my_num)
print(my_str)

