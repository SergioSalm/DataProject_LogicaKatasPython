from src import Excepciones
class UsuarioBanco:
    """
    Esta clase representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente
    """

    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        """
        Constructor de la clase UsuarioBanco

        Args:
            nombre (str): nombre del usuario
            saldo (float): saldo del usuario
            tiene_cuenta_corriente (boolean): Si el valor es True, significa que tiene cuenta corriente, si es False, no tiene cuenta corriente.
                                              Si no tiene cuenta corriente, el usuario no va a poder realizar ninguna operación bancaria
        """
        self.usuario = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, importe_a_retirar):
        if self.tiene_cuenta_corriente == False:
            raise Excepciones.NoCuentaBancaria(f"El usuario {self.usuario} no puede retirar dinero ya que no tiene cuenta bancaria")
        
        if self.saldo < importe_a_retirar:
            raise Excepciones.SinDineroEnBanco(f"El usuario {self.usuario} no puede retirar {importe_a_retirar}. Solamente le queda {self.saldo}")
        
        self.saldo -= importe_a_retirar
        print(f"{self.usuario} retira {importe_a_retirar}")


    def transferir_dinero(self, saldo_a_transferir, usuario_destino):
        if self.tiene_cuenta_corriente == False:
            raise Excepciones.NoCuentaBancaria(f"El usuario {self.usuario} no puede transferir dinero ya que no tiene cuenta bancaria")
        
        if usuario_destino.tiene_cuenta_corriente == False:
             raise Excepciones.NoCuentaBancaria(f"El usuario {usuario_destino.usuario} no puede recibir dinero ya que no tiene cuenta bancaria")
        
        if self.saldo < saldo_a_transferir:
            raise Excepciones.SinDineroEnBanco(f"El usuario {self.usuario} no puede transferir {saldo_a_transferir}. Solamente le queda {self.saldo}")
        
        usuario_destino.saldo += saldo_a_transferir
        self.saldo -= saldo_a_transferir
        print(f"{self.usuario} transfiere {saldo_a_transferir} a {usuario_destino.usuario}")

    def agregar_dinero(self, saldo):
        if self.tiene_cuenta_corriente == False:
            raise Excepciones.NoCuentaBancaria(f"El usuario {self.usuario} no puede agregar dinero ya que no tiene cuenta bancaria")
        
        self.saldo += saldo
        print(f"{self.usuario} ingresa {saldo}")

    def imprimir_saldo(self):
        print(f"El saldo de {self.usuario} es de {self.saldo}")