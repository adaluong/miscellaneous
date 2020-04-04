# print a sentence given a word
# for finding the number of times Hamlet mentions death  

import re

text = input('which text? ').lower()
word = input('what word? ').lower()

def find_word():
    counter = 0
    for line in open((text)+'.txt'):
        match = re.search(word, line.lower())
        if match:
            counter+=1
            print(line.strip())
    print(f'number of times the word {word} appears in {text}: {str(counter)}',end='\n')

while word:
    find_word()
    word = input('what word? ').lower()
