'''
Python の基本
if __name__ == "__main__" の例

__name__ は Python が自動的に設定する特殊な変数です。
- ファイルを直接実行したとき → __name__ は "__main__" になる
- 他のファイルから import されたとき → __name__ はファイル名（モジュール名）になる

この仕組みにより「直接実行したときだけ動く処理」を書くことができます。

動作確認の手順:
  1. python main.py を実行する
     → main.py の __name__ は "__main__" なので if ブロック内が実行される
     → greeting.py は import されただけなので greeting.py の if ブロック内は実行されない

  2. python greeting.py を実行する
     → greeting.py の __name__ が "__main__" になり、greeting.py の if ブロック内が実行される
'''

from greeting import say_hello, say_goodbye

# main.py を直接実行したときだけ、以下の処理が実行される
if __name__ == "__main__":
    print("--- main.py を直接実行しました ---")
    print(say_hello("花子"))
    print(say_goodbye("花子"))
