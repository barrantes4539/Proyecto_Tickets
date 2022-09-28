

import sys
import empleado as e


ISInvalida = False
ISValida = True

class admin:
        idAdmin = '305390775'
        nombreAdmin = 'Kevin'
        apellidoAdmin = 'Barrantes'
        correoAdmin = 'kevin.barrantes.montoya@cuc.cr'
        passAdmin = 'Progra3Admin'

class inicioSesionA(admin):
    
    def ISAdmin():
        print('============= LOGIN ================')
        correoAdmin = input('Correo: ')
        passAdmin = input('Contraseña: ')
        if passAdmin != admin.passAdmin or correoAdmin != admin.correoAdmin:
            return ISInvalida
        else:
            return ISValida
    
    def dashboard():
        
        print('Bienvenido Kevin \n'
            'Seleccione la acción de su preferencia \n'
            '1. Atender tickets activos \n'
            '2. Consultar tickets cerrados \n'
            '3. Consultar empleados \n'
            '4. Salir')
        panelAdmin = input('Digite la opcion que requiere ejecutar: ')
        
        if panelAdmin == '1':
            print(f'Tickets activos: {e.ticket}')
        elif panelAdmin == '2':
            print('Opcion 2')
        elif panelAdmin == '3':
            print(f'Los empleados disponibles son: {e.empleados}')
        elif panelAdmin == '4':
            return 4


    def sistemaA():
        if inicioSesionA.ISAdmin() == ISValida:
            print(f'Bienvenido al sistema de administrador {admin.nombreAdmin} \n')
            if inicioSesionA.dashboard() == 4:
                return 1
        elif inicioSesionA.ISAdmin() == ISInvalida:
            print('No se pudo accesar al sistema \n')
            return 2

# sysAdmin = inicioSesionA.sistemaA()
# sysAdmin



