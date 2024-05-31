from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pytube import YouTube
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = 'downloads'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        # Get YouTube URL from form
        url = request.form['url']
        yt = YouTube(url)

        # Get video information
        title = yt.title
        views = yt.views
        cover_image = yt.thumbnail_url
        length = yt.length
        stream = yt.streams.get_highest_resolution()

        # Download the video
        if not os.path.exists(DOWNLOAD_FOLDER):
            os.makedirs(DOWNLOAD_FOLDER)
        file_path = stream.download(output_path=DOWNLOAD_FOLDER)

        # Get file size
        size = os.path.getsize(file_path)

        # Calculate length in minutes and seconds
        length_minutes = length // 60
        length_seconds = length % 60

        # Get relative file path for download link
        file_name = os.path.basename(file_path)

        # Render result page
        return render_template('result.html', title=title, views=views, cover_image=cover_image, length_minutes=length_minutes, length_seconds=length_seconds, size=size, file_name=file_name)

    except Exception as e:
        return redirect(url_for('error', error_message=str(e)))

@app.route('/error')
def error():
    error_message = request.args.get('error_message')
    return render_template('error.html', error=error_message)

@app.route('/downloads/<filename>')
def serve_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
