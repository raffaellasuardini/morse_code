morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}
symbols_accepted = [",", "?", ".", ";", "!"]

def main():
    sentence = input('Insert your sentence (only letters and numbers): ')
    result = ''
    for word in sentence:
        word_dec = morse_code_dict.get(word.upper())
        if word_dec:
            result = result + word_dec
        else:
            print('this symbol is not permitted '+ word)
            main()
            break
    print('in morse code you sentence is: '+result)




if __name__ == '__main__':
    main()
