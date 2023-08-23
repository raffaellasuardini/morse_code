# Morse Code Converter

Convert text to Morse code and vice versa using this simple Python script.

## Introduction 
This project aims to provide a user-friendly way to convert text to International Morse code and decode Morse code back to text.
The script utilizes a predefined dictionary to map characters to their corresponding Morse code representations. The user can choose between conversion and decryption functionalities.

## Features
+ Convert text to Morse code
+ Decode Morse code to text
+ User-friendly command-line interface

 ## Installation
Clone the repository to your local machine
```bash 
 git clone https://github.com/raffaellasuardini/morse-code-converter.git 
 ```
## Usage
1. Open your terminal and navigate to the project directory
2. Run the script using the following command:
```bash
python3 morse_code_converter.py
```
3. Follow the prompt to either convert text to Morse or decode Morse code to text

## Examples
### Convert Text to Morse Code
```
W E L C O M E
Insert x to exit
Want to convert or decrypt in morse code? (insert c/d) c
Give me your sentence, I will transform it for you
Insert your sentence: Hello, World!
In Morse code, your sentence is: .... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.-- 
```
#### Note:
Just type letters, numbers and punctuation, 
but if the character cannot be translated will be replaced by '#'

### Decode Morse Code to Text
```
W E L C O M E
Insert x to exit
Want to convert or decrypt in morse code? (insert c/d) d
Insert your code Morse: .... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--
This is your sentence converted: hello, world!
```
#### Note:
You can type Morse code using "." for dot and "-" for dash. 
Letters are separated by spaces and words by "/". 
If a character can't be translated a "#" will appear in the output.

## Contributions
Contributions and feedback are welcome!
Feel free to fork the repository and submit pull requests.