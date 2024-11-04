# Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

# 1)
import json


def sum(indice):
    k = 0
    sum = 0
    while k < indice:
        k = k + 1
        sum = sum + k
    return sum


print(sum(13))

# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
# pertence ou não a sequência.

# 2)
number = input("your number belongs to the fibonacci sequence? ")


def fibonacci(number):
    valor = int(number)
    last_valor = 0
    new_valor = 1

    if valor in (0, 1):
        return f"The number {number} belongs to the fibonacci."

    while new_valor <= valor:
        if new_valor == valor:
            return f"The number {number} belongs to the fibonacci."

        temp = new_valor
        new_valor = last_valor + new_valor
        last_valor = temp
        # print(new_valor)
    return f"The number {number} doesn't belongs to the fibonacci."


print(fibonacci(number))

with open('faturamento.json', 'r') as file:
    data = json.load(file)
    daily_revenue = data['faturamento_diario']
    # print(faturamento)

    revenue_values = [day['valor'] for day in daily_revenue]

    revenue_days_count = 0
    days_above_averag = 0
    total_revenue = 0
    max_revenue = 0
    min_revenue = 0
    media = 0

    for value in revenue_values:
        if value != 0:
            total_revenue += value
            if max_revenue < value:
                max_revenue = value
            if min_revenue > value or min_revenue == 0:
                min_revenue = value
            revenue_days_count += 1

    average_revenue = total_revenue / revenue_days_count
    for day in revenue_values:
        if day > average_revenue:
            days_above_averag += 1

    # print(revenue_days_count)
    # print(total_revenue)
    # print(average_revenue)
    # print(min_revenue)
    # print(days_above_averag)

    print(f"The lowest revenue of the month was ${min_revenue}")
    print(f"The highest revenue of the month was ${max_revenue}")
    print(f"Have {days_above_averag} bigs days")


#  Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#     • SP – R$67.836, 43
#     • RJ – R$36.678, 66
#     • MG – R$29.229, 88
#     • ES – R$27.165, 48
#     • Outros – R$19.849, 53

# 4)

def porcent():

    dist = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.40,
        "OUTROS": 19849.53,
    }

    dist_porcent = {}

    total_revenue = 0

    for revenue in dist.values():
        total_revenue += revenue

    for dist, revenue in dist.items():
        dist_porcent[dist] = f"{(revenue * 100 / total_revenue):.2f}"

    for state, percent in dist_porcent.items():
        print(f"{state}: {percent}%")


porcent()

#  Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# 5)


def reverse(text):
    original_text = text
    text_reverse = ""

    i = len(text) - 1

    while i >= 0:
        text_reverse += original_text[i]
        i -= 1

    print(f"{text_reverse}")


reverse(input("Enter the text: "))
