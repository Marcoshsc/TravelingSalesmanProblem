
# Algoritmos para o Problema do Caixeiro Viajante

O artigo ao qual este repositório se refere pode ser encontrado [neste repositório](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/article.pdf).

- Autores: [Marcos Henrique](https://github.com/Marcoshsc) e [Natália Pereira](https://github.com/naalmeida98)
- Linguagem de Programação: Python

# Sumário

 1. [Descrição](#descrição)
 2. [Observações](#observações)
 3. [Utilização e Funcionamento](#utilização-e-funcionamento)
 4. [Contribuições](#contribuições)

## Descrição

O Problema do Caixeiro Viajante (PCV) é um problema extremamente popular na Teoria dos Grafos, visto que suas aplicações são inúmeras e sua solução de forma eficiente pode trazer grandes avanços à sociedade como um todo. Neste repositório, são apresentados dois algoritmos que solucionam o PCV, um que utliziza uma abordagem de força bruta, garantindo encontrar a melhor solução, porém com uma complexidade computacional de O(n!), e outro, o Algoritmo do Vizinho mais Próximo, que consiste de uma abordagem heurística que encontra uma solução para o PCV com um custo computacional de O(n²), porém quase nunca encontra a melhor solução. 

Além disso, é possibilitado ao usuário utilizar ferramentas de CLI (*Command-Line Interface*) que façam testes de tempo de execução entre os algoritmos, em grafos gerados aleatóriamente, de acordo com os parâmetros passados de forma elegante, via JSON.

Ademais, existe uma CLI poderosa que pode ser utilizada pelo usuário,  para fazer seus próprios testes em grafos, com parâmetros completamente personalizados, de acordo com suas preferências, passados também sem contato algum com o código, utilizando arquivos JSON. Caso o usuário não prefira utilizar o recurso de arquivos JSON, uma interface via terminal pode ser utilizada para a passagem de parâmetros. Ao final da passagem de parâmetros, o usuário poderá visualizar a solução apresentada pelo algoritmo escolhido e seu custo, bem como o tempo de execução do algoritmo escolhido.

## Observações

Todos os tutoriais de exemplo contidos neste manual, utilizarão como executável do python 3.8 a sigla **python3**, por exemplo:

	python3 main.py

Eventualmente, suas variáveis de ambiente podem estar configuradas de forma diferente. Por exemplo, muitos computadores, especialmente aqueles que têm sistema operacional Windows, utilizam **python** como executável do python 3.8. Dessa forma, executar o programa acima seria:

	python main.py

Além disso, os arquivos presentes na pasta resources deste repositório são arquivos de exemplo, com o intuito de mostrar ao usuário a estrutura utilizada.  Ou seja, todos eles podem ser substituídos com valores a escolha do usuário, da forma que será explicada a seguir.

## Utilização e Funcionamento

O usuário pode executar duas funções diferentes com este software: [comparação entre tempos de execução](#tempos-de-execução) e [busca por melhor caminho](#busca-por-melhor-caminho). Ambas as formas serão detalhadamente explicadas abaixo:

### Tempos de Execução

Esta funcionalidade compara os tempos de execução entre os dois algoritmos, para determinadas configurações de grafos, inseridas pelo usuário.

Para fazer a comparação de dados, o usuário deve primeiramente inserir os dados necessários para a execução, que são as configurações de grafos que serão testadas. Existem duas maneiras de fazer isto. Uma delas é através do arquivo **dataToCompare.json**, localizado dentro da pasta **resources**. Os dados devem ser inseridos no seguinte formato:

    [
	    {
			"vertex": inteiro | número de vértices do grafo,
			"min": float | menor peso para as arestas do grafo,
			"max": float | maior peso para as arestas do grafo
		},
		.
		.
		.
	]

Como mostrado acima, deve ser inserida uma lista de objetos JSON no formato especificado. Um exemplo deste arquivo pode ser encontrado [neste repositório](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/resources/dataToCompare.json).

Em seguida, basta executar o software utilizando a flag --predef:

	python3 comparison.py --predef

Caso o usuário prefira inserir os dados via terminal, basta que não utilize a flag --predef, e os dados serão requisitados via terminal.

Ao final da execução, será gerado um arquivo JSON chamado **results.json**, localizado na pasta **resources**, que segue a seguinte estrutura:

	{
		"VERTICES#PESOMINIMO#PESOMAXIMO": {
			"BruteForce": float | tempo de execução do algoritmo de força bruta,
			"NearestNeighbour": float | tempo de execução do algoritmo do Vizinho mais Próximo
		}
	}

Como observa-se acima, os parâmetros inseridos são os identificadores de cada um dos resultados gerados, portanto não se deve inserir um conjunto de parâmetros igual a outro já inserido. Um exemplo de resultados pode ser encontrado [aqui](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/resources/results.json).

Exemplos de Uso:

- [Comparação com flag](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/execution-examples/comparison-with-predef.png)
- [Comparação sem flag](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/execution-examples/comparison-without-predef.png)

### Busca por melhor caminho

Esta funcionalidade permite ao usuário interagir com diversos tipos de grafos, aleatórios ou não, encontrando as soluções para o PCV no grafo em questão, utilizando o algoritmo de sua escolha.

Existem três *flags* que podem ser utilizadas neste programa:

	-p, --predef       Utilizar configurações pré-definidas na pasta resources
	-s, --save         Salvar o grafo gerado
	-ng, --nogenerate  Utilizar grafo provido pelo usuário

A primeira flag pode ser utilizada caso o usuário queira utilizar a configuração que colocou em um arquivo chamado **predef.json**, localizado na pasta resources. Sua estrutura é da seguinte maneira:
	
	{
		"vertexes": int | número de vértices do grafo que será gerado,
		"minWeight": float | peso mínimo das arestas do grafo que será gerado,
		"maxWeight": float | peso máximo das arestas do grafo que será gerado,
		"algorithm": string | algoritmo a ser utilizado
	}

Vale dizer que o campo "algorithm" só pode ter estes valores: [ bruteforce, nearestneighbour ].  Um exemplo desta configuração pode ser encontrado [neste repositório](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/resources/predef.json)

Já a segunda flag pode ser utilizada quando o usuário desejar que o grafo que for gerado aleatóriamente seja salvo para posteriores análises. Este grafo é salvo em um arquivo chamado **generatedGraph.json**, localizado na pasta resources, e é salvo na forma de representação de **matriz de distâncias**. Esta flag só funciona caso o usuário também tenha utilizado a primeira flag. Caso contrário, será perguntado ao usuário se quer salvar a matriz, de qualquer maneira.

A terceira flag, pode ser utilizada caso o usuário não queira que o grafo seja gerado aleatóriamente, ou seja, sendo capaz de prover seu próprio grafo. Este grafo deve ser inserido na forma de **matriz de distâncias**, no arquivo **predefGraph.json**, localizado na pasta resources. Um exemplo de grafo pode ser encontrado [neste repositório](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/resources/predefGraph.json).

A não utilização de arquivos JSON para configuração, simplesmente fará com que o usuário tenha que digitar estas informações via terminal.

Ao final da execução, será mostrado ao usuário a solução para o PCV, seu custo e seu tempo de execução. Caso a segunda flag esteja ativada, o grafo utilizado para os testes será inserido no arquivo **generatedGraph.json**, localizado na pasta resources.

Exemplos de uso:

- [Sem usar configuração em JSON](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/execution-examples/tsp-without-predef.png)
- [Sem usar configuração em JSON, sem usar grafo aleatório](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/execution-examples/tsp-without-predef-custom-matrix.png)
- [Sem usar configuração em JSON, salvando grafo gerado](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/execution-examples/tsp-without-predef-save-matrix.png)
- [Usando configuração em JSON](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/execution-examples/tsp-with-predef.png)
- [Usando configuração em JSON, sem usar grafo aleatório](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/execution-examples/tsp-with-predef-custom-matrix.png)
- [Usando configuração em JSON, salvando grafo gerado](https://github.com/Marcoshsc/TravelingSalesmanProblem/blob/main/execution-examples/tsp-with-predef-save-matrix.png)

## Contribuições

Este repositório é aberto a todo tipo de contribuição. Caso você esteja interessado em contribuir com o projeto, crie uma branch nova a partir da branch **master** deste repositório, faça suas mudanças e então abra um **pull request** para que suas mudanças sejam avaliadas e eventualmente aprovadas.

