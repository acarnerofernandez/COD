
listatemp = [20, 25, 19, 18, 15, 18, 20]
tempcorte = int(input("Temperatura de corte: "))
i = 0

for tempdia in listatemp:

    i = i + 1

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


