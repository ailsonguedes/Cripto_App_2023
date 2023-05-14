
def decrip(entry_decr): # função decriptografar
    
    line_crip = entry_decr # linha do texto a ser decriptografado

    decript = ''

    for i in line_crip:
        decript = decript + chr (ord(i)-5)

    print("") #limpa a caixa
    print("Texto descriptografado: "+decript) # mosta o texto decriptado
    