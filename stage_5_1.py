"""**Сложность 1**
- При выходе из программы необходимо записать текущее состояние очереди, в CSV-файл, в случае если очередь не пуста.
  В файл записывается вся информация о клиенте.
- Файл должен быть записан в отдельную директорию, например queue_log, выберите имя самостоятельно.
- В имени файла указать дату и время создания файла.
- Если нужной директории не существует - создать ее самостоятельно в программе.

Используйте pathlib и его методы объекта Path для работы с файлами и директориями."""

from datetime import datetime, timedelta
from random import choice
from pathlib import Path

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
    files = {'log_dir': 'queue_log', 'logfile_template': 'base_log'}
    spec = {'output': output, 'windows': windows, 'files': files}
    idc = 1
    eq = {}
    version = "4.2"
    spec['codes_available'] = q.codes_available(spec)
    spec['win_codes'] = q.windows_by_code(spec)
    spec['win_status'] = {win: None for win in spec['windows'].keys()}
    try:
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
    except KeyboardInterrupt:
        filename = q.eq_write_logfile(eq, spec)
        print(f"Запись лог-файла произведена в файл {filename}")
        print("\nВсего вам доброго! До свидания!")


main()
