import os

import isodate
from googleapiclient.discovery import build

from helper.youtube_api_manual import youtube, printj, channel_id

class Channel:

    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    """Класс для ютуб-канала"""
    def __init__(self, channel_id) -> None:
        self.channel_id = channel_id
        self.title = None               # название канала
        self.description = None         # описание канала
        self.url = None                 # ссылка на канал
        self.subscriber_count = None    # количество подписчиков
        self.video_count = None         # количество видео
        self.view_count = None          # общее количество просмотров


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'  # Редакция
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics'
                                          ).execute()
        channel.print_info(channel)

    """ # получаем значения атрибутов
    print(vdud.title)  # вДудь
    print(vdud.video_count)  # 163 (может уже больше)
    print(vdud.url)  # https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA"""

    def playlist_info(self):
        playlists = youtube.playlists().list(channelId=channel_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        printj(playlists)
        for playlist in playlists['items']:
            print(playlist)
            print()