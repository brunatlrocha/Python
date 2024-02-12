# Bruna Rocha
morse_code_dict = {
    'A': '*-', 'B': '-***', 'C': '--', 'D': '-**', 'E': '*', 'F': '*-', 'G': '--*', 'H': '****',
    'I': '**', 'J': '*---', 'K': '-*-', 'L': '-*', 'M': '--', 'N': '-*', 'O': '---', 'P': '--*',
    'Q': '--*-', 'R': '-', 'S': '***', 'T': '-', 'U': '**-', 'V': '***-', 'W': '*--', 'X': '-**-',
    'Y': '-*--', 'Z': '--**',
    '1': '*----', '2': '**---', '3': '***--', '4': '****-', '5': '*****', '6': '-****-', '7': '--***',
    '8': '---**', '9': '----*', '0': '-----',
    '.': '--*-', ',': '--**--', ':': '---***', '?': '--', "'": '----', '-': '-****-', '/': '-**-*',
    '(': '----', ')': '----*', '"': '-**-', '_': '**--*-', '&': '*--*', '@': '*--*-*'
}

def sanitizeText(input_str, morse_dict):
    sanitized_str = ''
    for char in input_str.upper():
        if char in morse_dict:
            sanitized_str += char
    return sanitized_str

def textToMorseCode(input_str, morse_dict):
    return [morse_dict[char] for char in input_str.upper() if char in morse_dict]

def printMorseCode(morse_list, delay):
    for code in morse_list:
        for symbol in code:
            if symbol == '*':
                print("Ti", end=' ')
            elif symbol == '-':
                print("Ta", end=' ')
            else:
                print(" ", end=' ')
            time.sleep(delay)
        time.sleep(delay * 2)
    print()

test_string = "#$%Hello world; !@#"
sanitized_string = sanitizeText(test_string, morse_code_dict)
print("Sanitized String:", sanitized_string)

morse_code_list = textToMorseCode(sanitized_string, morse_code_dict)
print("Morse Code List:", morse_code_list)

printMorseCode(morse_code_list, 0.5)