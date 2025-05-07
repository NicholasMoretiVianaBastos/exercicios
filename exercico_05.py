from exercico_04 import somar_numeros

def cadastrar(nome, email, Serie, nota01, nota02, nota03):
    lista = []
    dicionario = {
        "nome" : nome, 
        "email" : email,
        "serie" : Serie, 
        "notas" : [nota01, nota02, nota03]
        }
    lista.append(dicionario)
    media = somar_numeros(dicionario["nota"])
    return dicionario

print (cadastrar(
        "Nicholas", 
        "nicholasmoreti65@gmail.com", 
        "2TB",
        10,
        6,
        9
    ))