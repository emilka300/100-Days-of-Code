import pandas as pd
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
dict_alpha = {row.letter: row.code for (index, row) in alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("input your name: ").upper()

phonetic_code_words = [dict_alpha[letter] for letter in name]
print(phonetic_code_words)