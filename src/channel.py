import json
import os
from googleapiclient.discovery import build
from src.utils import full_path_name_file

YT_API_KEY: str = os.getenv('YT_API_KEY')
# JSON_FILE: str = '..\src\yt_channel.json'

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        # self.youtube_str = str(youtube)

        channel = youtube.channels().list(id=channel_id,
                                          part='snippet,statistics').execute()

        self.url: str = 'https://www.youtube.com/channel/'+channel['items'][0]['id']
        self.subscriber_count: str = channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count: str = channel["items"][0]["statistics"]["videoCount"]
        self.view_count: str = channel["items"][0]["statistics"]["viewCount"]
        self.title: str = channel["items"][0]["snippet"]["title"]
        self.description: str = channel["items"][0]["snippet"]["description"]


    @property
    def channel_id(self):
        return self.__channel_id
    @channel_id.setter
    def channel_id(self, new_id):
        pass

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other) -> int:
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other: 'Channel') -> int:
        # метод для операции вычитания (self - other);
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __lt__(self, other: 'Channel') -> int:
        # метод для операции сравнения «меньше» (self < other);
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other: 'Channel') -> int:
        # метод для операции сравнения «меньше или равно»  (self <= other);
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __gt__(self, other: 'Channel') -> int:
        #  метод для операции сравнения «больше» (self > other);
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other: 'Channel') -> int:
        # метод для операции сравнения «больше или равно» (self >= other).
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __repr__(self):
        return f'id канала: {self.__channel_id}\n' \
               f'название канала: {self.title}\n' \
               f'описание канала: {self.description}\n' \
               f'ссылка на канал: {self.url}\n' \
               f'количество подписчиков: {self.subscriber_count}\n' \
               f'количество видео: {self.video_count}\n' \
               f'общее количество просмотров: {self.view_count}'



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)

        channel = youtube.channels().list(id=self.__channel_id,
                                          part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return f'{str(build("youtube", "v3", developerKey=YT_API_KEY))}'


    def to_json(self, name_file: str):
        json_list = {"id": self.__channel_id,
                     "title": self.title,
                     "description": self.description,
                     "url": self.url,
                     "subscriberCount": self.subscriber_count,
                     "videoCount": self.video_count,
                     "viewCount": self.view_count
                     }

        name_file = full_path_name_file(name_file)
        with open(name_file, 'w', encoding='UTF-8') as file:
            json.dump(json_list, file)

        # print(name_file)
