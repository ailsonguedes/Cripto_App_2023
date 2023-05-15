
def decrip(field_decript): # função decriptografar
    
    print("entrou")
    
    line_text = field_decript.get() # linha do texto a ser criptografado

    encript = ''

    for i in line_text:
        encript = encript + chr(ord(i)-5)
        
    line_text_cls = "" # limpa a caixa que recebe o texto a ser criptografado
    line_text = encript # mostra o texto encriptado na caixa 2
    
    print(line_text)
  