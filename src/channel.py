import os

import isodate

from helper.youtube_api_manual import youtube, printj


class Channel:
    api_key = os.getenv('YT_API_KEY')
    """Класс для ютуб-канала"""
    def __init__(self, channel_id) -> None:
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'  # Редакция
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        printj(channel)
