## デプロイメモ

1. venv で Python 実行環境構築

'''command
python -m venv venv
.\venv\Scripts\activate
pip install -r .\requirements.txt
'''

2. OCR（Tesseract-OCR）のインストール
   https://github.com/UB-Mannheim/tesseract/wiki
   tesseract-ocr-w32-setup-v5.0.1.20220118.exe (32 bit)
   ダウンロードしてインストール管理者でインストールして以下のパスになるようにすること。
   C:\Program Files (x86)\Tesseract-OCR

3. chromediriver の配置（実行する Chrome のバージョンと合わせる）
   https://chromedriver.chromium.org/downloads
   chromedriver_win32.zip
   解凍して exe をこのプロジェクト配下に配置

4. ファルダ作成
   .\data
   .\data\week_data
   .\temp_image

## 仕様

10:00 ~ 30分(游タイムリストと游タイム対象台番号を出力)
batch_yuu_time_csv_create.exe

10:40 ~ 15分(すべての台番号を出力)
batch_all_dai_list_csv_create.exe

10:57 ~ 30毎 20回繰り返し（游タイム対象台だけ出玉情報を取得　上書き）
batch_boom_real_time_csv_create.exe
11:07 ~ 30毎 20回繰り返し（游タイム対象台だけ出玉情報を取得　上書き）
batch_akasaka_real_time_csv_create.exe

23:00 ~ 1時間（すべての台の出玉情報を取得　上書き＋Weekフォルダに日ごと名で作成）
batch_all_dai_info_csv_json_create.exe

01:00 ~ 1分（Weekフォルダから７日のデータを集計）
batch_total_csv-json_create.exe


