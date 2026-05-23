def multiplicacao(): #Função de multiplicação entre dois números
    Fator_1 = float(input("Por favor, digite o primeiro fator que você deseja multiplicar: "))
    Fator_2 = float(input("Por favor, digite o segundo fator que você deseja multiplicar: "))
    Produto = Fator_1 * Fator_2
    print(f"O produto entre {Fator_1} e {Fator_2} é {Produto}")

multiplicacao()


def divisao():  #Função de divisão entre dois números
    dividendo = float(input("Por favor, digite o dividendo: "))
    divisor = float(input("Por favor, digite o divisor: "))
    if divisor == 0: 
        raise ValueError("Não é possível dividir por zero.")
    else: 
        quociente = dividendo / divisor
        return dividendo, divisor, quociente    
        
dividendo, divisor, resultado = divisao()
print(f"O quociente entre {dividendo} e {divisor} é {resultado}")

