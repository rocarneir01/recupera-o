# Faça um programa que solicite ao usuário sua idade, depois disso, exiba a classificação etária de acordo com as faixas de valores:
*
idade = int(input("Digite sua idade: "))
if idade < 12:
    classificacao = "Criança"
elif idade < 18:
    classificacao = "Adolescente"
elif idade < 60:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"
print(f"Você é classificado como: {classificacao}")