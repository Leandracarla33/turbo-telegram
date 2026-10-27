# ==========================================
# Aluna: Leandra
# Curso: Técnico em Desenvolvimento de Sistemas - SENAI/CEJO
# Descrição: Sistema de gerenciamento usando Listas (Adicionar, Listar e Remover)
# ==========================================

# A lista agora já começa com itens preenchidos! (Substitua pelos itens do seu projeto)
meus_itens = ["Teclado Mecânico", "Mouse sem fio", "Monitor 24 pol", "Headset"]

while True:
    print("\n" + "="*30)
    print("🚀 MENU DE GERENCIAMENTO 🚀")
    print("1 - Adicionar novo item")
    print("2 - Listar todos os itens")
    print("3 - Remover um item")
    print("0 - Sair")
    print("="*30)
    
    opcao = input("Escolha uma opção (0 a 3): ")
    
    if opcao == '1':
        novo_item = input("Digite o nome do novo item: ")
        meus_itens.append(novo_item)
        print(f"✅ '{novo_item}' foi adicionado com sucesso!")
        
    elif opcao == '2':
        if len(meus_itens) == 0:
            print("⚠️ A lista está vazia no momento.")
        else:
            print("\n📋 ITENS ATUALMENTE CADASTRADOS:")
            for indice, item in enumerate(meus_itens, start=1):
                print(f"{indice} - {item}")
                
    elif opcao == '3':
        if len(meus_itens) == 0:
            print("⚠️ A lista está vazia, não há o que remover.")
        else:
            item_remover = input("Digite o nome EXATO do item para remover: ")
            if item_remover in meus_itens:
                meus_itens.remove(item_remover)
                print(f"🗑️ '{item_remover}' foi removido com sucesso!")
            else:
                print("❌ Item não encontrado. Verifique se digitou corretamente (letras maiúsculas e minúsculas fazem diferença).")
                
    elif opcao == '0':
        print("Saindo do sistema. Até a próxima! 👋")
        break
        
    else:
        print("❌ Opção inválida. Digite apenas 0, 1, 2 ou 3.")
