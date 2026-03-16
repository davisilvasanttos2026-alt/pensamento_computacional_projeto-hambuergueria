'''
CRUD

hamburgueria

Entregar o cardapio
escolher seu produto
pagar
retirar no caixa



'''


print(" gestão da hamburgueria")
print("1. cadastro")
print("2. cardapio")
print("3.preços")
print("4.pagamento")

while True:
    escolha = input("\nEscolha uma opção")
    if escolha == '1':
        print("gestão da hamburgeria...")
    # codigo para entrega o cardapio


    elif escolha =='0': 
        print("saindo do sistema.até logo !")
    break


if escolha == '1':
        print("fazer seu cadastro ")
        #codigo para entrgar o cardapio
elif escolha == '2':
        print("cardapio")
        #codigo fazer o pedido do cliente
elif escolha == '3':
        print("preços")
        # codigo entregar o pedido
elif escolha == '4':
        print("pagamento")
        # codigo para anotar o pagamento n


            




if escolha ==  '1' :
        print("\n--- Novo Cadastro---")
    #Dados para o cliente

        Nome = input('nome :')
        email = input("email :")
        telefone = input(" Telefone :")
        cpf = input ("CPF :")
        senha = input("Senha:")




if escolha == '2' :
      
        print("\n---cardapio---")

      
        print("🍔 X-Burger") 
        print("Pão, hambúrguer bovino  queijo mussarela, alface e tomate.")

        print("🍔 X-Salada")
        print("Pão, hambúrguer bovino  queijo, alface, tomate e maionese da casa.")

        print(" 🍔 X-Bacon")
        print("Pão, hambúrguer bovino  queijo, bacon crocante e maionese da casa")

        print("🍔 X-Egg") 
        print("Pão, hambúrguer bovino  queijo e ovo frito.")

        print("🍔 X-Tudo") 
        print("Pão, hambúrguer bovino, queijo, bacon, ovo, alface, tomate, milho, batata palha e maionese.")

        print("🔥 Burgers Especiais")

        print("🍔 Smash Burger")
        print("Pão brioche, 2 smash burgers , queijo cheddar e molho especial.")

        print("🍔 Bacon Supreme")

        print("Pão brioche, hambúrguer , cheddar, bacon crocante e cebola caramelizada.")

        print("🍔 Cheddar Duplo")

        print("Pão brioche, 2 hambúrgueres , cheddar cremoso e molho especial.")

        print("🍔 Barbecue Burger")

        print("Pão brioche, hambúrguer , queijo, bacon e molho barbecue.")

        print("🍟 Porções")

        print("🍟 Batata Frita Pequena")

        print("🍟 Batata Frita Grande")

        print("🍟 Batata com Cheddar e Bacon")

        print("🍟 Onion Rings (Anéis de cebola)")


        print("🥤 Bebidas")

        print("🥤 Refrigerante lata")

        print("🥤 Refrigerante ")

        print("🥤 Água mineral")

        print("🥤 Suco natural")


if escolha == '3' :
       
        print("\n---preços---")

print("🍔 X-Burger") 
print("15$")

print("🍔 X-Salada")
print("15$")

print(" 🍔 X-Bacon")
print("16$")

print("🍔 X-Egg") 
print("16$")

print("🍔 X-Tudo") 
print("18$")

print("\n---burguers especiais---")



print("🍔 Bacon Supreme")

print("20$")

print("🍔 Cheddar Duplo")

print("20$")

print("🍔 Barbecue Burger")

print("20$")

print("\n---Batatas---")

print("🍟 Porções")
print("22$")

print("🍟 Batata Frita Pequena")
print("10$")

print("🍟 Batata Frita Grande")
print("15$")

print("🍟 Batata com Cheddar e Bacon")
print("18$")

print("🍟 Onion Rings (Anéis de cebola)")
print("18$")

print("\n---Bebidas---")


print("🥤 Refrigerante lata")
print("8$")

print("🥤 Refrigerante ")
print("9$")

print("🥤 Água mineral")
print("5$")

print("🥤 Suco natural")
print("7$")


if escolha == "4" :
 
        valor = input('valor :')
pagamento= input("forma de pagamento :")
concluir = input("autorizar  pagamento :")