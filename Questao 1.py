class fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, valor):
        self.itens.append(valor)

    def dequeue(self):
        if (not(self.isEmpty())):
            return self.itens.pop(0)

    def length(self):
        return len(self.itens)
    
    def isEmpty(self):
        return len(self.itens) == 0




class pilha():
    def __init__(self):
        self.lista = []
        
    def push(self,valor):
        self.lista.append(valor)
        
    def pop(self):
        if (not(self.isEmpty())):
            return self.lista.pop()
            
    def isEmpty(self):
        return len(self.lista) == 0
    
    def length(self):
        return len(self.lista)
    
    def peek(self):
        return self.lista[-1]

lista = [1,2,3]


p = pilha()
for i in lista:
    p.push(i)
f = fila()
for i in range(p.length()):
    valor = p.pop()
    f.enqueue(valor)


print(f.itens)
