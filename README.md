SWoPP 作業用レポジトリ
======================

# ディレクトリ構造

- archives/
  過去の資料など

- 2016/
  SWoPP2016のプログラム作成用
- 2017/
  SWoPP2017のプログラム作成用
- 2018/
  SWoPP2018のプログラム作成用 
- ... つづく

- その他、Jekyll用のファイルなど

# プログラムの作成方法
1. 前年度ディレクトリをコピーし、新年度ディレクトリを作る。  
cp -r 20XX 20YY

2. \_config.yaml を適切に修正する

3. \_sass/\_print.scss 内に新年度用の部屋名を記載する。

4. 20YY/schedule-details.md 及び 20YY/schedule-overview.md の最初の5行を適切に編集する。  
   基本的にはpermalinkを変更しURLパスを決める

5. プログラムの発表枠をmarkdownで記述する。この枠組み内の枠名部分が各研究会の発表順ファイルの枠名と置換される。  
   20XX/schedule-overview.md

6. 各研究会にテキストで発表順を書いてもらう。  
   20XX/sigs/OS.txt など。  
   情報処理学会のホームページに掲載する形式とほぼ同様。

7. 発表枠に発表順の情報を埋め込む。  
   `python embed-talks-to-sched.py`  
   20XX/schedule-details.md が生成される。
   
# 研究会幹事への作成依頼例

本年度もgithub を利用しましたプログラムの収集を行いたく、  
各会幹事の皆さまには情報を以下の手法で申告いただければ幸いです。  

1. github よりレポジトリをクローンする  
$ git clone https://github.com/swopp/swopp.github.io.git  

2. ディレクトリ 2018/sigs 内にある該当研究会のファイルフォーマットを参考に  
  枠名：(研究会)-(整数)  
枠タイトル：●(タイトル)  
座長：　座長：(座長名)  
各発表のタイトル：\*\*(タイトル)\*\*、  
および著者名  
  
の一覧を記述し、同様の名前で 2019/sigs に保存ください。

3.  2019/ 直下にあります py ファイルを実行してください  
$ python embed-talks-to-sched.py
(2020版からPython3限定になっているようなので注意)

4. github にデータをコミットする  
$ git add *  
$ git commit

なお、4に関しましては、github のアカウント、およびそのアカウントの  
swopp グループへのパーミッションが必要です。  
githubアカウントをご用意の上、報告いただければパーミッション設定を  
行いますのでご連絡ください。（昨年度設定された方は問題ありません）
  
不明点がありましたら連絡をお願いいたします。
