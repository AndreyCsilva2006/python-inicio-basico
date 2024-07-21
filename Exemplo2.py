# para que possa ter uma interação do usuário tornando o programa dinâmico,
# temos de trabalhar com a função de entrada de dados, que no Python é conhecida como: input
# Resumindo, input faz com que o Usuário consiga digitar algo para uma variável.
fruta = input("Digite o nome de uma fruta; ")
print(fruta)

# A Função input só recebe dados String, se queremos que receba dados int teremos que coverter.
codigo = int(input("Digite o código do funcionário: "))
nome = input("Digite o nome do funcionário: ")
salario = float(input("Informe o salario "))
ativo = True

print("Código: %d "% codigo)
print("Nome: %s "% nome)
print("Salário: %.2f"% salario)
print("Ativo: %r"% ativo)

# Utilizamos a sequência de escapes para auxiliar na formatação da exibição dos dados.
# Para aplicá-los, utilizamos uma combinação de caracteres associados a uma contra barra (\).
# Sequência	Descrição
# \n	Insere uma quebra de linha.
# \t	Insere tabulação horizontal.
# \v	Insere tabulação vertical.
# \r	Equivalente ao efeito da tecla Enter.
# \’	Aspas simples.
# \”	Aspas duplas.
# \\	Insere uma barra invertida (backslash).
# \a	Chamado de ASC bell ou beep do sistema. Se houver suporte, aciona um bipe.
# \b	Aciona o backspace, ou seja, apaga o caractere anterior.
# \f	Insere uma quebra de página.
# \u	Insere um caractere UNICODE. Deve acompanhar um código com 4 números.
print("\'d\'")
print("\ad\a")