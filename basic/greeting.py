'''
Python の基本
if __name__ == "__main__" の例（import される側のファイル）

このファイルは main.py から import されます。
直接実行した場合と、import された場合で動作が変わることを確認してください。
'''

def say_hello(name):
    return f"こんにちは、{name}さん！"

def say_goodbye(name):
    return f"さようなら、{name}さん！"

# このファイルを直接実行したときだけ、以下の処理が実行される
# 他のファイルから import されたときは実行されない
if __name__ == "__main__":
    print("--- greeting.py を直接実行しました ---")
    print(say_hello("太郎"))
    print(say_goodbye("太郎"))
