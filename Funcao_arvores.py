from binarytree import build, Node

# Função para inserir valores em uma árvore
def insert_values(tree, values):
    for value in values:
        tree.insert(value)

# Função para remover um valor de uma árvore
def remove_value(tree, value):
    node = tree.search(value)
    if node:
        tree.delete(node)

# Criar árvores
tree1 = build([45, 20, 30, 60, 81, 97, 100, 7, 8, 4])
tree2 = build([15, 6, 18, 3, 7, 16, 20, 4])

# Adicionar valor a uma árvore
tree1.insert(50)
tree2.insert(10)

# Remover valor de uma árvore (exemplo com valor 30)
remove_value(tree1, 30)

# Remover valor de outra árvore (exemplo com valor 18)
remove_value(tree2, 18)

# Exibir árvores
print("Árvore 1:")
print(tree1)

print("\nÁrvore 2:")
print(tree2)