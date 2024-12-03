class Arbol:
    """
    Clase para representar la estructura de un árbol.
    El árbol unicamente puede tener un tronco cuya longitud puede aumentar.
    El árbol puede tener una o varías ramas, y cada rama va a tener una longitud propia.
    El atributo rama va a se una lista que contenga una  sublista. Esta sublista tendrá el número de rama y su longitud.
    De esta manera, si borramos la rama 2, la rama 3 y superiores, conservan el número de rama, y si se busca la rama 2, ésta ya no existe.
    """

    def __init__(self):
        """
            Constructor de la clase Árbol
        """
                        
        self.tronco = 1
        self.ramas = []
        self.numero_ramas = 0
        
    def crecer_tronco(self):
        """
        Método para aumentar la longitud del tronco en una unidad.
        No le pasamos ningún parámetro, ya que las especificaciones indican que la función aumenta la longitud en una unidad
        """
        self.tronco += 1

    def nueva_rama(self):
        """
        Método para agregar una nueva rama de longitud 1 a la lista de ramas
        No le pasamos ningún parámetro, ya que las especificaciones indican que la función crea una nueva rama de longitud 1
        """
        self.numero_ramas += 1
     
        rama_nueva = [self.numero_ramas,1]

        self.ramas.append(rama_nueva)

    def crecer_ramas(self):
        """
        Método para aumentar en una unidad la longitud de todas las ramas existentes.
        No le pasamos ningún parámetro, ya que las especificaciones indican que la función debe aumentar en una unidad la longitud de todas las ramas existentes
        """
        
        for rama in self.ramas:
            rama[1] = rama[1]+1


    def quitar_rama(self, rama_a_eliminar):
        """
        Método para eliminar una rama en una posición específica
        
        Args:
            rama_a_eliminar (int): número de la rama del árbol a eliminar
        """
        
        for rama in self.ramas:
            if rama[0] == rama_a_eliminar:
                self.ramas.remove(rama) 
   

        
    def info_arbol(self):
        """
        Método que devuelve la información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas
        """
        print ("Información del árbol creado:")
        print (f"Longitud del tronco: {self.tronco}.")
        print (f"Número de ramas: {len(self.ramas)}")

        if (len(self.ramas)):
            print ("Longitud de las ramas: ")
               
            for rama in self.ramas:
                print(f"Rama {rama[0]},  tiene una longitud de {rama[1]}")