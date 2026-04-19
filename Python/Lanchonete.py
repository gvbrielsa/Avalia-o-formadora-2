cardapio = {
    1: {"nome": "Hambúrguer",          "preco": 12.00},
    2: {"nome": "Pizza 40cm",     "preco": 70.00},
    3: {"nome": "Açai 700ml",        "preco": 15.00},
    4: {"nome": "Refrigerante 350ml",  "preco": 7.00}
}

def mostrar_cardapio():
    print("\n" + "="*45)
    print("           CARDÁPIO DA LANCHONETE")
    print("="*45)
    for codigo, item in cardapio.items():
        print(f"{codigo:2d} - {item['nome']:20} R$ {item['preco']:6.2f}")
    print("="*45)


def main():
    pedido = []
    total = 0.0

    print("Bem-vindo à Lanchonete!\n")

    while True:
        mostrar_cardapio()
        
        try:
            codigo = int(input("\nDigite o código do produto (0 para finalizar): "))
            
            if codigo == 0:
                break
                
            if codigo not in cardapio:
                print("❌ Código inválido!")
                continue
                
            quantidade = int(input(f"Quantidade de '{cardapio[codigo]['nome']}'? "))
            
            if quantidade <= 0:
                print("❌ Quantidade deve ser maior que zero.")
                continue
                
            item = cardapio[codigo]
            subtotal = item["preco"] * quantidade
            
            pedido.append({
                "nome": item["nome"],
                "quantidade": quantidade,
                "preco_unitario": item["preco"],
                "subtotal": subtotal
            })
            
            total += subtotal
            print(f"✅ {quantidade}x {item['nome']} adicionado(a)!\n")
            
        except ValueError:
            print("❌ Por favor, digite apenas números.\n")
        except Exception:
            print("❌ Ocorreu um erro. Tente novamente.\n")

    # ================= TELA DE EXIBIÇÃO DOS ITENS =================
    print("\n" + "="*55)
    print("           ITENS DO SEU PEDIDO")
    print("="*55)
    
    if not pedido:
        print("Nenhum produto foi selecionado.")
    else:
        for item in pedido:
            print(f"{item['quantidade']:2d}x  {item['nome']:22} "
                  f"R$ {item['preco_unitario']:6.2f}   →   R$ {item['subtotal']:6.2f}")
    
    print("="*55)

   
    if pedido:
        for item in pedido:
            print(f"{item['quantidade']:2d}x {item['nome']:<25} "
                  f"R$ {item['subtotal']:6.2f}")
    
    print("-"*55)
    print(f"{'TOTAL A PAGAR':<35} R$ {total:8.2f}")
    print("="*55)
    print("Obrigado pela preferência! Volte sempre!\n")


# ===================== EXECUÇÃO =====================
if __name__ == "__main__":
    main()