def main():
    Tamanho = int(input("coloque o tamanho do bloco: "))
    bloco(Tamanho)

def bloco(tamanho):
    bloco = ("[]" * tamanho)
    print(f"{bloco}\n" * tamanho, end = '')

main()