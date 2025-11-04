'''Pide un numero de nota de corte para que el programa revise dia a dia para luego imprimirte que dias superaron ese corte y con que temperatura'''


#LSITA TEMPERATURA DIAS DE LA SEMANA [Lunes, martes...]
listatemp = [20, 25, 19, 18, 15, 18, 20]
#Pide un numero para usarlo con la temperatura de corte]
tempcorte = int(input("Temperatura de corte: "))
i = 0

#Bucle para poder ver en que dia de la semana estamos
for tempdia in listatemp:

    i = i + 1

#Chequea que dias superan la temperatura de corte y imprime el dia con la temperatura
    if tempdia > tempcorte:


        if i == 1:
            dia = "lunes"
            print (dia, tempdia)


        elif i == 2:
            dia = "martes"
            print (dia, tempdia)


        elif i == 3:
            dia = "miercoles"
            print (dia, tempdia)


        elif i == 4:
            dia = "jueves"
            print (dia, tempdia)


        elif i == 5:
            dia = "viernes"
            print (dia, tempdia)


        elif i == 6:
            dia = "sabado"
            print (dia, tempdia)


        elif i == 7:
            dia = "domingo"
            print (dia, tempdia)


