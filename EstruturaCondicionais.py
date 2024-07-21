# Estrutura de Decisão Simples
A = input("Informe um valor para a variável A: ")
B = input("Informe um valor para a variável B: ")

# Caso o valor seja maior, irá ter uma troca de valores, criando uma nova variável chamada aux para
# transferir o valor antigo sem perder ele.
if (A>B):
    aux=A;
    A=B;
    B=aux;
print("O valor da variável A agora é : ", A)
print("O valor da variável B agora é : ", B)

# Estrutura de Decisão Composta (if e else)
# No Python não existe abre e fecha de {}
# Aqui a identação é um "espaço" amais na linha. Exemplo:
idade = int(input("Digite a idade da pessoa: "))

if idade >= 18:
    print("Maior de idade")
#^^ Espaço
else:
    print("Menor de idade")
#^^ Espaço

# elif é a junção do else e do if (famoso else if). Tem a mesma utilidade do else if.
nota = int(input("Digite uma nota de: "))

if nota >= 10:
    print("Muito bom!")
elif nota >= 6:
    print("Bom.")
elif nota >= 3:
    print("Razoável.")
elif nota < 3:
    print("Ruim.")
else:
    print("variavél nota sem valor (Erro).")