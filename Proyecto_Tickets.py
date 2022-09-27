
import empleado as emp
import administrador as admin


class sistemaPrincipal:
    def main():
        print('---------Portal---------- \n'
                    '1. Iniciar sesion \n'
                    '2. Salir')

        opcIngreso = input('Digite la opcion con la que requiere ingresar al sistema: \n')
        if opcIngreso == '1':
            emp.registroEmpleado.sistemaE()
            print("Ingrese como administrador \n \n")
            admin.inicioSesionA.sistemaA()
        elif opcIngreso == '2':
            print('Ha salido con exito del sistema')

sistemaPrincipal.main()






   

   




    