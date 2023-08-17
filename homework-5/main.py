import datetime

from src.video import PlayList

if __name__ == '__main__':
    #
    # НАЧАЛО ПРОГРАММЫ
    #

    print('Создаем описание плэйлиста:  ')

    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    print(pl.my_repr())

    # проверка правильности создания плейлиста
    assert pl.title == "Moscow Python Meetup №81"
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

    duration = pl.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0

    print(f'Cуммарная длительность видеороликов плейлиста: {pl.total_duration}\n')

    sum_like_count = 0
    sum_view_count = 0

    for video in pl.video_pls:
        sum_like_count += video['likeCount']
        sum_view_count += video['viewCount']
        print(video['video_el'].my_repr())

    print(f' Общее количество лайков видео плейлиста: {sum_like_count}')
    print(f' Общее количество просмотров видео плейлиста: {sum_view_count}')

    print()
    print(f'Ссылка на видео с максимальным количеством просмотров: {pl.show_best_video()}')
    assert pl.show_best_video() == "https://www.youtube.com/watch?v=cUGyMzWQcGM"

    #
    # КОНЦЕ ПРОГРАММЫ
    #
