class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Lista:
    def __init__(self):
        self.root = None
        self.current = None

    def add(self, valor):
        if self.root is None:
            self.root = self.current = Node(valor)

        else:
            temp = Node(valor)
            self.current.next = temp
            self.current = temp


class Solution:
    def middleNode(self, head):
        self.search(head)
        return head

    def search(self, array, prev = None, tamanho = 0, meio = 0):
        if array is None:
            return meio // 2 + (0 if meio % 2 == 0 else 1)

        meio = self.search(array.next, array, tamanho + 1)
        if meio == tamanho:
            prev.next = array.next

        else:
            return meio


lista = Lista()
for i in range(5):
    lista.add(i + 1)

solution = Solution()
print(solution.search(lista))
