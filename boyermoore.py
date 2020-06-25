import time

'''Esse método tem como objetivo satisfazer a heurística do salto de caracteres. De maneira
sucinta, define-se essa função como: se um C (caracter) está em P (padrão), f(c) é o índice
da última ocorrência (mais à direita) de C em P. Senão, convenciona-se que f(c) = -1. A definição
pode parecer díficil, mas na prática não é.
'''
def buildLastFunction(padrao):
    '''Inicializando o arranjo com o valor convencional sendo -1'''
    last = [-1] * 256
    
    '''Convertendo os caracteres da string padrao para ASCII'''
    ascii = {ord(c) for c in padrao}

    '''Neste laço, queremos atribuir a posição da string 'padrao' no respectivo
    indice do arranjo, este por sua vez, é o caracter ASCII da string'''
    for i, j in zip(ascii, range(0, len(padrao))):
        '''Exemplo:
        pattern = 'ABC'
        ascii = [65,66,67]
        O caracter A possui a posição 0 da string, logo será atribuido 0 a posição 65
        do arranjo last, e assim por diante'''
        last[i] = j

    return last #retorna o arranjo

'''' Versão simplificada do algoritmo Boyer-Moore(BM), que usa apenas as
heurísticas do espelho e do salto de caracteres. Índice do começo da ocorrência mais à 
esquerda do texto igual ao padrão, ou -1 se não há tal ocorrência.
OBS: O algoritmo é sensível a letras mínusculas ou maísculas.
'''
def boyermoore(texto, padrao):
    last = buildLastFunction(padrao) #calcula a função last
    n = len(texto) #tamanho do texto
    m = len(padrao) #tamanho do padrao 
    i = m - 1 #indice

    if(i > n - 1):
        return "O padrão precisa ser menor do que o texto" 

    j = m - 1 #indice

    while(i <= n - 1):
        if(padrao[j] == texto[i]):
            if(j == 0):
                return "Padrão encontrado" 
            else: #Heurística do salto de caracteres
                i -= 1
                j -= 1
        else:
            i = i + m - min(j, 1 + last[ord(texto[i])])
            j = m - 1
    
    return "Padrão não encontrado"

print('===========Teste 1==========')
inicio = time.time()
print(boyermoore('Sara Sasha Suju', 'Sasha'))
fim = time.time()
print('Duração: %f' % (fim - inicio))

diretorio = input('Digite o diretório do arquivo (exemplo: textos/teste.txt): ')
padrao = input('Digite o padrão que deseja encontrar: ')

with open(diretorio, 'r') as f:
    inicio = time.time()
    print(boyermoore(f.read(), padrao))
    fim = time.time()
    print('Duração: %f' % (fim - inicio))