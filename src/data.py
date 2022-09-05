import re


class Data:
    def __init__(self):
        self.user = ""
        self.path = ""
        self.youtube_links = []

    def __str__(self):
        return f"User: {self.user} | Path: {self.path} | Youtube Links: {self.youtube_links}"

    def _parse_user(self, path):
        return (lambda x: x)(
            *re.findall(r"(?:Users/)(\w+).*", path))

    def _parse_path(self, data_path):
        return f"Users/{self._parse_user(data_path)}/Downloads/%(title)s.%(ext)s"

    def add_path(self, data_path: str):
        self.user = self._parse_user(data_path)
        self.path = self._parse_path(data_path)

    def add_youtube_links(self, youtube_link: str):
        self.youtube_links.append(youtube_link)

    def has_data(self):
        return True if self.user != "" and self.path != "" and self.youtube_links is not [] else False
