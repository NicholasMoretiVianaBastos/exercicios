def cadastrar(nome, email, Serie, nota01, nota02, nota03):
    lista = []
    dicionario = {
        "nome" : nome, 
        "email" : email,
        "serie" : Serie, 
        "notas" : [nota01, nota02, nota03]
        }
    lista.append(dicionario)
    return dicionario

print (cadastrar(
        "Nicholas", 
        "nicholasmoreti65@gmail.com", 
        "2TB",
        10,
        6,
        9
    ))