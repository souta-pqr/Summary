import argparse
import openai
import speech_recognition as sr

# OpenAIのAPIキーを設定します。
openai.api_key = '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'

def summarize_text(text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text},
            {"role": "assistant", "content": "上記のテキストを要約してください。"},
        ]
    )
    return response['choices'][0]['message']['content']

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='ja-JP')
        return text

def main():
    parser = argparse.ArgumentParser(description='Summarize text or transcribe and summarize audio.')
    parser.add_argument('--text', help='The text to summarize.')
    parser.add_argument('--audio', help='The audio file to transcribe and summarize.')
    args = parser.parse_args()

    if args.text:
        summary = summarize_text(args.text)
        print(f"要約: {summary}")
    elif args.audio:
        text = transcribe_audio(args.audio)
        summary = summarize_text(text)
        print(f"元のテキスト: {text}")
        print(f"要約: {summary}")
    else:
        print("テキストまたは音声ファイルを指定してください。")

if __name__ == "__main__":
    main()
