# Python 基礎 サンプルコード

Python の基本的な文法や機能を学ぶためのサンプルコード集です。各ファイルにテーマごとのコード例とコメントによる解説を記載しています。

## 前提条件

- Python 3 がインストール済みであること
- ターミナル（コマンドプロンプトなど）から `python` コマンドが実行できること

---

## セットアップ

### 1. リポジトリをクローンする

```bash
git clone https://github.com/tetsuo-nobe/python-basic.git
```

### 2. python_basic フォルダに移動する

```bash
cd python-basic/basic
```

### 3. サンプルコードを実行する

```bash
python hello.py
```

---

## ファイル一覧

| ファイル名 | テーマ | 概要 |
|-----------|--------|------|
| `hello.py` | Hello World | `print` 関数で文字列を表示する |
| `basic.py` | 変数・データ型・演算 | 変数の定義、文字列の連結、数値の四則演算、list 型の基本、import の使い方 |
| `external.py` | 外部ファイル | `basic.py` からインポートされる変数を定義したファイル |
| `if.py` | if 文 | `if`、`elif`、`else` による条件分岐 |
| `for.py` | for 文 | `range` や list を使ったループ処理 |
| `def.py` | 関数 | `def` による関数の定義と呼び出し、戻り値の受け取り |
| `dict.py` | 辞書型 | 辞書型データの定義と値の取得、入れ子の辞書、`get()` メソッドの連結による安全なアクセス |
| `try_except.py` | エラー処理 | `try`、`except`、`finally` によるエラーハンドリング |
| `standard_library.py` | 標準ライブラリ | `os`、`time`、`pprint`、`json`、`random` の基本的な使い方 |
| `main.py` / `greeting.py` | `if __name__ == "__main__"` | 直接実行時と import 時の動作の違いを理解する |

---

## 学習の進め方

上記の表の順番に沿って、上から順にファイルを読み進めることを推奨します。各ファイルのコメントを読みながらコードを実行し、動作を確認してください。

