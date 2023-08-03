import math
import random
import time
from Resultado import Resultado
from Tabu import Tabu
from utils import buscar_tarefa, calcula_makespan

def remover_tabus_expirados(lista_tabu):
    lista_tabu = [tabu for tabu in lista_tabu if tabu.cont < tabu.interacoes_saida]
    return lista_tabu

def busca_tabu(listaMaquinas, max_iteracoes, p):
    lista_tabu = []
    iteracoes = 0
    iteracoesSemMelhora = 1
    while iteracoesSemMelhora < max_iteracoes:
        for tabu in lista_tabu:
            tabu.incrementar_contador()

        lista_tabu = remover_tabus_expirados(lista_tabu)
        maiorMakespan = buscar_tarefa(listaMaquinas)
        tarefa = None

        if listaMaquinas[maiorMakespan[1]]["tarefas"]:
            tarefa = listaMaquinas[maiorMakespan[1]]["tarefas"][-1]
            #listaMaquinas[maiorMakespan[1]]["makespan"] -= tarefa


        if tarefa is None:
            # Se não encontrou tarefa não vazia, pular a iteração atual
            iteracoesSemMelhora += 1
            continue

        for i, maquina in enumerate(listaMaquinas):
            if (i != maiorMakespan[1]): ### Verifica se é a mesma máquina de origem
                if (any(tabu.maquina == i for tabu in lista_tabu) == False): ### Verifica se está presente na lista de tabu
                    if (maquina["makespan"] + tarefa < maiorMakespan[0] - tarefa): ### Verifica se há melhora
                        lista_tabu.append( Tabu(i, p) )
                        maquina["tarefas"].append(tarefa)
                        maquina["makespan"] += tarefa
                        iteracoesSemMelhora = 0
                        #if( len ( listaMaquinas[maiorMakespan[1]]["tarefas"] ) == 0 ):
                            #print("Antes do error:", listaMaquinas )
                        listaMaquinas[maiorMakespan[1]]["tarefas"].pop()
                        listaMaquinas[maiorMakespan[1]]["makespan"] -= tarefa
                        break

                    iteracoesSemMelhora += 1

        iteracoes += 1

    return listaMaquinas, iteracoes

def executarTabu():
    resultados = []
    m = 0
    r = 0
    p = 0
    cont = 0
    max_iteracoes = 1000  # Defina o número máximo de iterações aqui

    for i in range(3):
        if i == 1:
            m = 10
        elif i == 2:
            m = 20
        else:
            m = 50

        for j in range(2):
            if j == 1:
                r = 1.5
            else:
                r = 2

            for k in range(9):
                c = (k + 1) / 100

                for _ in range(10):
                    n = math.ceil(math.pow(m, r))
                    p = math.ceil(n * c)
                    listaMaquinas = [{'tarefas': [], 'makespan': 0} for _ in range(m)]
                    listaTarefas = [random.randint(1, 100) for _ in range(n)]
                    listaMaquinas[0]['tarefas'] = listaTarefas
                    calcula_makespan(listaMaquinas)
                    inicio = time.time()
                    listaMaquinas, iteracoes = busca_tabu(listaMaquinas, max_iteracoes, p)
                    fim = time.time()
                    tempoExecucao = (fim - inicio) * 1000  # Convertendo para milissegundos
                    valor = buscar_tarefa(listaMaquinas)[0]
                    resultado = Resultado("Busca Tabu", n, m, _, tempoExecucao, iteracoes, valor, c)
                    resultados.append(resultado)
                    cont = cont + 1

    for resultado in resultados:
        print("Heurística:", resultado.heuristica)
        print("Tarefas:", resultado.tarefas)
        print("Maquinas:", resultado.maquinas)
        print("Replicacao:", resultado.replicacao)
        print("Tempo (ms):", resultado.tempo)
        print("Iterações:", resultado.iteracoes)
        print("Valor:", resultado.valor)
        print("Parâmetro (p):", resultado.parametro)
        print()

    print("Contador: ", cont)
