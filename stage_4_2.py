"""
**Сложность 2**
- Реализовать процедуру освобождения очереди.
- Принимаем, что все клиенты проходят только через одного клерка/одно окно обслуживания.
- Режим наполнения очереди - “ручной”
Необходимо выделить тех клиентов, которые успеют покинуть очередь между двумя отображениями очереди на экране.
В ручном режиме ввода фамилий очередь выводится на экран перед приглашением ввести фамилию нового клиента.
Используйте время постановки в очередь, время обслуживания, текущее время и определите какие клиенты уже покинули очередь.
Подумайте в какой момент вы должны запустить процедуру очистки очереди.
Продумайте алгоритм, как по текущему времени определить кто из клиентов уже завершил обслуживание.
Обязательно при тестировании создайте ситуацию, когда очередь стала пустой и потом вновь наполняется.
![stage4-2.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/307886f4-f4e4-4232-8033-11da19a4ebc5/stage4-2.jpg)
**Подсказка:**
1. *Значимым является только время постановки первого клиента в очередь и время обслуживания каждого клиента.*
2. *Вы можете добавить клиенту дополнительную “внутреннюю” информацию, которая не будет отображаться на экране,
но поможет вам решить задачу.*"""

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
              'date_width': 21,
              'sep': '|',
              'timing_width': 7,
              'finish_width': 21,
              'win_width': 6}
    spec = {'output': output, 'windows': windows}
    idc = 1
    eq = {}
    version = "4.2"
    spec['codes_available'] = q.codes_available(spec)
    spec['win_codes'] = q.windows_by_code(spec)
    spec['win_status'] = {win: None for win in spec['windows'].keys()}
    while True:
        eq, spec = q.eq_clear(eq, spec)
        q.eq_print(eq, version, spec)
        q.eq_print_footer(eq, spec)
        surname = c.get_surname()
        if surname == "":
            raise KeyboardInterrupt
        while True:
            code = c.get_codes(spec)
            if q.is_code_valid(code, spec):
                break
            else:
                print("Неверный код, попробуйте еще раз")
        eq, spec = q.eq_clear(eq, spec)
        eq, spec = q.eq_add_client(eq, idc, surname, code, spec)
        idc += 1


try:
    main()
except KeyboardInterrupt:  # проверка в консоли
    print("\nВсего вам доброго! До свидания!")
