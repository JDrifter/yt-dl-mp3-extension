from flask import Flask, request, jsonify
import youtube_dl

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    data = request.get_json()
    if 'url' in data:
        url = data['url']
        if is_youtube_url(url):
            download_youtube_video(url)
            return jsonify({'message': 'Video downloaded successfully!'})
    return jsonify({'message': 'Invalid request or not a valid YouTube URL.'})

def is_youtube_url(url):
    # You can implement your own validation logic here
    return 'youtube.com' in url or 'youtu.be' in url

def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(id)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    app.run(port=8000)