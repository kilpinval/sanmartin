class BombaInfusion():
  def __init__(self, dosis_hora):
    self.dosis_hora = 1
    if dosis_hora > 10:
      print("F to py Respects")

dosificador = BombaInfusion(1)

def aumentar_dosis():
  dosificador.dosis_hora += 1

