'''
CRUD

hamburgueria

Entregar o cardapio
escolher seu produto
pagar
retirar no caixa



'''


print(" gestão da hamburgueria")
print("1.cadastro")
print("2.cardapio")
print("3.preços")
print("4.pagamento")
print("5.entrega")
print("6. feedback")
print("0.sair do sistema")

while True:
    escolha = input("\nEscolha uma opção")

    if escolha == '1':
        print("gestão da hamburgeria...")
        print("fazer seu cadastro ")
        print("\n Novo Cadastro :")
        Nome = input('nome :')
        email = input("email :")
        telefone = input(" Telefone :")
        cpf = input ("CPF :")
        senha = input("Senha:")

    elif escolha == '2':
        print("cardapio")
        print("\n cardapio :")
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

    elif escolha == '3':
        print("preços")
        print("\n preços :")
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
        print("\n burguers especiais :")
        print("🍔 Bacon Supreme")
        print("20$")
        print("🍔 Cheddar Duplo")
        print("20$")
        print("🍔 Barbecue Burger")
        print("20$")
        print("\n Batatas :")
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
        print("\n Bebidas :")
        print("🥤 Refrigerante lata")
        print("8$")
        print("🥤 Refrigerante ")
        print("9$")
        print("🥤 Água mineral")
        print("5$")
        print("🥤 Suco natural")
        print("7$")

    elif escolha == '4':
        print("pagamento")
        print("\n pagamento :")
        pagamento= input("forma de pagamento (debito\credito) :")
        concluir = input("autorizar pagamento com sim ou não  :")
        concluido = print('seu pagamento foi concluido com sucesso ')

    elif escolha == '5':
        print("entrega")
        print('\n Entrega :')
        input("Confirmar sua entrega com sim ou não :")
        print('seu pedido saiu para entrega')
        print('seu pedido foi entregue com sucesso ❗')



    elif escolha == '6' :

        print('mande sua sugestão\ seu feedback')
    

        input('mande seu feedback\sua segestão para nosa loja :')
        print('obrigado pela sua sugestão\ feedback ')


    elif escolha == '0':
        print("Saindo do sistema, obrigado por visitar a nossa hamburgueria ! ")
        break