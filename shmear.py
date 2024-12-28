'''
shmear
'''
import doctest

st = "hello"
print(st) 
print(st[0])
print(st[1])

print(len(st))


def letter_finder(word, letter):
    """
    this function takes in a word and
    a letter and returns the index of
    the letter in the word

    >>> letter_finder('word', 'y')
    -1
    >>> letter_finder(' ', ' ')
    0
    """
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

doctest.testmod(verbose = True)


st.isalpha() #tells if its all letters or not

st.isdigit() # tells if its a number or not

message = 'hello World!'

new_mes = 'w' + message[1:6] #everything after 0 prints until 6

