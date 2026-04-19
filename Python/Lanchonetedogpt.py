

pedidos = []
continuar = "s"

while continuar == "s":

    print("\n=== MENU ===")
    print("1 - Hambúrguer (R$20)")
    print("2 - Pizza (R$15)")
    print("3 - Refrigerante (R$5)")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = "Hambúrguer"
        preco = 20
    elif opcao == "2":
        item = "Pizza"
        preco = 15
    elif opcao == "3":
        item = "Refrigerante"
        preco = 5
    else:
        print("Opção inválida!")
        continue

    quantidade = int(input("Digite a quantidade: "))
    total = quantidade * preco

    print(f"Você pediu {quantidade}x {item}")
    print(f"Total: R$ {total}")

    pedidos.append((item, quantidade, total))

    continuar = input("Deseja fazer outro pedido? (s/n): ")

# Resumo final
print("\n=== RESUMO DO PEDIDO ===")

total_geral = 0

for pedido in pedidos:
    print(f"{pedido[0]} - Quantidade: {pedido[1]} - Valor: R$ {pedido[2]}")
    total_geral += pedido[2]

print(f"Total geral: R$ {total_geral}")
print("Obrigado pela preferência!")