import time

def computeFailFunction(padrao):
    fail = []
    fail.append(0)
    m = len(padrao)
    j = 0
    i = 1

    while(i < m):
        if(padrao[j] == padrao[i]): # j + 1 caracteres são iguais
            fail[i] = j + 1
            i += 1
            j += 1
        elif(j > 0): # j segue um prefixo que serve
            j = fail[j - 1]
        else:
            fail[i] = 0
            i += 1
    
    return fail

def kmp(texto, padrao):
    n = len(texto)
    m = len(padrao)
    fail = computeFailFunction(padrao)
    i = 0
    j = 0

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

print(kmp("Breno Henrique", "Henrique"))
        