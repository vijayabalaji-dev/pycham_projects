import pandas

dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in dataframe.iterrows()}

can_run = True

while can_run:
    user_input = input("Enter a word: ").strip()
    try:
        result = [data_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        pass
    else:
        print(result)
        can_run = False
