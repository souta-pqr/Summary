# Google News Summarizer
GoogleのRSSフィードから最新のニュースを取得し、OpenAIのGPT-3.5-turboモデルを使用してニュースを要約し、その要約をVOICEVOXのテキスト読み上げエンジンを使用して音声に変換します。

## 使用方法
1. スクリプトを実行
   ```
   python main.py
   ```
2. 要約したいニュースの番号を入力(1~30)
3. 記事が要約され，ずんだもんが結果を話すのを待つ
4. 0で終了，1~30で再度要約．

## 必要なパッケージ
- pydub
- requests
- BeautifulSoup
- openai
- os
