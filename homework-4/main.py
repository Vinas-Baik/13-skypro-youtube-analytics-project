from src.video import Video, PLVideo

if __name__ == '__main__':
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

    print('\n\033[32mОбщее количество просмотров у каналов\033[39m:')
    print(f'Канал {video1.title}: \033[32m{video1.view_count}\033[39m')
    print(f'Канал {video2.title}: \033[32m{video2.view_count}\033[39m')
    print()
    print(f'Сумма просмотров обоих каналов: \033[32m{moscowpython + highload}\033[39m')  #
