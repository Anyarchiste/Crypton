
def get_code_1():
    with open("Alpha.txt", "r") as f:
        code_f = f.read()
    return code_f


def get_alpha():
    alpha_f = []
    for n in range(0, 26):
        alpha_f.append(chr(97 + n))
    return alpha_f


def get_alphabet(alpha_t, code_t):
    alphabet = {}
    for i in range(0, 26):
        alphabet[alpha_t[i]] = code_t.split(",")[i]
    return alphabet


def get_ponctuation_crypter(alpha_spaces_2):
    with open("ponctuation.txt", "r") as m:
        code_ponctuation_crypter = m.read()

    # print(code_ponctuation_crypter.split(","))
    ponctuation = [",", ".", "?", "!", '"', "'", "«", "»", ":", ";"]
    for y in range(len(code_ponctuation_crypter.split(","))):
        alpha_spaces_2[ponctuation[y]] = code_ponctuation_crypter.split(",")[y]

    return alpha_spaces_2


def get_alphabet_code():
    code = get_code_1()
    alpha = get_alpha()
    asdf = get_alphabet(alpha, code)
    code_alpha_ponctuation = get_ponctuation_crypter(asdf)
    return code_alpha_ponctuation


def get_space_code():
    with open("space.txt") as f:
        spaces = f.read().split(",")
    return spaces


def get_alpha_decrypter():
    alpha_f = []
    for n in range(0, 26):
        alpha_f.append(chr(97 + n))
    return alpha_f


def get_alphabet_decrypter(alpha_t, code_t):
    alphabet = {}
    for i in range(0, 26):
        alphabet[code_t.split(",")[i]] = alpha_t[i]

    return alphabet


def get_spaces_decrypter(alphabet_2):
    with open("space.txt", "r") as k:
        spaces = k.read()

    for y in spaces.split(","):
        alphabet_2[y] = " "

    return alphabet_2


def get_ponctuation_decrypter(alpha_spaces_decrypter_2):
    with open("ponctuation.txt", "r") as l:
        code_ponctuation = l.read()

    # print(code_ponctuation)
    # print(code_ponctuation.split(","))
    # print(alpha_spaces_decrypter_2)

    ponctuation = [",", ".", "?", "!", '"', "'", "«", "»", ":", ";"]
    for y in range(len(code_ponctuation.split(","))):
        alpha_spaces_decrypter_2[code_ponctuation.split(",")[y]] = ponctuation[y]

    return alpha_spaces_decrypter_2


def get_alphabet_code_decrypter():
    code_decrypter = get_code_1()
    alpha_decrypter = get_alpha_decrypter()
    message_decypter = get_alphabet_decrypter(alpha_decrypter, code_decrypter)
    alpha_spaces_decrypter = get_spaces_decrypter(message_decypter)
    alpha_spaces_ponctuation_decrypter = get_ponctuation_decrypter(alpha_spaces_decrypter)
    return alpha_spaces_ponctuation_decrypter
