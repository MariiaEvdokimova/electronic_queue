"""
- Скорректировать структуру данных для очереди с учетом новых типов данных.
  Выбрать наиболее удобную структуру данных.
- Добавить в данные клиента еще один параметр - время постановки его в очередь, в который заносится текущее время.
  Скорректировать под эти данные вывод очереди на экран. Дату выводить в виде: dd-mm-yy hh:mm:ss, например так 07-04-23 16:20:35.
- Ограничить при выводе на экран длину фамилии клиента до 10 символов.
  Если фамилия длиннее, то обрезать ее и добавлять в конце троеточие.
- Перед приглашением пользователю ввести фамилию, показать длину очереди перед ним: сколько человек перед ним."""


###
def main():
    spec = {'idc_width': 3, 'surname_width': 15, 'code_width': 3}
    idc = 1
    eq = {}
    version = "2.2"
    codes = "MNPS"
    while True:
      eq_print(eq, version, spec)
      data = input("Введите фамилию или пустая строка для выхода: ")
      if data == "":
         print("Всего вам доброго! До свидания!")
         break
      while True:
          code = input(f"Введите код операции. Допустимые коды: {codes}: ")
          if is_code_valid(code, codes):
              break
          else:
           print("Неправильный код операции.")
    eq_add_client(eq, idc, data, code)
    idc += 1

#def is_code_valid(code: str, codes: str) -> bool:
#   if code.upper() in codes:
#        return True
#   else:
#        return False

def is_code_valid(code: str, codes: str) -> bool:
    return code.upper() in codes

def eq_add_client(eq: dict, idc: int, surname: str, code: str) -> list:
    eq[idc] = {'surname': surname, 'code': code.upper()}
    return eq
def idc_str(idc:int) -> str:
    return str(idc).zfill(3)

def table_row_str(idc: int, client: dict, spec: dict) -> str:
    result = f"|{idc_str(idc):^{spec['idc_width']}s}|" + \
             f"{client['surname']:^{spec['surname_width']}s}|" + \
             f"{client['code']:^{spec['code_width']}s}|"
    return result

def eq_print(eq: dict, version: str, spec: dict) -> None:
    print(f"Электронная очередь. Версия {version}")
    total_width = spec['idc_width'] + spec['surname_width'] + spec['code_width'] + 4
    print("-" * total_width)
    for idc, client in eq.items(): #{'surname': ххх, 'code': ххх}
        print(table_row_str(idc, client, spec))
    print("-" * total_width)

main()

