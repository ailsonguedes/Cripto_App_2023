from modules import encripto
from modules import decripto

entry_crip = input("Digite o texto a ser criptografado: ")

encripto.crip(entry_crip)

selectTf = False
selectTf = int(input("Deseja descriptografar: "))


if selectTf  == 1:
        entry_decr = input("Digite o texto a ser descriptografado: ")
        decripto.decrip(entry_decr)
else:
    print("__Encerrado__")
