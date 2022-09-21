from statistics import correlation
from xml.dom.minidom import Identified

##Variables
EmpRegistrado = True
EmpNRegistrado = False
empleados = []

class persona:
    def __init__(self, identificacion, nombre, apellido, correo, passw):
        self.identificacionP = identificacion
        self.nombreP = nombre
        self.apellidoP = apellido
        self.correoP = correo
        self.passwordP = passw
    
class empleado(persona):
    def __init__(self, idEmpleado, nombreEmpleado, apellidoEmpleado, correoEmpleado, passEmpleado):
        self.identificacionP = idEmpleado
        self.nombreP = nombreEmpleado
        self.apellidoP = apellidoEmpleado
        self.correoP = correoEmpleado
        self.passwP = passEmpleado

class registroEmpleado:
        def cuentaEmpleado():
                print('============= Sign in ==============')
                idE = input('Identificacion: ')
                nombreE = input('Nombre: ')
                apellidoE = input('Apellido: ')
                correoE = input('Correo: ')
                passwE = input('Contraseña ')
                registro = input('¿Desea registrarse? s/n \n')

                if registro == 's':
                        empleados.append(nombreE)
                        print(f'Estos son los empleados: {empleados}')
                        return EmpRegistrado
                        
                elif registro == 'n':
                        return EmpNRegistrado

# registroEmpleado.cuentaEmpleado()

        
        

      


# def ticketSoporte():
#     MSOP = 'Mantenimiento del sistema operativo'
#     SIMR = 'Solicitud instalacion de memoria RAM'
#     SLAT = 'Solicitud de limpieza de la maquina'
#     Ticket = None
#     print(f'================================================= \n'
#             'Seleccione el tipo de soporte que requiere \n \n'
#             f'1. {MSOP} \n'
#             f'2. {SIMR} \n'
#             f'3. {SLAT} \n'
#             '================================================= \n')
#     SelSoporte = input('Digite el numero de soporte de su preferencia: ')
#     if SelSoporte == 1:



    

    