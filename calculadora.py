def multiplicacao():  #Função de multiplicação entre dois números
    try:
        Fator_1 = float(input("Por favor, digite o primeiro fator que você deseja multiplicar: "))
        Fator_2 = float(input("Por favor, digite o segundo fator que você deseja multiplicar: "))
        Produto = Fator_1 * Fator_2
        return Fator_1, Fator_2, Produto
    except ValueError:
        print("Erro: Digite um número válido!")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None
    


def divisao():  #Função de divisão entre dois números
    try:
        dividendo = float(input("Por favor, digite o dividendo: "))
        divisor = float(input("Por favor, digite o divisor: "))
        if divisor == 0: 
            raise ValueError("Não é possível dividir por zero.")
        quociente = dividendo / divisor
        return dividendo, divisor, quociente
    except ValueError as e:
        print(f"Erro: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None
    

#Chama a função de multiplicacao 
resultado_mult = multiplicacao()
if resultado_mult is not None:
    Fator_1, Fator_2, Produto = resultado_mult
    print(f"O produto entre {Fator_1} e {Fator_2} é {Produto}")
else:
    print("Operação cancelada devido a erro.")

#Chama a funcao de divisao
resultado = divisao()
if resultado is not None:
    dividendo, divisor, quociente = resultado
    print(f"O quociente entre {dividendo} e {divisor} é {quociente}")
else:
    print("Operação cancelada devido a erro.")