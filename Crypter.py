import get_code
import random
import Décrypter

def crypter():
    with open("crypter_text.txt", "r") as f:
        texte = f.read()

    # print(texte)
    lettre = get_code.get_alphabet_code()
    # print(lettre)

    texte_mots = texte.split()

    # print(texte_mots)

    for n in range(len(texte_mots)):
        if "-" in texte_mots[n]:
            texte_mots.insert(n, texte_mots[n].split("-")[0])
            texte_mots.insert(n + 1, texte_mots[n + 1].split("-")[1])
            del texte_mots[n + 2]

    # print(texte_mots)
    texte_code = []
    for z in range(len(texte_mots)):
        for i in texte_mots[z].lower():
            texte_code.append(lettre.get(i))
        # print(texte_mots[z].lower())
    # print(texte_code)

    # texte_code + spaces
    spaces = get_code.get_space_code()

    # print(texte.split(" "))
    if "\n" in texte.split(" "):
        texte = texte.replace("\n", " ")

    g = len(texte.split(" ")[0])
    for e in range(len(texte.split(" "))):
        texte_code.insert(e + g, random.choice(spaces))
        if e < len(texte.split(" ")) - 1:
            g += len(texte.split(" ")[e + 1])

    print(texte_code)
    # final = ''.join(texte_code)
    final = ""
    for s in texte_code:
        final = final + str(s)

    with open("texte_code_final.txt", "w") as dick:
        dick.write(final)
    # print(final)

    # print(Décrypter.decrypter())

crypter()