import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()
phonetic_code = [phonetic_dict[char] for char in user_input]
print(phonetic_code)
