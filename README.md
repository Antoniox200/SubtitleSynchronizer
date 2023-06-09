# SubtitleSynchronizer

This repository contains a simple GUI application for the FFSubSync command line tool, built with PyQt5. FFSubSync is used to synchronize subtitles with video files. This GUI provides a user-friendly interface to this tool.

The repository contains both the Python script and the executable file for Windows. The Python script can be used on any platform, while the executable is specifically for Windows.

## Prerequisites

The FFSubSync GUI requires FFmpeg and FFSubSync to be installed on your system.

### FFmpeg

FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams. 

#### MacOS:

To install FFmpeg on MacOS, you can use the Homebrew package manager:

`brew install ffmpeg`

#### Windows:

For Windows users, make sure FFmpeg is on your path and can be referenced from the command line! You can download it from the [official FFmpeg site](https://ffmpeg.org/download.html) and then [add it to your PATH](https://www.wikihow.com/Install-FFmpeg-on-Windows).

### FFSubSync

Next, you need to install the FFSubSync Python package. It's compatible with Python >= 3.6.

You can install it using pip:

`pip install ffsubsync`

If you want to live dangerously, you can grab the latest version as follows:

`pip install git+https://github.com/smacke/ffsubsync@latest`

## Usage

### Windows:

For Windows users, you can simply run the .exe file included in this repository.

### Other platforms:

For users on other platforms (or if you want to run the Python script directly), you can do so with the following command:

`python ffsubsync_gui.py`

Once the application is open, drag and drop your video and subtitle files into the appropriate boxes, then click the 'Sync' button to synchronize your subtitles.

Please note: the output .srt file will be saved in the same directory as the original subtitle file, with "synchronized" appended to the original filename.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
