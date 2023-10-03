###
# 1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер,
# цифр у рядку. Виведіть обидві кількості на екран. (використовувати цикл)
###

user_input = input("Enter your password: ")
if user_input.isalpha() == True:
    letter_count = len(user_input)
    print(f"Letter count = {letter_count}\nDigit count = 0")
elif user_input.isnumeric() == True:
    digit_count = len(user_input)
    print(f"Digit count = {digit_count}\nLetter count = 0")
else:
