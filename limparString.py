def limpar_aux(string):
    i = 0
    resposta = ''
    while i < len(string):
        if i == len(string)-1:
            resposta = resposta + string[i]
            i = i + 1
        elif string[i] == string[i+1]:
            i = i + 2
        elif string[i] != string[i+1]:
            resposta = resposta + string[i]
            i = i + 1
    if resposta == '':
        return 'Empty String'
    return resposta

def limpar(string_antiga):
    while True:
        string_nova   = limpar_aux(string_antiga)
        if string_nova == string_antiga:
            return string_nova
        string_antiga = string_nova
        

limpar('aasffesfses')    
assert limpar('aab') == 'b'
assert limpar('abc') == 'abc'
assert limpar('aabdbcc') == 'bdb'
assert limpar('bbaa') == 'Empty String'
assert limpar('abbac') == 'c'
print('Passou em tudo!')