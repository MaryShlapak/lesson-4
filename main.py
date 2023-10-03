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