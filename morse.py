#Morse Code Interpreter
morse_code = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
    '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'
]
alpha = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
alpha = alpha.split(' ')
dict1 = {}
dict2 = {}
for i in range(26):
    dict1[alpha[i]] = morse_code[i]
    dict2[morse_code[i]] = alpha[i]
def main():
    while True:
        user_input = input('Alphabets to morse or Morse to alphabets:')
        user_input = user_input.strip().lower()
        try:
            if 'alphabets to morse' in user_input:
                get_morse()
                break
            elif 'morse to alphabets' in user_input:
                get_alphabet()
                break
            else:
                print('Please enter the correct format')
                pass
        except ValueError:
            pass

def get_morse():
    while True:
        y1 = ''
        try:
            x1 = input('Enter an alphabet: ').upper().strip()
            if x1 == 'EXIT':
                main()
                break
            list1 = []

            for j in x1:
                list1.append(j)

            for k in list1:
                if k in dict1:
                    y1 += dict1[k] + ' '
            print('Alphabets translates to: ', y1)

        except ValueError:
            pass

        except EOFError:
            break
def get_alphabet():
    while True:
        y2 = ''
        try:
            x2 = input('Enter Morse Code or exit: ').upper().strip()
            if x2 == 'EXIT':
                main()
                break
            x2 = x2.split()
            for k in x2:
                if k == '/':
                    y2 += ' '
                if k in dict2:
                    y2 += dict2[k]
            print('Morse Code translates to: ', y2.capitalize())
        except ValueError:
            pass
        except EOFError:
            break
main()











