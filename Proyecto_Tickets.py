import empleado as emp
import administrador as admin

class main:
    def pageMain():
        print('---------Portal---------- \n'
              '1. Empleado \n'
              '2. Administrador \n '
              '3. Registrarse(empleado)')
        opcIngreso = input('Digite la opcion con la que requiere ingresar al sistema: ')
        if opcIngreso == '1':
            emp.registroEmpleado.generadorTicket()
            return 1
        elif opcIngreso == '2':
            admin.inicioSesionA.dashboard()
            return 2
        elif opcIngreso == '3':
            emp.registroEmpleado.sistemaE()
            return 3
            









   

   




    