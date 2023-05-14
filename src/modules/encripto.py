import main 

def crip(entry_crip): # função criptografar
    
    print("Entrou")
    
    line_text = entry_crip # linha do texto a ser criptografado

    encript = ''

    for i in line_text:
        encript = entry_crip + chr (ord(i)+5)

    str(line_text("")) # limpa a caixa que recebe o texto a ser criptografado
    str(line_text(encript)) # mostra o texto encriptado na caixa 2
   
#entry_crip = ""

