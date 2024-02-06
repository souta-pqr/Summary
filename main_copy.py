from pydub import AudioSegment
from pydub.playback import play
import requests
from bs4 import BeautifulSoup
import openai
import os

def fetch_and_save_xml(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'xml')
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(soup.prettify()))

def read_and_parse_xml(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    soup = BeautifulSoup(content, 'xml')
    news_item = soup.find('item')
    return news_item.title.text, news_item.description.text

def summarize_text(full_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたはニュース記事を要約するための助け役です。"},
            {"role": "user", "content": f"次のニュース記事を要約してください: {full_text}"}
        ]
    )
    return response['choices'][0]['message']['content']

def save_summary(summary, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary)

def execute_command(command):
    os.system(command)

def play_audio(filename):
    song = AudioSegment.from_wav(filename)
    play(song)

# パラメータ設定
url = "https://news.google.com/rss?hl=ja&gl=JP&ceid=JP:ja"
xml_filename = "google_news.xml"
summary_filename = "summary.txt"
audio_filename = "audio.wav"

# xmlファイルの取得と保存
fetch_and_save_xml(url, xml_filename)

# xmlファイルの読み込みと解析
title, description = read_and_parse_xml(xml_filename)
full_text = title + " " + description

# 要約
openai.api_key = ''
summary = summarize_text(full_text)
print(f"Summary of the news article: {summary}")

# 結果をテキストファイルにも出力
save_summary(summary, summary_filename)

# summary.txtの内容を音声合成するためのコマンドを作成
execute_command(f'echo -n "$(cat {summary_filename})" >text.txt')
execute_command('curl -s -X POST "127.0.0.1:50021/audio_query?speaker=3" --get --data-urlencode text@text.txt > query.json')
execute_command('curl -s -H "Content-Type: application/json" -X POST -d @query.json "127.0.0.1:50021/synthesis?speaker=3" > ' + audio_filename)

# 音声合成の結果を再生
play_audio(audio_filename)
