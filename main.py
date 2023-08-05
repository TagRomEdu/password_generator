from func import check_is_num, check_is_correct, delete_symb, generate_password


DIGITS = '0123456789'
LOWERCASE_LETTER = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'


def main():

    chars = ''

    password_count = check_is_num(input("Сколько паролей желаешь создать? Введи число:\n"))

    len_password = check_is_num(input("Длина одного пароля? Число:\n"))

    digit_in_pass = check_is_correct(input(f"Будет ли он содержать {DIGITS}? Да или нет:\n"))
    if digit_in_pass.lower() == "да":
        chars += DIGITS

    upper_letters = check_is_correct(input(f"Будет ли он содержать прописные {UPPERCASE_LETTER}? Да или нет:\n"))
    if upper_letters.lower() == "да":
        chars += UPPERCASE_LETTER

    lower_letters = check_is_correct(input(f"Будет ли он содержать строчные {LOWERCASE_LETTER}? Да или нет:\n"))
    if lower_letters.lower() == "да":
        chars += LOWERCASE_LETTER

    symbols = check_is_correct(input(f"Включим символы {PUNCTUATION}? Да или нет:\n"))
    if symbols.lower() == "да":
        chars += PUNCTUATION

    exclude_symbols = check_is_correct(input("Будем исключать неоднозначные символы: il1Lo0O? Да или нет:\n"))
    if exclude_symbols.lower() == "да":
        chars = delete_symb(chars)

    generate_password(password_count, chars, len_password)


if __name__ == '__main__':
    main()
