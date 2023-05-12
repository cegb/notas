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
    for i in range(3,len(item)):
        suma = suma + float(item[i])
        contador = contador + 1
    prom = suma/contador
    return round(prom,1)

## main ##

# Procesar la lista completa
full_data.pop(0)
data_salida = []

for item in full_data:
    prom = promedio(item)
    data_salida.append([item[0],item[1],item[2],prom])

#print(data_salida)



with open(salida, "w", encoding="utf-8", newline='') as outfile:
    escribir = csv.writer(outfile,delimiter=",")

    escribir.writerow(["nombre","apellido","rut","promedio"])  ## en caso de requerir colocar encabezado (header)
    escribir.writerows(data_salida)

