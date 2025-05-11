import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

def criar_local():
    nome = input("Digite o nome do local: ").strip().capitalize()
    if nome in G:
        print(f"Local '{nome}' já existe.")
    else:
        G.add_node(nome)
        print(f"Local '{nome}' criado com sucesso.")

def criar_rota():
    origem = input("Digite o local de origem: ").strip().capitalize()
    destino = input("Digite o local de destino: ").strip().capitalize()
    try:
        peso = float(input("Digite a distância entre os locais (em km): "))
        G.add_edge(origem, destino, peso=peso)
        print(f"Rota de '{origem}' até '{destino}' criada com sucesso.")
    except ValueError:
        print("Distância inválida. Use números.")

def listar_locais():
    print("\nLocais no mapa:")
    for node in G.nodes:
        print(f" - {node}")

def listar_rotas():
    print("\nRotas cadastradas:")
    for origem, destino, dados in G.edges(data=True):
        print(f" - {origem} ↔ {destino} ({dados['peso']} km)")

def plotar_grafo(highlight_path=None):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, edge_color='gray')

    edge_labels = nx.get_edge_attributes(G, 'peso')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={k: f"{v} km" for k, v in edge_labels.items()})

    # Concertar essa função
    if highlight_path:
        path_edges = list(zip(highlight_path, highlight_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title("Mapa de Rotas")
    plt.axis('off')
    plt.show()

def menor_caminho():
    origem = input("Digite o local de origem: ").strip().capitalize()
    destino = input("Digite o local de destino: ").strip().capitalize()
    try:
        caminho = nx.dijkstra_path(G, origem, destino, weight='peso')
        distancia = nx.dijkstra_path_length(G, origem, destino, weight='peso')
        print(f"Caminho mais curto: {' → '.join(caminho)} (Total: {distancia:.2f} km)")
        plotar_grafo(caminho)
    except nx.NetworkXNoPath:
        print("Não há caminho entre os locais.")
    except nx.NodeNotFound as e:
        print(f"Erro: {e}")

def menu():
    while True:
        print("\n=== Mapa de Rotas ===")
        print("1. Criar local")
        print("2. Criar rota entre locais")
        print("3. Listar locais")
        print("4. Listar rotas")
        print("5. Calcular menor caminho (Dijkstra)")
        print("6. Plotar grafo")
        print("7. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            criar_local()
        elif opcao == '2':
            criar_rota()
        elif opcao == '3':
            listar_locais()
        elif opcao == '4':
            listar_rotas()
        elif opcao == '5':
            menor_caminho()
        elif opcao == '6':
            plotar_grafo()
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
