def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    firstLowerCode = ord('a')
    firstUpperCode = ord('A')
    alphabetLength = 26

    lengthOfPlainText = len(plaintext)
    textCodes = [ord(plaintext[i]) for i in range(lengthOfPlainText)]

    lengthOfKeywordText = len(keyword)
    keyCodes = [ord(keyword[i]) for i in range(lengthOfKeywordText)]

    for i in range(lengthOfKeywordText):
        if keyword[i].isupper():
            keyCodes[i] -= firstUpperCode
        else:
            keyCodes[i] -= firstLowerCode

    for i in range(lengthOfPlainText):
        if plaintext[i].isalpha():
            if plaintext[i].islower():
                textCodes[i] = (textCodes[i] - firstLowerCode + keyCodes[
                    i % lengthOfKeywordText]) % alphabetLength + firstLowerCode
            else:
                textCodes[i] = (textCodes[i] - firstUpperCode + keyCodes[
                    i % lengthOfKeywordText]) % alphabetLength + firstUpperCode

    for i in textCodes:
        ciphertext += chr(i)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    firstLowerCode = ord('a')
    firstUpperCode = ord('A')
    alphLen = 26

    n = len(ciphertext)
    textCodes = [ord(ciphertext[i]) for i in range(n)]

    m = len(keyword)
    keyCodes = [ord(keyword[i]) for i in range(m)]
    for i in range(m):
        if keyword[i].isupper():
            keyCodes[i] -= firstUpperCode
        else:
            keyCodes[i] -= firstLowerCode

    for i in range(n):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                textCodes[i] = (textCodes[i] - firstUpperCode - keyCodes[
                    i % m] + alphLen) % alphLen + firstUpperCode
            else:
                textCodes[i] = (textCodes[i] - firstLowerCode - keyCodes[
                    i % m] + alphLen) % alphLen + firstLowerCode

    for i in textCodes:
        plaintext += chr(i)

    return plaintext
