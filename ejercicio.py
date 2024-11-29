from src import UsuarioBanco

try:
    usuario1 = UsuarioBanco.UsuarioBanco("Alicia", 100, False)
    usuario2 = UsuarioBanco.UsuarioBanco("Bob", 50, True)

    usuario2.agregar_dinero(20)
    usuario2.imprimir_saldo()

    usuario2.transferir_dinero(50, usuario1)
    usuario2.imprimir_saldo()
    usuario1.imprimir_saldo()

    usuario1.retirar_dinero(50)
    usuario1.imprimir_saldo()
except ValueError as e:
    print(e)