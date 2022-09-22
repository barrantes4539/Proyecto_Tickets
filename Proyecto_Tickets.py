import empleado as Emp
import administrador as Admin


Emp.registroEmpleado.cuentaEmpleado()

if Admin.inicioSesionA.ISAdmin() == True:
    print(f'Bienvenido al sistema')
    Admin.dashboard()
# else:
#     print('Credenciales inválidas, intente de nuevo. \n')
# while Admin.inicioSesionA.ISAdmin() == False:
#     print('Credenciales inválidas, intente de nuevo. \n')
#     if Admin.inicioSesionA.ISAdmin() == True:
#         print(f'Bienvenido al sistema')
#         break







   

   




    