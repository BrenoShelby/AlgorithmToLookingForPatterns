import time

''' Método para calcular a função de falha da string (P), a idéia por trás é
pré-processar P para calcular uma função de falha, que indica quanto se deve avançar
P de forma que seja possível reutilizar as comparações realizadas anteriormente tanto
quanto possível.
'''
def computeFailFunction(padrao):
    m = len(padrao) #tamanho do padrao

    '''Inicializando o arranjo com o tamanho do padrao'''
    fail = [0] * m
    j = 0 #indice
    i = 1 #indice

    '''Enquanto i for menor que o tamanho do padrao, cada caracter será comparada com 
    o seguinte'''
    while(i < m):
        '''Exemplo: 
        padrao = 'sasha' 
        Saída esperada do arranjo fail = [0,0,1,0,0]'''
        if(padrao[j] == padrao[i]):
            fail[i] = j + 1
            i += 1
            j += 1
        elif(j > 0):
            j = fail[j - 1]
        else:
            fail[i] = 0
            i += 1

    return fail

'''Este método funciona de maneira simples, a parte principal do algoritmo é o seu laço while,
que realiza a comparação entre um caracter de T (texto) e um caracter de P (padrão) a cada 
interação. Dependendo do resultado desta comparação, o algoritmo passa para o caractere seguinte
em T e P, consultando a função de falha para um novo caractere candidato em P ou reinicia o
processo com o novo índice em T. O grande segredo está na função de falha, ela evita comparações
desnecessárias entre caracteres. 
OBS: O algoritmo é sensível a letras mínusculas ou maísculas.
'''
def kmp(texto, padrao):
    n = len(texto) #tamanho do texto
    m = len(padrao) #tamanho do padrao
    fail = computeFailFunction(padrao) #calcular função de falha
    i = 0 #indice
    j = 0 #indice

    '''Enquanto i for menor que o tamanho do padrao, cada caracter será comparada com 
    o seguinte, de maneira semelhante ao laço da função de falha'''
    while(i < n):
        if(padrao[j] == texto[i]):
            if(j == m - 1):
                return "Padrão encontrado"
            i += 1
            j += 1
        elif(j > 0):
            j = fail[j - 1]
        else:
            i += 1
    
    return 'Padrão não encontrado'

print('===========Teste 1==========')
inicio = time.time()
print(kmp("SARA SASHA MARTA", "SASHA"))
fim = time.time()
print('Duração: %f' % (fim - inicio))

diretorio = input('Digite o diretório do arquivo (exemplo: textos/teste.txt): ')
padrao = input('Digite o padrão que deseja encontrar: ')

with open(diretorio, 'r') as f:
    inicio = time.time()
    print(kmp(f.read(), padrao))
    fim = time.time()
    print('Duração: %f' % (fim - inicio))