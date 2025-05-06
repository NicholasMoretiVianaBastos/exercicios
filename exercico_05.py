def cadastrar(nome, email, Serie):
    lista = []
    dicionario = {
        "nome" : nome, 
        "email" : email,
        "serie" : Serie 
        }
    lista.append(dicionario)
    return dicionario

print(cadastrar("Nicholas", "nicholasmoreti65@gmail.com", "2TB"))
