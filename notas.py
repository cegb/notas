# A partir de este programa, agregar al reporte las notas máxima y mínima de cada estudiante

import csv

archivo = "datos.csv"
salida = "reporte.csv"

with open(archivo, "r", encoding="utf-8") as archivo_lectura:
    datos = csv.reader(archivo_lectura, delimiter=",")

    #print(datos)

    full_data = []
    for row in datos:
        #print(row)
        full_data.append(row)
    
#print(full_data)

def promedio(item):
    suma = 0
    contador = 0
    max = 2e-10
    min = 2e10
    for i in range(3,len(item)):
        suma = suma + float(item[i])
        contador = contador + 1
        if float(item[i]) > max:
            max = float(item[i])
        if float(item[i]) < min:
            min = float(item[i])  

    prom = suma/contador
    return round(prom,1), min, max

## main ##

# Procesar la lista completa
full_data.pop(0)
data_salida = []

for item in full_data:
    prom, nota_min, nota_max = promedio(item)
    data_salida.append([item[0],item[1],item[2],prom,nota_min,nota_max])

#print(data_salida)



with open(salida, "w", encoding="utf-8", newline='') as outfile:
    escribir = csv.writer(outfile,delimiter=",")

    escribir.writerow(["nombre","apellido","rut","promedio"])  ## en caso de requerir colocar encabezado (header)
    escribir.writerows(data_salida)

print("Programa finalizado...!")
