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

- その他、Jekyll用のファイルなど

# プログラムの作成方法

1. プログラムの発表枠をmarkdownで記述する。  
   20XX/schedule-overview.md

2. 各研究会にテキストで発表順を書いてもらう。  
   20XX/sigs/OS.txt など。  
   情報処理学会のホームページに掲載する形式とほぼ同様。

3. 発表枠に発表順の情報を埋め込む。  
   `python embed-talks-to-sched.py`  
   20XX/schedule-details.md が生成される。
