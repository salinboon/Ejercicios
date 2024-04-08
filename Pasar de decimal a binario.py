numero=10
b=''
lista=[]
if numero<=0 or type(numero)!=int:
  print(numero)
while numero>=1:
  a=numero%2
  numero=numero//2
  b=b+str(a)
  rev = ''.join(reversed(b))#Este comando fue usado para invertir caracteres en string
  t=int(rev)
try:
  print(t)  
  print(type(t))
except:
  print('Digite un caracter valido')