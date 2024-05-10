def decompor_moeda(valor):
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    notas_contagem = [0] * len(notas)
    moedas_contagem = [0] * len(moedas)

    # Calcula o número de notas
    for i, nota in enumerate(notas):
        while valor >= nota:
            notas_contagem[i] += 1
            valor -= nota

    # Calcula o número de moedas
    for i, moeda in enumerate(moedas):
        while valor >= moeda:
            moedas_contagem[i] += 1
            valor -= moeda

    return notas_contagem, moedas_contagem

def imprimir_decomposicao_moeda(notas_contagem, moedas_contagem):
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    print("Notas:")
    for i, contagem in enumerate(notas_contagem):
        if contagem > 0:
            print(f"{contagem} nota(s) de R$ {notas[i]:.2f}")

    print("\nMoedas:")
    for i, contagem in enumerate(moedas_contagem):
        if contagem > 0:
            print(f"{contagem} moeda(s) de R$ {moedas[i]:.2f}")

def main():
    valor = float(input("Digite o valor monetário (com duas casas decimais): "))
    notas_contagem, moedas_contagem = decompor_moeda(valor)
    imprimir_decomposicao_moeda(notas_contagem, moedas_contagem)

if __name__ == "__main__":
    main()
