import datetime

from src.video import PlayList

if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    print(pl.my_repr())
    # assert pl.title == "Moscow Python Meetup №81"
    assert pl.title == "MoscowPython"
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

    duration = pl.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0
    print(pl.show_best_video())
    assert pl.show_best_video() == "https://www.youtube.com/watch?v=cUGyMzWQcGM"
