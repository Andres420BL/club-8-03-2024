import os
os.system('cls')

#un parqueadero registra el ingreso y salida de vehiculos,que el sistema lleva un conteo de:motos,autos,bicicletas y patinetas;cada vez que ingresa un vehiculo el sistema debe sumar la categoria correspondiente ;el sistema tambien contempla la salida de vehiuculos,el sistema no debe permitir la salida del vehiculo,el sistema no debe permitir valores negativos en la cantidad.
import os
os.system('cls')

conteo_motos = 0
conteo_autos = 0
conteo_bicicletas =0
conteo_patinetas =0
var_controlbln = True
while var_controlbln == True:
    print('\tBienvenido al parqueadero Seguridad')
    opcionint =int(input('Ingrese el tipo de vehiculos \n1.Motos\n2.Auto\n3.Bicicletas\n4.Patineta\n5.Reporte\n6.Salir'))

    if opcionint == 1:  
            movimientoStr=(input('\n1.Entrada ---------------------------->\n2.Salida---------------------------->'))
            
            if movimientoStr=='1':#entrada
                cantidadint=int(input('Cantidad de Motos a ingresar---------------------------->'))
                conteo_motos += cantidadint
            if movimientoStr=='2': #salida
                cantidadint=int(input('Cantidad de Motos a salir---------------------------->'))
                
                if cantidadint <= conteo_motos:
                    conteo_motos -= cantidadint   
                else:
                    print('No hay suficientes motos en el parqueadero')
                                     
    if opcionint == 2:  
            movimientoStr=(input('\n1.Entrada ---------------------------->\n2.Salida---------------------------->'))
            
            if movimientoStr=='1':#entrada
                cantidadint=int(input('Cantidad de Autos a ingresar---------------->'))
                conteo_autos += cantidadint
            if movimientoStr=='2': #salida
                cantidadint=int(input('Cantidad de Autos a sacar------------------>'))
                if cantidadint <= conteo_autos:
                    conteo_autos -= cantidadint   
                else:
                    print('No hay suficientes autos en el parqueadero')
                                            
    if opcionint == 3:  
            movimientoStr=(input('\n1.Entrada ---------------------------->\n2.Salida---------------------------->'))
            
            if movimientoStr=='1':#entrada
                cantidadint=int(input('Cantidad de Bicicletas a ingresar---------------------------->'))
                conteo_bicicletas += cantidadint
            if movimientoStr=='2': #salida
                cantidadint=int(input('Cantidad de Bicicletas a salir---------------------------->'))
                if cantidadint <= conteo_bicicletas:
                    conteo_bicicletas -= cantidadint   
                else:
                    print('No hay suficientes Bicicletas en el parqueadero')
                    
    if opcionint == 4:  
            movimientoStr=(input('\n1.Entrada -------------------->\n2.Salida----------------------------------->'))
            
            if movimientoStr=='1':#entrada
                cantidadint=int(input('Cantidad de patinetas a ingresar---------------------------->'))
                conteo_patinetas += cantidadint
            if movimientoStr=='2': #salida
                cantidadint=int(input('Cantidad de patinetas a salir---------------------------->'))
                if cantidadint <= conteo_patinetas:
                    conteo_patinetas -= cantidadint   
                else:
                    print('No hay suficientes Patinetas en el parqueadero')
                        
    if opcionint ==5:
        print('La cantidad de motos restantes',conteo_motos)
        print('La cantidad de Autos restantes',conteo_autos)
        print('La cantidad de Bicicletas restantes',conteo_bicicletas)
        print('La cantidad de Patinetas restantes',conteo_patinetas)
    
    if opcionint ==6:
        var_controlbln= False



        
