
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
    tipo = input("Digite o tipo do veiculo: ")

    carro = {
        "marca_veiculo" : marca_veiculo,
        "modelo_veiculo" : modelo_veiculo,
        "ano_fabricacao" : ano_fabricacao,
        "cor_veiculo" : cor_veiculo,
        "tipo": tipo
}
    return carro

# def obter_dados_moto():
#     marca_moto = input("Digite a Marca da moto: ")
#     modelo_moto = input("Digite o Modelo da moto: ")
#     ano_fabricacao_moto = int(input("Digite o Ano de Fabricação: "))
#     cor_moto = input("Digite a Cor do veiculo: ")

#     moto = {
#        "marca_moto" : marca_moto,
#         "modelo_moto" : modelo_moto,
#         "ano_fabricacao_moto" : ano_fabricacao_moto,
#         "cor_moto" : cor_moto
# }
#     return moto    

# def cadastrar_moto(dados_veiculo):
#     carros = carregar_dados()
#     carros.append(dados_veiculo)

#     with open(data, "w", encoding="utf-8") as arq_json:
#         json.dump(carros, arq_json, indent=4, ensure_ascii=False)

def cadastrar_veiculos(dados_veiculo):
    motos = carregar_dados()
    motos.append(dados_veiculo)

    with open(data, "w", encoding="utf-8") as arq_json:
        json.dump(motos, arq_json, indent=4, ensure_ascii=False)

def mostrar_veiculos(dados_veiculo):
    if dados_veiculo:
       for carro in dados_veiculo:
            if carro["tipo"].lower() == "carro":
                print("="*80)
                print(f"""
                Marca do carro: {carro["marca_veiculo"]}
                Modelo do veiculo: {carro["modelo_veiculo"]}
                Ano da fabricação: {carro["ano_fabricacao"]}
                Cor do veiculo: {carro["cor_veiculo"]}             
                Tipo do veiculo: {carro["tipo"]}             
                """)
            # else:
            #     print("não entrado veiculos com o tipo carro")
    else: 
        print("="*80)
        print("Não existe nenhum carro cadastrado!")


def mostrar_moto(dados_veiculo):
    if dados_veiculo:
       for moto in dados_veiculo:
            if moto["tipo"].lower() == "moto":
                print("="*80)
                print(f"""
                Marca do moto: {moto["marca_veiculo"]}
                Modelo do veiculo: {moto["modelo_veiculo"]}
                Ano da fabricação: {moto["ano_fabricacao"]}
                Cor do veiculo: {moto["cor_veiculo"]}              
                Tipo do veiculo: {moto["tipo"]}             
                """)
            # else:
            #     print("não entrado veiculos com o tipo carro")
    else: 
        print("="*80)
        print("Não existe nenhuma moto cadastrado!")

def iniciar_sistema():
    veiculo = carregar_dados()

    while True:

        print(" ")
        print("="*80)
        print("Opição 1 - Mostrar lista de carros.")
        print("Opição 2 - Mostrar lista de carros.")
        print("Opição 3 - Cadastrar carros.")
        print("Opição 4 - Sair do Sistema.")
        print("="*80)

        opcao = input("Escolha uma opição do Menu: ")

        if opcao == "1":
            mostrar_veiculos(veiculo)
        elif opcao == "2":
            mostrar_moto(veiculo)    
        elif opcao == "3":
            cadastrar_veiculos(obter_dados_veiculos())      
        elif opcao == "4":
            print("Sistema Finalizado!")
            break
        else: 
            print("Opção invalida!")
iniciar_sistema()