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
                ValueError: "Vron number",           
                IndexError: "Index out of range. Please provide valid input.",
                TypeError: "Invalid number of arguments. Please check your input.",
                NameError: "Vrong command"
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
    """Функція, яка приймає обробляє команди користувача і повертає відповідь 
    """
    if user_command[0] == 'hello':
        return(hello_user())
    elif user_command[0] == 'add':
        return(add_contact(*user_command[1:]))
    elif user_command[0] == 'change':
        return(change_phone(*user_command[1:]))
    elif user_command[0] == 'phone':
        return(show_phone(*user_command[1:]))
    elif user_command[0] == 'show' and  user_command[1] == 'all':
        return(show_all())
    elif user_command[0] in ('good bye', 'close', 'exit'):
        return(farewell())
        sys.exit()
    else:
        return('Invalid command.')


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
