# Sort Visualizer

    Sort Visualizer é um programa Python criado usando a biblioteca Pygame que permite visualizar diversos algoritmos de ordenação em tempo real. Este programa inclui 9 algoritmos de ordenação, são eles: Merge Sort, Quick Sort, Bubble Sort, Insertion Sort, Selection Sort, Heap Sort, Counting Sort, Shell Sort e Cocktail Sort. Além disso, existem algumas funcionalidades adicionais que podem ser usadas para redefinir o estado da ordenação e alternar entre diferentes algoritmos.



# Instalação

Antes de usar o Sort Visualizer, é necessário garantir que as biblioteca Pygame, numba e numpy estejam instaladas em seu computador. Você pode instalar executando o seguinte comando no terminal ou prompt de comando:



```bash
pip install pygame numba numpy
```

---

# Uso

> Para iniciar o programa Sort Visualizer, basta executar o arquivo 'main.py' usando o Python.

O programa inclui as seguintes funcionalidades:

- Algoritmos de ordenação:
  Para alternar entre diferentes algoritmos de ordenação, use as teclas numéricas de 1 a 9. Os algoritmos de ordenação disponíveis são Merge Sort (1), Quick Sort (2), Bubble Sort (3), Insertion Sort (4), Selection Sort (5), Heap Sort (6), Counting Sort (7), Shell Sort (8) e Cocktail Sort (9).

- Resetar:
  Para redefinir o estado da ordenação, pressione a tecla de espaço. Isso gerará um novo conjunto de valores não ordenados e interromperá qualquer processo de ordenação que possa estar em execução.

- Sair:
  Para sair do programa, basta clicar no botão 'x' no canto superior direito da janela.

---

# Algoritmos

- Merge Sort:
  O Merge Sort é um algoritmo de ordenação eficiente baseado na técnica de "dividir e conquistar". Ele divide a lista em sub-listas menores, ordena essas sub-listas recursivamente e, em seguida, combina as sub-listas ordenadas para produzir a lista final ordenada. A complexidade do Merge Sort é O(n log n), tornando-o mais eficiente que muitos outros algoritmos de ordenação.
  
  O Merge Sort foi inventado por John von Neumann em 1945, embora tenha sido publicado pela primeira vez por um de seus alunos, Arthur Burks, em 1948. Von Neumann trabalhava no desenvolvimento de algoritmos para computadores digitais na época, e o Merge Sort foi um dos primeiros algoritmos a serem projetados especificamente para computadores eletrônicos.
  
  Embora o Merge Sort tenha sido inventado em meados do século XX, ele só se tornou popular como algoritmo de ordenação na década de 1970, quando os computadores se tornaram mais rápidos e mais poderosos. Desde então, o Merge Sort tem sido amplamente utilizado em uma variedade de aplicações, incluindo processamento de texto, ordenação de bancos de dados e processamento de imagens. Ele é considerado um dos algoritmos de ordenação mais eficientes e é frequentemente usado como referência para comparar a eficiência de outros algoritmos de ordenação.

- Quick Sort:
  O Quick Sort é um algoritmo de ordenação eficiente baseado na técnica de "dividir e conquistar". Ele escolhe um elemento como "pivô" e divide a lista em dois subconjuntos: um com elementos menores que o pivô e outro com elementos maiores. Em seguida, ordena recursivamente os subconjuntos menores e maiores, combinando-os novamente no final para obter a lista final ordenada. A complexidade do Quick Sort é O(n log n), tornando-o um dos algoritmos de ordenação mais rápidos para grandes conjuntos de dados.
  
  O Quick Sort foi inventado por Tony Hoare em 1960, quando ele trabalhava na Elliott Brothers, uma empresa britânica que fabricava computadores. Hoare inventou o Quick Sort como uma solução mais eficiente para a ordenação de dados em memória do que o algoritmo de ordenação Bubble Sort, que era amplamente utilizado na época.
  
  Desde sua invenção, o Quick Sort se tornou um dos algoritmos de ordenação mais populares e amplamente utilizados. Ele é especialmente adequado para grandes conjuntos de dados e é frequentemente usado em aplicações como bancos de dados, linguagens de programação e processamento de texto. A versatilidade e eficiência do Quick Sort o tornaram um algoritmo fundamental para a ciência da computação.

- Bubble Sort:
  O Bubble Sort é um algoritmo de ordenação simples, mas ineficiente, que percorre a lista várias vezes, comparando pares de elementos adjacentes e trocando-os se eles estiverem na ordem errada. O algoritmo recebe seu nome porque os elementos "flutuam" gradualmente para suas posições finais à medida que as iterações ocorrem. A complexidade do Bubble Sort é O(n^2), tornando-o lento e inadequado para grandes conjuntos de dados.
  
  Embora a origem exata do Bubble Sort seja desconhecida, ele é considerado um dos algoritmos de ordenação mais antigos e básicos da história da ciência da computação. Acredita-se que o algoritmo tenha sido inventado na década de 1950, no início da era dos computadores eletrônicos. O Bubble Sort foi amplamente utilizado nos primeiros computadores digitais e ainda é usado em algumas aplicações de ordenação simples.
  
  Embora o Bubble Sort seja ineficiente em comparação com muitos outros algoritmos de ordenação, ele é relativamente fácil de entender e implementar. Por esse motivo, o Bubble Sort é freqüentemente usado em atividades de ensino e como um exemplo de como não se deve ordenar grandes conjuntos de dados.

- Insertion Sort:
  O Insertion Sort é um algoritmo de ordenação simples, eficiente e estável, que percorre a lista de elementos da esquerda para a direita, inserindo cada elemento na posição correta em uma sublista ordenada. A sublista ordenada é construída à medida que os elementos são inseridos, e o processo continua até que todos os elementos sejam inseridos na sublista ordenada. A complexidade do Insertion Sort é O(n^2) no pior caso, mas é O(n) no melhor caso quando a lista já está ordenada.
  
  Embora a origem exata do Insertion Sort seja desconhecida, ele é considerado um dos algoritmos de ordenação mais antigos e básicos da história da ciência da computação. O algoritmo tem suas raízes na ordenação manual de cartões perfurados em mecanismos de processamento de dados primitivos. O Insertion Sort foi descrito pela primeira vez no livro "The Art of Computer Programming" de Donald Knuth, em 1968, e desde então se tornou um dos algoritmos de ordenação mais populares e amplamente utilizados.
  
  O Insertion Sort é frequentemente usado para ordenar pequenos conjuntos de dados e é uma boa escolha quando a lista já está quase ordenada. O algoritmo também é usado como um passo intermediário em outros algoritmos de ordenação mais complexos. Sua simplicidade e eficiência tornam o Insertion Sort um algoritmo importante na ciência da computação.

- Selection Sort:
  O Selection Sort é um algoritmo de ordenação simples e ineficiente que percorre a lista várias vezes, selecionando o menor elemento e colocando-o na primeira posição, depois o segundo menor e colocando-o na segunda posição, e assim por diante, até que a lista esteja ordenada. A complexidade do Selection Sort é O(n^2), tornando-o inadequado para grandes conjuntos de dados.
  
  Embora a origem exata do Selection Sort seja desconhecida, ele é considerado um dos algoritmos de ordenação mais antigos e básicos da história da ciência da computação. O algoritmo foi originalmente descrito no livro "The Art of Computer Programming" de Donald Knuth, em 1968, mas já era conhecido e utilizado em computadores mecânicos desde a década de 1940. O Selection Sort é uma das primeiras técnicas de ordenação de dados que foram desenvolvidas e ainda é usado em algumas aplicações de ordenação simples.
  
  Embora o Selection Sort seja ineficiente em comparação com muitos outros algoritmos de ordenação, ele é relativamente fácil de entender e implementar. Por esse motivo, o Selection Sort é frequentemente usado em atividades de ensino e como um exemplo de como não se deve ordenar grandes conjuntos de dados.

- Heap Sort:
  O Heap Sort é um algoritmo de ordenação eficiente que utiliza uma estrutura de dados chamada heap para organizar os elementos a serem ordenados. A ideia é construir uma árvore binária completa que satisfaz a propriedade heap, onde cada nó é maior ou igual aos seus filhos (no caso de uma heap máxima) ou menor ou igual aos seus filhos (no caso de uma heap mínima). Em seguida, o algoritmo retira sucessivamente o elemento de maior (ou menor) valor da heap e coloca-o no final do vetor, até que todos os elementos estejam ordenados.
  
  O Heap Sort foi inventado em 1964 por J. W. J. Williams, um programador britânico, embora sua complexidade tenha sido analisada pela primeira vez por R. W. Floyd em 1962. O algoritmo é considerado um dos mais eficientes algoritmos de ordenação em termos de tempo de execução, com uma complexidade de O(n log n), o que o torna adequado para conjuntos de dados de tamanho moderado e grande.
  
  O Heap Sort é frequentemente usado como um exemplo de como a estrutura de dados heap pode ser usada para resolver problemas de ordenação e outras aplicações em ciência da computação. Além disso, ele é frequentemente usado como uma alternativa mais rápida e eficiente para algoritmos de ordenação como o Selection Sort e o Insertion Sort.

- Counting Sort:
  O Counting Sort é um algoritmo de ordenação que utiliza uma abordagem de contagem para ordenar os elementos. A ideia básica é contar o número de ocorrências de cada elemento no vetor e, em seguida, reconstruir o vetor ordenado a partir dessas contagens.
  
  O Counting Sort foi proposto pela primeira vez em 1954 por Harold H. Seward, mas só ganhou destaque na comunidade acadêmica em 1962, quando foi apresentado por Robert C. Prim. O algoritmo é adequado para ordenar grandes conjuntos de dados com valores discretos e com um intervalo limitado de valores.
  
  O algoritmo funciona criando um array auxiliar de contagem com tamanho igual ao intervalo de valores possíveis no vetor de entrada. Em seguida, percorre o vetor de entrada, contando o número de ocorrências de cada valor possível e armazenando essas contagens no array auxiliar. Em seguida, percorre o array auxiliar e utiliza as contagens para reconstruir o vetor de entrada ordenado.
  
  O Counting Sort é um algoritmo eficiente em termos de tempo de execução, com uma complexidade de O(n+k), onde n é o tamanho do vetor de entrada e k é o intervalo de valores possíveis. No entanto, ele requer uma grande quantidade de memória auxiliar para armazenar as contagens, o que pode limitar sua utilidade em algumas situações.

- Shell Sort:
  O Shell Sort é um algoritmo de ordenação baseado no método de inserção direta, que busca melhorar a eficiência deste método em vetores com um grande número de elementos. Ele foi proposto em 1959 por Donald Shell, e é considerado um dos primeiros algoritmos de ordenação com desempenho superior ao O(n^2).
  
  O algoritmo funciona dividindo o vetor em subconjuntos menores e aplicando o método de inserção direta em cada um desses subconjuntos. A diferença é que, ao contrário do método de inserção direta, o Shell Sort não ordena os elementos apenas em pares adjacentes, mas sim em intervalos maiores. Esses intervalos são chamados de "intervalos de incremento", e são determinados por uma sequência de números, como 1, 4, 13, 40, etc.
  
  O Shell Sort começa aplicando o método de inserção direta com o maior intervalo de incremento, reduzindo gradualmente esse intervalo até chegar a 1. Quando o intervalo de incremento é 1, o Shell Sort é equivalente ao método de inserção direta. No entanto, como os elementos já estão parcialmente ordenados em intervalos maiores, a quantidade de comparações e movimentações de elementos é reduzida em comparação com o método de inserção direta aplicado diretamente no vetor original.
  
  O desempenho do Shell Sort depende da escolha da sequência de incrementos, e existem várias sequências propostas na literatura. Em geral, quanto maior a sequência de incrementos, melhor é o desempenho do algoritmo, mas isso também aumenta a complexidade do algoritmo. O Shell Sort tem uma complexidade média de O(n log n), mas pode ser ainda mais rápido em certos casos específicos.

- Cocktail Sort:
  O Cocktail Sort, também conhecido como Shaker Sort, é um algoritmo de ordenação que é uma variação do Bubble Sort. Assim como o Bubble Sort, ele compara e troca pares de elementos adjacentes até que a lista esteja completamente ordenada. No entanto, o Cocktail Sort realiza o processo de ordenação em ambas as direções da lista, ou seja, da esquerda para a direita e da direita para a esquerda.
  
  O Cocktail Sort foi desenvolvido com o objetivo de melhorar a eficiência do Bubble Sort em casos específicos, como listas que possuem elementos menores no final da lista. O algoritmo começa comparando e trocando pares de elementos adjacentes da esquerda para a direita, como no Bubble Sort. Quando o final da lista é alcançado, o algoritmo inverte a direção e começa a comparar e trocar pares de elementos adjacentes da direita para a esquerda.
  
  Assim como o Bubble Sort, o Cocktail Sort é simples de entender e implementar, mas é considerado um algoritmo menos eficiente do que outros algoritmos de ordenação. A complexidade do Cocktail Sort é O(n^2), assim como a do Bubble Sort.
  
  Apesar de ser menos utilizado do que outros algoritmos, o Cocktail Sort ainda é uma opção viável em alguns casos, especialmente quando a lista já está parcialmente ordenada ou possui poucos elementos. Sua história é relativamente recente, com a primeira menção do algoritmo aparecendo em um artigo acadêmico publicado em 1991 por David Gries e Paul Gibbons. Desde então, o Cocktail Sort tem sido objeto de estudos e análises por parte de especialistas em algoritmos de ordenação.