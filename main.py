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


###
# 2. Користувач вводить з клавіатури рядок та символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається потрібний символ. Отримане число виведіть на екран.
###

user_input = input("Enter your sentence: ")
user_search = input("Enter your search symbol: ")

if user_input.count(user_search) >= 1:
    symbols_number = user_input.count(user_search)
    print(f"Number of symbols in the sentence = {symbols_number}")
elif len(user_search) > 1:
    print("Enter one symbol only please")
else:
    print("The sentence does not include this symbol")


###
# 3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
###

while True:
    user_input = input("Enter your sentence: ")
    user_search = input("Enter your search word: ")


    if user_input.count(user_search) >= 1:
        user_replace = input("Enter a word for replacement: ")
        print(user_input.replace(user_search,user_replace))
        break

    elif len(user_search) <= 1 and user_input.count(user_search) <= 1:
        print("The sentence does not include this symbol")
        while True:
            user_search = input("Enter your search word: ")
            if user_input.count(user_search) >= 1:
                user_replace = input("Enter a word for replacement: ")
                print(user_input.replace(user_search, user_replace))
                break
            elif len(user_search) > 1 and user_input.count(user_search) <= 1 and user_search.isnumeric() == True:
                print("The sentence does not include this digit")
                continue
            elif len(user_search) > 1 and user_input.count(user_search) <= 1 and user_search.isalpha() == True:
                print("The sentence does not include this word")
                continue
            else:
                print("The sentence does not include this symbol")
                continue
        break
    elif len(user_search) > 1 and user_input.count(user_search) <= 1 and user_search.isalpha() == True:
        print("The sentence does not include this word")
        while True:
            user_search = input("Enter your search word: ")
            if user_input.count(user_search) >= 1:
                user_replace = input("Enter a word for replacement: ")
                print(user_input.replace(user_search, user_replace))
                break
            elif len(user_search) > 1 and user_input.count(user_search) <= 1 and user_search.isnumeric() == True:
                print("The sentence does not include this digit")
                continue
            elif len(user_search) > 1 and user_input.count(user_search) <= 1 and user_search.isalpha() == True:
                print("The sentence does not include this word")
                continue
            else:
                print("The sentence does not include this symbol")
                continue
        break
    elif len(user_search) > 1 and user_input.count(user_search) <= 1 and user_search.isnumeric() == True:
        print("The sentence does not include this digit")
        while True:
            user_search = input("Enter your search word: ")
            if user_input.count(user_search) >= 1:
                user_replace = input("Enter a word for replacement: ")
                print(user_input.replace(user_search, user_replace))
                break
            elif len(user_search) > 1 and user_input.count(user_search) <= 1 and user_search.isnumeric() == True:
                print("The sentence does not include this digit")
                continue
            elif len(user_search) > 1 and user_input.count(user_search) <= 1 and user_search.isalpha() == True:
                print("The sentence does not include this word")
                continue
            else:
                print("The sentence does not include this symbol")
                continue
        break
    else:
        print("The sentence does not include this symbols")

        while True:
            user_search = input("Enter your search word: ")
            if user_input.count(user_search) >= 1:
                user_replace = input("Enter a word for replacement: ")
                print(user_input.replace(user_search, user_replace))
                break
            else:
                print("The sentence does not include this symbols")
                continue
        break