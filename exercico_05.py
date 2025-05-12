from exercico_04 import somar_numeros

def cadastrar(nome, email, Serie, nota01=0, nota02=0, nota03=0):
    lista = []
    
    notas = [nota01, nota02, nota03]

    dicionario = {
        "nome" : nome, 
        "email" : email,
        "serie" : Serie, 
        "notas" : notas, 
        "media" : somar_numeros(notas)
        }
    lista.append(dicionario)
    media = somar_numeros(dicionario["nota"])
    return dicionario

print (cadastrar(
        "Nicholas", 
        "nicholasmoreti65@gmail.com", 
        "2TB",
        
    ))