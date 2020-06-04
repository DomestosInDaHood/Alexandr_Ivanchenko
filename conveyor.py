#! /usr/bin/env python3
import random

"""Модуль сожержит класс конвеер"""

class Conveyor:
    """Данный класс является реализацией конвеера для партии деталей.
    В атрибутах хранится информация о партии деталей и количество
    партий.
    
    """
    
    def __init__(self, number_of_details, spent_time, reload_time):
        """Конструктор атрибутов партии - количество деталей, время
        затраченое на производство деталей(список) и матрица
        перезагрузок деталей(список списков).
        
        """
        
        self.number_of_details = number_of_details
        self.spent_time = spent_time
        self.reload_time = reload_time

    def info(self):
        """Вывод содержимого атрибутов"""
        
        print("Количестов деталей:", self.number_of_details)
        print("Вектор времени производства:", self.spent_time)
        print("Матрица перезагрузки:")
        for i in range(len(self.reload_time)):
            print(self.reload_time[i])

    def gen_jobs(self, amount_jobs):
        """Генерация вариантов работ"""
        variables = [i for i in range(self.number_of_details)]
        list_of_variables = []
        for i in range(amount_jobs):
            list_of_variables.append(random.shuffle(variables))
            if len(list_of_variables) != 1:
                for i in range(len(list_of_variables)):
                    while True:
                        if list_of_variables[i] != list_of_variables[-1]:
                            break
                        list_of_variables.pop()
                        list_of_variables.append(random.shuffle(variables))

        return list_of_variables

    def info_jobs(self, list_of_variables):
        print("Варианты работ:")
        for i in range(len(list_of_variables)):
            print(list_of_variables[i])


def main():
    """Область тестирования модуля"""

    while True:
        shell = input(">> ")
        if shell == "новый пустой":
            TestObject = Conveyor(0, [], [[]]) # создаем пустой конвеер
            break
        elif shell == "новый пример":
            TestObject = Conveyor(2, [1, 1], [[1, 1], [1, 1]])
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