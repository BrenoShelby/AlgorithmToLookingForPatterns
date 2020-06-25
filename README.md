# Introdução

Durante meus estudos, centrado no livro **Estrutura de Dados & Algoritmos** (escrito por Michael T. Goodrich e Roberto Tamassia), deparei-me com um assunto muito interessante: algoritmos para procura de padrões. Este por sua vez, possui aplicabilidade em diversas situações na computação, como por exemplo, quando você procura uma determinada palavra em um documento. Existe uma vasta literatura que aborda esse assunto e suas aplicabilidades. Entretanto, vamos nos focar na implementação e como funciona esses algoritmos. Serão apresentados três algoritmos, sendo eles: Força Bruta, Boyer-Moore e Knuth-Morris-Pratt (com um nível de dificuldade progressivo). Todo meu embasamento e o código vem do livro anteriormente citado, porém o código na versão em **Python** é de minha autoria, fique-se à vontade de alterá-lo, corrigi-lo ou melhorá-lo.

## Análise de algoritmos

Antes de tudo, vale salientar que ao longo das explicações será diversas vezes utilizada a notação *O*. Para quem não conhece, irei fazer uma breve introdução sobre. Existe um consenso na computação de que não há como você caracterizar, de maneira precisa, a performance de um algoritmo baseado em experimentos, ou seja, não basta você desenvolver um algoritmo que execute em X milissegundos na sua máquina, que isso necessariamente irá ocorrer em uma outra máquina. Segundo Goodrich & Tamassia, é difícil comparar dois experimentos de algoritmos sem que haja uma igualdade em termos de hardware da máquina.
Dito isso, existe uma forma melhor de definir a performance de um algoritmo através da notação *O*, esta utiliza de funções consolidadas na matemática, por exemplo, função exponencial, função polinomial, função constante e todas as outras (~~que você já deve estar careca de saber~~). Em termos simples, funciona assim, a notação *O* simplifica as coisas para você, pegando um exemplo bobo: considere um método que retorna o tamanho de um array (```len(array)```), este por sua vez possui uma notação O(1), isto é, o método é constante, o resultado independe do tamanho do array. Para ficar mais claro, um outro exemplo: considere um método que retorna o maior número de um array (~~caso você não saiba como funciona, procure no Google~~), para descobrir o maior número é necessário um laço que percorra o array, o quanto será percorrido depende do tamanho (n), portanto, a notação seria O(n). Enfim, este assunto é bem mais cabeludo, mas nada impossível de se entender. Recomendo uma literatura mais detalhada em: (https://en.wikipedia.org/wiki/Analysis_of_algorithms) ou (https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

## Algoritmos para busca de padrões

- **Força bruta**: o padrão de projeto algorítmico baseado em força bruta é uma técnica simples e poderosa quando se deseja procurar algo. Aplicando esta técnica para o algoritmo de ***procura de padrões por força bruta***, deriva-se o que é provavelmente o primeiro algoritmo em que se pode pensar para resolver o problema, simplesmente testam-se todas as possíveis colocações da palavra em relação ao texto. Isto é, ele consiste em dois laços aninhados, com o laço externo pesquisando todos os possíveis índices do padrão dentro do texto, e o laço interno pesquisando cada caractere do padrão, comparando-o a seu correspondente potencial no texto. Evidentemente, o tempo de execução da procura de padrões por força bruta no pior caso não é bom, pois para cada índice-candidato do texto pode ser realizado até *X* comparações de caracteres para descobrir que o padrão não está no texto.
  - **Desempenho**: devido aos laços aninhados, sem entrar nos méritos matemáticos, este algoritmo possui um tempo de execução quadrático O(n²).

- **Boyer-Moore**: este algoritmo consegue evitar comparações entre *P* (padrão) e uma boa parte dos caracteres em *T* (texto). O único problema é que, enquanto o algoritmo de força bruta pode trabalhar com um alfabeto ilimitado, o algoritmo Boyer-Moore assume que o alfabeto tem tamanho finito. Ou seja, ele exije que inicializemos um arranjo onde armazenaremos esse alfabeto e faremos as comparações. Ele tem melhor desempenho quando o alfabeto é de tamanho moderado e o padrão é relativamente longo. Assim, o algoritmo BM é ideal para procurar palavras em documentos. Sua principal caracteristíca é a utilização de duas heurísticas, são elas:
  - **Heurística do Espelho**: quando se testa uma possível colocação de *P* em *T*, começam-se as comparações de forma invertida, isto é, pelo final de *P*, e recua-se até o   início de *P*.
  - **Heurística do salto de caracteres**: durante um teste de uma possível colocação de *P* em *T*, uma diferença entre o caractere ```T[i] = c``` com o caractere           correspondente ```P[j]``` é tratada como segue: se *c* não está contido em lugar algum de *P*, então move-se *P* completamente para depois de ```T[i]``` (pois ```T[i]``` não   pode estar em *P*). Caso contrário, move-se *P* para frente até que uma ocorrência do caractere *c* em *P* esteja alinhada com ```T[i]```. Esta heurística é mais elaborada, logo, define-se uma função last(*c*) que recebe um caractere *c* do alfabeto e caracteriza o quanto é possível avançar o padrão *P* se um caractere igual a *c* for encontrado no texto e não fizer parte do padrão. Em particular, define-se last(*c*) como: "se um *C* (caracter) está em *P* (padrão), f(*c*) é o índice da última ocorrência (mais à direita) de *C* em *P*. Senão, convenciona-se que f(*c*) = -1."
  
  Eu sei, parece extremamente complicado entender da maneira formal, mas acredite, é muito mais fácil do que parece. O que é necessário entender é que as duas heurísticas trabalham de maneira complementar. A heurística do espelho permite que a heurística do salto de caracteres evite comparações em *P* e grupos inteiros de caracteres em *T*. Caso ainda tenha dúvida, a melhor coisa que eu indico é fazer o famoso ***teste de mesa*** (~~isso ajuda muito a entender esses algoritmos desgraçados~~) com um exemplo fácil, você verá que não é tão assustador e realmente faz sentido.
  
  - **Desempenho**: o tempo de execução de pior caso do algoritmo BM é O(m + |Σ|) (na verdade, segundo o livro que uso para consultar, o algoritmo original tem um tempo de    O(n + m + |Σ|)), entretanto, estamos utilizando a versão simplificada). Já a função last(*c*), tem um desempenho também de O(m + |Σ|) e a procura do padrão custa tempo O(n²) no pior caso, o mesmo que o algoritmo de força bruta.
  
- **Knuth-Morris-Pratt**: um problema recorrente com os algoritmos anteriores era o desperdício de informação, quando descobria-se um caractere que falhava na comparação, jogava-se fora toda a informação adquirida pelas comparações anteriorese e começa-se novamente (do zero) no ponto em que o padrão for posicionado, mais à frente. Já o algoritmo Knuth-Morris-Pratt evita este desperdício de informação. E, como ele faz isso? Simples (~~ou nem tão simples~~), utilizando uma função de falha. Esta função de falha tem a finalidade de pré-processar *P* (padrão) para calcular uma função de falha, que indica quanto se deve avançar *P* de forma que seja possível reutilizar as comparações realizadas anteriormente tanto quanto possível. Novamente, volto a dizer, esses conceitos aparentam ser difíceis, mas na prática, nem tanto. O melhor a se fazer é *debugar* o código, fazer um teste de mesa e ir testando.

  - **Desempenho**: o tempo de execução no pior caso é de O(n + m). Isso significa um ótimo desempenho, ainda mais comparado com os outros (~~Uhul!~~)

## Conclusão

Se você for uma pessoa curiosa como eu, esse assunto irá brilhar seus olhos. Esses algoritmos são só a ponta do iceberg, fico pensando na infinidade de aplicações disso no nosso cotidiano e como isso é interessante. De fato, eu achei extremamente complicado os conceitos escritos de maneira formal, e piorava quando me deparava com os códigos, isso me assustava mais ainda. Contudo, lendo com calma e atenção, tentando abstrair a idéia para o meu modo de entender as coisas, percebi que não é tão complicado quanto parece. Nada que algumas boas horas (~~indo trecho por trecho~~) de estudo não ajude.

## Referências
- Goodrich, T.; Tamassia, R. (2013). Estrutura de Dados & Algoritmos - 5 edição.
