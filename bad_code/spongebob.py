# a program to capitalise the first vowel of a word

sentence = input('sentence: ')

while sentence:
    spongebob = ""
    counter = 0
    for letter in sentence:
        if letter == ' ':
            counter = 0
        elif letter in 'aeiou' and counter == 0:
            letter = letter.upper()
            counter += 1
        spongebob += letter
    print(spongebob)

    print(
    '''
              *
               *
          ----//-------
          \..C/--..--/ \   `A
           (@ )  ( @) \  \// |w
            \          \  \---/
             HGGGGGGG    \    /`
             V `---------`--'
                 <<    <<
                ###   ###
    '''
        )
    sentence = input('sentence: ')

#import re; print(re.sub(r'[^aeiou ]*([aeiou])[^ ]*', lambda c: c[0].replace(c[1], c[1].upper(), 1), input('Sentence: ')))

