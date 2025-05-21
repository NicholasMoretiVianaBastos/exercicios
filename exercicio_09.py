import json
import os

data = "funcionarios.json" 

def carregar_dados():
    if os.path.exists(data): 
        with open(data, "r", encoding= "utf-8") as arq_jason:
            return json.load(arq_jason)
    else: 
        return[]
    
funcionarios = carregar_dados()

for funcionario in funcionarios:
    if funcionario["salario"] > 5500:
        print(f"="* 50)
        print(f"Nome do funcionario: {funcionario["nome"]}, ")
        print(f"Salario do funcionario: {funcionario["salario"]}")
    else:
        print(f"="*50)
        print(f"O(A) funicionario(a): {funcionario["nome"]} nâo recebe mais que 5500!")