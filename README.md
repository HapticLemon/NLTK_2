# NLTK_2
Uso de NLTK sobre textos para obtener gráficas de frecuencia de longitudes de palabras

Algunas notas :

Los textos usados pueden encontrarse en http://libroteca.net . El formato elegito es el de texto plano (.txt) y son de dominio público. Si hay algún problema de licencias, por favor, hazmelo saber y los retiraré

Para ejecutar el programa (asumiendo que tu sistema está correctamente configurado) :

- Coloca signature.py y los archivos de texto .txt en el mismo directorio
- Ejecutar el programa con "python signature.py *.txt "
- También puedes hacerlo indicando los nombres de archivo con "python signature.py texto1.txt texto2.txt" etc

Básicamente el programa desmenuza los textos en palabras (tokeniza), contando cuántas hay de cada longitud determinada
(Ej : 'a' tiene longitud 1, 'the' longitud 3, etc). Obtendremos las frecuencias relativas 
(Ej : palabras de longitud 3/ Total de palabras ) y haremos una gráfica distintiva de cada obra indicada como parámetro.

En el eje y de la gráfica podemos ver las frecuencias relativas de las palabras usadas en cada texto. En el eje x las longitudes ordenadas de las palabras ( 1- un carácter, 2- 2 caracteres...) usadas en los textos.

Hay que tener en cuenta que ambos textos no tienen por qué usar palabras de la misma longitud, es decir, en el primero podemos tener algún vocablo de longitud 23 y en el segundo no. Para una comparación precisa hay que descartar todas las longitudes que no sean comunes. Así mismo, al tener las obras diferentes longitudes, uso frecuencias relativas para poder comparar. Probablemente las palabras más largas (que en este caso suelen ser las más propensas a eliminarse) sean las que más información sobre la autoría pueden aportar. Espero poder investigar más a fondo la cuestión en el futuro.

El código está más ordenado que la versión anterior, sin elementos hardcodeados y dividido en funciones. Obviamente es mejorable (control de errores, etc), pero sirve como prueba de concepto e introducción al uso de NLTK, matplotlib, etc.
