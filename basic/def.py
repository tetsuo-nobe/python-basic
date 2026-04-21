'''
Python の基本
関数の例
'''

# def 文を使って関数を定義する
# def 文の次の行はインデントをずらす (2または4文字程度)
# そのずらした行が def による関数定義の範囲

# 関数の定義 
def say_hello(name):
    return 'Hello! ' + name

# 関数を呼び出して結果を受け取る (1回目)
result = say_hello('John Doe')

# 結果の表示 (1回目)
print(result)

# 関数を呼び出して結果を受け取る (2回目)
result = say_hello('Jane Doe')

# 結果の表示 (2回目)
print(result)

# 外部ファイルのインポート
import external

# 外部ファイルの関数の実行
result = external.add_number(10, 5)
print(result)

# 関数の組み合わせ
print("2+8=" + str(external.add_number(2,8)))

