
# PYTHON -- Você pode executar esse código em um ambiente Python de sua escolha.

def pertence_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    if a == numero:
        return f"{numero} pertence à sequência de Fibonacci."
    else:
        return f"{numero} não pertence à sequência de Fibonacci."

numero_informado = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
resultado = pertence_fibonacci(numero_informado)
print(resultado)