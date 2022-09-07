import os
from data import Data
from yt_dlp import YoutubeDL


class FileReader:
    def __init__(self, data_path: str):
        self.data = self._get_file(data_path)

    def _get_file(self, data_path: str):
        file_to_data = Data()
        try:
            with open(os.path.abspath(data_path)) as file:
                file_to_data.add_path(data_path)
                for line in file:
                    if line != "":
                        file_to_data.add_youtube_links(line.rstrip())

        except Exception as exception:
            exception_msg = str(exception)
            print(exception_msg)

        return file_to_data

    def run_cmds(self):

        if self.data.has_data():
            ydl_opts = {'format': 'bestaudio/best',
                        'outtmpl': self.data.path,
                        'ffmpeg_location': os.path.join(os.path.dirname(__file__), 'ffmpeg'),
                        'postprocessors': [{

                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                        }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download(self.data.youtube_links)

        return True if self.data.has_data() else False
