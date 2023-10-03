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

