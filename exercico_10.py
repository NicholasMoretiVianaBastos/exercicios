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
    tempo_filme = input("Digite a duração do filme: ")
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
    filmes = carregar_dados()
    filmes.append(dados_filme)

    with open(data, "w", encoding="utf-8") as arq_json:
        json.dump(filmes, arq_json, indent=4, ensure_ascii=False)

def mostrar_dados_filmes(dados_filmes):
    for filme in dados_filmes:
        print(f"""
              Nome do filme: {filme["nome_filme"]}
              Classificação do filme: {filme["classificacao_filme"]}
              Data de lançamento: {filme["lancamento_filme"]}
              Duração do filme: {filme["tempo_filme"]}
              Generos do filme: {filme["generos_filme"]}
              """)
        
def iniciar_sistema():
    filmes = carregar_dados()
    
    while True:

        print(" ")
        print("="*80)
        print("Opcao 1 - Mostrar Lista de Filmes")
        print("Opcao 2 - Cadastrar Filmes")
        print("Opcao 3 - Sair do Sistema.")
        print("="*80)

        opcao = input("Escolha uma das opções do Menu: ")

        if opcao == "1": 
            mostrar_dados_filmes(filmes)
        elif opcao == "2":
            cadastrar_filmes(obter_dados_filmes())
        elif opcao == "3":
            print("Sistema Finalizado")
            break
        else:
            print("Opção invalida, escolha uma das opções do menu.")
iniciar_sistema()