import empleado as empAdmin

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
          '3. Consultar empleados \n')
    panelAdmin = input('Digite la opcion que requiere ejecutar: ')
    
    if panelAdmin == 1:
        print('Opcion 1')
    elif panelAdmin == 2:
        print('Opcion 2')
    elif panelAdmin == 3:
        print(f'Los empleados disponibles son: {empAdmin.empleados}')

