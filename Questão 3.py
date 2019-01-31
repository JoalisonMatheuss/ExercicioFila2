import random
import time

class Fila:
  def __init__(self):
    self.elementos = []
    self.nome = ["Dri", "Jooj"]
    self.hora = ["10:10", "10:11"]

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
print("'==================== '' ===================='")
print("\n")
print("   CAT - Centro de Atendimento Telefônico")
print("\n")
print("'==================== '' ===================='")
print("\n")


for i in range(1,3):
  fila.enqueue("cliente: %s"%(i))

print(fila.elementos)
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

