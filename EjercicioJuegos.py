words= ["","1","1","1","1"]
change=int(input ("Bienvenido Jefe. Ingrese la cantidad de corrimientoss de sus mensajes: "))


for i in range(5):
  words[i]=input(f"mensaje {i}: ")
dictionary=["a","b", "c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(0,len(words)):
  print(words[i],end=" ")
  st=words[i]

print("")

for i in range(0,len(words)):
  st=words[i]
  change_word=""
  for x in range(0,len(st)):
    
    if st[x] in dictionary:
      #Si la letra esta dentro del diccionario(si es una letra)
      original_letter=st[x]
      pos=(dictionary.index(original_letter)+change)%len(dictionary)
      change_letter=dictionary[pos]
      change_word=change_word+change_letter
    else:
      #es un caracter, numero, espacio
      change_word=change_word+st[x]
    #guardo la nueva palabra modificada
    words[i]=change_word

for i in range(0,len(words)):
  print(words[i],end=" ")
  st=words[i]
print("")