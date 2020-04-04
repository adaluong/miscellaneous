# Calculates the scrabble value associated with a name, given a list of names
# prints names sorted from smallest to largest scrabble value

score = {'E':1,'A':1,'I':1,'O':1,'N':1,'R':1,'T':1,'L':1,'S':1,'U':1,
         'D':2,'G':2,
         'B':3,'C':3,'M':3,'P':3,
         'F':4,'H':4,'V':4,'W':4,'Y':4,
         'K':5,'J':8,'X':8,'Q':10,'Z':10,
         ',':0,' ':0,'-':0}

names = {}

with open('2019_names.txt') as f:
  for name in f:
    name = name.strip()
    total = 0
    for letter in name:
        total += score[letter]
    names[name] = total

sorted_names = sorted(names.items(), key = lambda x: x[1])
for name, value in sorted_names:
  print(value, name)
