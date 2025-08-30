# Exercício - Cálculo de Salário com Descontos

# 1. Solicitar ao usuário os valores de entrada
try:
    valor_por_hora = float(input("Digite o valor recebido por hora trabalhada: R$ "))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

    # 2. Calcular os valores
    salario_bruto = valor_por_hora * horas_trabalhadas

    desconto_ir = salario_bruto * 0.11  # 11% de desconto do Imposto de Renda
    desconto_inss = salario_bruto * 0.09 # 9% de desconto do INSS
    desconto_sindicato = salario_bruto * 0.04 # 4% de desconto do Sindicato

    soma_descontos = desconto_ir + desconto_inss + desconto_sindicato
    salario_liquido = salario_bruto - soma_descontos

    # 3. Apresentar o resultado formatado
    print("\n--- Holerite ---")
    print(f"+ Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"- IR (11%): R$ {desconto_ir:.2f}")
    print(f"- INSS (9%): R$ {desconto_inss:.2f}")
    print(f"- Sindicato (4%): R$ {desconto_sindicato:.2f}")
    print("----------------")
    print(f"= Salário Líquido: R$ {salario_liquido:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite apenas números.")
