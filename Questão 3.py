import random
import time

class Fila:
  def __init__(self):
    self.itens = []
    self.nome = ["Dri", "Jooj"]
    self.hora = ["10:10", "10:11"]

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
print("'==================== '' ===================='")
print("\n")
print("   CAT - Centro de Atendimento Telefônico")
print("\n")
print("'==================== '' ===================='")
print("\n")


for i in range(1,3):
  fila.enqueue("cliente: %s"%(i))

print(fila.itens)
print("\n")
print("'============== Fila de Espera =============='")
print("\n")

soma = 0 
for i in range(2):
  print("%s chegou de %s AM"%(fila.nome[i],fila.hora[i]))
  print("%s em espera para ser atendido"%(fila.nome[i]))

  espera = random.randint(1,6)

  tempo = time.time()
  time.sleep(espera)
  fila.dequeue()
  tempo2 = time.time()

  tempoTotal = tempo2 - tempo

  print("Tempo de espera até ser atentido: %d minutos \n"%(tempoTotal))

  soma += tempoTotal


media = soma/2

print("\n")
print("==================== '' ====================")
print("\n")
print("Tempo médio que os consumidores levaram para serem atendidos: %d minutos"%(media))
