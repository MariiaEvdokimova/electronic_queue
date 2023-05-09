"""
- Фамилии клиентов вводятся с клавиатуры. Система ставит клиента в очередь.
  После этого вновь выводит приглашение ввести фамилию (следующему клиенту).
  Реализовать цикл ввода фамилий. Выход из цикла – по вводу пустой строки.
- Для хранения фамилий использовать список.
- После ввода очередной фамилии (и перед вводом следующей)
  отобразить содержимое очереди в форматированном виде. Ширины полей - произвольные.
"""

def main():
    eq = []
    version = 2.1
    while True:
        eq_print(eq, version)
        data = input("Введите фамилию или пустая строка для выхода: ")
        if data == "":
            print("Всего вам доброго! До свидания!")
            break
        eq.append(data)

def eq_print(eq: list, version: str) -> None:
    print(f"Электронная очередь. Версия {version}")
    print("*" * 25)
    for client in eq:
        print(f"|{client:^20s}|")
    print("*" * 25)



main()