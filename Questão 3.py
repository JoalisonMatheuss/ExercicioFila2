import random
import time

class Fila:
  def __init__(self):
    self.elementos = []
    self.nome = ["Dri", "Jooj"]
    self.hora = []

  def lenght(self):
    return len(self.elementos)

  def isEmpyt(self):
    return len(self.elementos)==0

  def enqueue(self,valor):
    self.elementos.append(valor)

  def dequeue(self):
    if(not(self.isEmpyt())):
      self.elementos.pop(0)

fila = Fila()

for i in range(1,3):
  fila.enqueue("cliente: %s"%(i))

print("Hora de chegada 10:10 AM do %s"%(fila.elementos[0]))
print("Hora de chegada 10:11 AM do %s"%(fila.elementos[1]))
print(fila.elementos)
print("\n")
print("==================== '' ====================")
print("\n")

soma = 0 
for i in range(2):
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
print("Tempo médio que os consumidores levam para serem atendidos: %d minutos"%(media))
