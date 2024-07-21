codigo = 105
salario = 1650.00
nome = 'José Santana'
ativo = True

# Assim como em outras linguagens, é possível utilizar identificadores para representar os tipos de dados armazenados nas variáveis que devem ser exibidas na tela.

# Formatação para int (inteiro), pode ser usado %d ou %i.
print("Código: %d"% codigo)

# formatando para tipo String um valor inteiro.
print("Código: %s"% codigo)
print("Nome: %s "% nome)

# Com o %.2f vemos que ele controla as casas decimais, nessse caso 2, mas mudando pra 5 vai ficar 1650.00000
print("Salário: %.2f"% salario)

# Sem a formatação fica 1650.0
print("Salário:", salario)

# Formatação Booleana.
print("Ativo: %r"% ativo)