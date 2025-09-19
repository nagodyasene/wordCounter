alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word_list = []

def word_counter():
    user_text = input("Please enter a sentence: ")
    find_space(user_text)
    clean_words(word_list)
    check_how_many(word_list)

def find_space(input_text):
    word_finder = ""
    for letter in input_text:
        if letter != " ":
            word_finder += letter
        elif letter == " ":
            word_list.append(word_finder.lower())
            word_finder = ""
    if word_finder:
        word_list.append(word_finder.lower())

def clean_words(complete_word_list):
    word_index = 0
    while word_index < len(complete_word_list):
        letter_index = 0
        cleaned_word = ""
        while letter_index < len(complete_word_list[word_index]):
            if complete_word_list[word_index][letter_index] in alphabet:
                cleaned_word += complete_word_list[word_index][letter_index].strip()
            letter_index += 1
        complete_word_list[word_index] = cleaned_word
        word_index += 1

def check_how_many(complete_word_list):
    counted_words = []
    for word in complete_word_list:
        if word not in counted_words and word:
            word_count = complete_word_list.count(word)
            print(f'The word {word} is in the sentence {word_count} times.')
            counted_words.append(word)

word_counter()