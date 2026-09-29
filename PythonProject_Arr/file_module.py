__author__ = 'Богушевич Д.А.'

def input_in_file (l : list, file_name : str) -> None :
    """
    Функция для записи списка в текстовый файл в CSV формате
    :param l: Массив данных
    :param file_name: Имя файла в который необходимо вывести значения массива
    """
    f = open(file_name, 'w')
    for e in l:
        f.write(str(e) + ", " + '\n')
    f.close()


def output_from_file (file_name  : str) -> list :
    """
    Функция для вывода списка из файл в новый список
    :param file_name: Имя файла из которого получаем массив
    :return: Возвращает список
    """
    f = open(file_name, 'r')
    l: list = []
    for line in f:
        l.append(int(line.rstrip(", \n ")))
    f.close()
    return l