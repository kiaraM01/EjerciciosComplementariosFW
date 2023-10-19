# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

print("Ingrese numeros, si ingresa el 0, el programa finaliza")
n_par=0
n_impar=0
numb=100
index=1
while numb!=0:
  print(f"Usted tiene {n_par} numeros pares, y {n_impar} numeros impares")
  numb=int(input(f"N°{index}: "))
  if numb!=0:
    
    if numb%2==0:
      n_par=n_par+1
    else:
      n_impar=n_impar+1
  

  index=index+1
print(f"Usted ingresó {n_par} numeros pares, y {n_impar} numeros impares")