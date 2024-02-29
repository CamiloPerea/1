# precios de los productos 
PRECIO_COMPUTADOR_ESCRITORIO =2000000
PRECIO_COMPUTADOR_PORTATIL = 1000000
PRECIO_TABLETA = 700000
PRECIO_VIDEOBEMA = 500000
PRECIO_TELEVISOR =1000000

#Canttidad inicial de productos
cantidad_computador_escritorio = 0
cantidad_computador_portatil = 0
cantidad_tableta = 0
cantidad_videobeam = 0
cantidad_televisor = 0

while True:
    print("\nPRODUCTOS DISPONIBLES:")
    print("1. comútador de escritorio")
    print("2. computador de portatil")
    print("3. tableta")
    print("4. videobeam")
    print("5. televisor")
    print("6. Facturar")
    opcion = int(input("seleccione una opcion"))
    
    if opcion ==1:
        cantidad_computador_escritorio += 1
    elif opcion == 2:
        cantidad_computador_portatil += 1
    elif opcion == 3:
        cantidad_tableta += 1
    elif opcion == 4:
        cantidad_videobeam += 1
    elif opcion == 5:
        cantidad_televisor += 1
    elif opcion ==6:
        total_pagar = (cantidad_computador_escritorio * PRECIO_COMPUTADOR_ESCRITORIO +
                       cantidad_computador_portatil * PRECIO_COMPUTADOR_PORTATIL +
                       cantidad_tableta * PRECIO_TABLETA +
                       cantidad_videobeam * PRECIO_VIDEOBEMA +
                       cantidad_televisor * PRECIO_TELEVISOR) 
        print("\nRESUMEN DE COMPRA:")
        print("computadores de escritorio:", cantidad_computador_escritorio)
        print("computadores de portatil:", cantidad_computador_portatil)
        print("tabletas:", cantidad_tableta)
        print("videbeams:", cantidad_videobeam)
        print("televisrores:", cantidad_televisor)
    
        print("total a pagar:", total_pagar)
        break