#un parqueadero registra el ingreso y salida de vehiculos,que el sistema lleva un conteo de:motos,autos,bicicletas y patinetas;cada vez que ingresa un vehiculo el sistema debe sumar la categoria correspondiente ;el sistema tambien contempla la salida de vehiuculos,el sistema no debe permitir la salida del vehiculo,el sistema no debe permitir valores negativos en la cantidad.
import os
os.system('cls')

conteo_motos = 0
conteo_autos = 0
conteo_bicicletas =0
conteo_patinetas =0
controlBln = True
while controlBln == True :
    print('\tBienvenido al parqueadero Seguridad')
    opcion =input('Ingrese el tipo de vehiculos \n1.Motos\n2.Auto\n3.Bicicletas\n4.Patineta\n5.Reporte\n6.Salir')

    if opcion == '1':  
        cantidadint=int(input('Cantidad de Motos a ingresar---------------------------->'))
        movimientoStr=(input('\n1.Entrada ---------------------------->\n2.Salida---------------------------->'))
        if movimientoStr=='1':#entrada
                conteo_motos += cantidadint
        if movimientoStr=='2': #salida
            if  cantidadint <= conteo_motos:
                conteo_motos -= cantidadint
            else:
                print("no hay tantos vehiculos registrados")
            
            
    elif opcion=='2': 
        cantidadint=int(input('Cantidad de Autos---------------------------->'))
        movimientoStr=(input('\n1.Entrada ---------------------------->\n2.Salida---------------------------->'))
        if movimientoStr=='1':#entrada
                conteo_autos += cantidadint
        if movimientoStr=='2': #salida
            if cantidadint <= conteo_autos:
                conteo_autos -= cantidadint
            else:
                print("no hay tantos vehiculos registrados")
                                    
    elif opcion == '3':
        cantidadint=int(input('Cantidad de Bicicletas a ingresar---------------->'))
        movimientoStr=(input('\n1.Entrada ---------------------------->\n2.Salida---------------------------->'))
        if movimientoStr=='1':#entrada
                conteo_bicicletas += cantidadint
        if movimientoStr=='2': #salida
            if cantidadint <= conteo_bicicletas:
                conteo_bicicletas -= cantidadint
            else:
                print("no hay tantos vehiculos registrados")
                        
                        
    elif opcion == '4': 
        cantidadint=int(input('Cantidad de Patinetas a ingresar---------------------------->')) 
        movimientoStr=(input('\n1.Entrada ---------------------------->\n2.Salida---------------------------->'))
        if movimientoStr=='1':#entrada
            conteo_patinetas += cantidadint
        if movimientoStr=='2': #salida
            if cantidadint <= conteo_patinetas:
                conteo_patinetas -= cantidadint
            else:
                 print("no hay tantos vehiculos registrados")
                
                    
    
    elif opcion == '5':
        print ('\nla cantidad total de motos es : ',conteo_motos)
        print ('la cantidad total de carros es :', conteo_autos)
        print('la cantidad total de bicicletas  es :',conteo_bicicletas)
        print('la cantidad total de patinetas es :', conteo_patinetas)
        
    elif opcion == '6':
        controlBln = False
                        
      
       



        



            
           
