#!/usr/bin/python
#!encoding: UTF-8

print "Introduzca el nombre del fichero donde se encuentran los resultados:"
nombre_fichero = raw_input ();

# Una forma de averiguar si un fichero existe o no puede ser esta
# debemos de incluir el paquete os.path
#  if os.path.isfile(nombre_fichero):
#    fichero = open (nombre_fichero, "a")
#  else:
#    fichero = open (nombre_fichero, "w")
#Otra forma puede ser mediante excepciones, como vemos a continuacion
try:
	fichero = open (nombre_fichero)
	linea = fichero.readline()
	while (linea != ""):                           #repiterá hasta llegar al final del fichero
		aproximaciones = int (linea.split()[3])      # nos leerá la posiciñon 3 y lo paso a entero.
		print ("Nº de intervalos: %d" % (aproximaciones))   
		for i in range (5):
			linea = fichero.readline()            #me lee la linea
			porcentaje = linea.split()[0]         # la posición 0 contiene el porcentaje
			umbral = float (linea.split()[6])     # y me quedo con el umbral
			print ("%s de fallos para el umbral %2.5f" % (porcentaje, umbral))
		linea = fichero.readline()
except:
	print "El nombre del fichero introducido es incorrecto"

