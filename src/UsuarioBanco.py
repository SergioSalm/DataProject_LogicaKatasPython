class UsuarioBanco:
    """
    Esta clase representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente
    """

    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        
        self.usuario = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, saldo):
        if self.tiene_cuenta_corriente == False:
            raise ValueError (f"El usuario {self.usuario} no puede retirar dinero ya que no tiene cuenta bancaria")
        
        self.saldo -= saldo
        print(f"{self.usuario} retira {saldo}")

    def transferir_dinero(self, saldo, usuario_destino):
        if self.tiene_cuenta_corriente == False:
            raise ValueError(f"El usuario {self.usuario} no puede transferir dinero ya que no tiene cuenta bancaria")
        
        if usuario_destino.tiene_cuenta_corriente == False:
             raise ValueError(f"El usuario {usuario_destino.usuario} no puede recibir dinero ya que no tiene cuenta bancaria")
        
        usuario_destino.saldo += saldo
        self.saldo -= saldo
        print(f"{self.usuario} transfiere {saldo} a {usuario_destino.usuario}")

    def agregar_dinero(self, saldo):
        if self.tiene_cuenta_corriente == False:
            raise ValueError(f"El usuario {self.usuario} no puede agregar dinero ya que no tiene cuenta bancaria")
        
        self.saldo += saldo
        print(f"{self.usuario} ingresa {saldo}")

    def imprimir_saldo(self):
        print(f"El saldo de {self.usuario} es de {self.saldo}")