
# PYTHON -- Você pode executar esse código em um ambiente Python de sua escolha.

def inverte_string(string):
    string_invertida = ''
    for i in range(len(string)-1, -1, -1):
        string_invertida += string[i]
    return string_invertida

# Solicita que o usuário digite a string
texto = input("Digite uma string: ")

texto_invertido = inverte_string(texto)
print("String invertida: ", texto_invertido)