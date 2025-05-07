def cadastrar_filmes(nome,
    descricao, 
    classificacao, 
    categoria01, 
    categoria02, 
    categoria03 ):
    lista = []
    discionario = {
        "nome" : nome, 
        "descricao" : descricao,
        "classificacao" : classificacao,
        "categorias" : [categoria01, categoria02, categoria03]
    }
    lista.append(discionario)
    return discionario

print(cadastrar_filmes("Pequeno principe", 
    "é uma história sobre um piloto que encontra um menino de outro planeta no deserto do Saara. O príncipe, que vem do asteroide B-612, viaja pelo universo, aprendendo sobre a vida e os seres humanos, e encontra o piloto, com quem compartilha suas experiências e lições.", 
    "Livre", 
    "Literatura infantil e juvenil. ", 
    "Ficção",
    "Conto"
    ))