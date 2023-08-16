import os
import json
from googleapiclient.discovery import build

YT_API_KEY: str = os.getenv('YT_API_KEY')


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Videos():
    def __init__(self, id_video: str):
        self.__id_video: str = id_video
        self.title = ''
        self.like_count = 0
        self.view_count = 0
        self.url = ''

    @property
    def id_video(self):
        return self.__id_video

    @id_video.setter
    def id_video(self, new_id):
        self.__id_video = new_id
        # self.load_video_yt()
        # pass

    def __str__(self):
        return f'{self.title}'

    def my_repr(self):
        return f'id видео: {self.id_video}\n' \
               f'название видео: {self.title}\n' \
               f'ссылка на канал: {self.url}\n' \
               f'количество лайков: {self.like_count}\n' \
               f'общее количество просмотров: {self.view_count}\n'

    def __add__(self, other):
        if isinstance(self, Videos) and isinstance(other, Videos):
            temp_videos = Videos('')
            temp_videos.like_count = int(self.like_count) + int(other.like_count)
            temp_videos.view_count = int(self.view_count) + int(other.view_count)
            return temp_videos
        return None

class Video(Videos):

    def __init__(self, id_video: str):
        super().__init__(id_video)
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
                                               id=self.id_video).execute()
        # printj(video_response)
        response_video = video_response['items'][0]
        self.title: str = response_video['snippet']['title']
        self.url: str = 'https://www.youtube.com/watch?v=' + response_video['id']
        self.view_count: int = response_video['statistics']['viewCount']
        self.like_count: int = response_video['statistics']['likeCount']


    def __repr__(self):
        return f"Video('{self.id_video}')"

    def my_repr(self):
        return f'{super().my_repr()}'


class PLVideo(Videos):

    def __init__(self, id_video: str, id_playlist: str):
        super().__init__(id_video)
        self.__id_playlist = id_playlist
        self.load_video_yt()

    @property
    def id_playlist(self):
        return self.__id_playlist


    @id_playlist.setter
    def id_playlist(self, new_id: str):
        pass

    def __repr__(self):
        return f"PLVideo('{self.id_video}', '{self.id_playlist}')"

    def my_repr(self):
        return f'{super().my_repr()}' \
               f'id плэйлиста: {self.id_playlist}'

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

        response_video = video_response['items'][0]
        # printj(video_response)

        self.title: str = response_video['snippet']['title']
        self.url: str = 'https://www.youtube.com/watch?v=' + response_video['id']
        self.view_count: int = response_video['statistics']['viewCount']
        self.like_count: int = response_video['statistics']['likeCount']

class PlayList():

    def __init__(self, id_playlist: str):
        self.__id_playlist = id_playlist
        self.video_pls = []
        self.load_video_yt()

    @property
    def id_playlist(self):
        return self.__id_playlist

    @id_playlist.setter
    def id_playlist(self, new_id: str):
        pass

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
                                                       part='contentDetails,snippet',
                                                       maxResults=100,
                                                       ).execute()
        # printj(playlist_videos)
        self.url = 'https://www.youtube.com/playlist?list='+ \
                   playlist_videos['items'][0]['snippet']['playlistId']
        self.title = playlist_videos['items'][0]['snippet']['channelTitle']


        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in
                                playlist_videos['items']
                                if 'videoPublishedAt' in video['contentDetails']]
        # print(video_ids)
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)).execute()
        for t_video in video_response['items']:
            print(t_video)
        # for temp_video in video_ids:
        #     self.video_pls.append(Video(temp_video))


    def my_repr(self):
        return f'id плейлиста: {self.id_playlist}\n' \
               f'название плейлиста: {self.title}\n' \
               f'ссылка на плейлист: {self.url}\n' \
               f'количество роликов в плейлисте: {self.__len__()}\n'

    def __len__(self):
        return len(self.video_pls)

    def total_duration(self):
        pass

# video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
# print(video2)
# print(video2.__repr__())
# print(video2.my_repr())
#
# video1 = Video('AWX4JnAnjBE')
# print(video1)
# print(video1.__repr__())
# print(video1.my_repr())
# video1.id_video = 'AWX4JnAnjBE-001'
# print(video1)
#
# temp_video = video1 + video2
# print(temp_video.view_count)
# print(temp_video.like_count)

pl = PlayList('PLZ_AMw_dAdXffKmUzSu7Z3vkqP4Sz9qL5')
print(pl.my_repr())
# for i in pl.video_pls:
#     print(i)