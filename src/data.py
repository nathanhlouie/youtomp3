class Data:
    def __init__(self):
        self.user = ""
        self.path = ""
        self.youtube_links = []

    def _parse_path(self):
        return f'Users/{self.user}/Downloads/%(title)s.%(ext)s'

    def add_user(self, user: str):
        self.user = user
        self.path = self._parse_path(user)

    def add_youtube_links(self, youtube_link: str):
        self.youtube_links.append(youtube_link)
