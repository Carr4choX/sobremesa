import sys

ROT_MAY = 3
ROT_MIN = 7


def mover(texto):
    salida = []
    for c in texto:
        if "A" <= c <= "Z":
            salida.append(chr((ord(c) - 65 + ROT_MAY) % 26 + 65))
        elif "a" <= c <= "z":
            salida.append(chr((ord(c) - 97 + ROT_MIN) % 26 + 97))
        else:
            salida.append(c)
    return "".join(salida)


def cifrar(frase):
    return mover(frase)[::-1]


if __name__ == "__main__":
    print(cifrar(sys.argv[1]))
