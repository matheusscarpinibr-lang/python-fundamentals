import random

print("=== ROLADOR DE DADOS ===")
print("1 - d4")
print("2 - d6")
print("3 - d8")
print("4 - d10")
print("5 - d12")
print("6 - d20")

opcao = int(input("Escolha o dado: "))

dados = {
    1: 4,
    2: 6,
    3: 8,
    4: 10,
    5: 12,
    6: 20
}

dado = dados[opcao]
resultado = random.randint(1,dado)

print(f"\nVocê rolou um d{dado}!")
print(f"Resultado: {resultado}")