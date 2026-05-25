def soma():
    try:
        x = float(input("Por favor, digite o primeiro valor: "))
        y = float(input("Por favor, digite o segundo valor: "))
        resultado = x + y
        return x, y, resultado
    except ValueError:
        print("Erro: Digite um número válido!")
        return None

def subtracao():
    try:
        x = float(input("Por favor, digite o primeiro valor: "))
        y = float(input("Por favor, digite o segundo valor: "))
        resultado = x - y
        return x, y, resultado
    except ValueError:
        print("Erro: Digite um número válido!")
        return None

def multiplicacao():
    try:
        Fator_1 = float(input("Por favor, digite o primeiro fator que você deseja multiplicar: "))
        Fator_2 = float(input("Por favor, digite o segundo fator: "))
        Produto = Fator_1 * Fator_2
        return Fator_1, Fator_2, Produto
    except ValueError:
        print("Erro: Digite um número válido!")
        return None

def divisao():
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

# Chamadas
resultado_soma = soma()
if resultado_soma is not None:
    x, y, total = resultado_soma
    print(f"A soma entre {x} e {y} é: {total}")

resultado_sub = subtracao()
if resultado_sub is not None:
    x, y, total = resultado_sub
    print(f"Subtrair {y} de {x} resulta em: {total}")

resultado_mult = multiplicacao()
if resultado_mult is not None:
    Fator_1, Fator_2, Produto = resultado_mult
    print(f"O produto entre {Fator_1} e {Fator_2} é {Produto}")

resultado_div = divisao()
if resultado_div is not None:
    dividendo, divisor, quociente = resultado_div
    print(f"O quociente entre {dividendo} e {divisor} é {quociente}")