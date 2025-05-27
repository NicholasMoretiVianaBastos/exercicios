
import json
import os 

data = "cadastrar_veiculos.json"

def carregar_dados():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]
    
def obter_dados_veiculos():
    marca_veiculo  = input("Digite a Marca do veiculo: ")
    modelo_veiculo = input("Digite o Modelo do veiculo: ")
    ano_fabricacao = int(input("Digite o Ano de Fabricação: "))
    cor_veiculo = input("Digite a Cor do veiculo: ")

    carro = {
        "marca_carro" : marca_veiculo,
        "modelo_veiculo" : modelo_veiculo,
        "ano_fabricacao" : ano_fabricacao,
        "cor_veiculo" : cor_veiculo
}
    return(carro)


def cadastrar_veiculos(dados_veiculo):
    carros = carregar_dados()
    carros.append(dados_veiculo)

    with open(data, "w", encoding="utf-8") as arq_json:
        json.dump(carros, arq_json, indent=4, ensure_ascii=False)

def mostrar_veiculos(dados_veiculo):
    if dados_veiculo:
       for carro in dados_veiculo:
            print("="*80)
            print(f"""
              Marca do carro: {carro["marca_carro"]}
              Modelo do veiculo: {carro["modelo_veiculo"]}
              Ano da fabricação: {carro["ano_fabricacao"]}
              Cor do veiculo: {carro["cor_veiculo"]}              
              """)
    else: 
        print("="*80)
        print("Não existe nenhum carro cadastrado!")

def iniciar_sistema():
    carros = carregar_dados()

    while True:

        print(" ")
        print("="*80)
        print("Opição 1 - Mostrar lista de carros.")
        print("Opição 2 - Cadastrar carros.")
        print("Opição 3 - Sair do Sistema.")
        print("="*80)

        opcao = input("Escolha uma opição do Menu: ")

        if opcao == "1":
            mostrar_veiculos(carros)
        elif opcao == "2":
            cadastrar_veiculos(obter_dados_veiculos())
        elif opcao == "3":
            print("Sistema Finalizado!")
            break
        else: 
            print("Opção invalida!")
iniciar_sistema()