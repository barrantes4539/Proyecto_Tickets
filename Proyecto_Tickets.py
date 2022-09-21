

from ast import Return, While
from msilib.schema import AdminExecuteSequence
from xml.dom.minidom import parseString

ISInvalida = False
ISValida = True

class persona:
    def __init__(self, identificacion, nombre, apellido, correo, passw):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = passw
    
class empleado(persona):
    def cuentaEmpleado(self,idEmpleado, nombreEmpleado, apellidoEmpleado, correoEmpleado, passEmpleado):
        self.identificacion = idEmpleado
        self.nombre = nombreEmpleado
        self.apellido = apellidoEmpleado
        self.correo = correoEmpleado
        self.passw = passEmpleado

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

class soporte:
    def ticketSoporte():
        MSOP = 'Mantenimiento del sistema operativo'
        SIMR = 'Solicitud instalacion de memoria RAM'
        SLAT = 'Solicitud de limpieza de la maquina'
        print(f'================================================= \n'
               'Seleccione el tipo de soporte que requiere \n \n'
               f'1. {MSOP} \n'
               f'2. {SIMR} \n'
               f'3. {SLAT} \n'
               '================================================= \n')
        SelSoporte = input('Digite el numero de soporte de su preferencia: ')



while inicioSesionA.ISAdmin() == ISInvalida:
    print('Credenciales inválidas, intente de nuevo. \n')
if inicioSesionA.ISAdmin() == ISValida:
    print(f'Bienvenido al sistema')
   

   




    