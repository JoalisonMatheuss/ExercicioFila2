import random
import time 


class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self,valor):
        self.itens.append(valor)

    def dequeue(self):
        if (not(self.isEmpty())):
            return self.itens.pop(0)

    def length(self):
        return len(self.itens)
    
    def isEmpty(self):
        return len(self.itens) == 0

fila = Fila()
print("\n")
print("===================== '' =====================")
print("\n")


for j in range(1,3):
    fila.enqueue("documento: %s"%(j))
print(fila.itens)

print("\n")
print("=============== Fila de Espera ===============")
print("\n")


for k in range(len(fila.itens)):
    print("Documento: %d em espera para ser impresso"%(k+1))
    print("impressão...")

    espera = random.randint(1,6)

    tempo = time.time()
    time.sleep(espera)
    fila.dequeue()
    tempo2 = time.time()

    tempoTotal = tempo2 - tempo

    print("tempo de espera para executar o trabalho impresso: %d segundos \n"%(tempoTotal))

print(fila.itens)





    
