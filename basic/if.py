'''
Python の基本
if 文の例
'''
# 文字列のデータ定義
country = "日本"

# 数値のデータの定義
num1 = 7
num2 = 3
num3 = num1 + num2

# if 文で条件分岐を行う
# if 文の次の行はインデントをずらす (2または4文字程度)
# そのずらした行が if 文の範囲

# 例 1: if のみ
if  country == "日本":
    print("首都は東京です。")

# 例 2: if と else
if country == "日本":
    print("英語ではJapanです。")
else:
    print("日本以外の国ですね。")

# 例 3: if と elif と else 
if  num3 >= 10:
    print('10 以上です。')
elif  num3 >=5:
    print('5 以上 10 未満です。')
else:
    print('5 未満です。')
