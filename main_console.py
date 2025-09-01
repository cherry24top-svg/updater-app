
import os
from updater import self_update

def main_menu():
    while True:
        print("\n==== Обновлятор ====")
        print("1. Проверить обновление")
        print("2. Установить обновление")
        print("3. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            print("[*] Проверка обновлений...")
            result = self_update(check_only=True)
            print(result)
        elif choice == "2":
            print("[*] Обновление...")
            result = self_update()
            print(result)
        elif choice == "3":
            print("Выход...")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main_menu()
