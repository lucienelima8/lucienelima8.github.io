#Cálculo IMC (índice de massa corporal)

altura = float(input('Qual é a usa altura em cm: '))
peso = float(input('Qua é o seu peso em kg: '))

#dividindo por 100 porque pedi altura em cm
IMC = peso / (altura/100) **2
print(IMC)

if IMC < 18.5:
    print('Seu peso está abaixo do normal.')
elif IMC >= 18.5 and IMC < 24.9:
    print('Seu peso está normal')
elif IMC >= 25.0 and IMC < 29.9:
    print('Tome cuidado! Você está com sobrepeso.')
elif IMC >= 30.0 and IMC < 39.9:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade grave. Procure um médico.')