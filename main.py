import random

DIGITS = '0123456789'
LOWERCASE_LETTER = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''

password_count = int(input("Сколько паролей желаешь создать? Введи число:\n"))
len_password = int(input("Длина одного пароля? Число:\n"))
digit_in_pass = input(f"Будет ли он содержать {DIGITS}? Да или нет:\n")
upper_letters = input(f"Будет ли он содержать прописные {UPPERCASE_LETTER}? Да или нет:\n")
lower_letters = input(f"Будет ли он содержать строчные {LOWERCASE_LETTER}? Да или нет:\n")
symbols = input(f"Включим символы {PUNCTUATION}? Да или нет:\n")
exclude_symbols = input("Будем исключать неоднозначные символы: il1Lo0O?\n")

