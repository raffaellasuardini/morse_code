morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}
symbols_accepted = [",", "?", ".", ";", "!", ' ']


def convert():
    print('Give me your secrets, i will transform it for you')
    sentence = input('Insert your sentence (only letters and numbers): ')
    result = ''
    for char in sentence:
        if char == ' ':
            result += ' '
        else:
            word_dec = morse_code_dict.get(char.upper())
            if word_dec:
                result += word_dec + ' '
            else:
                print('this symbol is not permitted ' + char)
                convert()
                break
    print('in morse code you sentence is: ' + result)


def decript():
    pass


def main():
    print('W E L C O M E')
    print('Insert x to exit')
    again = True
    while again:
        choice = input('Want to convert or decript in morse code? (insert c/d) ')
        if choice.lower() == 'c':
            convert()
        elif choice.lower() == 'd':
            decript()
        elif choice.lower() == 'x':
            print('See you later alligator')
            again = False
        else:
            print('Sorry i do not understand right, repeat')
            continue


if __name__ == '__main__':
    main()
