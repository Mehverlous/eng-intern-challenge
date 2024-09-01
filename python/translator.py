import sys
from array import *

braille_to_english = {
    'O.....' : 'a',
    'O.O...' : 'b',
    'OO....' : 'c',
    'OO.O..' : 'd',
    'O..O..' : 'e',
    'OOO...' : 'f',
    'OOOO..' : 'g',
    'O.OO..' : 'h',
    '.OO...' : 'i',
    '.OOO..' : 'j',
    'O...O.' : 'k',
    'O.O.O.' : 'l',
    'OO..O.' : 'm',
    'OO.OO.' : 'n',
    'O..OO.' : 'o',
    'OOO.O.' : 'p',
    'OOOOO.' : 'q',
    'O.OOO.' : 'r',
    '.OO.O.' : 's',
    '.OOOO.' : 't',
    'O...OO' : 'u',
    'O.O.OO' : 'v',
    '.OOO.O' : 'w',
    'OO..OO' : 'x',
    'OO.OOO' : 'y',
    'O..OOO' : 'z',
    '.....O' : 'cf',
    '.O...O' : 'df',
    '.O.OOO' : 'nf',
    '..OO.O' : '.',
    '..O...' : ',',
    '..O.OO' : '?',
    '..OOO.' : '!',
    '..OO..' : ':',
    '..O.O.' : ';',
    '....OO' : '-',
    '.O..O.' : '/',
    '.OO..O' : '<',
    'O.O..O' : '(',
    '.O.OO.' : ')',
    '......' : ' '
}

english_to_braille = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'p' : 'OOO.O.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO',
    'cf' : '.....O',
    'df' : '.O...O',
    'nf' : '.O.OOO',
    '.' : '..OO.O',
    ',' : '..O...',
    '?' : '..O.OO',
    '!' : '..OOO.',
    ':' : '..OO..',
    ';' : '..O.O.',
    '-' : '....OO',
    '/' : '.O..O.',
    '<' : '.OO..O',
    '(' : 'O.O..O',
    ')' : '.O.OO.',
    ' ' : '......'
}



def check(argv):
    for x in argv[1]:
        if (x != '.') & (x != 'O'):
            return 0
    
    return 1

def combine(argv):
    result = argv[1]

    for x in argv[2:]:
        result += " " + x

    return result


def translate_to_english(b_input):
    cap_follows = False
    num_follows = False
    dec_follows = False
    result = ""

    while len(b_input) > 5: 
        braille = b_input[:6]
        b_input = b_input[6:]
        translation = braille_to_english.get(braille)

        if translation == 'cf':
            cap_follows = True
            continue
        elif translation == 'nf':
            num_follows = True
            braille_to_english.update({'O..OO.':'>'})
            continue
        elif translation == ' ':
            num_follows = False
            braille_to_english.update({'O..OO.':'o'})

        if cap_follows == True:
            translation = translation.capitalize()
            cap_follows = False
        elif num_follows == True:
            translation =  '{}'.format((ord(translation) - 96) % 10)

        result += translation
    
    print(result)

def translate_to_braille(e_input):
    cap_follows = False
    num_follows = False
    dec_follows = False
    result = ""

    for x in e_input:
        if x == ' ':
            num_follows = False
            english_to_braille.pop('>', None)
            english_to_braille.update({'o' : 'O..OO.'})
            translation = english_to_braille.get(x) 
        elif x.isupper():
            result += english_to_braille.get('cf')
            translation = english_to_braille.get(x.lower())
        elif (48 <= ord(x) <= 57) & (num_follows == False):
            num_follows = True
            result += english_to_braille.get('nf')
            english_to_braille.pop('o', None)
            english_to_braille.update({'>' : 'O..OO.'})

            if ord(x) == 48:
                translation = english_to_braille.get('j')
            else:
                translation = english_to_braille.get(chr(ord(x) + 48))
        elif (num_follows == True):
            if ord(x) == 48:
                translation = english_to_braille.get('j')
            else:
                translation = english_to_braille.get(chr(ord(x) + 48))
        else:
            translation = english_to_braille.get(x)


        result += str(translation) 
    print(result)

def main():
    if len(sys.argv) > 2:
        translate_to_braille(combine(sys.argv))
    elif check(sys.argv) == 0:
        translate_to_braille(sys.argv[1])
    else:
        translate_to_english(sys.argv[1])
    

if __name__ == '__main__':
    main()