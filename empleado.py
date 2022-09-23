import re
from statistics import correlation
from xml.dom.minidom import Identified

##Variables
EmpRegistrado = True
EmpNRegistrado = False
empleados = []
ticket = None


print('============= Sign in ==============')
iden = input('Identificacion: ')
nombre = input('Nombre: ')
apellido = input('Apellido: ')
email = input('Correo: ')
password = input('Contraseña: ')

class persona:
    def __init__(self, identificacion, nombre, apellido, correo, passw):
        self.identificacionP = identificacion
        self.nombreP = nombre
        self.apellidoP = apellido
        self.correoP = correo
        self.passwordP = passw

    def getID(self):
        return f'{self.identificacionP}'
    def getNom(self):
        return f'{self.nombreP}'
    def getApell(self):
        return f'{self.apellidoP}'
    def getEmail(self):
        return f'{self.correoP}'
    def getPass(self):
        return f'{self.passwordP}'

class registroEmpleado(persona):

    def empleado(self, identificacion, nombre, apellido, email, password):
        super().__init__(identificacion, nombre, apellido, email, password)
    
    def registroEmp(self):
        
        self.nombreP = nombre
        self.apellidoP = apellido
        self.correoP = email
        self.passwordP = password
        self.identificacionP = iden
        registro = input('¿Desea registrarse? s/n \n')
        if registro == 's':
            # empleados.append(personaEmp.nombreP)
            # print(f'Estos son los empleados: {}')
            ############################################################
            print(f'Ha sido registrado con exito \n')
            return EmpRegistrado
            ############################################################
        elif registro == 'n':
            return EmpNRegistrado


# class ISEmpleado(registroEmpleado):

    def generadorTicket(self):
            
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
            if SelSoporte == '1':
                    print('\n \n')
                    desMSOP = input('Describa su problema técnico: ')


                    ticket = dict(Empleado = self.getNom(), Apellido = self.getApell(), Descripcion = desMSOP)
                    
            print(f'{ticket}')

    def sistemaE():
        datosEmpleado = registroEmpleado(iden, nombre, apellido, email, password)
        if datosEmpleado.registroEmp() == EmpRegistrado:
            print(f'Ha sido registrado con exito \n')
            datosEmpleado.generadorTicket()
        elif datosEmpleado.registroEmp() == EmpNRegistrado:
            print('No se registro el empleado')


# persona.getID()
sisEmp = registroEmpleado.sistemaE()
sisEmp

      





    

    