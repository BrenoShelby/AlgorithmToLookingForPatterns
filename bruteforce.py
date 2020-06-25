import time

'''O método de força bruta consiste em dois laços aninhados, com o laço externo
pesquisando todos os possíveis índices do padrão dentro do texto, e o laço interno
pesquisando cada caractere do padrão, comparando-o a seu correspondente potencial no
texto.
OBS: O algoritmo é sensível a letras mínusculas ou maísculas.
'''
def bruteForce(texto, padrao):
    for i in range(0, len(texto) - len(padrao)):
        j = 0
        while j < len(padrao) and texto[i + j] == padrao[j]:
            j = j + 1
        if j == len(padrao):
            return 'Padrão encontrado'
    return "Padrão não encontrado"

print('===========Teste 1==========')
inicio = time.time()
print(bruteForce('Breno foi até a padaria', 'até'))
fim = time.time()
print('Duração: %f' % (fim - inicio))

diretorio = input('Digite o diretório do arquivo (exemplo: textos/teste.txt): ')
padrao = input('Digite o padrão que deseja encontrar: ')

with open(diretorio, 'r') as f:
    inicio = time.time()
    print(bruteForce(f.read(), padrao))
    fim = time.time()
    print('Duração: %f' % (fim - inicio))
    
