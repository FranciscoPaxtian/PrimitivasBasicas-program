import sys
import matplotlib.pyplot as plt
import math

print("      HECHO POR FRANCISCO JAVIER PAXTIAN GORDILLO       ")
print("--------------------------------------------------------")
print(" ANALIZADOR DE DIFERENCIA DIGITAL Y COORDENADAS POLARES ")
print("--------------------------------------------------------")

print("⓵ ➔ Tienes solo dos vertices\n")
print("⓶ ➔ Tienes un vertice, la pendiente y la distancia\n")
print("⓷ ➔ Tienes un vertice, el angulo y la distancia\n")

print("--------------------------------------------------------")
print("      ALGORITMO DE PUNTO MEDIO PARA CIRCUNFERENCIAS     ")
print("--------------------------------------------------------")

print("⓸ ➔ Tienes el radio\n")

opc=int(input("Elige una de la opciones dependiendo el caso que tenga\n"))
if(opc==1):
    print("--------------------------------------------------------")
    print("           SELECCIONA LA OPERACION A REALIZAR           ")
    print("--------------------------------------------------------")

    print("⓵ ➔ ANALIZADOR DE DIFERENCIA DIGITAL Y COORDENADAS POLARES\n")
    print("⓶ ➔ ALGORITMO DE BRESENHAM\n")
    opc1=int(input("Elige una de las dos opciones\n"))
    if(opc1==1):
        x1=float(input("Ingrese el eje x1 del primer vertice \n"))
        y1=float(input("Ingrese el eje y1 del primer vertice \n"))

        x2=float(input("Ingrese el eje x2 del segundo vertice \n"))
        y2=float(input("Ingrese el eje y2 del segundo vertice \n"))

        #CALCULANDO LA PENDIENTE
        m=(y2-y1)/(x2-x1)

        #CALCULANDO EL ANGULO
        res= math.atan(m)
        angulo = math.degrees(res)

        #CALCULANDO LA DISTANCIA
        dis = pow((pow((x1-x2),2)+pow((y1-y2),2)),1/2)

        x=[x1,x2]
        y=[y1,y2]
        #MOSTRAR RESULTADO DE LA PENDIENTE
        print("--------------------------------------------------------")
        print("La pendiente es: ")
        print("{:.4f}".format(m))
        print("--------------------------------------------------------")
        #MOSTRAR RESULTADO DEL ANGULO
        print("--------------------------------------------------------")
        print("El angulo es: ")
        print("{:.4f}".format(angulo))
        print("--------------------------------------------------------")
        #MOSTRAR RESULTADO DE LA DISTANCIA
        print("--------------------------------------------------------")
        print("La distancia es: ")
        print("{:.4f}".format(dis))
        print("--------------------------------------------------------")
        #MOSTRAR LA GRAFICA DE LOS 2 PUNTOS
        plt.plot(x,y,":",color="b")
        plt.show()


        print("Si = 1 || No = 0")
        ban=int(input("¿La recta va de izquierda a derecha? \n"))
        if(ban==1):
            #Condicional cuando el valor de m esta entre 1 y -1
            if (-1<= m) and (m<= 1):
                if x1<x2:
                    cont=1
                    mm=y1+m
                    xuno=x1+1
                    print("Formula utilizada: Y(k+1) = Y (k+m)")
                    print("{:.4f}".format(y1)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                    cont=2
                    xuno=xuno+1
                    while(cont<=y2+2):
                        print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                        mm=mm+m
                        cont=cont+1
                        xuno=xuno+1   
                if x2<x1:
                    cont=1
                    mm=y2+m
                    xdos=x2+1
                    print("Formula utilizada: Y(k+1) = Y (k+m)")
                    print("{:.4f}".format(y2)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                    cont=2
                    xdos=xdos+1
                    while(cont<=y1+2):
                        print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                        mm=mm+m
                        cont=cont+1
                        xdos=xdos+1   
            else:
                if y1>y2:
                    cont=1
                    m=1/m
                    mm=x1+m
                    yuno=y1+1
                    print("Formula utilizada: X(k+1) = Xk + 1/m")
                    print("{:.4f}".format(x1)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                    cont=2
                    yuno=yuno-1
                    while(cont<=x2):
                        print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                        mm=mm+m
                        cont=cont+1
                        yuno=yuno+1    
                if y2>y1:
                    cont=1
                    m=1/m
                    mm=x2+m
                    ydos=y2+1
                    print("Formula utilizada: X(k+1) = Xk + 1/m")
                    print("{:.4f}".format(x2)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                    cont=2
                    ydos=ydos-1
                    while(cont<=x1):
                        print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                        mm=mm+m
                        cont=cont+1
                        ydos=ydos+1        
        else:
            #Condicional cuando el valor de m esta entre 1 y -1
            if (-1<= m) and (m<= 1):
                if x1>x2:
                    cont=1
                    mm=y1-m
                    xuno=x1-1
                    print("Formula utilizada: Y(k+1) = Y (k-m)")
                    print("{:.4f}".format(y1)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                    cont=2
                    xuno=xuno-1
                    while(cont<=y2+1):
                        print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                        mm=mm-m
                        cont=cont+1
                        xuno=xuno-1
                if x2>x1:
                    cont=1
                    mm=y2-m
                    xdos=x2-1
                    print("Formula utilizada: Y(k+1) = Y (k-m)")
                    print("{:.4f}".format(y2)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                    cont=2
                    xdos=xdos-1
                    while(cont<=y1+1):
                        print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                        mm=mm-m
                        cont=cont+1
                        xdos=xdos-1  
            else:
                if y1>y2:
                    cont=1
                    m=1/m
                    mm=x1-m
                    yuno=y1-1
                    print("Formula utilizada: X(k+1) = Xk - 1/m")
                    print("{:.4f}".format(x1)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                    cont=2
                    yuno=yuno-1
                    while(cont<=x2):
                        print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                        mm=mm-m
                        cont=cont+1
                        yuno=yuno-1 
                if y2>y1:
                    cont=1
                    m=1/m
                    mm=x2-m
                    ydos=y2-1
                    print("Formula utilizada: X(k+1) = Xk - 1/m")
                    print("{:.4f}".format(x2)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                    cont=2
                    ydos=ydos-1
                    while(cont<=x1):
                        print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                        mm=mm-m
                        cont=cont+1
                        ydos=ydos-1 

        plt.plot(x,y,":",color="b")
        plt.show()
    elif(opc1==2):
        #EMPIEZA CALCULO ALGORITMO DE BRESEMHAM
        x1=float(input("Ingrese el eje x1 del primer vertice \n"))
        y1=float(input("Ingrese el eje y1 del primer vertice \n"))

        x2=float(input("Ingrese el eje x2 del segundo vertice \n"))
        y2=float(input("Ingrese el eje y2 del segundo vertice \n"))

        #Calculando delta x
        Deltax=x2-x1
        #Calculando delta y
        Deltay=y2-y1
        #Validacion pendiente indefinida
        if (Deltax==0):
            print("--------------------------------------------------------------------------")
            print("PROGRAMA TERMINADO POR DIVISION ENTRE CERO EN EL RESULTADO DE LA PENDIENTE")
            print("--------------------------------------------------------------------------")
            sys.exit(1)
        #Calculando la pendiente
        m= Deltay/Deltax

        if(m<=1):
            #MOSTRAR RESULTADO DE LA PENDIENTE
            print("--------------------------------------------------------")
            print("La pendiente es: ")
            print("{:.4f}".format(m))
            print("--------------------------------------------------------")
            #MOSTRAR RESULTADO DE DELTA X
            print("--------------------------------------------------------")
            print("(Δx) Delta x es: ")
            print("{:.4f}".format(Deltax))
            print("--------------------------------------------------------")
            #MOSTRAR RESULTADO DE DELTA Y
            print("--------------------------------------------------------")
            print("(Δy) Delta y es: ")
            print("{:.4f}".format(Deltay))
            print("--------------------------------------------------------") 

            Deltax2 = Deltax*2
            Deltay2 = Deltay*2

            if x1<x2:
                cont=0
                #mm=y1+m
                po=Deltay2-Deltax2
                xuno=x1+1
                yy=y1
                if(po>=0):
                    yy=y1+1
                print("Po "," = ","{:.4f}".format(Deltay2)," - ","{:.4f}".format(Deltax2)," = ", "{:.4f}".format(po)," | Valor k: ",cont," Valor Pk: ",(po)," Valor Xk: ",(xuno)," Valor Xy: ",(y1))
                cont=1
                xuno=xuno+1
           
                if(po<0):
                    pasado=Deltay2
                    poo=po+pasado
                    yy=yy+1
                elif(po>=0):
                    pasado=Deltay2-Deltax2
                    poo=po+pasado
                    yy= yy+2

                while(xuno-1<=x2):
                    print("P",cont," = ","{:.4f}".format(po)," + ","{:.4f}".format(pasado)," = ", "{:.4f}".format(poo)," | Valor k: ",cont," Valor Pk: ",(poo)," Valor Xk: ",(xuno)," Valor Xy: ",(yy))
                    cont=cont+1
                    xuno=xuno+1
                    po=poo
                    if(poo<0):
                        pasado=Deltay2
                        poo=po+pasado
                    elif(poo>=0):
                        pasado=Deltay2-Deltax2
                        poo=po+pasado
                        yy= yy+1 
                x=[x1,x2]
                y=[y1,y2]
                #MOSTRAR LA GRAFICA DE LOS 2 PUNTOS
                plt.plot(x,y,":",color="b")
                plt.show()
            if x2<x1:
                cont=0
                po=Deltay2-Deltax2
                xdos=x2+1
                yy=y2
                if(po>0):
                    yy=y2+1
                print("Po "," = ","{:.4f}".format(Deltay2)," - ","{:.4f}".format(Deltax2)," = ", "{:.4f}".format(po)," | Valor k: ",cont," Valor Pk: ",(po)," Valor Xk: ",(xdos)," Valor Xy: ",(y2))
                cont=1
                xdos=xdos+1
                if(po<0):
                    pasado=Deltay2
                    poo=po+pasado
                    yy=yy+1
                elif(po>=0):
                    pasado=Deltay2-Deltax2
                    poo=po+pasado
                    yy= yy+2
                while(xdos-1<=x2):
                    print("P",cont," = ","{:.4f}".format(po)," + ","{:.4f}".format(pasado)," = ", "{:.4f}".format(poo)," | Valor k: ",cont," Valor Pk: ",(poo)," Valor Xk: ",(xdos)," Valor Xy: ",(yy))
                    cont=cont+1
                    xdos=xdos+1
                    po=poo
                    if(poo<0):
                        pasado=Deltay2
                        poo=po+pasado
                    elif(poo>=0):
                        pasado=Deltay2-Deltax2
                        poo=po+pasado
                        yy= yy+1 
                x=[x1,x2]
                y=[y1,y2]
                #MOSTRAR LA GRAFICA DE LOS 2 PUNTOS
                plt.plot(x,y,":",color="b")
                plt.show()  
        else:
            print("------------------------------------------------------------") 
            print("NO SE REALIZO EL ALGORITMO DEBIDO A QUE LA PENDIENTE FUE: ",m) 
            print("   COMO ES MAYOR A 1 NO SE PUEDE EJECUTAR ESTA OPERACION    ") 
            print("------------------------------------------------------------") 
              
elif(opc==2):

    x1=float(input("Ingrese el eje x1 del primer vertice \n"))
    y1=float(input("Ingrese el eje y1 del primer vertice \n"))

    m=float(input("Ingrese el valor de la pendiente \n"))
    dis2=float(input("Ingrese el valor de la distancia \n"))

    #CALCULANDO EL ANGULO
    res= math.atan(m)
    angulo = math.degrees(res)
    
    #CALCULANDO EL XO
    grados=angulo
    radianes = (grados* math.pi)/180
    coseno = math.cos(radianes)
    #print("{:.4f}".format(coseno))

    #CALCULANDO EL Y0
    grados2=angulo
    radianes2 = (grados2* math.pi)/180
    seno = math.sin(radianes2)
    #print("{:.4f}".format(seno))

    #CALCULANDO X2
    x2=((dis2*coseno)+x1)
    y2=((dis2*seno)+y1)

    #MOSTRAR RESULTADO X2
    print("--------------------------------------------------------")
    print("El vertice x2 es: ")
    print("{:.4f}".format(x2))
    print("--------------------------------------------------------")   
    #MOSTRAR RESULTADO Y2
    print("--------------------------------------------------------")
    print("El vertice y2 es: ")
    print("{:.4f}".format(y2))
    print("--------------------------------------------------------")  

    x=[x1,x2]
    y=[y1,y2]

    #MOSTRAR RESULTADO DEL ANGULO
    print("--------------------------------------------------------")
    print("El angulo es: ")
    print("{:.4f}".format(angulo))
    print("--------------------------------------------------------")

    #MOSTRAR LA GRAFICA DE LOS 2 PUNTOS
    plt.plot(x,y,":",color="b")
    plt.show()


    print("Si = 1 || No = 0")
    ban=int(input("¿La recta va de izquierda a derecha? \n"))
    if(ban==1):
        #Condicional cuando el valor de m esta entre 1 y -1
        if (-1<= m) and (m<= 1):
            if x1<x2:
                cont=1
                mm=y1+m
                xuno=x1+1
                print("Formula utilizada: Y(k+1) = Y (k+m)")
                print("{:.4f}".format(y1)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                cont=2
                xuno=xuno+1
                while(cont<=y2+2):
                    print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                    mm=mm+m
                    cont=cont+1
                    xuno=xuno+1   
            if x2<x1:
                cont=1
                mm=y2+m
                xdos=x2+1
                print("Formula utilizada: Y(k+1) = Y (k+m)")
                print("{:.4f}".format(y2)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                cont=2
                xdos=xdos+1
                while(cont<=y1+2):
                    print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                    mm=mm+m
                    cont=cont+1
                    xdos=xdos+1   
        else:
            if y1>y2:
                cont=1
                m=1/m
                mm=x1+m
                yuno=y1+1
                print("Formula utilizada: X(k+1) = Xk + 1/m")
                print("{:.4f}".format(x1)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                cont=2
                yuno=yuno-1
                while(cont<=x2):
                    print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                    mm=mm+m
                    cont=cont+1
                    yuno=yuno+1    
            if y2>y1:
                cont=1
                m=1/m
                mm=x2+m
                ydos=y2+1
                print("Formula utilizada: X(k+1) = Xk + 1/m")
                print("{:.4f}".format(x2)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                cont=2
                ydos=ydos-1
                while(cont<=x1):
                    print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                    mm=mm+m
                    cont=cont+1
                    ydos=ydos+1        
    else:
        #Condicional cuando el valor de m esta entre 1 y -1
        if (-1<= m) and (m<= 1):
            if x1>x2:
                cont=1
                mm=y1-m
                xuno=x1-1
                print("Formula utilizada: Y(k+1) = Y (k-m)")
                print("{:.4f}".format(y1)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                cont=2
                xuno=xuno-1
                while(cont<=y2+1):
                    print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                    mm=mm-m
                    cont=cont+1
                    xuno=xuno-1
            if x2>x1:
                cont=1
                mm=y2-m
                xdos=x2-1
                print("Formula utilizada: Y(k+1) = Y (k-m)")
                print("{:.4f}".format(y2)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                cont=2
                xdos=xdos-1
                while(cont<=y1+1):
                    print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                    mm=mm-m
                    cont=cont+1
                    xdos=xdos-1  
        else:
            if y1>y2:
                cont=1
                m=1/m
                mm=x1-m
                yuno=y1-1
                print("Formula utilizada: X(k+1) = Xk - 1/m")
                print("{:.4f}".format(x1)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                cont=2
                yuno=yuno-1
                while(cont<=x2):
                    print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                    mm=mm-m
                    cont=cont+1
                    yuno=yuno-1 
            if y2>y1:
                cont=1
                m=1/m
                mm=x2-m
                ydos=y2-1
                print("Formula utilizada: X(k+1) = Xk - 1/m")
                print("{:.4f}".format(x2)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                cont=2
                ydos=ydos-1
                while(cont<=x1):
                    print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                    mm=mm-m
                    cont=cont+1
                    ydos=ydos-1 

    plt.plot(x,y,":",color="b")
    plt.show()
elif(opc==3):

    x1=float(input("Ingrese el eje x1 del primer vertice \n"))
    y1=float(input("Ingrese el eje y1 del primer vertice \n"))

    angulo=float(input("Ingrese el valor del angulo \n"))
    dis2=float(input("Ingrese el valor de la distancia \n"))
    
    #CALCULANDO EL XO
    grados=angulo
    radianes = (grados* math.pi)/180
    coseno = math.cos(radianes)
    #print("{:.4f}".format(coseno))

    #CALCULANDO EL Y0
    grados2=angulo
    radianes2 = (grados2* math.pi)/180
    seno = math.sin(radianes2)
    #print("{:.4f}".format(seno))

    #CALCULANDO X2
    x2=((dis2*coseno)+x1)
    #CALCULANDO Y2
    y2=((dis2*seno)+y1)

    #CALCULANDO LA PENDIENTE
    equis=int(x2-x1)
    
    if (equis==0):
        #sys.exit(1)
        print("--------------------------------------------------------------------------")
        print("PROGRAMA TERMINADO POR DIVISION ENTRE CERO EN EL RESULTADO DE LA PENDIENTE")
        print("--------------------------------------------------------------------------")
    else:
        m=(y2-y1)/(equis)

        #MOSTRAR RESULTADO X2
        print("--------------------------------------------------------")
        print("El vertice x2 es: ")
        print("{:.4f}".format(x2))
        print("--------------------------------------------------------")   
        #MOSTRAR RESULTADO Y2
        print("--------------------------------------------------------")
        print("El vertice y2 es: ")
        print("{:.4f}".format(y2))
        print("--------------------------------------------------------")  

        x=[x1,x2]
        y=[y1,y2]

        #MOSTRAR RESULTADO DE LA PENDIENTE
        print("--------------------------------------------------------")
        print("La pendiente es: ")
        print("{:.4f}".format(m))
        print("--------------------------------------------------------")

        #MOSTRAR LA GRAFICA DE LOS 2 PUNTOS
        plt.plot(x,y,":",color="b")
        plt.show()


        print("Si = 1 || No = 0")
        ban=int(input("¿La recta va de izquierda a derecha? \n"))
        if(ban==1):
            #Condicional cuando el valor de m esta entre 1 y -1
            if (-1<= m) and (m<= 1):
                if x1<x2:
                    cont=1
                    mm=y1+m
                    xuno=x1+1
                    print("Formula utilizada: Y(k+1) = Y (k+m)")
                    print("{:.4f}".format(y1)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                    cont=2
                    xuno=xuno+1
                    while(cont<=y2+2):
                        print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                        mm=mm+m
                        cont=cont+1
                        xuno=xuno+1   
                if x2<x1:
                    cont=1
                    mm=y2+m
                    xdos=x2+1
                    print("Formula utilizada: Y(k+1) = Y (k+m)")
                    print("{:.4f}".format(y2)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                    cont=2
                    xdos=xdos+1
                    while(cont<=y1+2):
                        print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                        mm=mm+m
                        cont=cont+1
                        xdos=xdos+1   
            else:
                if y1>y2:
                    cont=1
                    m=1/m
                    mm=x1+m
                    yuno=y1+1
                    print("Formula utilizada: X(k+1) = Xk + 1/m")
                    print("{:.4f}".format(x1)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                    cont=2
                    yuno=yuno-1
                    while(cont<=x2):
                        print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                        mm=mm+m
                        cont=cont+1
                        yuno=yuno+1    
                if y2>y1:
                    cont=1
                    m=1/m
                    mm=x2+m
                    ydos=y2+1
                    print("Formula utilizada: X(k+1) = Xk + 1/m")
                    print("{:.4f}".format(x2)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                    cont=2
                    ydos=ydos-1
                    while(cont<=x1):
                        print("{:.4f}".format(mm)," + ","{:.4f}".format(m)," = ", "{:.4f}".format(mm+m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                        mm=mm+m
                        cont=cont+1
                        ydos=ydos+1        
        else:
            #Condicional cuando el valor de m esta entre 1 y -1
            if (-1<= m) and (m<= 1):
                if x1>x2:
                    cont=1
                    mm=y1-m
                    xuno=x1-1
                    print("Formula utilizada: Y(k+1) = Y (k-m)")
                    print("{:.4f}".format(y1)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                    cont=2
                    xuno=xuno-1
                    while(cont<=y2+1):
                        print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(xuno)," Valor y: ",round(mm))
                        mm=mm-m
                        cont=cont+1
                        xuno=xuno-1
                if x2>x1:
                    cont=1
                    mm=y2-m
                    xdos=x2-1
                    print("Formula utilizada: Y(k+1) = Y (k-m)")
                    print("{:.4f}".format(y2)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                    cont=2
                    xdos=xdos-1
                    while(cont<=y1+1):
                        print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(xdos)," Valor y: ",round(mm))
                        mm=mm-m
                        cont=cont+1
                        xdos=xdos-1  
            else:
                if y1>y2:
                    cont=1
                    m=1/m
                    mm=x1-m
                    yuno=y1-1
                    print("Formula utilizada: X(k+1) = Xk - 1/m")
                    print("{:.4f}".format(x1)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                    cont=2
                    yuno=yuno-1
                    while(cont<=x2):
                        print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(yuno))
                        mm=mm-m
                        cont=cont+1
                        yuno=yuno-1 
                if y2>y1:
                    cont=1
                    m=1/m
                    mm=x2-m
                    ydos=y2-1
                    print("Formula utilizada: X(k+1) = Xk - 1/m")
                    print("{:.4f}".format(x2)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                    cont=2
                    ydos=ydos-1
                    while(cont<=x1):
                        print("{:.4f}".format(mm)," - ","{:.4f}".format(m)," = ", "{:.4f}".format(mm-m)," | Valor k: ",cont," Valor x: ",(mm)," Valor y: ",round(ydos))
                        mm=mm-m
                        cont=cont+1
                        ydos=ydos-1 

        plt.plot(x,y,":",color="b")
        plt.show()
elif(opc==4):
    XC = float(input("ingrese coordenada x \n"))
    YC = float(input("ingrese coordenada y \n"))
    rad = float(input("Ingrese el radio \n"))
    if rad<0:
        print("El radio no puede ser negativo\n")
    else:
        x = 0
        y = rad
        p = (5/4)-rad
        #p = -(rad * 4/5)
        
        listaX = []
        listaY = []
        
        cont=0
        contt=1
    
        print("Formula utilizada: p0 = 5/4 - r")
        print("Po"," = ","5/4"," - ","{:.4f}".format(rad)," = ", "{:.4f}".format(p)," = ",round(p))
        print("Valor k: ",cont," Valor Pk: ",round(p)," Valor Xk: ",(contt)," Valor Yk: ",(rad))
        
        cont=cont+1
        rr= rad
        ppk=p
        if(ppk>=0):
            ppk=(ppk)+(2*contt)+1-(2*ppk)
            rr=rr-1
        elif(ppk<0):
            ppk=(ppk)+(2*contt)+1
        contt=contt+1
        while(contt!=rr):
            print("Valor k: ",cont," Valor Pk: ",round(ppk)," Valor Xk: ",(contt)," Valor Yk: ",(rr))

            cont=cont+1
            if(ppk>=0):
                ppk=ppk+(2*contt)+1-(2*ppk)
                rr=rr-1
            else:
                ppk=ppk+(2*contt)+1
            contt=contt+1
        
        print("Valor k: ",cont," Valor Pk: ",round(ppk)," Valor Xk: ",(contt)," Valor Yk: ",(rr))
        
        while x <= y:
            #puntos simétrico
            x_octante1 = y
            y_octante1 = x
            x_octante2 = -y
            y_octante2 = x
            x_octante3 = -x
            y_octante3 = y
            x_octante4 = -x
            y_octante4 = -y
            x_octante5 = -y
            y_octante5 = -x
            x_octante6 = y
            y_octante6 = -x
            x_octante7 = x
            y_octante7 = -y
             
            # Agregar los puntos a las listas
            listaX.append(x + XC)
            listaY.append(y + YC)
            
            listaX.append(x_octante1 + XC)
            listaY.append(y_octante1 + YC)
            listaX.append(x_octante2 + XC)
            listaY.append(y_octante2 + YC)
            listaX.append(x_octante3 + XC)
            listaY.append(y_octante3 + YC)
            listaX.append(x_octante4 + XC)
            listaY.append(y_octante4 + YC)
            listaX.append(x_octante5 + XC)
            listaY.append(y_octante5 + YC)
            listaX.append(x_octante6 + XC)
            listaY.append(y_octante6 + YC)
            listaX.append(x_octante7 + XC)
            listaY.append(y_octante7 + YC)
            
        #pp
            if p < 0:
                x += 1
                p = p + (2*x) + 1
            else:
                x += 1
                y -= 1
                p = p + (2*x) + 1 - (2*y)

        plt.title("Circular")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.fill(listaX,listaY,color="green",alpha=0.5)
        plt.grid()
        plt.plot(listaX, listaY, 'o', color="black", markersize=6)
        plt.axis('equal')
        plt.show()


print("--------------------------------------------------------")
print("                  FIN DEL EJERCICIO                     ")
print("--------------------------------------------------------")