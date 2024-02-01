name = input("Digite seu nome: ")
name2 = name
stars = len(name) * "*"
#print(stars)

for i in range(0, len(name)):
  for j in range(0, i+1):
    num = len(name) - j-1
    num2 = "* "*i
    if(name2[j] != "*"):
      print(name2[j] + " *"*num, sep="", end=" ")
      name2 = name2[:j] + "*" + name2[j+1:]
    else: 
      print("*", end = " ")
    #print(name[j], sep="", end=" ")
  print()