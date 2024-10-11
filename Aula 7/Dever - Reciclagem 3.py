def main():
    print("Bem-vindo ao programa de reciclagem!")

    papel = 0
    plastico = 0
    vidro = 0
    metal = 0
    organico = 0
    nao_reciclavel = 0

    while True:
        material = input("Que material você deseja reciclar? (papel, plástico, vidro, metal, orgânico ou não reciclável): ").strip().lower()

        if material == 'papel':
            print("Descarte na lixeira azul.")
            papel += 1
        elif material == 'plástico':
            print("Descarte na lixeira vermelha.")
            plastico += 1
        elif material == 'vidro':
            print("Descarte na lixeira verde.")
            vidro += 1
        elif material == 'metal':
            print("Descarte na lixeira amarela.")
            metal += 1
        elif material == 'orgânico':
            print("Descarte na lixeira marrom.")
            organico += 1
        elif material == 'não reciclável':
            print("Descarte na lixeira cinza.")
            nao_reciclavel += 1
        else:
            print("Erro! Material não reconhecido.")

        continuar = input("Deseja continuar reciclando? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\nResumo da reciclagem:")
    print(f"Papel: {papel}")
    print(f"Plástico: {plastico}")
    print(f"Vidro: {vidro}")
    print(f"Metal: {metal}")
    print(f"Orgânico: {organico}")
    print(f"Não reciclável: {nao_reciclavel}")

    print("Obrigado por contribuir com a reciclagem!")

if __name__ == "__main__":
    main()
    