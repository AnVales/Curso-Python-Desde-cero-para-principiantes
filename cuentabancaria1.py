from cuentabancaria import CuentaBancaria

cuenta1 = CuentaBancaria('Pepe', 2000)
print(cuenta1.depositar(10))
print(cuenta1.retirar(10))
print(cuenta1.mostrar_saldo)