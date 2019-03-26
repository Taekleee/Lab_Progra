#BLOQUE DE DEFINICION

import numpy

from PIL import Image


# LA FUNCION SE ENCARGA DE ABRIR LA IMAGEN QUE SE ENCUENTRA EN LA MISMA CARPETA
#QUE EL PROGRAMA Y LA TRASNFORMA POR MEDIO DE NUMPY A MATRIZ.
def funcionAbrirImagen(imagen):
    imagen= imagen+".bmp"
    abrirImagen= Image.open(imagen)
    matriz= numpy.array(abrirImagen)
    abrirImagen.show()
    
    return matriz

#LA FUNCION MENU SE UTILIZA PARA MOSTRAR AL USUARIO LAS FUNCIONES QUE PUEDE
#REALIZAR ELEGIENDO UNO DE SUS VALORES, COMO ES FUNCION PUEDE SER LLAMADA
#AL INICIAR LA EDICION Y NUEVAMENTE, SI EL USUARIO DESEA REALIZAR OTRA MODIFICACION
def funcionMenu():
    print '''Elija la modificacion que desea realizar a la imagen
    1.-Escala de grises
    2.-Rotar Imagen
    3.-Imagen Embossing
    4.-Recortar Imagen
    5.-Margen
    6.-Ampliar o reducir
    7.-Contraste '''

#LA FUNCION GRIS TRANSFORMA LA IMAGEN INGRESADA A UNA ESCALA DE GRISES,MEDIANTE EL
#CALCULO DEL PROMEDIO DE LOS VALORES DE LOS PIXELES, Y LOS INSERTA EN LA MATRIZ
def funcionGris(matriz):
    print "Se esta generando su imagen, por favor espere..."
    for fila in matriz:
        for pixel in fila:
            suma= int(pixel[0])+int(pixel[1])+int(pixel[2])
            promedio= suma/3
            pixel[0]=promedio
            pixel[1]=promedio
            pixel[2]=promedio
   
    return matriz

#LA FUNCION INGRESA LA MATRIZ SE GENERA UNA
#LISTA MEDIANTE EL COMANDO SHAPE QUE NOS INDICA LOS VALORES DE EL ANCHO Y LARGO DE LA
#IMAGEN, Y QUE SON INTERCAMBIADOS PARA GENERAR UNA MATRIZ SOLO CON CEROS, A LA CUAL SE
#INGRESAN LOS DATOS ANTERIORES, LUEGO SE CONVIERTE EN ARRAY. GIRA EN SENTIDO ANTIHORARIO.

def funcionRotarImagen(matriz):
        med=  list(matriz.shape)
        i= med[1]
        j= med[0]
        k= med[2]
        matrizRotada= numpy.zeros((i,j,k))
        m=i-1
        f=0
        l=0
        while f<(i-1):
            while l<(j-1)and m>0:
                matrizRotada[f][l]= matriz[l][m]
                l+=1
               
            f+=1
            m-=1 
            l=0
        print "Se esta generando su imagen, por favor espere..."          
        matrizRotada= numpy.array(matrizRotada)
        return matrizRotada


#INGRESA LA MATRIZ EN ESCALA DE GRISES, LUEGO TOMA EL PRIMER BIT DE CADA PIXEL,
#LO APROXIMA DE ACUERDO A UN RANGO DEFINIDO POR EL PROGRAMADOR Y CAMBIA EL BIT 0,1 Y 2 POR
#ESE VALOR
def funcionEmbossing(matriz):
    for lista in matriz:
        for pixel in lista:
            i= pixel[0]
            if i<30:
                pixel[0]=0
                pixel[1]=0
                pixel[2]=0
            elif i>30 and i<104:
                pixel[0]=40
                pixel[1]=40
                pixel[2]=40
            elif i>104 and i<150:
                pixel[0]=120
                pixel[1]=120
                pixel[2]=120
            elif i>150 and i<200:
                pixel[0]=180
                pixel[1]=180
                pixel[2]=180
            elif i>200 and i<=255:
                pixel[0]=255
                pixel[1]=255
                pixel[2]=255
                
    return matriz

#LA FUNCION INGRESA LA MATRIZ Y SOLICITA AL USUARIO INGRESAR LAS MEDIDAS QUE DESEA
#CORTAR, LAS CUALES SE RESTAN A LA MEDIDA ORIGINAL (EL ANCHO ES RESTADO CON EL VALOR
#IZQUIERDO Y DERECHO Y EL ALTO CON EL VALOR INFERIOR Y SUPERIOR) PARA GENERAR UNA NUEVA
#MATRIZ DE CEROS CON ESAS DIMENSIONES, LUEGO, UTILIZANDO EL LIMITE IZQUIERDO Y SUPERIOR
#COMIENZA A REEMPLAZAR LOS VALORES DE LA MATRIZ 0 
def funcionRecortarImagen(matriz,i,j,k,iz,der,sup,inf):
        print "Se esta generando su imagen, por favor espere..."
        m= j-(iz+der)
        f= i-(sup+inf)
        d= iz
        print "Su imagen  sera de: ", f,"x",m
        nuevaMatriz= numpy.zeros((f,m,k))
        a=0
        b=0
        
        while a< (f-1): # REALIZA EL PROCESO HASTA LLEGAR A LA MEDIDA INFERIOR
            while b<=(m-1) : #REALIZA EL PROCESO HASTA LLEGAR A LA MEDIDA SUPERIOR
                nuevaMatriz[a][b]=matriz[sup][iz]
                iz+=1
                b+=1
            a+=1
            sup+=1
            iz= d
            b=0
        
        return nuevaMatriz


#LA ENTRADA ES LA MATRIZ, LA SALIDA ES UNA NUEVA MATRIZ AMPLIADA AL DOBLE
    
def funcionAmpliar(matriz):
     print "Se esta generando su imagen, por favor espere..."
     med=  list(matriz.shape)
     i= med[0]*2 #MULTIPLICA EL LARGO Y EL ANCHO AL DOBLE PARA GENERAR UNA NUEVA MATRIZ.
     j= med[1]*2
     k= med[2]
     nuevaMatriz= numpy.zeros((i,j,k))
     l=0
     m=0
     a=0
     b=0
     c=0
     d=0
     while a<i-1: #ITERA HASTA EL LARGO DE LA NUEVA MATRIZ -1
         while b<j-1 and c<2: #C Y D AYUDAN A QUE SE COPIE DOS  VECES EL PIXEL DE LA MATRIZ EN LA NUEVA MATRIZ
             #ITERA HASTA EL ANCHO DE LA NUEVAMATRIZ-1
             nuevaMatriz[a][b]=matriz[l][m]
             b+=1
             c+=1
             while c==2:
                m+=1
                c=0
         b=0
         m=0
         a+=1
         d+=1
         while d==2:
            l+=1
            d=0
      
     return nuevaMatriz

#INGRESA LA MATRIZ, SE GENERA UNA NUEVA MATRIZ REDUCIENDO A LA MITAD LA MEDIDA DE ANCHO Y LARGO
#Y A LA NUEVA MATRIZ AGREGA PIXEL POR MEDIO (NO SE DEFORMA LA IMAGEN PORQUE REDUCE EN PROPORCION 1:2)
def funcionReducir(matriz):
    print "Se esta generando su imagen, por favor espere..."
    med=  list(matriz.shape)
    i= med[0]/2
    j= med[1]/2
    k= med[2]
    nuevaMatriz= numpy.zeros((i,j,k))
    l=0
    m=0
    a=0
    b=0
    while a<i-1:
        while b<j-1:
             nuevaMatriz[a][b]=matriz[l][m]
             b+=1
             m+=2
        a+=1
        b=0
        l+=2
        m=0
    return nuevaMatriz

#EL MARCO LO DEFINIMOS DE 60 PIXELES (30 EN CADA EXTREMO), PRIMERO SE INGRESO UNA IMAGEN COLOR CAFE
#PARA OBTENER LOS VALORES DE LOS PIXELES QUE SON (46,13,4), SE GENERA UNA NUEVA MATRIZ CON LAS MEDIDAS
#ANTERIORES + 60 Y UNA MATRIZ DE CERO COMO REFERENCIA
def funcionMarco(matriz,color):
    print "Se esta generando su imagen, por favor espere..."
    med=  list(matriz.shape)
    i= med[0]+60
    j= med[1]+60
    k= med[2]
    nuevaMatriz= numpy.zeros((i,j,k))
    matrizAux= numpy.zeros((i,j,k))
    if color=="1":
        for lista in nuevaMatriz:
           for pixel in lista:
                pixel[0]= int(192)
                pixel[1]= int(154)
                pixel[2]= int(107)
    elif color=="2":
        for lista in nuevaMatriz:
           for pixel in lista:
                pixel[0]= int(188)
                pixel[1]= int(36)
                pixel[2]= int(24)
    elif color=="3":
        for lista in nuevaMatriz:
           for pixel in lista:
                pixel[0]= int(0)
                pixel[1]= int(113)
                pixel[2]= int(193)
    elif color=="4":
        for lista in nuevaMatriz:
           for pixel in lista:
                pixel[0]= int(89)
                pixel[1]= int(150)
                pixel[2]= int(47)
    for lista in nuevaMatriz:
        l=0
        m=0
        a=i-1
        s=j-1
        while l<60 and m<60:
#LUEGO PARA CADA LISTA EN LA NUEVA MATRIZ, SE INTERCAMBIAN LOS PIXELES DE LAS ESQUINAS HASTA EL VALOR
#DE 59 (PARA GENERAR LA LINEA NEGRA)
           nuevaMatriz[l][m]=matrizAux[l][m]
           nuevaMatriz[m][s]=matrizAux[l][m]
           nuevaMatriz[a][s]=matrizAux[l][m]
           nuevaMatriz[a][l]=matrizAux[l][m]
           a-=1
           s-=1
           l+=1
           m+=1
    
    b=0
    c=0
    d=30
    e=30
#DESDE EL PUNTO (30,30) HASTA EL ANCHO Y LARGO -60 SE INTERCAMBIAN LOS PIXELES DE LA MATRIZ CON
#LOS DE LA NUEVA MATRIZ(PARA PEGAR SOBRE EL MARCO REALIZADO LA IMAGEN)
    while b<i-60:
        while c<j-60:
            nuevaMatriz[d][e]=matriz[b][c]
            e+=1
            c+=1
        b+=1
        d+=1
        e=30
        c=0
    return nuevaMatriz
#RESTA 255 A CADA PIXEL PARA GENERAR EL COLOR "INVERSO", INGRESA LA MATRIZ Y SALE LA MATRIZ MODIFICADA
def funcionContraste(matriz):
    print "Se esta generando su imagen, por favor espere..."
    for fila in matriz:
        for pixel in fila:
            pixel[0]= int(255-pixel[0])
            pixel[1]=int(255-pixel[1])
            pixel[2]=int(255-pixel[2])
    return matriz

#LA FUNCION DEVOLVER IMAGEN PIDE LA MATRIZ Y EL NOMBRE CON EL QUE SE QUIERE GUARDAR
#LA IMAGEN, EL COMANDO .SAVE GUARDA LA IMAGEN Y .CLIP PERMITE QUE EL RANGO DE LOS
#PIXELES SE ENCUENTRE ENTRE 0 Y 255, LOS CUALES SON LOS VALORES QUE PUEDE TENER
#UN COLOR, ASTYPE ( uint8: ENTEROS DE 8 BITS EN EL RANGO DE [0,255])) Y SE DEBE GUARDAR EN RGB

def funcionDevolverImagen(matriz, nombreNuevaImagen):
    matrizSalida=numpy.array(matriz)
    nuevaImagen = Image.fromarray(matrizSalida.clip(0,255).astype('uint8'), 'RGB')
    nuevaImagen.save(nombreNuevaImagen)
    
    print  "La imagen a sido guardada exitosamente  :) "


        
#BLOQUE PRINCIPAL
p_1=True
print '''BIENVENIDO AL EDITOR DE IMAGENES
INSTRUCCIONES:

1)Ingrese el nombre de la imagen que quiere editar (debe estar en la misma carpeta que el programa)
2)Elija la opcion que desea realizar\n\n'''

#SE LE SOLICITA EL NOMBRE DEL ARCHIVO AL USUARIO Y SE ABRE LA IMAGEN
while p_1:
    try:
        #LA FUNCION TRY Y EXCEPT PERMITE VOLVER A EJECUTAR EL CODIGO CUANDO SE ENCUENTRE UN ERROR EN ESPECIFICO. AYUDAN
        #A UN MEJOR FUNCIONAMIENTO DEL PROGRAMA Y PERMITEN AL USUARIO EQUIVOCARSE SIN BOTAR EL PROGRAMA
        imagen=raw_input("Ingrese el nombre de la imagen que desea editar: ")
        abrirImagen= funcionAbrirImagen(imagen)
        #SE GENERA EL MENU PARA QUE LA IMAGEN SEA GUARDADA AL FINAL DE TODAS LAS MODIFICACIONES QUE DESEA REALIZAR
        #EL USUARIO
        menu1= True
        while menu1==True :
            funcionMenu()
            opcionElegida= raw_input("\n\nIngrese el numero de edicion que desea: ")
            #AL TERMINAR CADA FUNCION, LA VARIABLE ABRIR IMAGEN QUE CONTIENE LA MATRIZ SE MODIFICA POR LA OBTENIDA MEDIANTE
            #ALGUNA DE LAS FUNCIONES PARA PODER VOLVER A MODIFICAR DENTRO DE ESTA
            if opcionElegida== "1":
                imagenGris= funcionGris(abrirImagen)
                aux=1
                menu1=False
            elif opcionElegida=="2":
               
               menu= True
               while menu==True:
                    grados= raw_input("En cuantos grados desea rotar la imagen?: \n1)90\n2)180\n3)270\n")
                    if grados=="1":
                        imagenRotada= funcionRotarImagen(abrirImagen)
                        abrirImagen= imagenRotada
                        menu= False
                    elif grados=="2":
                        imagenRotada= funcionRotarImagen(abrirImagen)
                        segundaRotacion= funcionRotarImagen(imagenRotada)
                        abrirImagen= segundaRotacion
                        menu= False
                    elif grados=="3":
                        imagenRotada= funcionRotarImagen(abrirImagen)
                        segundaRotacion= funcionRotarImagen(imagenRotada)
                        terceraRotacion= funcionRotarImagen(segundaRotacion)
                        abrirImagen=terceraRotacion
                        menu= False
                    else:
                        print "Ingrese una opcion valida"
                        menu= True
                    aux=2
                    menu1=False 
                
            elif opcionElegida=="3":
                imagenGris= funcionGris(abrirImagen)
                imagenEmbossing= funcionEmbossing(imagenGris)
                aux=3
                menu1=False
                abrirImagen=imagenEmbossing

                
            elif opcionElegida=="4":
                med=  list(abrirImagen.shape)
                i_1= med[0]
                j_1= med[1]
                k_1= med[2]
                aux_a=True
                while aux_a:
                    try:
                        print "Ingrese area que desea recortar del extremo izquierdo (debe ser menor a:",j_1,")\n"
                        iz= input("valor izquierdo: ")
                        if int(iz)>j_1:
                            print "Ingrese un valor valido"
                            aux_a=True
                        else:
                            aux_a=False
                    except (NameError,SyntaxError):
                        print "Ingrese un valor valido"
                        
                aux_b=True
                while  aux_b:
                    try:
                        print "Ingrese area que desea recortar del extremo derecho (debe ser menor a:",j_1- iz,")\n"
                        der= input("valor derecho: ")
                        if int(der)>(j_1- iz):
                            print "Ingrese un valor valido"
                            aux_b=True
                        else:
                            aux_b=False
                    except (NameError,SyntaxError):
                        print "Ingrese un valor valido"
                aux_c= True
                while aux_c:
                    try:
                        print "Ingrese area que desea recortar del extremo superior (debe ser menor a:",i_1,")\n"
                        sup= input("valor superior: ")
                        if int(sup)>i_1:
                            print "Ingrese un valor valido"
                            aux_c=True
                        else:
                            aux_c=False
                    except (NameError,SyntaxError):
                        print "Ingrese un valor valido"       
                aux_d=True
                while aux_d:
                    try:
                        print "Ingrese area que desea recortar del extremo inferior (debe ser menor a:",i_1-sup,")\n"
                        inf=input("valor inferior: ")
                        if int(inf)>(i_1-sup):
                            aux_d=True
                        else:
                            aux_d=False
                    except (NameError,SyntaxError):
                        print "Ingrese un valor valido"
                imagenRecortada= funcionRecortarImagen(abrirImagen,i_1,j_1,k_1,iz,der,sup,inf)
                aux=4
                menu1=False
                abrirImagen= imagenRecortada
            
            elif opcionElegida=="5":
                marco_aux=True
                while marco_aux:
                    color= raw_input("Seleccione el color de marco: \n1)Cafe\n2)Rojo\n3)Azul\n4)Verde\n")
                    if color=="1":
                        marco_aux=False
                    elif color=="2":
                        marco_aux=False
                    elif color=="3":
                        marco_aux=False
                    elif color=="4":
                        marco_aux=False
                    else:
                        marco_aux==True
                imagenMarco= funcionMarco(abrirImagen,color)
                aux=5
                menu1=False
                abrirImagen= imagenMarco
            elif opcionElegida=="6":
                menu3= True
                while menu3==True:
                    opcion=raw_input("\n\nElija la opcion que quiere realizar: \n1)Ampliar\n2)Reducir\n")
                    if opcion=="1":
                        imagenAmpliada= funcionAmpliar(abrirImagen)
                        menu3=False
                        abrirImagen=imagenAmpliada
                    elif opcion=="2":
                        imagenReducida= funcionReducir(abrirImagen)
                        menu3=False
                        abrirImagen= imagenReducida
                    else:
                        print "Ingrese opcion valida"
                        menu3=True
                aux=6
                menu1=False
            elif opcionElegida=="7":
                imagenContraste= funcionContraste(abrirImagen)
                aux=7
                menu1=False
                abrirImagen= imagenContraste
            else:
                print "Ingrese una opcion valida"
                menu1=True
                


            
        #SE PREGUNTA AL USUARIO SI DESEA REALIZAR OTRA MODIFICACION, SI EL VALOR ES INCORRECTO VUELVE A PREGUNTAR
        #SI EL USUARIO OPRIME LA OPCION DOS, TERMINA EL CODIGO
        #AUX AYUDA A SABER CUAL FUE LA ULTIMA MATRIZ DE LA MODIFICACION REALIZADA POR EL USUARIO, PARA LUEGO GENERAR
        #CON ESA MATRIZ LA IMAGEN
            menu2= True
            while menu2==True and menu1==False :
                continuar=raw_input("\nDesea realizar otra modificacion a la imagen: \n1)Si\n2)No\n ")
                if continuar=="1":
                    menu2=False
                    menu1=True
                elif continuar=="2":
                    menu2= False
                    nombreImagen2= raw_input("Ingrese el nombre con el cual desea guardar la imagen: ")
                    nombreImagenNueva= nombreImagen2+".bmp"
                    if aux==1:
                        devolver= funcionDevolverImagen(imagenGris, nombreImagenNueva)
                        p_1= False
                    elif aux==2:
                        if grados=="1":
                            devolver2= funcionDevolverImagen(imagenRotada, nombreImagenNueva)
                            p_1= False
                        elif grados=="2":
                            devolver2= funcionDevolverImagen(segundaRotacion, nombreImagenNueva)
                            p_1= False
                        elif grados=="3":
                            devolver3= funcionDevolverImagen(terceraRotacion, nombreImagenNueva)
                            p_1= False
                    elif aux==3:
                        devolver= funcionDevolverImagen(imagenEmbossing, nombreImagenNueva)
                        p_1= False
                    elif aux==4:
                        devolver= funcionDevolverImagen(imagenRecortada, nombreImagenNueva)
                        p_1= False
                    elif aux==5:
                        devolver= funcionDevolverImagen(imagenMarco, nombreImagenNueva)
                        p_1= False
                    elif aux==6:
                        if opcion==1:
                            devolver= funcionDevolverImagen(imagenAmpliada, nombreImagenNueva)
                            p_1= False
                        else :
                            devolver= funcionDevolverImagen(imagenReducida, nombreImagenNueva)
                            p_1= False
                    elif aux==7:
                        devolver= funcionDevolverImagen(imagenContraste, nombreImagenNueva)
                        print "Gracias por utilizar el editor de imagenes :D"
                        p_1= False
                        
                else:
                    print "Ingrese un valor valido "
                    menu2=True



    except (IOError,SyntaxError,NameError):
        print '''El nombre ingresado no se encuentra en la carpeta,por favor
Ingrese un nombre valido'''
        

