'''
Python の基本
for 文の例
'''

# for 文で繰り返し処理を行う
# for 文の次の行はインデントをずらす (2または4文字程度)
# そのずらした行が for 文の範囲

# for 文 (1 から 10 までを表示) 
for num in range(1,11):
    print(num)
    
# フルーツのデータをもった list 型変数の定義
fruits = ['りんご','バナナ','さくらんぼ']

# for 文 (fruitsのすべてのデータを表示) 
for item in fruits:
    print(item)
