"""
Сложность 1
- Выделить в коде программы два модуля
  - функции для работы с данными клиента
  - функции для работы со структурой очереди
- Провести корректный импорт своих модулей в основной модуль с использованием псевдонимов.
- Ввести для клиента дополнительный параметр - номер окна/клерка который будет его обслуживать.
  Пусть будет 3-4 окна обслуживания.
- Каждое окно обрабатывает только определенные коды операций, не все, но обязательно коды операций пересекаются между окнами.
  Выбрать подходящую структуру данных для хранения информации о том какие окна какие коды операций обрабатывают.
- Окно обработки для клиента назначается случайным образом среди тех, кто подходит под выбранный тип операции.
- Перед вводом кода операции печатать список допустимых кодов операций, исходя из того какие окна работают и их кодами.
  Ограничить допустимые коды операций именно ими."""


from datetime import datetime, timedelta
from random import choice

import e_eq as q
import e_client as c

def main():
    windows = {'win1': 'MP',
               'win2': 'NS',
               'win3': 'P',
               'win4': 'NP',
               'win5': 'MS'}
    output = {'idc_width': 3,
              'surname_width': 15,
              'code_width': 3,
              'date_width': 23,
              'sep': '|',
              'timing_width': 7,
              'win_width': 6}
    spec = {'output': output, 'windows': windows}
    idc = 1
    eq = {}
    version = "4.1"
    codes = q.codes_availiable(spec)
    win_codes = q.windows_by_code(spec)
    while True:
        q.eq_print(eq, version, spec)
        lenght = len(eq)
        print(f"Длина очереди перед Вами: {lenght} человек{c.man_cases(lenght)}")
        if lenght !=0:
             mean = sum([client['timing'] for client in eq.values()], start=timedelta(0,0,0,0,0,0))
             mean1 = str(mean/lenght)[2:7]
             print(f"Среднее время обслуживания клиента: {mean1}")
        surname = c.get_surname()
        if surname == "":
             raise KeyboardInterrupt
        while True:
             code = c.get_codes(codes)
             if q.is_code_valid(code, codes):
                 break
             else:
                 print("Неверный код, попробуйте еще раз")
        win = choice(win_codes[code])
        q.eq_add_client(eq, idc, surname, code, win)
        idc += 1


try:
   main()
except KeyboardInterrupt: #проверка в консоли
    print("\nВсего вам доброго! До свидания!")