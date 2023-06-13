import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    n = len(plaintext)
    letterCodes = [ord(plaintext[i]) for i in range(n)]
    ciphertext = ""
    firstUpperCode = ord('A')
    firstLowerCode = ord('a')
    alphabetLength = 26

    for i in range(n):

        if plaintext[i].isalpha():
            if plaintext[i].islower():
                letterCodes[i] = (letterCodes[i] - firstLowerCode + shift) % alphabetLength + firstLowerCode
            else:
                letterCodes[i] = (letterCodes[i] - firstUpperCode + shift) % alphabetLength + firstUpperCode

    for i in letterCodes:
        ciphertext += chr(i)

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    firstUpperCode = ord('A')

    firstLowerCode = ord('a')
    alphapbetLength = 26

    n = len(ciphertext)
    codes = [ord(ciphertext[i]) for i in range(n)]

    for i in range(n):
        if ciphertext[i].isalpha():
            if ciphertext[i].islower():
                codes[i] = (codes[i] - firstLowerCode - shift + alphapbetLength) % alphapbetLength + firstLowerCode
            else:
                codes[i] = (codes[i] - firstUpperCode - shift + alphapbetLength) % alphapbetLength + firstUpperCode

    for i in codes:
        plaintext += chr(i)
        
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
