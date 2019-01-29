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
print("******************* BANCO DO POVÃO *******************")
print("\n")
print("========================= '' =========================")
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

print("\n")
print("========================= '' =========================")
print("\n")

media1 = finalTempo1 - inicioTempo1
print("1º cliente")
print("Tempo medio na fila:", media1, "\n")

media2 = finalTempo2 - inicioTempo2
print("2º cliente")
print("Tempo medio na fila:", media2, "\n")

media3 = finalTempo3 - inicioTempo3
print("3º cliente")
print("Tempo medio na fila:", media3)


print("\n")
print("========================= '' =========================")
print("\n")

print("OBRIGADO PELA PREFERENCIA!!!!!")





