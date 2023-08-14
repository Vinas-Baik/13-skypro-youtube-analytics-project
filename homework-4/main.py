from src.video import Video, PLVideo
from src.utils import nice_number_output

if __name__ == '__main__':
    #
    # НАЧАЛО программы
    #
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id видео из ютуб
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'

    for temp_video in (video1, video2):
        print()
        print(f'\033[33m{temp_video.__repr__()}\033[39m')
        print(f'\033[32m{temp_video}\033[39m')
        print(temp_video.my_repr())

    temp_video = video1 + video2
    print('\n\033[32mОбщее количество просмотров у каналов\033[39m:')
    print(f'Канал \033[33m{video1.title}: '
          f'\033[32m{nice_number_output(video1.view_count)}\033[39m просмотров')
    print(f'Канал \033[33m{video2.title}: '
          f'\033[32m{nice_number_output(video2.view_count)}\033[39m просмотров')

    print(f'\nСумма просмотров обоих каналов: '
          f'\033[32m{nice_number_output(temp_video.view_count)}\033[39m')  #

    print('\n\033[32mОбщее количество лайков у каналов\033[39m:')
    print(f'Канал \033[33m{video1.title}: '
          f'\033[32m{nice_number_output(video1.like_count)}\033[39m лайков')
    print(f'Канал \033[33m{video2.title}: '
          f'\033[32m{nice_number_output(video2.like_count)}\033[39m лайков')

    print(f'\nСумма лайков обоих каналов: '
          f'\033[32m{nice_number_output(temp_video.like_count)}\033[39m')  #

    #
    # КОНЕЦ программы
    #
