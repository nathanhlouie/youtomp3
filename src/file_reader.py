import os
from data import Data
from typing import List


class FileReader:
    def __init__(self):
        self.data = self._get_file()
        self.cmds = self._parse_cmds(self.data)

    def _get_file(self):
        try:
            with open(os.path.abspath()) as file:
                file_to_data = Data()
                file_to_data.add_user(file.readline())
                for line in file:
                    file_to_data.add_youtube_links(line.rstrip())
                return file_to_data

        except Exception as exception:
            exception_msg = str(exception)
            print(exception_msg)

        return None

    def _parse_cmds(self, data: Data):
        cmds = []
        for link in data.youtube_links:
            cmds.append(
                f'youtube-dl -o {data.path} --prefer-ffmpeg --extract-audio --audio-format mp3 {link}')
        return cmds
