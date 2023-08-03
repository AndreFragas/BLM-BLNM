def calcula_makespan(listaMaquinas):
    for maquina in listaMaquinas:
        total_tarefas = sum(maquina['tarefas'])
        maquina['makespan'] = total_tarefas

def buscar_tarefa(listaMaquinas):
    max_value = -1
    max_index = 0

    ### Pega o indice e o makespan da máquina com maior makespan
    for i, maquina in enumerate(listaMaquinas):
        if ( maquina["makespan"] > max_value ):
            max_index = i
            max_value = maquina["makespan"]

    return max_value, max_index