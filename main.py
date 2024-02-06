from pydub import AudioSegment
from pydub.playback import play
import requests
from bs4 import BeautifulSoup
import openai
import os

# GoogleのニュースのRSSフィードのURLを指定します。
url = "https://news.google.com/rss?hl=ja&gl=JP&ceid=JP:ja"

# URLからデータを取得します。
response = requests.get(url)

# レスポンスのテキストを解析します。
soup = BeautifulSoup(response.text, 'xml')

# XMLファイルとして保存します。
with open("google_news.xml", "w", encoding="utf-8") as f:
   f.write(str(soup.prettify()))

# OpenAIのAPIキーを設定します。
openai.api_key = ''

# XMLファイルからニュース記事を読み込みます。
with open("google_news.xml", "r", encoding="utf-8") as f:
   content = f.read()

soup = BeautifulSoup(content, 'xml')
news_item = soup.find('item')

# ニュース記事のタイトルと説明を取得します。
title = news_item.title.text
description = news_item.description.text

# 記事の本文を結合します。
full_text = title + " " + description

print(f"Title of the news article: {title}\n")

# GPT-3.5-turboを使用して記事を要約します。
response = openai.ChatCompletion.create(
 model="gpt-3.5-turbo",
 messages=[
       {"role": "system", "content": "あなたはニュース記事を要約するための助け役です。"},
       {"role": "user", "content": f"次のニュース記事を要約してください: {full_text}"}
   ]
)

summary = response['choices'][0]['message']['content']

print(f"Summary of the news article: {summary}")

# 結果をテキストファイルにも出力します。
with open("summary.txt", "w", encoding="utf-8") as f:
   f.write(summary)  # "Summary of the news article: "を削除

# summary.txtの内容を音声合成するためのコマンドを作成します。
command = 'echo -n "$(cat summary.txt)" >text.txt'

# コマンドを実行します。
os.system(command)

# 音声合成のためのクエリを作成します。
command = 'curl -s -X POST "127.0.0.1:50021/audio_query?speaker=3" --get --data-urlencode text@text.txt > query.json'

# コマンドを実行します。
os.system(command)

# 音声合成を実行します。
command = 'curl -s -H "Content-Type: application/json" -X POST -d @query.json "127.0.0.1:50021/synthesis?speaker=3" > audio.wav'

# コマンドを実行します。
os.system(command)

# wavファイルを開く
song = AudioSegment.from_wav("audio.wav")

# 音声を再生
play(song)