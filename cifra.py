import base64
import sys

ROT_MAY = 5
ROT_MIN = 11


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


def cifrar(secreto):
    b64 = base64.b64encode(secreto.encode()).decode()
    frase = f"El carracho no tiene mesa en Carballesa: {b64} :]"
    return mover(frase)[::-1]


if __name__ == "__main__":
    print(cifrar(sys.argv[1]))
