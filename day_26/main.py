
import pandas

#TODO 1: create a dictionary using the csv file in this format { 'A' : 'Alpha' }
#TODO 2 : create a phonetic word from the input word provided by the user

data = pandas.read_csv("nato_phonetic_alphabet.csv")
names = { row.letter:row.code for (index, row) in data.iterrows()}
word = input("Enter a word:").upper()

phonetic_name = { names[letter] for letter in word}
print(phonetic_name)