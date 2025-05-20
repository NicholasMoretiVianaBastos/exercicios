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
    print(f"="* 50)
    print(f"Nome do funcionario: {funcionario["nome"]}, ")
    print(f"Salario do funcionario: {funcionario["salario"]}")