import csv
import random

empleados = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
             "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

info_empleados = {}

def asignar_sueldos():
    for empleado in empleados:
        sueldo = random.randint(300000, 2500000)
        info_empleados[empleado] = sueldo
    print("Sueldos asignados de manera aleatoria")    

def clasificar_sueldos():
    menos_800k = {}
    entre_800k_y_2M = {}
    mas_2M = {}

    for empleado, sueldo in info_empleados.items():
        if sueldo < 800000:
            menos_800k[empleado] = sueldo
        elif 800000 <= sueldo <= 2000000:
            entre_800k_y_2M[empleado] = sueldo
        else:
            mas_2M[empleado] = sueldo
    
    print("\nSueldos menores a $800.000: ")
    for empleado, sueldo in menos_800k.items():
        print(f"{empleado}: ${sueldo:,}")

    print("\nSueldos entre $800.000 y $2.000.000: ")
    for empleado, sueldo in entre_800k_y_2M.items():
        print(f"{empleado}: ${sueldo:,}")

    print("\nSueldos superiores a $2.000.000: ")
    for empleado, sueldo in mas_2M.items():
        print(f"{empleado}: ${sueldo:,}")

def ver_datos():
    sueldos = list(info_empleados.values())
    if sueldos:
        sueldo_maximo = max(sueldos)
        sueldo_minimo = min(sueldos)
        promedio_sueldos = sum(sueldos) / len(sueldos)
        
        print("\nEstadísticas de los sueldos:")
        print(f"Sueldo más alto: ${sueldo_maximo:,}")
        print(f"Sueldo más bajo: ${sueldo_minimo:,}")
        print(f"Promedio de sueldos: ${promedio_sueldos:,.2f}")
    else:
        print("No hay sueldos asignados aún.")

def reporte_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["Nombre", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Neto"])
        
        for empleado, sueldo in info_empleados.items():
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_neto = sueldo - descuento_salud - descuento_afp
            escritor_csv.writerow([empleado, sueldo, descuento_salud, descuento_afp, sueldo_neto])
    
    print("Reporte de sueldos generado en 'reporte_sueldos.csv'.")

def finalizar_programa():
    print("Finalizando el programa ...")
    print("Desarrollado por Valentina Esquivel")

while True:
    print("******MENÚ******")
    print("1.- Asignar sueldos aleatorios")
    print("2.- Clasificar sueldos")
    print("3.- Ver estadísticas")
    print("4.- Reporte de sueldos")
    print("5.- Salir del programa")
    print("************")
    try:
        opcion = int(input("Seleccionar una opción (1-5): "))
        if opcion == 1:
            asignar_sueldos()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            ver_datos()
        elif opcion == 4:
            reporte_sueldos()
        elif opcion == 5:
            finalizar_programa()
            break
        else:
            print("Opción no válida")
    except ValueError:
        print("Debes ingresar una opción numérica del 1 al 5")