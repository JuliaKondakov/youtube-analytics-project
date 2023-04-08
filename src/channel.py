import os                                                           # модуль os для работы с переменными окружения
import json                                                         # модуль json для работы с JSON файлами
from googleapiclient.discovery import build                         # функция build из модуля googleapiclient.discovery


class Channel:

    api_key = os.getenv('YT_API_KEY')                               # значение переменной api_key получено из переменных окружения.

    youtube = build('youtube', 'v3', developerKey=api_key)          # build() указывают на ключ разработчика
    """
       Атрибуты Класс для работы с каналом YouTube.
    """
    def __init__(self, channel_id):                                 # конструктор класса  инициализирует объект канала
        self._channel_id = channel_id                               # идентификатор канала YouTube/ПРИВАТ
        self.title = None                                           # название канала YouTube
        self.description = None                                     # хранит описание канала YouTube
        self.url = None                                             # хранит URL-адрес канала YouTube
        self.subscriber_count = None                                # хранит количество подписчиков канала
        self.video_count = None                                     # хранит количество видео на канале
        self.view_count = None                                      # хранит количество просмотров на канале
        self._get_channel_info()                                    # метод получает инфу о канале из API и сохраняет ее

    """
        получает информацию о канале YouTube из API
        и сохраняет ее в атрибуты объекта
    """
    def _get_channel_info(self):
        channel_info = self.youtube.channels().list(
            id=self._channel_id,
            part='snippet,statistics'
        ).execute()
        # присваивают значения атрибутам, полученной из API:
        channel = channel_info['items'][0]
        self.title = channel['snippet']['title']
        self.description = channel['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self._channel_id}"
        self.subscriber_count = int(channel['statistics']['subscriberCount'])
        self.video_count = int(channel['statistics']['videoCount'])
        self.view_count = int(channel['statistics']['viewCount'])

    """
        Геттер-методи, который возвращает значение атрибута channel_id. 
        это необходимо, т.к. это ПРИВАТНЫЙ атрибут и доступный только для чтения
    """
    @property
    def channel_id(self):
        return self._channel_id

    """
        Сеттер-метод, НЕизменяемый атрибут. При попытки изменить его выведет ошибку
        AttributeError с текстом: "Can't set attribute".
     """
    @channel_id.setter
    def channel_id(self, value):
        raise AttributeError("Can't set attribute")

    """
        Метод класса, возвращает объект build 
        Необходим для создания экземпляров класса Channel.
    """
    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)
    """
        Метод to_json сохраняет атрибуты объекта. 
        Метод json.dump() записывает данные из словаря __dict__ в заданном формате.
    """
    def to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.__dict__, file, ensure_ascii=False, indent=4)
