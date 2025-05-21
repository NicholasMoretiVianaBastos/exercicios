import json
import os

data = "Cadastro_de_filmes.json"

def carregar_dados():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]
    
def obter_dados_filmes():
    nome_filme = input("Informe o nome do filme: ")
    classificacao_filme = int(input("Informe a classificação: "))
    lancamento_filme = int(input("Digite a data de lançamento do filme: "))
    tempo_filme = int(input("Digite a duração do filme: "))
    generos_filme = input("Digite os generos do filme: ")

    filme = {
        "nome_filme" : nome_filme,
        "classificacao_filme" : classificacao_filme,
        "lancamento_filme" : lancamento_filme,
        "tempo_filme" : tempo_filme,
        "generos_filme" : generos_filme
    }
    

    return filme

def cadastrar_filmes(dados_filme):
    filme = carregar_dados()
    filme.append(dados_filme)

    with open(data, "w", encoding="utf-8") as arq_json:
        json.dump(filme, arq_json, indent=4, ensure_ascii=False)

def mostrar_dados_filmes():
    for filme in obter_dados_filmes:
        print(f"""
              Nome do filme: {filme["nome do filme"]}
              Classificação do filme: {filme["classificação do filme"]}
              Data de lançamento: {filme["data de lançamento do filme"]}
              Duração do filme: {filme["duração do filme"]}
              Generos do filme: {filme["generos do filme"]}
              """)
        
def iniciar_sistema():
    filme = 