# Média de Notas
notaA=float(input("Informe nota 1: "))
notaB=float(input("Informe nota 2: "))

# Calculando
mediafinal = (notaA + notaB) / 2

# Verificação
if mediafinal >= 7.0:
    print("A Média: %.1f - Aprovado "% mediafinal)
else:
    print("A Média: %.1f - Reprovado " % mediafinal)