from exercico_04 import somar_numeros
   
lista = []

def obter_dados_aluno():
    nome_aluno = input("Informe o nome completo do aluno: ")
    email_aluno = input("Informe o email do aluno: ")
    serie_aluno = input("Informe a serie do aluno: ")
    nota01_aluno = int(input("Informe a primeira nota do aluno: "))
    nota02_aluno = int(input("Informe a segunda nota do aluno: "))
    nota03_aluno = int(input("Informe a terceira nota do aluno: "))
   
    return cadastrar(nome_aluno, email_aluno, serie_aluno, nota01_aluno, nota02_aluno, nota03_aluno)

def cadastrar(nome, email, Serie, nota01=0, nota02=0, nota03=0):
    
    notas = [nota01, nota02, nota03]

    dicionario = {
        "nome" : nome, 
        "email" : email,      
        "serie" : Serie, 
        "notas" : notas, 
        "media" : somar_numeros(notas)
        }
    lista.append(dicionario)
    media = somar_numeros(dicionario["notas"])
    return dicionario

obter_dados_aluno()

def mostrar_dados_alunos(dados_alunos):
    for lista in dados_alunos:
        print(f"Nome do aluno: {lista["nome"]}")

    return 

mostrar_dados_alunos(lista)