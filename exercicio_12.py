import os 
import json

data = "agenda_cabeleleiro.json"

def carregar_dados():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
def obter_dados():
    nome_cliente = input("Digite seu nome: ")
    servico = input("Escolha o serviço de sua escolha: ")
    dia = int(input("Escolha um dia para fazer seu serviço: "))
    horario = (input("Digite o horario de sua preferencia: "))
    observacao = input("Digite sua observação (se tiver): ")

    cliente = {
        "nome_cliente" : nome_cliente,
        "servico" : servico,
        "dia" : dia,
        "horario" : horario,
        "observacao" : observacao
}
    return cliente

def cadastrar_agendamento(dados_cliente):
    cliente = carregar_dados()
    cliente.append(dados_cliente)
    
    with open(data, "w", encoding="utf-8") as arq_json:
        json.dump(data, arq_json, indent=4, ensure_ascii=False)


def mostrar_agendamento(dados_cliente):
    if dados_cliente:
        for cliente in dados_cliente: 
            print("="*80)
            print(f"""
                  Nome do cliente: {cliente["nome_cliente"]}
                  Escolha de serviço: {cliente["servico"]}
                  Escolha um dia: {cliente["dia"]}
                  Escolha um horario: {cliente["horario"]}
                  Observação: {cliente["observacao"]}
                  """)
        else:
            print("="*80)
            print("Nenhum cliente cadastrado!")


def iniciar_sistema():
    cliente = carregar_dados()

    while True:
        
        print(" ")
        print("="*80)
        print("Opição 1 - Mostrar agendamentos")
        print("Opição 2 - Cadastrar novo cliente")
        print("Opição 1 - Sair do sistema.")
        print("="*80)

        opcao = input("Digite uma opição do Menu: ")

        if opcao == "1":
            mostrar_agendamento(cliente)
        elif opcao == "2":
            cadastrar_agendamento(obter_dados())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Opção invalida, escolha outra opção.")
iniciar_sistema()