import pandas

export_letter_code = {}
df = pandas.read_csv('nato_phonetic_alphabet.csv')
for (index, row) in df.iterrows():
    letter_code_dict = {row.letter:row.code for letter in row}
    export_letter_code.update(letter_code_dict)

user_word = input('Enter a word: ').upper()

user_nato = [export_letter_code[letter] for letter in user_word]
print(user_nato)
