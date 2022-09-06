from Grafos import graph_plot

select = 0
grafo = {}

while select != 4:

   print('''
   Gerador de Grafos

   1- Construir um novo grafo
   2- Visualizar dicionário do grafo
   3- Gerar imagem de grafo
   4- Sair
         ''')

   select = int(input('Informe sua escolha: '))

   match select:
      case 1:

         grafo = {}
         vertices = []
         add_vertices = ''
         while add_vertices != '0':

            # Adicionando vértices
            print(f'Vértices: {vertices}')
            add_vertices = input('\n Informe o nome do novo vértice (0 para prosseguir): ')
            print(add_vertices)

            # Verifica se já existe o vértice
            if(add_vertices != '0'):
               if (add_vertices in vertices):
                  print('O vértice já existe.')
                  pass
               else:
                  # Adiciona vértice
                  vertices.append(add_vertices)
                  print(f'O Vértice {add_vertices} foi adicionado.')
                  pass

         for vertice in vertices:
            # Fazendo array de vertices disponíveis
            vertices_disponiveis = []
            vertices_disponiveis.extend(vertices)
            print(f'Vertices {vertices}, Vertices disponíveis {vertices_disponiveis}')
            vertices_disponiveis.remove(vertice)

            # Atribuindo ligações entre os vértices
            print(f'Existe alguma ligação entre o vértice "{vertice}" e algum outro ({vertices_disponiveis})?')
            add_arestas = ''
            vertice_ligacoes = {vertice: []}
            while add_arestas != '0':
               print(f'Vértices disponíveis: {vertices_disponiveis}')
               add_arestas = input(f'\n Selecione vértice que é ligado ao {vertice} (0 para prosseguir): ')
               
               if (add_arestas != '0'):
                  vertices_disponiveis.remove(add_arestas)
                  vertice_ligacoes[vertice].append(add_arestas)
                  print(vertice_ligacoes)
            # Atualizando grafo com as 
            grafo.update(vertice_ligacoes)
         
         print(grafo)
         pass

      case 2:
         if (grafo != {}):
            print(f'O Grafo é: {grafo}.')
            pass
         else:
            print('O grafo não foi construído. ')

      case 3:
         img_x = int(input('Insira o tamanho horizontal da imagem em pixels (recomendado 300 ou mais): '))
         img_y = int(input('Insira o tamanho vertical da imagem em pixels (recomendado 300 ou mais): '))

         graph_plot(grafo, img_x, img_y, 'white', 'circle')
         pass

      case 4:
         print('Finalizando processo...')
         break