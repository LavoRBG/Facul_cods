#função calcular o imc com as informações de peso e altura
def calcular_imc (peso, altura):
    return peso / (altura ** 2)

#função para calcular o IMC ideal com base nas informações de altura, idade e gênero
def calcular_imc_ideal(altura, idade, genero):
    if genero == 'M' or genero == 'm':
        imc_ideal = 22 if idade >= 18 else 21
    elif genero == 'F' or genero == 'f':
        imc_ideal = 21 if idade >= 18 else 20
    else:
       return "erro"

    return imc_ideal

#função para verificar a classificação com base na tabela de IMC
def verificar_classificacao(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau 1"
    elif imc < 39.9:
        return "Obesidade grau 2 (severa)"       
    else:
        return "Obesidade grau 3 (mórbida)"   

#Mostrar na tela o que o programa faz
print("Vamos calcular seu IMC (INDICE DE MASSA CORPORAL)")

#coletar as informações necessarias para os calculos
peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite sua idade: "))
genero = input("Digite seu genero: 'M'para masculino ou 'F' para feminino ")

#chamar funções
imc = calcular_imc(peso, altura)
imc_ideal = calcular_imc_ideal(altura, idade, genero)
classificacao = verificar_classificacao(imc)  
    
#printar resultados
print("\nSeu IMC é: {:.2f}".format(imc))
print("Sua classificação é: {}".format(classificacao))

if imc_ideal == 'erro':
    print("Não foi possivel verificar o IMC ideal pois o gênero não foi informado corretamente")
else:
    print("O IMC ideal com base na sua idade, altura e gênero é de: {}".format(imc_ideal))

