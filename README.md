# Text and Audio Summarizer
このプログラムは，テキストまたは，音声ファイルの内容を要約します．OpenAiのGPT3-5-turboモデルとGoogleのSpeech Recognition APIを使用しています．

## 使用方法
このプログラムはコマンドラインから実行します．
テキストファイルを要約する例：
`python main.py --text path_to_your_text_file.txt`
音声ファイルを要約する例：
`python main.py --audio path_to_your_audio_file.wav`

## 必要なパッケージ
pip install openai==0.28
pip install SpeechRecongnition
