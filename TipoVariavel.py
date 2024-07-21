# Na linguagem de programação Python, as variáveis armazenam endereços de memória e não valores.
# o conceito de variável em Python é representado sempre por um objeto, e toda variável é uma referência.
codigo = 10
salario = 1500.00
nome = 'José'
situacao = True

# type é o typeof do JS, ele mostra o tipo da varíavel
tipo = type (salario)

print(salario)
print(tipo)

print("Código", codigo, "Nome:", nome, "O Sálario atual é de", salario)
# Também podemos concatenar as informações na linguagem Python utilizando o sinal de soma (+).
# Neste caso, temos de converter os valores que não são string para o tipo string.
# Para isso, utilizamos o comando (str) antes da impressão da variável. (Parece que não funciona mais 2024).
# print("Código", + str (codigo)+ "Nome:"+ nome+ "O Sálario atual é de" + str (salario))
