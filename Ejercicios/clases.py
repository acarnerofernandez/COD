class Personaje:
    """
    Clase base para crear objetos Personaje. Representa el MOLDE.
    Define las características (atributos) y comportamientos (métodos)
    comunes a todos los personajes.
    """

    # Método Constructor: Se llama automáticamente al crear un nuevo objeto.
    # Inicializa los atributos de la instancia.
    def __init__(self, nombre, vida):
        self.nombre = nombre  # Atributo: Nombre del personaje
        self.vida = vida  # Atributo: Puntos de vida actuales
        print(f"*** Nuevo personaje creado: {self.nombre} ***")

    # Método simple: Muestra un comportamiento del personaje.
    def saludar(self):
        return f"Hola, soy {self.nombre} y mi vida actual es {self.vida}."

    # Método interactivo: Modifica el estado (atributo) del objeto.
    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        # Aseguramos que la vida no baje de cero
        if self.vida < 0:
            self.vida = 0
        print(f"¡{self.nombre} ha recibido {cantidad} de daño! Vida restante: {self.vida}")