"""Консольний бот-помічник, що розпізнає команди та відповідає"""
import sys


def errors_commands(func):
    """Функія-декоратор, що ловить помилки вводу"""
    def inner(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError, TypeError, NameError) as err:
            error_messages = {
                KeyError: "Enter user name",
                ValueError: "Wron number",           
                IndexError: "Index out of range. Please provide valid input.",
                TypeError: "Invalid number of arguments. Please check your input.",
                NameError: "Wrong command"
            }
            return error_messages.get(type(err), "An error occurred.")
    return inner


users_dict = {}


def hello_user():
    """Функція обробляє команду-привітання 'hello'
    """
    return "How can I help you?"


def add_contact(name, phone):
    """Функція обробляє команду 'add'
    """
    users_dict[name] = int(phone)
    return f"Contact {name} added."


def change_phone(name, phone):
    """Функція обробляє команду 'change'
    """
    if name in users_dict:
        users_dict[name] = int(phone)
        return f"Phone {name} changed."
    else:
        return f"Contact {name} not found."


def show_phone(name):
    """Функція обробляє команду 'phone'
    """
    if name in users_dict:
        return f"The phone {name} is {users_dict[name]}."
    else:
        return f"Contact {name} not found."


def show_all():
    """Функція обробляє команду 'show all'
    """
    if users_dict:
        return "\n".join([f"{name}: {phone}" for name, phone in users_dict.items()])
    else:
        return "No contacts found."

def farewell():
    """Функція обробляє команди виходу
    """
    return "Good bye!"


@errors_commands
def parser_command(user_command):
    """Функція, яка обробляє команди користувача і повертає відповідь 
    """
    users_commands = {
        'hello': hello_user,
        'add': add_contact,
        'change': change_phone,
        'phone': show_phone,
        'show'+' '+'all': show_all,
        'good'+' '+'bye': farewell,
        'close': farewell,
        'exit': farewell
    }

    command = user_command[0]
    if command in users_commands:
        if len(user_command) > 1:
            return users_commands[command](*user_command[1:])
        else:
            return users_commands[command]()
    else:
        return 'Invalid command.'


def main():
    """Функція, яка приймає консольні команди користувача і відповідає 
    """
    while True:
        user_command = input("Please enter a command: ").lower().split()
        if not user_command:
            continue
        else:
            print(parser_command(user_command))
            if parser_command(user_command) == "Good bye!":
                sys.exit()


if __name__ == '__main__':
    main()
