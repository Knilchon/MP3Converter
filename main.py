import os
from flask import Flask, send_file, request, abort
import yt_dlp

app = Flask(__name__)

# Define the path where MP3 files will be temporarily stored
DOWNLOAD_FOLDER = 'downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_audio(video_id):
    """
    Download the audio of a YouTube video as an MP3.
    """
    output_template = os.path.join(DOWNLOAD_FOLDER, f"{video_id}")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_template,  # Save the file with video ID as the name
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'https://www.youtube.com/watch?v={video_id}'])
    
    return output_template

@app.route('/<video_id>', methods=['GET'])
def download_mp3(video_id):
    """
    Flask route to download the YouTube video as an MP3 and send it to the user.
    Expects a 'video_id' parameter in the request.
    """
        
    if not video_id:
        abort(400, "Missing 'video_id' parameter")

    try:
        # Download the audio as MP3
        mp3_file = download_audio(video_id)
        print(mp3_file)
        print(mp3_file)
        print(mp3_file)
        print(mp3_file)
        # Send the file back to the client
        return send_file(f"{mp3_file}.mp3", as_attachment=True, download_name=f"{video_id}.mp3", mimetype='audio/mpeg')
    
    except Exception as e:
        abort(500, f"Error processing video: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
