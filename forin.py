# a variável n é inicialmente ajustada para 0 (inicialização com valor padrão).
# Uma vez que n é menor do que 10 (condição), o comando print é executado.
# Essa condição é adicionada com o comando range.
# A variável n é incrementada em 1 (incremento padrão) e é testado se o valor de n ainda é menor do que 10.
# O processo se repete até que o valor de n fique maior ou igual a 10.
# Neste instante, o laço termina e o programa segue a execução das instruções do bloco de repetição.
for n in range(10):
    print('(Crescente):',n)

# Neste caso, os valores apresentados na tela terão como mínimo, o número 5 e, no máximo, 15.
for n in range(5, 16):
    print('(5 até 15):',n)

# Também é possível utilizar o decremento no contador, dentro do comando range.
# Neste caso, os valores apresentados na tela estarão em ordem decrescente.
for n in range(10, 0, -1):
    print('(Decrescente):',n)