

##Variables


nombre = None
apellido = None
iden = None
email = None
password = None

EmpRegistrado = True
EmpNRegistrado = False
empleados = []
ticket = []



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
        regOpcion = input('¿Desea registrarse? s/n \n')
        if regOpcion == 's':
            print('============= Sign in ==============')
            iden = input('Identificacion: ')
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            email = input('Correo: ')
            password = input('Contraseña: ')
        
            self.nombreP = nombre
            self.apellidoP = apellido
            self.correoP = email
            self.passwordP = password
            self.identificacionP = iden

            empleados.append(email)
            # empleados.append(personaEmp.nombreP)
            # print(f'Estos son los empleados: {}')
            ############################################################
            return 1
            ############################################################
        elif regOpcion == 'n':
            return 2

    def generadorTicket(self):
            
            MSOP = 'Mantenimiento del sistema operativo'
            SIMR = 'Solicitud instalacion de memoria RAM'
            SLAT = 'Solicitud de limpieza de la maquina'

            ##Terminar inicio de sesion de empleado y guardar la informacion del empleado registrado en una lista


            print('=================Inicio de Sesion=================== \n')
            ISemailEmp = input('Correo: ')
            ISpassEmp = input('Contraseña: ')
            if ISemailEmp == empleados[0]:
                print(f'================================================= \n'
                    f'Bienvenido al sistema {empleados[0]} \n'
                    'Seleccione el tipo de soporte que requiere \n \n'
                    f'1. {MSOP} \n'
                    f'2. {SIMR} \n'
                    f'3. {SLAT} \n'
                    f'4. Salir \n'
                    '================================================= \n')
                SelSoporte = input('Digite el numero de soporte de su preferencia: ')
                if SelSoporte == '1':
                    print('\n')
                    desMSOP = input('Describa su problema técnico: ')
                    print('\n \n')
                    # ticket = dict(Empleado = self.getNom(), Apellido = self.getApell(), aTecnica = MSOP, Descripcion = desMSOP)
                    # print(ticket)
                    ticket.append(self.getID())
                    ticket.append(self.getNom())
                    ticket.append(self.getApell())
                    ticket.append(MSOP)
                    ticket.append(desMSOP)
                    return 4
                elif SelSoporte == '2':
                    print('\n')
                    desMSOP = input('Describa su problema técnico: ')
                    print('\n \n')
                    # ticket = dict(Empleado = self.getNom(), Apellido = self.getApell(), aTecnica = MSOP, Descripcion = desMSOP)
                    # print(ticket)
                    ticket.append(self.getID())
                    ticket.append(self.getNom())
                    ticket.append(self.getApell())
                    ticket.append(SIMR)
                    ticket.append(desMSOP)

                elif SelSoporte == '3':
                    print('\n')
                    desMSOP = input('Describa su problema técnico: ')
                    print('\n \n')
                    # ticket = dict(Empleado = self.getNom(), Apellido = self.getApell(), aTecnica = MSOP, Descripcion = desMSOP)
                    # print(ticket)
                    ticket.append(self.getID())
                    ticket.append(self.getNom())
                    ticket.append(self.getApell())
                    ticket.append(SLAT)
                    ticket.append(desMSOP)
                elif SelSoporte == '4':
                    return print('Ha salido del sistema')

            




            
                    

##Hacer metodo de inicio de sesion para empleado

    def sistemaE():
        datosEmpleado = registroEmpleado(iden, nombre, apellido, email, password)
        if datosEmpleado.registroEmp() == 1:
            print(f'Ha sido registrado con exito \n \n')
            datosEmpleado.generadorTicket()
            return 1
        elif datosEmpleado.registroEmp() == 2:
            print('No se registro el empleado \n \n')
            return 2








      





    

    