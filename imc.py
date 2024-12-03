# Fórmula do cálculo do IMC
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

# Classificação do IMC
def classificar_imc(imc):
    if imc < 16:
        return "Magreza grau 3º"
    elif 16 <= imc < 16.99:
        return "Magreza grau 2º"
    elif 17 <= imc < 18.49:
        return "Magreza grau 1º"
    elif 18.50 <= imc < 24.99:
        return "Normal"
    elif 25 <= imc < 29.99:
        return "Sobrepeso"
    elif 30 <= imc < 34.99:
        return "Sobrepeso 1º"
    elif 35 <= imc < 39.99:
        return "Sobrepeso 2º"
    else:
        return "Sobrepeso 3º"
