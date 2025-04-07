def calcular_kelly(odd_casa, odd_justa, fracao_kelly=1.0):
    b = odd_casa - 1
    p = 1 / odd_justa
    q = 1 - p

    kelly_cheia = ((b * p) - q) / b

    if kelly_cheia <= 0:
        return 0.0

    aposta = kelly_cheia * fracao_kelly
    return round(aposta * 100, 2)  # em %

def main():
    print("=== Calculadora de Kelly ===")
    try:
        odd_casa = float(input("Informe a odd da casa: "))
        odd_justa = float(input("Informe a odd justa (sua estimativa): "))
        #fracao_kelly = float(input("Informe a fração de Kelly (ex: 0.2 para Kelly 20%): "))
        fracao_kelly = 0.15

        resultado = calcular_kelly(odd_casa, odd_justa, fracao_kelly)
        print(f"\n➡️ Você deve apostar: {resultado}% da sua banca com Kelly {fracao_kelly}")
    
    except ValueError:
        print("⚠️ Entrada inválida. Por favor, insira apenas números.")

if __name__ == "__main__":
    main()
