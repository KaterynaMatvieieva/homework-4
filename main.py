
#Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран. (використовувати цикл)

# try:
#
#     letters_count = 0
#     digits_count = 0
#
#     message = input("Enter several words or sentence or just random symbols to count amount of letters and digits in it")
#
#     if message == "":
#         raise Exception("Please try again and enter at least one symbol")
#
#     for symbol in message:
#
#         if symbol.isalpha():
#             letters_count += 1
#
#         if symbol.isnumeric():
#             digits_count += 1
#
#         if letters_count + digits_count == 0:
#             raise Exception("There is no any letter or digit in the entered text")
#
#     print(f"Letters amount in entered text is: {letters_count}, digits amount in entered text is {digits_count}")
#
# except Exception as e:
#     print(f"Error: {e}")

# #Користувач вводить з клавіатури рядок та символ для пошуку. Порахуйте скільки разів у рядку зустрічається потрібний символ. Отримане число виведіть на екран.

# try:
#
#     message = input("Enter several words or sentence or just random symbols: ")
#
#     if message == "":
#         raise Exception("Please try again and enter at least one symbol")
#
#     ready_message = message.strip()
#
#     message_lower = ready_message.lower()
#
#     search = input("\nEnter the symbol you want to know the amount of in entered text:")
#
#     if search == "":
#         raise Exception("Please try again and enter at least one symbol for search")
#
#     ready_search = search.strip()
#
#     search_lower = ready_search.lower()
#
#     if len(search_lower) > 1:
#         raise Exception("There should be only one symbol for search. Please try again")
#
#     symbol_count = message_lower.count(search_lower)
#
#     print(f"\nThe amount of symbol {search_lower} in entered text is {symbol_count}")
#
# except Exception as e:
#    print(f"Error: {e}")

#Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни. Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.

# try:
#
#     text = input("Enter several random words or sentence: ")
#     if text == "":
#         raise Exception("Please try again and enter at least one word")
#
#     searched_word = input("Enter the word you want to replace: ")
#     if searched_word == "":
#         raise Exception("Please try again and enter at least one word to be replaced")
#     ready_searched_word = searched_word.strip()
#
#     new_word = input("Enter the word with what you want to replace the previous one: ")
#     if new_word == "":
#         raise Exception("Please try again and enter at least one word to be replaced")
#     ready_new_word = new_word.strip()
#
#     final_text = text.replace(ready_searched_word, ready_new_word)
#
#     print(f"Changed text: {final_text}")
#
# except Exception as e:
#     print(f"Error: {e}")

# Дано рядок. (зробити зрізи)
# - Спершу виведіть третій символ цього рядка.
# - У другому рядку виведіть передостанній символ цього рядка.
# - У третьому рядку виведіть перші п'ять символів цього рядка.
# - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# - У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться з першого).
# - У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
# - У сьомому рядку виведіть усі символи у зворотному порядку.
# - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
# - У дев'ятому рядку виведіть довжину цього рядка.

#text = input("Enter several random words or sentence: ")

# print("The third symbol in entered text is: ", text[2])
#
# print("The second symbol from the end in entered text is: ", text[-2])
#
# print("The first five symbols of the entered text is: ", text[0:5])
#
# print("Entered text except the last two symbols: ", text[0:-2])
#
# print("All symbols with the even indexes: ", text[2::2])
#
# print("All symbols with the odd indexes: ", text[1::2])
#
# print("Reversed text: ",text[::-1])

# print("All symbols of the text one by one in reverse order, starting with the last one: ", text[::-2])

# print("The length of the entered text is ",len(text), "symbols")

# Є певний текст. Реалізуйте наступну функціональність:
# ■ Порахуйте скільки разів цифри зустрічаються у тексті;
# ■ Порахуйте скільки разів розділові знаки зустрічаються в тексті;
# ■ Порахуйте кількість знаків оклику в тексті.

# digits_count = 0
# separators_count = 0
# letter_count = 0
# spaces_count = 0
#
#text = input("Enter some text which contains several sentences:")

# exclamation_mark_count = text.count("!")
#
# for symbol in text:
#
#     if symbol.isnumeric():
#         digits_count += 1
#     elif symbol == " ":
#         spaces_count += 1
#     elif symbol.isalpha():
#         letter_count += 1
#     else:
#         separators_count += 1
#
# print(f"Digits amount is {digits_count}, separators amount is {separators_count}, exclamation marks amount is {exclamation_mark_count}")

# ■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;

# text = input("Enter several sentences each of what starts with letter in lower register and ends with simple dot:")
#
# search_item = ". "
# first_index = text.find(search_item)
# first_sentence = text[:first_index + len(search_item)].capitalize()
#
# next_index = 0
# next_sentence = ""
#
#
# while next_index >= 0:
#     next_index = text.find(search_item, first_index+1)
#     next_sentence = text[first_index+len(search_item):next_index+len(search_item)].capitalize()
#     new_sentence = first_sentence + next_sentence
#     first_index = next_index
#     first_sentence = new_sentence
#
# print(first_sentence)