alunos = {
    
}

def menu():
    print("\t\t****  Menu  ****\n")
    print("\t0. Sair")
    print("\t1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)")
    print("\t2. Inserir aluno e nota")
    print("\t3. Alterar a nota de un aluno")
    print("\t4. Consultar nota de un aluno específico")
    print("\t5. Apagar um aluno da lista")
    print("\t6. Dar a média da turma\n")
    opcoes= int(input("\tEscola uma das opcões acima?\n"))
    return opcoes
op = menu()

def exibirLista():
    print("*** Lista de Alunos Com suas notas!!! ***\n")
    for nome in alunos.keys():
        print("Aluno:",nome,"------------ nota:", alunos[nome])

def inserir():
    print("*** Inserir Aluno e Nota !! ***\n")
    nome= input("Digite nome do aluno?\n")
    nota= float(input("Digite á nota?\n"))
    if alunos.get(nome) ==None:
        alunos[nome] = nota
        print("Auno adicionado com sucesso!")
    else:
        print(" Aluno já exixte!")

def alterar():
     print("*** Alterar nota do aluno !! ***\n")
     nome= input("Digite nome do aluno?\n")
     nota= float(input("Digite á nota?\n"))
     if nome in alunos.keys():
         alunos[nome] = nota
         print("Dados alterados, com sucesso!")
     else:
         print("Esse aluno não existe")

def consultanota():
    print("*** Consulta nota do aluno !! ***\n")
    nome= input("Digite nome do aluno?\n")
    if alunos.get(nome)==None:
        print("Esse aluno, não costa na lista!")
    else:
        print(nome," tirou nota: ", alunos[nome])

def apagarAluno():
    print("*** Excluir aluno da lista !! ***\n")
    nome= input("Digite nome do aluno ?\n")
    if alunos.get(nome)==None:
        print("Esse aluno, não costa na lista!")
    else:
        alunos.pop(nome)
        print("Aluno excluido com sucesso.")
        
def media():
    cout = 0
    reslt = 0
    for media in alunos.values():
        cout += media
        reslt+= 1
    media=cout/reslt
    print("A média da turma é :",round(media,2))  

sair = 1

while sair == True:
    if op == 0:
       sair = 0
    elif op == 1:
        exibirLista()
        op=menu()
               
    elif op == 2:
        inserir()
        op=menu()
    elif op == 3:
        alterar()
        op=menu()
    elif op == 4:
        consultanota()
        op=menu()
    elif op == 5:
        apagarAluno()
        break
    elif op == 6:
        media()
        op=menu()
    else:
        print("Opção digitada está incorreta!\n")
       
