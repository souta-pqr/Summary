# Google News Summarizer
GoogleのRSSフィードから最新のニュースを取得し、OpenAIのGPT-3.5-turboモデルを使用してニュースを要約し、その要約をVOICEVOXのテキスト読み上げエンジンを使用して音声に変換します。

## 使用方法
1. VOICEVOX Engineのリポジトリをクローンし、そのREADMEに従ってエンジンをセットアップし起動。
```
git clone https://github.com/VOICEVOX/voicevox_engine.git
```
- クローンした後、そのディレクトリに移動し、Dockerコンテナを作成して実行。
### CPUを使用する場合
```
docker pull voicevox/voicevox_engine:cpu-ubuntu20.04-latest
docker run --rm -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:cpu-ubuntu20.04-latest
```
### GPUを使用する場合
```
docker pull voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
docker run --rm --gpus all -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
```

2. スクリプト内のOpenAI APIキーを設定、実行。
```
python main.py
```

## 必要なパッケージ
```
pip install pydub requests beautifulsoup4 openai
```
