#! /usr/bin/env python3

"""В данном модуле содержатся функции для иницализации объекта Конвеер"""

from conveyor import Conveyor

def cli():
    """В этой функции производится ручная инициализация объекта класса
    Conveyor и валидация ввода.

    """
    print("\t\t\t --- Этап ввода данных ---")

    print("Введите количество деталей")
    while True:
        try:
            number_of_detailes = int(input(': '))
        except ValueError:
            print("Это не целое число.")
        else:
            break
    
    # Создание последовательность от 0 до number_of_detailes в формате string
    details_range = [str(i) for i in range(number_of_detailes)]
    print("Введите время производства i-ой детали в минутах и нажмите Enter")
    spent_time = []
    for i in details_range:
        while True:
            try:
                in_string = input("i" + i + ": ")
                spent_time.append(int(in_string))
            except ValueError:
                print('Часть данных не является целочислеными')
                spent_time.pop()
            else:
                break
    print('Ввод матрици затраты перезагрузки')
    print('Для каждой i-ой детали введите время перезагрузки j-ой детали после нее')
    reload_time = []
    for i in range(number_of_detailes):
        print("---i" + str(i) +"---\n")
        vector = []
        for j in range(number_of_detailes):
            while True:
                try:
                    in_string = input("j" + str(j) + ': ')
                    vector.append(int(in_string))
                except ValueError:
                    print('Часть данных не является целочислеными')
                    vector.pop()
                else:
                    break
        reload_time.append(vector)
    
    ResultObject = Conveyor(number_of_detailes, spent_time, reload_time)

    return ResultObject

def main():
    """Область тестирования модуля"""
    while True:
        shell = input(">>" )
        if shell == "ввод":
            TestObject = cli()
            break
        elif shell == "выход":
            return
        else:
            print("Комманда не найдена")

    while True:
        shell = input(">> ")
        if shell == "вывод":
            TestObject.info()
        elif shell == "выход":
            return
        else:
            print("Комманда не найдена")

if __name__ == "__main__":
    main()