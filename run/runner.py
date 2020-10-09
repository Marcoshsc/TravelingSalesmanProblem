import json
from typing import List
from common.randomic import getRandomGraph
from common.executionTime import getExecutionTime
from abs.algorithmFactory import AlgorithmFactory
from abs.enumerator import EnumAlgorithms

def getAndSaveGraph(saveGraph: bool, vertexes: int, minWeight: float, maxWeight: float) -> List[List[float]]:
    graph = getRandomGraph(vertexes, minWeight, maxWeight)
    if saveGraph:
        print('Salvando grafo...')
        with open('resources/generatedGraph.json', 'w+') as graphF:
            json.dump(graph, graphF)
    return graph


def runAlgorithms(generateGraph: bool, predef: bool, saveGraph: bool) -> None:

    print('Executando Traveling Salesman Problem CLI 1.0')
    data: dict
    if predef:
        with open('resources/predef.json', 'r') as dataF:
            data = json.loads(dataF.read())

    graph: List[List[float]]
    if generateGraph:
        if predef:
            print('Gerando grafo aleatório com configurações pré-definidas...')
            graph = getAndSaveGraph(saveGraph, data['vertexes'], data['minWeight'], data['maxWeight'])
        else:
            print('Você escolheu entrar com os dados do grafo a ser gerado via terminal. Entre com os dados a seguir:')
            vertexes = int(input('Digite a quantidade de vértices do grafo: '))
            minWeight = float(input('Digite o peso mínimo de uma aresta no grafo: '))
            maxWeight = float(input('Digite o peso máximo de uma aresta no grafo: '))
            answer = str(input('Deseja salvar o grafo gerado? S/N: '))
            willSave = answer.upper() == 'S'
            print('Gerando o grafo com a configuração inserida...')
            graph = getAndSaveGraph(willSave, vertexes, minWeight, maxWeight)

    else:
        with open('resources/predefGraph.json', 'r') as graphFile:
            graph = json.loads(graphFile.read())
    
    algorithmName = str
    if predef:
        print('Você escolheu usar as configurações predefinidas em predef.json!')
        algorithmName = data['algorithm']
    else:
        print('Você escolheu ler os dados. Insira os dados a seguir...')
        print('\nVocê pode escolher entre dois algoritmos: NearestNeighbour e BruteForce.')
        algorithmName = str(input('Digite o nome do algoritmo a ser executado: '))
        
    print(f'Executando algoritmo {algorithmName.upper()}...')
    factory = AlgorithmFactory()
    algorithmEnum = EnumAlgorithms.FromString(algorithmName)
    algorithm = factory.getAlgorithm(algorithmEnum)

    result = algorithm.execute(graph)
    print(f'Solução encontrada (Sequência de vértices): {result.path}')
    print(f'Custo: {result.cost}')
    print(f'Tempo de execução: {result.executionTime}')


def compare(predef: bool) -> None:
    data = []

    if predef:
        print('Você optou por utilizar os dados definidos no JSON.')
        with open('resources/dataToCompare.json', 'r') as dataFile:
            data = json.loads(dataFile.read())
    else:
        print('Você optou por inserir os dados via terminal.')
        i = 1
        while True:
            v = int(input(f'Digite o número de vértices do {i} registro: '))
            mi = float(input(f'Digite o peso mínimo do {i} registro: '))
            ma = float(input(f'Digite o peso máximo do {i} registro: '))
            ans = str(input('Deseja inserir outro registro? S/N: '))
            i += 1
            data.append({
                'vertex': v,
                'min': mi,
                'max': ma
            })
            if ans.upper() == 'N':
                break

    print(f'Total de {len(data)} registros...')
    results = {}

    for d in data:
        vertexes = d['vertex']
        minimum = d['min']
        maximum = d['max']
        print(f'Rodando para {vertexes} vértices, {minimum} peso mínimo e {maximum} peso máximo...')
        times = getExecutionTime(d)
        key = (f'{vertexes}#{minimum}#{maximum}')
        results[key] = {
            'BruteForce': str(times[0]) if times[0] == float('inf') else times[0],
            'NearestNeighbour': str(times[1]) if times[1] == float('inf') else times[1]
        }

    with open('resources/results.json', 'w+') as resultsFile:
        json.dump(results, resultsFile)