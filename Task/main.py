from colorama import Fore, init
from commands import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from address_book import AddressBook
import sys

# Перекодування для підтримки емодзі
sys.stdout.reconfigure(encoding='utf-8')

# Ініціалізація кольорів для терміналу
init(autoreset=True)

def parse_input(user_input):
    # Розділяємо команду і аргументи користувача
    cmd, *args = user_input.split()
    return cmd.lower(), args

def main():
    book = AddressBook()  # Ініціалізація книги контактів
    print(Fore.BLUE + "Welcome to the assistant bot! 🤖")

    while True:
        user_input = input(Fore.BLUE + "Enter a command: ").strip()
        
        # Якщо введено порожній рядок, пропускаємо ітерацію
        if not user_input:
            continue
        
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.BLUE + "Good bye! 👋")
            break
        elif command == "hello":
            print(Fore.BLUE + "How can I help you? 😊")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print(Fore.RED + "❌ Invalid command. Use 'add', 'change', 'phone', 'all', 'add-birthday', 'show-birthday', 'birthdays', 'hello', 'exit', or 'close'.")

if __name__ == "__main__":
    main()