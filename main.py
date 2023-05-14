from src.modules import encripto
from src.modules import decripto

entry_crip = input("Digite o texto a ser criptografado: ")

encripto.crip(entry_crip)

selectTf = input("Deseja descriptografar y/n: ")

try:
        if selectTf  == "y":
                entry_decr = input("Digite o texto a ser descriptografado: ")
                decripto.decrip(entry_decr)
        elif selectTf == "n":
                print("__Encerrado__") 
        else:
                print("__Escolha_Inválida__")
except:
        print("Erro (01): selectTf não cumpre os pré-requisitos")
