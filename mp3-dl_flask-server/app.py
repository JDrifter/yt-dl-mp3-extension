from flask import Flask, request
import yt_dlp
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def download_video():
    data = request.get_json()
    url = data['url']
    
    # Set the download and conversion directory paths
    download_dir = '/app/downloads'
    
    # Configure the options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{download_dir}/%(title)s.%(ext)s',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', 'video')
            video_title = video_title.replace('/','-') # No directory confusion
            file_path = f'{download_dir}/{video_title}.webm'
            ydl.download([url])
        
        # Convert the downloaded file to MP3 using ffmpeg
        output_path = f'{download_dir}/{video_title}.mp3'
        subprocess.run(['ffmpeg', '-i', file_path, '-vn', '-acodec', 'libmp3lame', '-y', output_path], check=True)
        
        # Delete .webms
        subprocess.run(['rm', 'downloads/*.webm'], check = True)
        return 'Download and conversion complete!'
    except (yt_dlp.DownloadError, subprocess.CalledProcessError) as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

