import sys 
from departamentos_judiciales_clase import departamentosJudiciales

archivo_entrada = sys.argv[1]
archivo_salida = sys.argv[2]
f = open(archivo_entrada,"r", encoding = "latin-1")
departamentos = departamentosJudiciales()

for linea in f:
    if "Fuero" in linea:
        continue
    valores = linea.split(";")
    dependencia = valores[2]
    departamento = valores[6]
    if departamentos.existe_departamento(departamento):
        departamentos.agregar_dependencia(departamento, dependencia, valores)
    else:
        departamentos.agregar_departamento(departamento, dependencia, valores)
 
f.close()

departamentos.ordenar() #usamos la función definida antes que ordena los elementos

departamentos.guardar_en_archivo(archivo_salida) #usamos la función definida antes que guarda el txt
    