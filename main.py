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

        ###
        # 4. Дано рядок. (зробити зрізи)
        #
        # - Спершу виведіть третій символ цього рядка.
        #
        # - У другому рядку виведіть передостанній символ цього рядка.
        #
        # - У третьому рядку виведіть перші п'ять символів цього рядка.
        #
        # - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
        #
        # - У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0,
        # тому символи виводяться з першого).
        #
        # - У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
        #
        # - У сьомому рядку виведіть усі символи у зворотному порядку.
        #
        # - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
        #
        # - У дев'ятому рядку виведіть довжину цього рядка.
        ###

user_input = input("Enter your word: ")
print(user_input[2])
print(user_input[-2])
print(user_input[0:5])
print(user_input[0:-2])
print(user_input[2::2])
print(user_input[1::2])
print(user_input[len(user_input)::-2])
print(len(user_input))