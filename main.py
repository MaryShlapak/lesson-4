###
# 1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер,
# цифр у рядку. Виведіть обидві кількості на екран. (використовувати цикл)
###

user_input = input("Enter your password: ")
letter_count = 0
digit_count = 0

for char in user_input:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
print("The number of letters =", letter_count)
print("The number of digits =", digit_count)