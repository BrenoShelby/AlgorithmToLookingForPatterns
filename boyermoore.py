import time

def buildLastFunction(padrao):
    '''Criando um arranjo'''
    last = []

    '''Inicializando o arranjo com o valor convencional sendo -1'''
    for i in range(0,256):
        last.append(-1)
    
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
heurísticas do espelho e do salto de caracteres.
@return Índice do começo da ocorrência mais à esquerda do texto igual ao
padrão, ou -1 se não há tal ocorrência.
'''
def boyermoore(texto, padrao):
    last = buildLastFunction(padrao)
    n = len(texto)
    m = len(padrao)
    i = m - 1

    if(i > n - 1):
        return "O padrão precisa ser menor do que o texto" 
    
    j = m - 1

    while(i <= n - 1): # 2 <= 7
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