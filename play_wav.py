from pydub import AudioSegment
from pydub.playback import play

# コードが実行し終わったら音声を再生
# ここにあなたのコードを書く

# wavファイルを開く
song = AudioSegment.from_wav("audio.wav")

# 音声を再生
play(song)
