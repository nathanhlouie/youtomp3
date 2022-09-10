youtomp3 – download videos from youtube.com as mp3s

- [INSTALLATION](#installation)
- [DESCRIPTION](#description)
- [USE](#use)
- [COPYRIGHT](#copyright)

# INSTALLATION

To build the executable, you must have Python3 and PyInstaller installed, then cd into youtomp3/src/ and run the command:

```
pyinstaller -F --clean --add-binary ffmpeg:. youtomp3.py
```

The binary executable will be found in the dist folder.

# DESCRIPTION

**youtomp3** is a simple Python GUI application to download videos from Youtube.com as mp3 files to your local files. Currently, it only works on macOS.

# USE

Running the executable will open the application window.

![image](https://user-images.githubusercontent.com/53024905/189504450-3ac53345-7f2b-40d6-9612-43b33ddd1e4a.png)

Browse your local files to attach a **.txt** file with each youtube link separated by a new line:

![image](https://user-images.githubusercontent.com/53024905/189504536-571ee2b0-9f99-4ef1-8923-224b291cc2a7.png)

Click the download button, wait for the terminal process to complete, and the files will be downloaded in the user's /Downloads folder.

# COPYRIGHT

youtomp3 is intended to be used responsibly, please follow fair use and copyright laws.
