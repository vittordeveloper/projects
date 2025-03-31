#Crie uma função que verifique se um número é primo e retorne um valor booleano. Teste a função com diferentes números.
# Um número primo é divisivel por 1 e por ele mesmo ou seja

def e_primo(valor):
    if valor < 2:
        return False
    for i in range(2, valor):
        if valor % i == 0:
            return False
    return True
        

print(e_primo(4))
    
