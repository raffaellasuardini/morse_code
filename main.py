morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' ',
}

reverse_morse_dict = {v: k for k, v in morse_code_dict.items()}


def convert():
    print('Give me your secrets, i will transform it for you')
    sentence = input('Insert your sentence: ')
    result = ''
    for char in sentence:
        if char == ' ':
            result += '/ '
        else:
            word_dec = morse_code_dict.get(char.upper())
            if word_dec:
                result += word_dec + ' '
            else:
                print('this symbol is not permitted ' + char)
                convert()
                break
    print('in morse code you sentence is: ' + result)


def decrypt():
    code_morse = input('Insert your code morse: ').strip()
    result = ''
    arr = code_morse.split(' ')
    for el in arr:
        if el == '/':
            result += ' '
        else:
            letter = reverse_morse_dict.get(el)
            if letter:
                result += letter.lower()
            else:
                print('This code contains error, this is not valid code: ' + el)
                break
    print('This is your sentence converted: ' + result)


def main():
    print('W E L C O M E')
    print('Insert x to exit')
    again = True
    while again:
        choice = input('Want to convert or decrypt in morse code? (insert c/d) ')
        if choice.lower() == 'c':
            convert()
        elif choice.lower() == 'd':
            decrypt()
        elif choice.lower() == 'x':
            print('See you later alligator')
            again = False
        else:
            print('Sorry i do not understand right, repeat')
            continue


if __name__ == '__main__':
    main()
