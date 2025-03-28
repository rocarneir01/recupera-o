#  Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso, faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.
*

ano_nascimento = int(input("Digite o ano que você nasceu: "))
from datetime import datetime
ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento

if idade == 18:
    print("Você fará ou já fez 18 anos neste ano!")
else:
    print("Você não completará 18 anos neste ano.")