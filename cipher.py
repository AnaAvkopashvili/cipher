def encryptAtbashCipher(text):
    new_text = ""
    for i in range(0, len(text)):
        new_char = chr(219 - ord(text[i]))
        new_text += new_char
    return new_text


def decryptAtbashCipher(new_text):
    text = ""
    for i in range(0, len(new_text)):
        new_char = chr(219 - ord(new_text[i]))
        text += new_char
    return text


def encryptCaesarCipher(text, key):
    dic1 = {'!': '?', '?': '!', ',': '.', '.': ','}
    dic2 = {'0': '1', '1': '0', '2': '3', '3': '2', '4': '5', '5': '4', '6': '7', '7': '6', '8': '9', '9': '8'}

    new_text = ""
    for i in range(0, len(text)):
        if text[i].isalpha():
            new_char = chr(ord(text[i]) + (key % 26))
            new_text += new_char
        elif text[i] == '?' or text[i] == '!' or text[i] == ',' or text[i] == '.':
            new_char = dic1[text[i]]
            new_text += new_char
        elif text[i].isnumeric():
            new_char = dic2[text[i]]
            new_text += new_char
        else:
            new_char = text[i]
            new_text += new_char
    return new_text


def decryptCaesarCipher(new_text, key):
    dic1 = {'!': '?', '?': '!', ',': '.', '.': ','}
    dic2 = {'0': '1', '1': '0', '2': '3', '3': '2', '4': '5', '5': '4', '6': '7', '7': '6', '8': '9', '9': '8'}

    text = ""
    for i in range(0, len(new_text)):
        if new_text[i].isalpha():
            new_char = chr(ord(new_text[i]) - (key % 26))
            text += new_char
        elif new_text[i] == '?' or new_text[i] == '!' or new_text[i] == ',' or new_text[i] == '.':
            new_char = dic1[new_text[i]]
            text += new_char
        elif new_text[i].isnumeric():
            new_char = dic2[new_text[i]]
            text += new_char
        else:
            new_char = new_text[i]
            text += new_char
    return text


def encryptVigenereCipher(text, key_list):
    dic1 = {'!': '?', '?': '!', ',': '.', '.': ','}
    dic2 = {'0': '1', '1': '0', '2': '3', '3': '2', '4': '5', '5': '4', '6': '7', '7': '6', '8': '9', '9': '8'}

    new_text = ""
    new_str = ''.join(z for z in text if z not in ['?', '!', ',', '.'] and not z.isnumeric())
    for j in range(0, len(new_str)):
        if new_str[j].isalpha():
            new_char = chr(ord(new_str[j]) + (key_list[j % len(key_list)] % 26))
            new_text += new_char
    for i in range(0, len(text)):
        if text[i] == '?' or text[i] == '!' or text[i] == ',' or text[i] == '.':
            new_text = new_text[:i] + dic1[text[i]] + new_text[i:]
        elif text[i].isnumeric():
            new_text = new_text[:i] + dic2[text[i]] + new_text[i:]
        elif not text[i].isalpha() and not text[i].isnumeric() and text[i] not in ['?', '!', ',', '.']:
            new_text = new_text[:i] + text[i] + new_text[i:]
    return new_text


def decryptVigenereCipher(new_text, key_list):
    dic1 = {'!': '?', '?': '!', ',': '.', '.': ','}
    dic2 = {'0': '1', '1': '0', '2': '3', '3': '2', '4': '5', '5': '4', '6': '7', '7': '6', '8': '9', '9': '8'}

    text = ""
    new_str = ''.join(z for z in new_text if z not in ['?', '!', ',', '.'] and not z.isnumeric())
    for j in range(0, len(new_str)):
        if new_str[j].isalpha():
            new_char = chr(ord(new_str[j]) - (key_list[j % len(key_list)] % 26))
            text += new_char
    for i in range(0, len(new_text)):
        if new_text[i] == '?' or new_text == '!' or new_text == ',' or new_text == '.':
            text = text[:i] + dic1[new_text[i]] + text[i:]
        elif new_text[i].isnumeric():
            text = text[:i] + dic2[new_text[i]] + text[i:]
        elif not new_text[i].isalpha() and not new_text[i].isnumeric() and new_text[i] not in ['?', '!', ',', '.']:
            text = text[:i] + new_text[i] + text[i:]
    return text


def encryptSimpleEnigmaCipher(text, key_tuple):
    new_text = ''
    for i in range(0, len(text)):
        if text[i].isalpha():
            letter = text[i].lower()
            pos = ord(letter) - 97
            new_ord = ord(key_tuple[0][pos]) - 97
            new_ord = ord(key_tuple[1][new_ord]) - 97
            new_char = chr(ord(key_tuple[2][new_ord]))
            if text[i].islower():
                new_text += new_char
            else:
                new_text += new_char.upper()
        else:
            new_char = text[i]
            new_text += new_char
    return new_text


def decryptSimpleEnigmaCipher(new_text, key_tuple):
    text = ''
    new_char = ''
    for i in range(0, len(new_text)):
        if new_text[i].isalpha():
            letter = new_text[i].lower()
            index = key_tuple[2].index(letter)
            new_char = chr(index + 97)
            index = key_tuple[1].index(new_char)
            new_char = chr(index + 97)
            index = key_tuple[0].index(new_char)
            new_char = chr(index + 97)
            if new_text[i].isupper():
                text += new_char.upper()
            else:
                text += new_char
        else:
            new_char = new_text[i]
            text += new_char
    return text


if __name__ == '__main__':
    x = input("Enter: ")
    # print(encryptAtbashCipher(x))
    # print(decryptAtbashCipher(encryptAtbashCipher(x)))
    # print(encryptCaesarCipher(x, 3))
    print(decryptCaesarCipher(encryptCaesarCipher(x, 3), 3))
    # print(encryptVigenereCipher(x, [1, 3, 2]))
    # print(encryptVigenereCipher(x, [1, 3, 2]))
    # print(decryptVigenereCipher(encryptVigenereCipher(x, [1, 3, 2]), [1, 3, 2]))
    # print(encryptSimpleEnigmaCipher(x, ('bcdefghijklmnopqrstuvwxyza',
    #                                     'qwertyuioplkjhgfdsazxcvbnm',
    #                                     'zxcvbnmlkjhgfdsaqwertyuiop')))
    # print(decryptSimpleEnigmaCipher(encryptSimpleEnigmaCipher(x, ('bcdefghijklmnopqrstuvwxyza',
    #                                     'qwertyuioplkjhgfdsazxcvbnm',
    #                                     'zxcvbnmlkjhgfdsaqwertyuiop')), ('bcdefghijklmnopqrstuvwxyza',
    #                                     'qwertyuioplkjhgfdsazxcvbnm',
    #                                     'zxcvbnmlkjhgfdsaqwertyuiop')))
