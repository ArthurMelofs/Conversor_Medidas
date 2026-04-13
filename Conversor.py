#Função que faz a conversão celsius para fahrenheit#
def temperatura():
  c = float (input("Digite a temperatura em Celsius: "))
  f = (c * 9/5) + 32
  print("Fahrenheit: ", round(f, 2) )

#Função que faz a conversão de metros para pés#
def metros():
  m = float(input("Digite o valor em metros: "))
  p = m * 3.280
  print("Pés: ", round(p, 2))

#Função que faz a conversão de Quilos para libras#
def quilos():
  kg = float(input("Digite o valor em quilos(Kg): "))
  lb = kg * 2.20
  print("Libras: ", round(lb, 2))

#Função que faz a conversão de quilometros para milhas#
def quilometros():
    km = float(input("Digite o valor em quilometros(Km): "))
    ml = km * 0.621
    print("Milhas: ", round (ml, 2))

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