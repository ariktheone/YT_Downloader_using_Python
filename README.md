# YouTube Downloader using Flask

This is a simple web application built with Flask that allows users to download YouTube videos.

![YouTube Downloader](images/img1.png)
![YouTube Downloader](images/img2.png)

## Features

- **Download YouTube Videos**: Users can input the URL of a YouTube video and download it directly from the web app.
- **Display Video Information**: Before downloading, the web app displays information about the video, such as title, views, length, and cover image.
- **Error Handling**: If any errors occur during the download process, users are redirected to an error page displaying the error message.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ariktheone/YT_Downloader_using_Python.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/).

3. Enter the URL of the YouTube video you want to download and click the "Download" button.

4. The web app will display information about the video and provide a download link. Click the link to download the video.

## Configuration

- The `DOWNLOAD_FOLDER` variable in `app.py` specifies the directory where downloaded videos will be saved. You can change this to a different directory if needed.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request or you can mail me at [arijitmondal200430@gmail.com](mailto:arijitmondal200430@gmail.com).

## Contributors

Thanks goes to these wonderful people for their contributions:

<div style="display: flex; justify-content: center; align-items: center; gap: 40px; flex-wrap: wrap; margin-top: 20px;">

<div style="text-align: center;">
  <a href="https://github.com/ariktheone" style="text-decoration: none; color: inherit;">
    <img src="https://avatars.githubusercontent.com/u/117704271?v=4" width="100" height="100" style="border-radius: 50%;" alt="ariktheone"/>
    <br>
    <strong>ariktheone</strong>
  </a>
</div>

<div style="text-align: center;">
  <a href="https://github.com/Arighna2003" style="text-decoration: none; color: inherit;">
    <img src="https://avatars.githubusercontent.com/u/121758941?v=4" width="100" height="100" style="border-radius: 50%;" alt="Arighna2003"/>
    <br>
    <strong>Arighna2003</strong>
  </a>
</div>

</div>
