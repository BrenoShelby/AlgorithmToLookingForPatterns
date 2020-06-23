#def last(padrao):
    #em construção

def boyermoore(texto, padrao):
    last = last(padrao)
    n = len(texto)
    m = len(padrao)
    i = m - 1

    if(i > n - 1):
        return -1
    
    j = m -1

    while(i <= n -1):
        if(padrao[j] == texto[i]):
            if(j == 0):
                return i
            else:
                i = i - 1
                j = j - 1
        else:
            i = i + m - min(j, 1 + last[i])
            j = m - 1
    
    return -1
