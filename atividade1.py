# Função para verificar semelhança pelo critério LAL (Lado-Ângulo-Lado)
def semelhança_lal(lado1_t1, lado2_t1, ângulo_t1, lado1_t2, lado2_t2, ângulo_t2):
    if ângulo_t1 == ângulo_t2 and (lado1_t1 / lado1_t2) == (lado2_t1 / lado2_t2):
        return True
    return False

# Função para verificar semelhança pelo critério AA (Ângulo-Ângulo)
def semelhança_aa(ângulo1_t1, ângulo2_t1, ângulo1_t2, ângulo2_t2):
    if (ângulo1_t1 == ângulo1_t2 and ângulo2_t1 == ângulo2_t2) or \
       (ângulo1_t1 == ângulo2_t2 and ângulo2_t1 == ângulo1_t2):
        return True
    return False

# Função para verificar semelhança pelo critério LLL (Lado-Lado-Lado)
def semelhança_lll(lado1_t1, lado2_t1, lado3_t1, lado1_t2, lado2_t2, lado3_t2):
    proporção1 = lado1_t1 / lado1_t2
    proporção2 = lado2_t1 / lado2_t2
    proporção3 = lado3_t1 / lado3_t2

    if proporção1 == proporção2 == proporção3:
        return True
    return False

# Função principal para verificar qual critério foi satisfeito
def verificar_semelhança():
    print("Escolha o critério de verificação: LAL, AA ou LLL")
    critério = input("Digite o critério: ").strip().upper()

    if critério == "LAL":
        # Entrada para o critério LAL
        lado1_t1 = float(input("Digite o lado 1 do Triângulo 1: "))
        lado2_t1 = float(input("Digite o lado 2 do Triângulo 1: "))
        ângulo_t1 = float(input("Digite o ângulo entre os lados do Triângulo 1: "))

        lado1_t2 = float(input("Digite o lado 1 do Triângulo 2: "))
        lado2_t2 = float(input("Digite o lado 2 do Triângulo 2: "))
        ângulo_t2 = float(input("Digite o ângulo entre os lados do Triângulo 2: "))

        if semelhança_lal(lado1_t1, lado2_t1, ângulo_t1, lado1_t2, lado2_t2, ângulo_t2):
            print("Os triângulos são semelhantes pelo critério LAL.")
        else:
            print("Os triângulos NÃO são semelhantes pelo critério LAL.")

    elif critério == "AA":
        # Entrada para o critério AA
        ângulo1_t1 = float(input("Digite o ângulo 1 do Triângulo 1: "))
        ângulo2_t1 = float(input("Digite o ângulo 2 do Triângulo 1: "))

        ângulo1_t2 = float(input("Digite o ângulo 1 do Triângulo 2: "))
        ângulo2_t2 = float(input("Digite o ângulo 2 do Triângulo 2: "))

        if semelhança_aa(ângulo1_t1, ângulo2_t1, ângulo1_t2, ângulo2_t2):
            print("Os triângulos são semelhantes pelo critério AA.")
        else:
            print("Os triângulos NÃO são semelhantes pelo critério AA.")

    elif critério == "LLL":
        # Entrada para o critério LLL
        lado1_t1 = float(input("Digite o lado 1 do Triângulo 1: "))
        lado2_t1 = float(input("Digite o lado 2 do Triângulo 1: "))
        lado3_t1 = float(input("Digite o lado 3 do Triângulo 1: "))

        lado1_t2 = float(input("Digite o lado 1 do Triângulo 2: "))
        lado2_t2 = float(input("Digite o lado 2 do Triângulo 2: "))
        lado3_t2 = float(input("Digite o lado 3 do Triângulo 2: "))

        if semelhança_lll(lado1_t1, lado2_t1, lado3_t1, lado1_t2, lado2_t2, lado3_t2):
            print("Os triângulos são semelhantes pelo critério LLL.")
        else:
            print("Os triângulos NÃO são semelhantes pelo critério LLL.")
    else:
        print("Critério inválido. Por favor, escolha entre LAL, AA ou LLL.")

# Executa o programa
verificar_semelhança()
