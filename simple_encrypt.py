from collections import deque


def shift_list(paramater, shift):
    #
    shifted = deque(paramater)
    shifted.rotate(shift)
    return shifted


def encode(texts, shift):
    # var init
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "[]{}()+-*/:;<>,.?!_@#"
    shift = int(shift)
    # make shifted list
    s_letters = shift_list(letters, shift) + shift_list(letters.upper(), shift)
    s_numbers = shift_list(numbers, shift)
    s_symbols = shift_list(symbols, shift)
    # make shifted dictionary
    dicts = dict(zip(letters+letters.upper()+numbers+symbols,
                     s_letters+s_numbers+s_symbols))
    # replace words
    ntext = []
    for text in texts:
        if text not in dicts.keys():
            ntext.append(text)
        else:
            ntext.append(dicts[text])
    return "".join(ntext)
<<<<<<< Updated upstream

#enter inputs
text = input("Enter filename:\n" ) #e.g. test.txt
shift = int(input("Enter the number of places you want to shift:\n" )) #e.g. -2
#texts = "Hello World A123456 @{* Ωñæ"

#open file
with open(text, 'r') as filename:
    texts = filename.read().replace('\n', ' ')
print(encode(texts, shift))


#shift = -2
#texts = "Hello World A123456 @{* Ωñæ"
#print(encode(texts, shift))

"""
ISSUES TO BE SOLVED:
Make Test code
Test code
Make a decrpytor
Clean code
Break code
Optimize code
Open file to encrypt
Test more 
"""
=======
>>>>>>> Stashed changes
