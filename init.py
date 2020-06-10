"""В цьому модулі знаходятся функції для ініціалазі' обєкту Conveyor,
різними способами"""

import random
import xlrd
from conveyor import Conveyor

def example():
    """Демонстраційний приклад"""
    Job = Conveyor(4, [5, 3, 2, 7], [[0, 8, 3, 8],
                           [10, 0, 7, 3], [15, 11, 0, 5],
                           [12, 5, 3, 0]])

    return Job


def keyboard():
    """Шаблон для ручного вводу"""
    Job = Conveyor(3, [1, 1, 1], [[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    
    return Job


def rand_init(details_min, details_max, time_min, time_max):
    """Генерує випадковий конвеєр по параметрам з аргументів
    details_min - мінімум деталей
    details_max - максимум деталей
    time_min - мінамальний час обробки деталі та перенаголодження верстату
    time_max - максимальний час обратки деталі та переналогдження верстау
    """
    number_of_details = random.randint(details_min, details_max)

    spent_time = [random.randint(time_min, time_max) for i in range(number_of_details)]

    reload_time = [[random.randint(time_min, time_max) for i in 
                    range(number_of_details)] for i in range(number_of_details)]

    for i in range(number_of_details): # заповнюємо головну діагональ нулями
        reload_time[i][i] = 0

    Job = Conveyor(number_of_details, spent_time, reload_time)
    
    return Job

def excel_file(input_file):
    """"""

    book = xlrd.open_workbook(input_file)
    sheet = book.sheet_by_index(0)

    if sheet.nrows != sheet.ncols + 2:
        return "SizeError"
    else:
        try:
            number_of_details = sheet.ncols
            spent_time = [int(sheet.cell(0, i).value) for i in range(number_of_details)] 
            reload_time = [[int(sheet.cell(i + 2, j).value) for j in range(number_of_details)] for i in range(number_of_details)]
        except ValueError:
            return "ValueError"


        Job = Conveyor(number_of_details, spent_time, reload_time)

        return Job