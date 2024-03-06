class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)


# Завдання 1
def find_max(node):
    if node is None:
        return None
    while node.right is not None:
        node = node.right
    return node.key


# Завдання 2
def find_min(node):
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node.key


# Завдання 3
def sum_values(node):
    if node is None:
        return 0
    return node.key + sum_values(node.left) + sum_values(node.right)


# Створення AVL-дерева
avl = AVLTree()
root = None
keys = [20, 30, 40, 50, 25, 15]
for key in keys:
    root = avl.insert(root, key)

# Виклик функцій
print("Максимальне значення: ", find_max(root))
print("Мінімальне значення: ", find_min(root))
print("Сума всіх значень: ", sum_values(root))
