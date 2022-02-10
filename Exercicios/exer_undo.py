# Fracassei
def adiciona_tarefa():
    lista_aux = []
    tarefa = input(str('Digite uma tarefa: '))
    lista_de_tarefas.append(tarefa)
    lista_aux.append(lista_de_tarefas)
    historico.append(lista_aux)
    

lista_de_tarefas = []
historico = []
for i in range(3):
    adiciona_tarefa()
print(lista_de_tarefas)
print(historico)

