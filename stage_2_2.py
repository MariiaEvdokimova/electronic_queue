"""
- При добавлении в очередь каждому клиенту назначается уникальный id - целое уникальное число.
- Фамилию клиента необходимо при занесении в очередь приводить к правильному регистру:
  первая буква заглавная, остальные - строчные.
- Реализовать для клиента возможность выбрать код операции, после ввода фамилии.
  Кодов операции несколько, например, M,N,P,S.
  Если код введен клиентом неправильно, то предлагаем ввести еще раз, до тех пор пока правильно не введет.
  Только после этого заносим в очередь. Регистр букв при вводе кода значения не имеет.
- Реализовать форматированный вывод содержимого очереди на экран - табличный вид.
  Определенные ширины полей под каждое поле. При выводе id на экран дополнять его нулями до трехзначного номера.
- Выделить значимые куски программы и оформить их в виде функций. На этом этапе у вас может получиться 5-7 функций."""

def main():
    idc = 1
    eq = []
    version = 2.2
    codes = "MNPS"
    while True:
        eq_print(eq, version)
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

def eq_add_client(eq:list, idc:int, surname:str, code:str) -> list:
    eq.append([idc, surname.title(), code.upper()])
    return eq
def idc_str(idc:int) -> str:
    return str(idc).zfill(3)
def eq_print(eq: list, version: str) -> None:
    print(f"Электронная очередь. Версия {version}")
    idc_width = 3
    surname_width = 15
    code_width = 3
    total_width = idc_width + surname_width + code_width + 4
    print("-" * total_width)
    for idc, surname, code in eq: #сlient: [id, "Иванов", "code"]
        print(f"|{idc_str(idc):^{idc_width}s}|{surname:^{surname_width}s}|{code:^{code_width}s}|")
    print("-" * total_width)

main()