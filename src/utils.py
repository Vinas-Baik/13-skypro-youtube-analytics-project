import os

def full_path_name_file(name_file):
    """
    формируем полный путь до файла
    :param name_file: имя файла с указанием подпапки
    :return: полный пусть в UNIX системы
    """
    # return os.getcwd() + '\\' + name_file
    # return os.path.join(*name_file.replace('\\','/').split('/'))
    # cur_path = os.path.dirname(__file__)
    return os.path.realpath(name_file)

def nice_number_output(number) -> str:
    """
    возвращает красиво номер 100000.011 в виде "100 000.011"
    """
    # 10200300.01          10200300         - исходная
    # 10.00300201          00300201         - переворот строки
    # 01234567890          01234567         - позиция в строке
    # 10.003 002 01        003 002 01       - расcтавляем пробелы
    # 10 200 300.01        10 200 300       - переворачиваем обратно
    result = ''
    str_number = str(number)
    # ищем точку в числе
    if str_number.count('.') > 0:
        is_dot = False                  # переменная - Точка найдена и пройдена
        index_dot = 0                   # позиция точки в строке
        # число преобразуем в строку и переворачиваем строку к виду
        # было '10000.01' -> стало '10.00001' - для удобства работы с числом
        for i, str_n in enumerate(str_number[::-1]):
            result = str_n + result
            if is_dot:
                if (i - index_dot) % 3 == 0:   # ставим пробел после каждого 3го нуля
                    result = ' ' + result
            if str_n == '.':   # найдена . - значит дробная часть закончилась
                is_dot = True
                index_dot = i
    else:
        # точки нет - выводим число с пробелами
        for i, str_n in enumerate(str_number[::-1]):
            result = str_n + result
            if i % 3 == 2:
                result = ' ' + result

    return result.strip()
