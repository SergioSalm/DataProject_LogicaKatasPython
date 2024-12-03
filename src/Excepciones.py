class ListaVacia(Exception): 
      def __init__(self, mensaje): 
            super().__init__(mensaje) 

class EdadFueraRango(Exception): 
      def __init__(self, mensaje): 
            super().__init__(mensaje)         

class NoCuentaBancaria(Exception):
      def __init__(self, mensaje): 
            super().__init__(mensaje)        

class SinDineroEnBanco(Exception):
      def __init__(self, mensaje): 
            super().__init__(mensaje)   

                    
             