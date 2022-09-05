import os
from data import Data
from typing import List


class FileReader:
    def __init__(self, data_path: str):
        self.data = self._get_file(data_path)

    def _get_file(self, data_path: str):
        file_to_data = Data()
        try:
            with open(os.path.abspath(data_path)) as file:
                file_to_data.add_path(data_path)
                for line in file:
                    file_to_data.add_youtube_links(line.rstrip())

        except Exception as exception:
            exception_msg = str(exception)
            print(exception_msg)

        return file_to_data

    def run_cmds(self):
        if self.data.has_data():
            for link in self.data.youtube_links:
                os.system(
                    f"youtube-dl -o \"{self.data.path}\" --prefer-ffmpeg --extract-audio --audio-format mp3 \"{link}\"")

        return False if self.data.has_data() else True
