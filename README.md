# python-basic
Python の基礎のハンズオン

---

## 環境への接続について

**このワーク環境は、ワーク実施時だけの一時的な環境になります。**

1. インストラクターより提示された **2桁の番号** を覚えておいてください。

1. インストラクターが指定する AWS アカウント、IAM ユーザー、パスワードを使用して AWS マネジメントコンソールにサインインします。
    - 環境へのアクセスは [こちら](https://tnobep.signin.aws.amazon.com/console)
1. リージョンは　**東京リージョン** をご使用ください。
1. Cloud 9 のページを表示します。IAM ユーザー毎に 1つの Cloud 9 IDE が用意されているので、[**開く**] をクリックします。

---

## Cloud 9 の一時認証情報の無効化
1. Cloud 9 画面の右上にある**歯車アイコン**をクリックします。
1. Preferences タブ の左側で **AWS Settings** をクリックします。
1. 右側の **Credentials** にある **AWS managed temporary credentials** トグルを OFFにします。
  ![codepipeline-demo-img](https://eks.nobelabo.net/images/mod7-cloud9.png)
1. Preferences のタブを閉じます。

---

## サンプルの取得

1. Cloud9 の下部のターミナルで下記を実行し、このリポジトリを取得します。
    - ```
      git clone https://github.com/tetsuo-nobe/python-basic.git
      ```
    - ```
      cd python-basic/basic/
      ```
      

