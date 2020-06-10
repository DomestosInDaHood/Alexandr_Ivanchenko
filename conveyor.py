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

    def gen_transitions(self, amount_transitions):
        """Генерация вариантов работ"""
        
        base_transition = [i for i in range(self.number_of_details)]
        transitions = []
        for i in range(amount_transitions):
            if i == 0:
                random.shuffle(base_transition)
                print("Сгенерирован переход:", base_transition)
                transitions.append(base_transition)
            else:
                base_transition = [i for i in range(self.number_of_details)]
                random.shuffle(base_transition)
                counter = 0
                while counter != len(transitions):
                    if base_transition == transitions[counter]:
                        base_transition = [i for i in range(self.number_of_details)]
                        random.shuffle(base_transition)
                        counter = 0
                    else:
                        counter += 1
                print("Сгенерирован переход:", base_transition)
                transitions.append(base_transition)

        return transitions

    def get_target_functions(self, transitions):
        target_functions = []
        z = 0
        for i in range(len(transitions)):
            for j in range(len(transitions[i])):
                try:
                    z += (self.spent_time[transitions[i][j]] + self.reload_time[transitions[i][j]][transitions[i][j + 1]])
                except IndexError:
                    z += (self.spent_time[transitions[i][j]] + self.reload_time[transitions[i][j]][transitions[i][j]])
            target_functions.append(z)
            z = 0
        
        print("---Расчет целевых функций---")
        for i in range(len(transitions)):
            print("z:", transitions[i], "->", target_functions[i])

        return target_functions



    def get_best_transitions(self, transitions):
        tuple_transitions = transitions.copy()
        for i in range(len(transitions)):
            tuple_transitions[i] = tuple(transitions[i])
        hash_table = dict(zip(tuple_transitions, self.get_target_functions(transitions)))
        list_hash_table = list(hash_table.items())
        list_hash_table.sort(key=lambda i: i[1])
        list_hash_table = [list_hash_table[i] for i in range(len(list_hash_table) // 2)]
        for i in list_hash_table:
            print(i[0], ":", i[1])

        for i in range(len(list_hash_table)):
            list_hash_table[i] = list(list_hash_table[i])
            list_hash_table[i][0] = list(list_hash_table[i][0])
            
        
        print(list_hash_table)

        return list_hash_table

    def gen_neighborhood(self):
        neighborhood = []
        for i in range(self.number_of_details - 1):
            neighborhood.append([i, i + 1])

        print(neighborhood)

        return neighborhood

    def get_solo_target_function(self, transition):
        z = 0
        for j in range(len(transition)):
            try:
                z += (self.spent_time[transition[j]] + self.reload_time[transition[j]][transition[j + 1]])
            except IndexError:
                z += (self.spent_time[transition[j]] + self.reload_time[transition[j]][transition[j]])

        print(z)
        return z


def main():
    """Область тестирования модуля"""

    print("---Новый пример---")
    TestObject = Conveyor(4, [5, 3, 2, 7], [[0, 8, 3, 8], [10, 0, 7, 3], [15, 11, 0, 5], [12, 5, 3, 0]])
    print("---Вывод работы---")
    TestObject.info()
    print("---Генерация переходов---")
    test_list = TestObject.gen_transitions(12)
    print("---Выбор лучших---")
    best_list = TestObject.get_best_transitions(test_list)
    print("---Генерация окрестностей---")
    neighborhood = TestObject.gen_neighborhood()
    print("---Получение целевой функции для одного перехода---")
    solo_list = TestObject.get_solo_target_function(test_list[0])

if __name__ == "__main__":
    main()