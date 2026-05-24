#Adicionando a função de somar e adaptando ela à interação com o usuário
def soma():
    x = float(input("Por favor, digite o primeiro valor: "))
    y = float(input("Por favor, digite o segundo valor: "))
    soma = x + y
    return print(f"A soma entre {x} e {y} é: {soma}")



def multiplicacao(): #Função de multiplicação entre dois números
    Fator_1 = float(input("Por favor, digite o primeiro fator que você deseja multiplicar: "))
    Fator_2 = float(input("Por favor, digite o segundo fator que você deseja multiplicar: "))
    Produto = Fator_1 * Fator_2
    return Fator_1, Fator_2, Produto

#Fator_1, Fator_2, Produto = multiplicacao()
#print(f"O produto entre {Fator_1} e {Fator_2} é {Produto}")
    


def divisao():  #Função de divisão entre dois números
    dividendo = float(input("Por favor, digite o dividendo: "))
    divisor = float(input("Por favor, digite o divisor: "))
    if divisor == 0: 
        raise ValueError("Não é possível dividir por zero.")
    else: 
        quociente = dividendo / divisor
        return dividendo, divisor, quociente    
        
#dividendo, divisor, resultado = divisao()
#print(f"O quociente entre {dividendo} e {divisor} é {resultado}")

#Adicionando a função de subtrair, e adaptando ela à interação com o usuário
def subtracao():
    x = float(input("Por favor, digite o primeiro valor: "))
    y = float(input("Por favor, digite o segundo valor: "))
    total = x - y
    return print(f"Subtrair {y} de {x} resulta em: {total}")
