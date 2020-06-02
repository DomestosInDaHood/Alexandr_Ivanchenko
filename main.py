#! /usr/bin/env python3

def cheak_input_size(number_of_detailes != len(in_string.split())):
    if len() != number_of_detailes:
        print('Введенных данных больше или меньше, чем количество деталей. Либо пропущен пробел.')
        return False
    else:
        return True

def cli_initialition():
    # В этой функции выполняется ввод и проверка данных
    print('\t\t\t --- Этап ввода данных ---')

    print('Введите количество деталей')
    while True:
        try:
            number_of_detailes = int(input(': '))
        except ValueError:
            print('Это не целое число.')
        else:
            break

    print('Введите через пробел количество времени затраченное на производство i-ой детали')
    while True:
        try:
            in_string = input(': ')
            if !cheak_input_size():
                continue
            
            time_spent = [int(i) for i in in_string.split()]
        except ValueError:
            print('Часть данных не является целочислеными')
        else:
            break
    print('Ввод матрици затраты перезагрузки')
    print('Для каждой i-ой детали введите время перезагрузки j-ой детали после нее')
    while True:
        for in range(number_of_detailes):
            while True:
                try:
                    in_string = input(str(i) + ': ')
                    if !cheak_input_size():
                        continue
                except ValueError:
                    print('Часть данных не является целочислеными')

    print(number_of_detailes)
    print(time_spent)


def main():
    cli_initialition()

main()