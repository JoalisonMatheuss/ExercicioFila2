import random
import time


class fila:
    def __init__(self):
        self.itens = []
        self.valorMaximo = 0

    def enqueue(self,valor):
        self.itens.append(valor)

    def dequeue(self):
        if (not(self.isEmpty())):
            return self.itens.pop(0)

    def lenght(self):
        return len(self.itens)
    
    def isEmpty(self):
        return len(self.itens) == 0        


f = fila()


print("\n")
inicioTempo1 = time.time()
f.enqueue(1)
print("o cliente entrou na fila no tempo: ",inicioTempo1)
print(f.itens)

inicioTempo2 = time.time()
f.enqueue(2)
print("O cliente entrou na fila no tempo: ",inicioTempo2)
print(f.itens)

inicioTempo3 = time.time()
f.enqueue(3)
print("O cliente entrou na fila no tempo: ",inicioTempo3)
print(f.itens)

print("\n")
print("========================= '' =========================")
print("\n")

finalTempo1 = time.time()
f.dequeue()
print("O 1º cliente foi atendido: ",finalTempo1)
print(f.itens)


finalTempo2 = time.time()
f.dequeue()
print("O 2º cliente foi atendido: ",finalTempo2)
print(f.itens)

finalTempo3 = time.time()
f.dequeue()
print("O 3º cliente foi atendido ",finalTempo3)
print("Fila vazia",f.itens)


media1 = finalTempo1 - inicioTempo1

media2 = finalTempo2 - inicioTempo2

media3 = finalTempo3 - inicioTempo3

mediaGeral = (media1+media2+media3)/3

print("\n")
print("========================= '' =========================")
print("\n")
print("Tempo medio na fila: ", mediaGeral)
print("\n")




