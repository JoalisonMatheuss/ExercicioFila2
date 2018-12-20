class fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, valor):
        self.itens.append(valor)

    def dequeue(self):
        if (not(self.isEmpty())):
            return self.itens.pop(0)

    def lenght(self):
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
    
    def lenght(self):
        return len(lista.self)
    
    def peek(self):
        return self.lista[-1]


    
f = fila()
f.enqueue(1)
f.enqueue(2)
f.enqueue(3) 

print("Lista normal -->",f.itens)
aux = 0 
p = pilha()
for i in range(f.lenght()):
    aux = f.dequeue()
    p.push(aux)
    
for i in range(f.lenght()):
    aux = p.pop()
    f.enqueue(aux)

print("Fila vazia -->",f.itens)
print("Fila na pilha -->",p.lista)
