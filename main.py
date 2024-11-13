def menu():
    """Exibe o menu de opções de operações"""
    print("[1] - Adicionar tarefa")
    print("[2] - Listar tarefas")
    print("[3] - Marcar tarefa como concluída")
    print("[4] - Remover tarefa")
    print("[0] - Sair")

def entrada(lista):
    """Recebe a operação desejada e chama a função de escolha de operação.
    
    Args: 
        lista: Lista de tarefas.
    """
    while True:
        menu()
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 0:
                break
            escolher_opcao(opcao, lista)
        except ValueError:
            print("Digite um número inteiro.") 

def escolher_opcao(opcao, lista):
    """Chama a função correspondente à operação escolhida.
    
    Args:
        opcao: Número da opção escolhida.
        lista: Lista de tarefas.
    """
    match opcao:
        case 1:
            add_tarefa(lista)
            return
        case 2:
            listar_tarefas(lista)
        case 3:
            marcar_concluida(lista)
        case 4:
            remover_tarefa()
        case _:
            print("Opção inválida.")

def add_tarefa(lista):
    """Adiciona uma tarefa à lista.
    
    Args:
        lista: Lista de tarefas.
    """
    tarefa = input("Digite a tarefa: ")
    id = int(input("Digite o id da tarefa: "))
    lista.append([id, tarefa, False])

def listar_tarefas(lista):
    """Exibe a lista de tarefas.
    
    Args:
        lista: Lista de tarefas.
    """
    if (lista):
        for item in lista:
            if(item[2]):
                print(f"{item[0]}: {item[1]} - Concluído")
            else:
                print(f"{item[0]}: {item[1]} - Pendente")
    else:
        print("Não há nenhuma tarefa")

def marcar_concluida(lista):
    """Conclui a tarefa da lista selecionada.
    
    Args:
        lista: Lista de tarefas.
    """
    listar_tarefas(lista)
    tarefa = int(input("Digite a tarefa que deseja marcar como concluída: "))
    for item in lista:
        if item[0] == tarefa:
            item[2] = True

def remover_tarefa():
    """Remove a tarefa da lista selecionada.
    
    Args:
        lista: Lista de tarefas.
    """
    listar_tarefas(lista)
    tarefa = int(input("Digite a tarefa que deseja remover: "))
    for item in lista:
        if item[0] == tarefa:
            lista.remove(item)

lista = []
entrada(lista)