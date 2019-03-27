# Copyright (C) <2019>  <John Díaz / HapticLemon / jdl.profesional@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# Gráficas de frecuencias relativas de longitudes de palabras en textos.
# Ejemplo de uso de las librerías nltk (tokenización), matplotlib (gráficas),
# random (aleatorios) y copy (deepcopy en diccionario).

import nltk
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys
import copy
import random

# Abre archivo y devuelve su contenido
# nombre : nombre del archivo
def read_file(nombre):
	try:
		file_handle = open(nombre,'r')
		return file_handle.read()
	except:
		print('Error al abrir el archivo ' + nombre)
		sys.exit()

# Frecuencia relativa de una palabra en un texto.
# texto : el texto en el que se mide
# freq_palabra : frecuencia absoluta de la palabra.
def frecuencia_relativa(texto, frecuencia_absoluta):
	return frecuencia_absoluta / len(texto)

# Leo el contenido del archivo pasado como paŕametro y calculo
# la frecuencia de distribución de las palabras ordenada por
# longitudes de palabra.
def frecuencia_distribucion(archivo):
	texto = read_file(archivo)
	tokens = nltk.word_tokenize(texto)
	fdist = FreqDist(len(token) for token in tokens)

	# Quizá la ordenación se haga por defecto con el primero y sobre la lambda
	fdist_sorted_by_first = sorted(fdist.items(), key=lambda tup: tup[0])

	return fdist_sorted_by_first

# Devuelve el número de palabras de un texto.
# No me gusta mucho leer el archivo en dos sitios distintos,
# resulta ineficiente.
#
def longitud_texto(archivo):
	texto = read_file(archivo)
	texto_tokenizado = nltk.word_tokenize(texto)
	return(len(texto_tokenizado))

# Con el siguiente fragmento paso de 
# lista = [(1,11),(2,22),(3,33)]
# lista (en una segunda vuelta) = [(1,12),(2,23),(3,34)]
# a {1: [11, 12], 2: [22, 23], 3: [33, 34]}
def procesa_textos(lista_textos):
	dicc = {}
	for texto in lista_textos:
		fd_list = frecuencia_distribucion(texto)
		len_texto = longitud_texto(texto)
		print(len_texto)
		# Con el siguiente fragmento paso de 
		# lista = [(1,11),(2,22),(3,33)]
		# lista (en una segunda vuelta) = [(1,12),(2,23),(3,34)]
		# a {1: [11, 12], 2: [22, 23], 3: [33, 34]}
		# donde la clave es la longitud de la palabra y la lista son las frecuencias
		# absolutas de dicha palabra en cada uno de los archivos que se procesen.
		for item in fd_list:
			if item[0] not in dicc:
				lista = [item[1]/len_texto]
				dicc.update({item[0]:lista})
			else:
				lista = dicc[item[0]]
				lista.append(item[1]/len_texto)

	return dicc

# Si alguna de las claves (longitudes de palabra) no tiene entradas para cada archivo
# (es decir, en cada archivo hay palabras de esa longitud), la borro para tener datos de las
# mismas longitudes de palabra para todos los archivos. No es una solución que me entusiasme,
# pero de momento es lo que hay :\
#
def limpia_diccionario_frecuencias(diccionario_frecuencias, MAXFILES):
	dicc_frecuencias_copy = copy.deepcopy(diccionario_frecuencias)
	for key in dicc_frecuencias_copy:
		if len(dicc_frecuencias_copy[key]) < MAXFILES:
			diccionario_frecuencias.pop(key)
	return diccionario_frecuencias

# Puedo sacar los colores así. Limito a dos decimales.
def random_float_2dec():
	return float("{0:.2f}".format(random.random()))

# Dibuja la gráfica de frecuencias generando un color diferente para gráfica y 
# leyenda por cada una de las obras.
#
def plotea(claves, dicc_frec_texto):
	# La usaremos para poner los títulos de los textos.
	leyenda = []
	for obra in dicc_frec_texto:
		# Creo un color al azar para cada texto
		R = random_float_2dec() 
		G = random_float_2dec() 
		B = random_float_2dec() 

		color_RGB = (R,G,B)

		# Ploteo las frecuencias de cada obra.
		plt.plot(dicc_frec_texto[obra], color = color_RGB)

		# Creo un nuevo título y lo añado al cuadro de leyenda.
		patch = mpatches.Patch(color = color_RGB, label = obra)
		leyenda.append(patch)

	plt.legend(handles = leyenda)
	# De este modo toma las x como etiquetas (3,1,2...) en lugar de como valores
	# (lo que desordena la gráfica ya que dejaría los espacios correspondientes entre,
	# por ejemplo 20 y 34, etc). Si quieres ver cuál es el problema, quita la parte de range :)
	plt.xticks(range(len(claves)), claves)
	plt.show()

# Principal
#
def main():

	# Compruebo que indiquemos algún texto como parámetro.
	if len(sys.argv) < 2:
		print('Error : Falta texto de entrada')
		print('Uso : signature.py archivo1 ... archivoN')
		sys.exit(1)

	# Lista de los libros a procesar. (Quitamos el nombre del programa de la primera posición)
	text_list = sys.argv[1:]

	MAXFILES = len(text_list)
	diccionario_frecuencias = procesa_textos(text_list)

	diccionario_frecuencias_limpio = limpia_diccionario_frecuencias(diccionario_frecuencias, MAXFILES)

	# Saco las claves (las longitudes de palabra)
	claves = diccionario_frecuencias_limpio.keys()

	# Diccionario con una clave por archivo y la lista de frecuencias 
	dicc_frec_texto = {}

	# dicc_frec_texto tendrá la forma de 
	# {'Título de la obra 1': (frec_relativa1, frec_relativa2,..., frec_relativaN),'Título de la obra 2':(frec_relativa1...
	#
	for pos in range(MAXFILES):
		lista = []
		for key in diccionario_frecuencias_limpio:
			lista.append(diccionario_frecuencias_limpio[key][pos])
		dicc_frec_texto.update({text_list[pos]: tuple(lista)})

	# Dibujo las gráficas.
	plotea(claves, dicc_frec_texto)

if __name__ == "__main__":
    main()
