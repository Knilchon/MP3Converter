from pytube import YouTube
from pydub import AudioSegment

# Download YouTube video
def install(id):
    yt = YouTube("https://www.youtube.com/watch?v=" + id)
    stream = yt.streams.filter(only_audio=True).first()
    output_file = stream.download()

    # Convert to mp3 using pydub
    audio = AudioSegment.from_file(output_file)
    audio.export("output.mp3", format="mp3")