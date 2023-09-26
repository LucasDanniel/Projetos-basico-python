numeros = [
          [0,0],  
          [0,0],  
          [0,0]   
        ]       
             
positivo=[]
negativo=[]
soma=0
totalpositivo=0
totalnegativo=0
n1=0
maior = 0
n=0

for linha in range(3):
  for coluna in range(2):
    numeros[linha][coluna]=int(input("digite um numero: "))
    if numeros[linha][coluna] >= 0:
      positivo.append(numeros[linha][coluna])
      maior=numeros[linha][coluna]
      if maior >=n:
       n=maior
        
        

    else:
      negativo.append(numeros[linha][coluna])

print(numeros)


for i in range(len(positivo)):
  numero=positivo[i]
  totalpositivo=numero+totalpositivo
print("resultado da media do positivo",totalpositivo/len(positivo))


for i in range(len(negativo)):  
  numero=negativo[i]
  totalnegativo=numero+totalnegativo
print("Resultado da soma dos numeros negativos",totalnegativo) 


print("maior numero posito : " , n)

for coluna in range(0,2):
  if numeros[1][coluna] >=n1:
    n1=numeros[1][coluna]
print("O maior numero da segunda linha é: ", n1)
