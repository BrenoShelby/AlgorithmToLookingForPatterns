import time

def bruteForce(texto, padrao):
    for i in range(0, len(texto) - len(padrao)):
        j = 0
        while j < len(padrao) and texto[i + j] == padrao[j]:
            j = j + 1
        if j == len(padrao):
            return 'Padrão Encontrado'
    return "Não existe um padrão especificado no texto"

print('===========Teste 1==========')
inicio = time.time()
print(bruteForce('Breno foi até a padaria, durante seu trajeto se deparou com seu amigo Lucas', 'até'))
fim = time.time()
print('Duração: %f' % (fim - inicio))

diretorio = input('Digite o diretório do arquivo (exemplo: textos/teste.txt): ')
padrao = input('Digite o padrão que deseja encontrar: ')

with open(diretorio, 'r') as f:
    inicio = time.time()
    print(bruteForce('Breno foi até a padaria, durante seu trajeto se deparou com seu amigo Lucas', 'até'))
    fim = time.time()
    print('Duração: %f' % (fim - inicio))
    
