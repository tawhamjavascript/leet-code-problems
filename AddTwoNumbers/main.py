class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Lista:
    def __init__(self, root = None):
        self.root = root
        self.cursor = root

    def add(self, valor):
        if self.cursor is None:
            self.root = self.cursor = Node(valor)
      

        else:
            temp = Node(valor)
            self.cursor.next = temp
            self.cursor = temp

    def root(self) -> Node:
        return self.root

    def __str__(self):
        string = ""
        cursor = self.root
        while True:
            if cursor is None:
                break

            else:
                string += str(cursor.val)
                cursor = cursor.next
        
class Solution:      
    def addTwoNumbers(self, l1, l2):
        listNode = Lista()
        n1 = int(self.inversor(l1))
        n2 = int(self.inversor(l2))
        n3 = str(n1 + n2)
        for i in range(len(n3) - 1, -1, -1):
            listNode.add(n3[i])

        return listNode.root()

    def inversor(self, lista, string = ""):
        if lista.next is None:
            return str(lista.val)

        else:
            string += self.inversor(lista.next, string)
            string += str(lista.val)
            return string



            
       
        
    
        

    
            
                
            
