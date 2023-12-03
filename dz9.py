def errors_commands(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as err:
            error_messages = {
                KeyError: "Enter user name",
                ValueError: "Give me name and phone please",
                IndexError: "Index out of range. Please provide valid input."
            }
            return error_messages.get(type(err), "An error occurred.")
    return inner

users_dict = {}

@errors_commands
def hello_user():
    return "How can I help you?"

@errors_commands
def add_contact(name, phone):
    users_dict[name] = phone
    return "Contact added."

@errors_commands
def change_phone(name, phone):
    if name in users_dict:
        users_dict[name] = phone
        return "Phone changed."
    else:
        return "Invalid command."

@errors_commands
def show_phone(name):
    if name in users_dict:
        return users_dict[name]
    else:
        return "Invalid command."

@errors_commands
def show_all():
    return users_dict

@errors_commands
def farewell():
    return "Good bye!"


def main():
    while True:
        user_command = input("Please enter a command: ").lower().split()
        if not user_command:
            continue

        if user_command[0] == 'hello':
            print(hello_user())
        elif user_command[0] == 'add':
            print(add_contact(*user_command[1:]))
        elif user_command[0] == 'change':
            print(change_phone(*user_command[1:]))
        elif user_command[0] == 'phone':
            print(show_phone(user_command[1:]))
        elif user_command[0] == 'show all':
            for name, phone in show_all().items():
                print(users_dict[name], end='\n')
        elif user_command[0] in ('good bye', 'close', 'exit'):
            print(farewell())
            exit()
        else:
            print('Invalid command.')


if name == 'main':
    main()