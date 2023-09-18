#Cálculo da média simples de 4 bimestres

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
nota4 = float(input('Digite a nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

#print('Sua media é: ', media)

if media < 7:
  print(f' Sua média é: {media}. Você foi Reprovado. Estude mais.')
elif media < 10:
  print(f' Sua média é: {media}. Você foi Aprovado. Parabéns!')
else:
  print(f' Parabéns!! Sua média é: {media}. Você foi aprovado com mérito.')
