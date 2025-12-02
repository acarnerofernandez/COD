import Personaje


if __main__ == "__main__":
  # Creación de dos OBJETOS (instancias) distintos de la clase Personaje
  guerrero = Personaje("Aragorn", 100)
  mago = Personaje("Gandalf", 80)

  print("-" * 30)

  # Interacción y acceso a atributos
  print(guerrero.saludar())

  # Aplicar un método al objeto mago (solo afecta al mago)
  mago.recibir_dano(15)

  # Aplicar un método al objeto guerrero (solo afecta al guerrero)
  guerrero.recibir_dano(5)

  print("-" * 30)
  # Se comprueba que cada objeto tiene su propio estado (vida)
  print(f"Estado final - Guerrero vida: {guerrero.vida}")
  print(f"Estado final - Mago vida: {mago.vida}")



