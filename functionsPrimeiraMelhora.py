import math
import random
import time
from Resultado import Resultado
from utils import buscar_tarefa, calcula_makespan

def verificaMelhora(listaMaquinas):
    value, index = buscar_tarefa(listaMaquinas)

    ### Itera sobre todas as máquinas e verifica se o makespan da máquina fica menor que o makespan da pior máquina.
    for maquina in listaMaquinas:
        if ( maquina["makespan"] + listaMaquinas[index]["tarefas"][-1] < listaMaquinas[index]["makespan"] ):
            return True

    ### Se nenhuma máquina fica melhor que a máquina com maior makespan, retorna falso e finaliza.
    return False

def primeiraMelhora(tarefa, listaMaquinas):
    ### Pega a última tarefa da máquina e armazena o tamanho da tarefa em ultima_tarefa
    ultima_tarefa = listaMaquinas[tarefa[1]]["tarefas"].pop()

    ### Remove o tempo da tarefa da máquina escolhida
    listaMaquinas[tarefa[1]]["makespan"] -= ultima_tarefa

    for i, maquina in enumerate(listaMaquinas):
        if (i != tarefa[1]):
            if (maquina['makespan'] + ultima_tarefa < listaMaquinas[tarefa[1]]['makespan']):
                maquina['makespan'] += ultima_tarefa
                maquina['tarefas'].append(ultima_tarefa)
                return

def PrimeiraMelhora(listaMaquinas):
    interacoes = 0
    ### Loop de verificação se é possível realizar a melhora
    while( verificaMelhora(listaMaquinas) ):
        ### Primeira melhora
        primeiraMelhora(buscar_tarefa(listaMaquinas), listaMaquinas)
        interacoes = interacoes + 1

    return interacoes

def executaPrimeiraMelhora():
    resultados = []
    m = 0
    r = 0
    cont = 0
    ### Define o número de máquinas
    for i in range(3):
        if i == 1:
            m = 10
        elif i == 2:
            m = 20
        else:
            m = 50

        ### define valor de r
        for j in range(2):
            if j == 1:
                r = 1.5
            else:
                r = 2

            #Executa 10 instancias
            for i in range(10):
                interacoes = 0
                n = math.ceil(math.pow(m, r))
                listaMaquinas = [{'tarefas': [], 'makespan': 0} for _ in range(m)] ### Inicialização das máquinas
                listaTarefas = [random.randint(1, 100) for _ in range(n)] ### Criação das tarefas
                listaMaquinas[0]['tarefas'] = listaTarefas ### Definindo as tarefas da primeira máquina
                calcula_makespan(listaMaquinas) ### Calculando o makespan das máquinas
                inicio = time.time() ### Inicia contador
                interacoes = PrimeiraMelhora(listaMaquinas) ### Primeira Melhora
                fim = time.time() ### Finaliza contador
                tempoExecucao = (fim - inicio) * 1000
                valor = buscar_tarefa(listaMaquinas)[0]
                resultado = Resultado("Primeira Melhora", n, m, i, tempoExecucao, interacoes, valor, "NA")
                resultados.append(resultado)
                cont = cont + 1

    for resultado in resultados:
        print("Heurística:", resultado.heuristica)
        print("Tarefas:", resultado.tarefas)
        print("Maquinas:", resultado.maquinas)
        print("Replicacao:", resultado.replicacao)
        print("Tempo(ms):", resultado.tempo)
        print("Iterações:", resultado.iteracoes)
        print("Valor:", resultado.valor)
        print("Parâmetro:", resultado.parametro)
        print()

    print('Contador : ', cont)