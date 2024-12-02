#função principal
def main():
    num = int(input("digite um número:"))
    verificação(num)

#verifica a paridade
def verificação(num):
    if num % 2 == 0:
        print("\no número é par!")
    else:
        print("\no número é impar!")
main()