def crip(entry_crip): # função criptografar
    
    line_text = entry_crip # linha do texto a ser criptografado

    encript = ''

    for i in line_text:
        encript = encript + chr (ord(i)+5)

    print("") # limpa a caixa que recebe o texto a ser criptografado
    print("Texto encriptografado: "+encript) # mostra o texto encriptado na caixa 2
    
#entry_crip = ""

