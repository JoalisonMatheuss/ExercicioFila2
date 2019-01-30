import random
import time 


class fila:
    def __init__(self):
        self.itens = []
        self.elementos = ["cliente 1", "cliente 2"]

    def enqueue(self,valor):
        self.itens.append(valor)

    def dequeue(self):
        if (not(self.isEmpty())):
            return self.itens.pop(0)

    def length(self):
        return len(self.itens)
    
    def isEmpty(self):
        return len(self.itens) == 0

f = fila()


soma = 0 
for i in range(2):
    print("Aguarde: %s"%(f.elementos[i]))
    espera = random.randint(1,6)

    tempo = time.time()
    time.sleep(espera)
    f.dequeue()
    tempo2 = time.time()

    tempoTotal = tempo2 - tempo
    print("O tempo na fila foi: %d"%(tempoTotal))

    soma += tempoTotal

media = soma/2
print("Tempo medio na fila: %d"%(media))
    


