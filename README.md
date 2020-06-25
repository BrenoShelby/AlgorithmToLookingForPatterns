# Introdução

Durante meus estudos, centrado no livro **Estrutura de Dados & Algoritmos** (escrito por Michael T. Goodrich e Roberto Tamassia), deparei-me com um assunto muito interessante: algoritmos para procura de padrões. Este por sua vez, possui aplicabilidade em diversas situações na computação, como por exemplo, quando você procura uma determinada palavra em um documento. Existe uma vasta literatura que aborda esse assunto e suas aplicabilidades. Entretanto, vamos nos focar na implementação e como funciona esses algoritmos. Serão apresentados três algoritmos, sendo eles: Força Bruta, Boyer-Moore e Knuth-Morris-Pratt (com um nível de dificuldade progressivo). Todo meu embasamento e o código vem do livro anteriormente citado, porém o código na versão em **Python** é de minha autoria, fique-se à vontade de alterá-lo, corrigi-lo ou melhorá-lo.

## Análise de algoritmos

Antes de tudo, vale salientar que ao longo das explicações será diversas vezes utilizada a notação *O*. Para quem não conhece, irei fazer uma breve introdução sobre. Existe um consenso na computação de que não há como você caracterizar, de maneira precisa, a performance de um algoritmo baseado em experimentos, ou seja, não basta você desenvolver um algoritmo que execute em X milissegundos na sua máquina, que isso necessariamente irá ocorrer em uma outra máquina. Segundo Goodrich & Tamassia, é difícil comparar dois experimentos de algoritmos sem que haja uma igualdade em termos de hardware da máquina.
Dito isso, existe uma forma melhor de definir a performance de um algoritmo através da notação *O*, esta utiliza de funções consolidadas na matemática, por exemplo, função exponencial, função polinomial, função constante e todas as outras (~~que você já deve estar careca de saber~~). Em termos simples, funciona assim, a notação *O* simplifica as coisas para você, pegando um exemplo bobo: considere um método que retorna o tamanho de um array (```len(array)```), este por sua vez possui uma notação O(1), isto é, o método é constante, o resultado independe do tamanho do array. Para ficar mais claro, um outro exemplo: considere um método que retorna o maior número de um array (~~caso você não saiba como funciona, procure no Google~~), para descobrir o maior número é necessário um laço que percorra o array, o quanto será percorrido depende do tamanho (n), portanto, a notação seria O(n). Enfim, este assunto é bem mais cabeludo, mas nada impossível de se entender. Recomendo uma literatura mais detalhada em: (https://en.wikipedia.org/wiki/Analysis_of_algorithms) ou (https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

## Algoritmos para busca de padrões

- **Força bruta**: 
- **Boyer-Moore**:
- **Knuth-Morris-Pratt**
