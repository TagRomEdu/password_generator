def check_is_num(string: str) -> str:
    """
    To check the string is digit
    """
    while not string.isdigit():
        string = input("Введите число:\n")
    return string


def check_is_correct(string: str) -> str:
    """
    To check the string is YES or NO
    """
    while string.lower() != "да" and string.lower() != "нет":
        string = input("Введите да или нет...\n")
    return string


def delete_symb(string: str) -> str:
    """
    To delete specific symbols
    """
    for letter in 'il1Lo0O':
        if letter in string:
            string = string.replace(letter, '')
    return string
