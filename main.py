import pandas


df_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in df_alphabet.iterrows()}

def generate_phonetic():
    input_word = input("Write a word: ")
    try:
        output_list = [phonetic_dict[letter.upper()] for letter in input_word]
    except KeyError:
        print(f"ERROR - '{input_word}' uses symbols that are not in the NATO phonetic alphabet. \n"
              f"Try Again.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()