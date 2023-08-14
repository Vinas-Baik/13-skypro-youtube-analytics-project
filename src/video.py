import os
import json
from googleapiclient.discovery import build

YT_API_KEY: str = os.getenv('YT_API_KEY')


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Video:

    def __init__(self, id_video: str):
        self.__id_video: str = id_video
        self.load_video_yt()

    def load_video_yt(self):
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        # self.youtube_str = str(youtube)
        #
        # получить статистику видео по его id
        #
        # получить id можно из адреса видео https: // www.youtube.com / watch?v = gaoc9MPZ4bw
        # или https: // youtu.be / gaoc9MPZ4bw
        #
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=self.__id_video).execute()
        # printj(video_response)

        self.title: str = video_response['items'][0]['snippet']['title']
        self.url: str = 'https://www.youtube.com/watch?v=' + video_response['items'][0]['id']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']

    @property
    def id_video(self):
        return self.__id_video

    @id_video.setter
    def id_video(self, new_id):
        # self.__id_video = new_id
        # self.load_video_yt()
        pass

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f"Video('{self.id_video}')"

    def my_repr(self):
        return f'id видео: {self.id_video}\n' \
               f'название видео: {self.title}\n' \
               f'ссылка на канал: {self.url}\n' \
               f'количество лайков: {self.like_count}\n' \
               f'общее количество просмотров: {self.view_count}'


class PLVideo:

    def __init__(self, id_video: str, id_playlist: str):
        self.__id_video = id_video
        self.__id_playlist = id_playlist
        self.load_video_yt()

    @property
    def id_video(self):
        return self.__id_video

    @id_video.setter
    def id_video(self, new_id: str):
        pass


    @property
    def id_playlist(self):
        return self.__id_playlist


    @id_playlist.setter
    def id_playlist(self, new_id: str):
        pass

    def __repr__(self):
        return f"PLVideo('{self.id_video}', '{self.id_playlist}')"

    def __str__(self):
        return f'{self.title}'

    def my_repr(self):
        return f'id видео: {self.id_video}\n' \
               f'id плэйлиста: {self.id_playlist}\n' \
               f'название видео: {self.title}\n' \
               f'ссылка на канал: {self.url}\n' \
               f'количество лайков: {self.like_count}\n' \
               f'общее количество просмотров: {self.view_count}'

    def load_video_yt(self):
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        # self.youtube_str = str(youtube)
        #
        # получить данные по видеороликам в плейлисте
        # docs: https://developers.google.com/youtube/v3/docs/playlistItems/list
        #
        # получить id плейлиста можно из браузера, например
        # https://www.youtube.com/playlist?list=PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn
        # или из ответа API: см. playlists выше
        #
        playlist_videos = youtube.playlistItems().list(playlistId=self.id_playlist,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        # printj(playlist_videos)

        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in
                                playlist_videos['items']
                                if video['contentDetails']['videoId'] == self.id_video]
        # print(video_ids)
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_ids[0]).execute()

        # printj(video_response)

        self.title: str = video_response['items'][0]['snippet']['title']
        self.url: str = 'https://www.youtube.com/watch?v=' + video_response['items'][0]['id']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']



# video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
# print(video2)
# print(video2.__repr__())
# print(video2.my_repr())

# video1 = Video('AWX4JnAnjBE')
# print(video1)
# print(video1.__repr__())
# print(video1.my_repr())
# video1.id_video = 'AWX4JnAnjBE-001'
# print(video1)
