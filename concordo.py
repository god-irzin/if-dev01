def main():
    resposta = input("você concorda?").lower()
    concordo(resposta)

def concordo(resposta):
    if resposta == "sim" or resposta == "s" or  resposta == "SIM":
        print("concordo")
    elif resposta == "não" or resposta == "n" or resposta == "NÃO":
        print("não concordo")

main()
