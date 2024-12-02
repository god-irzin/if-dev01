nome = "Krystrian grey"
def main():
    nome = input("qual seu nome?")
    diga_olá(nome)


def diga_olá(para="Mundo"):
    print(f"Olá, {para}!")

main()