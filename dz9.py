"""Консольний бот-помічник, що розпізнає команди та відповідає"""
import sys


def errors_commands(func):
    """Функія-декоратор, що ловить помилки вводу"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            return "Invalid number of arguments. Please check your input."
        except (KeyError, ValueError, IndexError):
            return "An error occurred."
    return inner

users_dict = {}

@errors_commands
def hello_user():
    """Функція обробляє команду-привітання 'hello'
    """
    return "How can I help you?"

@errors_commands
def add_contact(name, phone):
    """Функція обробляє команду 'add'
    """
    users_dict[name] = phone
    return f"Contact {name} added."

@errors_commands
def change_phone(name, phone):
    """Функція обробляє команду 'change'
    """
    if name in users_dict:
        users_dict[name] = phone
        return f"Phone {name} changed."
    # else:
    #     return f"Contact {name} not found."

@errors_commands
def show_phone(name):
    """Функція обробляє команду 'phone'
    """
    if name in users_dict:
        return f"The phone {name} is {users_dict[name]}."
    # else:
    #     return f"Contact {name} not found."

@errors_commands
def show_all():
    """Функція обробляє команду 'show all'
    """
    if users_dict:
        return "\n".join([f"{name}: {phone}" for name, phone in users_dict.items()])
    # else:
    #     return "No contacts found."

@errors_commands
def farewell():
    """Функція обробляє команди виходу
    """
    return "Good bye!"


def main():
    """Функція, яка приймає консольні команди користувача і відповідає 
    """
    while True:
        user_command = input("Please enter a command: ").lower().split()
        if not user_command:
            continue

        if user_command == 'hello':
            print(hello_user())
        elif user_command[0] == 'add':
            print(add_contact(*user_command[1:]))
        elif user_command[0] == 'change':
            print(change_phone(*user_command[1:]))
        elif user_command[0] == 'phone':
            print(show_phone(*user_command[1:]))
        elif user_command[0] == 'show' and  user_command[1] == 'all':
            print(show_all())
        elif user_command[0] in ('good bye', 'close', 'exit'):
            print(farewell())
            sys.exit()
        else:
            print('Invalid command.')


if __name__ == '__main__':
    main()
