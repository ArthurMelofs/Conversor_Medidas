#Função que faz a conversão celsius para fahrenheit#
def temperatura():

  print("1 - Celsius para Fahrenheit")
  print("2 - Fahrenheit para Celsius")

  opcao = int(input("Escolha uma das opções: "))

  if opcao == 1: 
    c = float (input("Digite a temperatura em Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit: ", round(f, 2) )
 
  elif opcao == 2:
    f = float (input("Digite a temperatura em Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Celsius: ", round(c, 2) )
  
  else:
    print("Opção inválida")

#Função que faz a conversão de metros para pés#
def metros():

  print("1 - Metros para Pés")
  print("2 - Pés para Metros")

  opcao = int(input("Escolha uma das opções: "))

  if opcao == 1:
    m = float(input("Digite o valor em metros: "))
    p = m * 3.280
    print("Pés: ", round(p, 2))
  
  elif opcao == 2:
    p = float(input("Digite o valor em pés: "))
    m = p / 3.280
    print("Metros: ", round(m, 2))
  
  else:
    print("Opção inválida")

#Função que faz a conversão de Quilos para libras#
def quilos():

  print("1 - Quilos para Libras")
  print("2 - Libras para quilos")

  opcao = int(input("Escolha uma das opções: "))

  if opcao == 1:
    kg = float(input("Digite o valor em quilos(Kg): "))
    lb = kg * 2.20
    print("Libras: ", round(lb, 2))

  elif opcao == 2:
    lb = float(input("Digite o valor em libras: "))
    kg = lb / 2.20
    print("Quilos: ", round(kg, 2))
  
  else:
    print("Opção inválida")

#Função que faz a conversão de quilometros para milhas#
def quilometros():
    
    print("1 - Quilometros ppara Milhas")
    print("2 - Milhas para Quilometros")

    opcao = int(input("Escolha uma das opções: "))

    if opcao == 1:
      km = float(input("Digite o valor em quilometros(Km): "))
      ml = km * 0.621
      print("Milhas: ", round (ml, 2))

    elif opcao == 2:
      ml = float(input("Digite o valor em milhas: "))
      km = ml / 0.621
      print("Quilometros: ", round(km, 2))
    
    else:
      print("Opção inválida")
#Menu pnde o usuário pode escolher o que quer converter #
def menu():
  print("=== Conversor de unidades ===")

  print("1 - Temperatura")
  print("2 - Metros")
  print("3 - Quilos")
  print("4 - Quilômetros")
  print("5 - Sair")

  opcao = int(input("Escolha uma das opções: "))

  if opcao == 1:
      temperatura()
  elif opcao == 2:
        metros()
  elif opcao == 3:
        quilos()
  elif opcao == 4:
      quilometros()
  elif opcao == 5:
    print("Encerrando programa")
    exit()
  else:
        print("Opção inválida")

#laço para fazer o usuário retornar a tela de opções#
while True:
    menu()

    # loop de validação
    while True:
        resposta = input("Deseja fazer outra conversão? (s/n): ").lower()

        if resposta == 's':
            break
        elif resposta == 'n':
            print("Encerrando programa...")
            exit()
        else:
            print("Opção inválida! Digite apenas 's' ou 'n'")