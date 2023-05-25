"""**Сложность 2**

- При старте программы считывание предыдущего состояния очереди из файла. Файл того же формата,
как запись состояния очереди в файл.
- Имя файла передается как параметр запуска из командной строки. Имя директории где он расположен -
фиксировано, выберите самостоятельно как вам удобно. ПРи запуске программы считаем, что имя файла и
режим работы программы random/manual будут переданы обязательно.
- Клиенты, которые были считаны из файла должны быть поставлены в очередь.
- Используйте pathlib и его методы объекта Path для работы с файлами и директориями.

**Примечание:**

- Подумайте про id клиента. Нужно ли его считывать?
- Необходимо гарантировать, что порядок клиентов в файле будет точно воспроизведен при их автоматической постановке в очередь.
- При новом запуске программы конфигурация окна-коды может другая, поэтому назначение клиента в окно должно происходить,
исходя из актуальной конфигурации. Для простоты считаем, что все коды операций будут обрабатываться и при новом запуске программы.
Т.е. не будет ситуации, когда клиент (из файла) не может быть отнесен ни к одному окну."""

from datetime import datetime, timedelta
from fileinput import filename
from random import choice
from pathlib import Path
from sys import argv

import e_eq as q
import e_client as c


def main(argv: list):
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
    files = {'log_dir': 'queue_log',
             'logfile_template': 'base_log',
             'startup_dir': 'startup_files'}
    spec = {'output': output, 'windows': windows, 'files': files}
    idc = 1
    eq = {}
    version = "5.2"
    spec['codes_available'] = q.codes_available(spec)
    spec['win_codes'] = q.windows_by_code(spec)
    spec['win_status'] = {win: None for win in spec['windows'].keys()}

    #argv = ['*****', 'manual', 'base_log.txt']
    if len(argv) != 3:
        print(f"Недостаточное или избыточное количество параметров {len(argv)}")
        return
    _, mode, startup_filename = argv
    if mode not in {'random', 'manual'}:
        print(f"Неправильный режим:  {mode}")
        return
    startup_file_path = Path(__file__).parent / spec['files']['startup_dir'] / startup_filename
    if not startup_filename.exists():
        for surname, code in q.eq_read_startup(startup_file_path):
            eq, spec = q.eq_add_client(eq, idc, surname, code, spec)
            idc += 1

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


main(argv)
