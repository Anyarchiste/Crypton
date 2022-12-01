import get_code

def decrypter():
    with open("texte_code_final.txt", "r") as dick:
        message_brut = dick.read()

    # print(message_brut)

    UwU = get_code.get_alphabet_code_decrypter()

    message_v1 = list(message_brut.rsplit(":", -1))
    del(message_v1[0])

    message_refined = []
    for i in range(int(len(message_v1) / 4)):
        message_v2 = ':'.join(message_v1[0:4])
        message_refined.append(message_v2)
        del(message_v1[0:4])

    # print(message_refined)

    message_refined_v2 = []
    for y in message_refined:
        message_refined_v2.append(":" + y)

    # print(message_refined_v2)

    message_traduit = []
    for z in range(len(message_refined)):
        decrypte = UwU.get(message_refined_v2[z])
        message_traduit.append(decrypte)

    final = ""
    for s in message_traduit:
        final = final + str(s)
    # print(message_traduit)
    # print("".join(message_traduit))
    with open("texte_decrypte.txt", "w") as l:
        l.write(final)
    return "done"

print(decrypter())