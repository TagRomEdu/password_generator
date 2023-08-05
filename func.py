def check_is_num(string: str) -> str:
    while not string.isdigit():
        string = input("Введите число:\n")
    return string


def check_is_correct(string: str) -> str:
    while string.lower() != "да" and string.lower() != "нет":
        string = input("Введите да или нет...\n")
    return string


def delete_symb(string: str) -> str:
    for letter in 'il1Lo0O':
        if letter in string:
            string = string.replace(letter, '')
    return string


def generate_password():
    pass