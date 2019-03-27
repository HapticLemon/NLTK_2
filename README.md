# NLTK_2
Uso de NLTK sobre textos para obtener gráficas de frecuencia de longitudes de palabras

Algunas notas :

Los textos usados pueden encontrarse en libroteca.net . El formato elegito es el de texto plano (.txt) y son de dominio público. Si hay algún problema de licencias, por favor, hazmelo saber y los retiraré

Puedes ejecutar el programa con python signature.py *.txt

En el eje y de la gráfica podemos ver las frecuencias relativas de las palabras usadas en cada texto. En el eje x las longitudes ordenadas de las palabras usadas en los textos.

Hay que tener en cuenta que ambos textos no tienen por qué usar palabras de la misma longitud, es decir, en el primero podemos tener algún vocablo de longitud 23 y en el segundo no. Para una comparación precisa hay que descartar todas las longitudes que no sean comunes. Así mismo, al tener las obras diferentes longitudes, uso frecuencias relativas para poder comparar. Probablemente las palabras más largas (que en este caso suelen ser las más propensas a eliminarse) sean las que más información sobre la autoría pueden aportar. Espero poder investigar más a fondo la cuestión en el futuro.

El código está más ordenado que la versión anterior, sin elementos hardcodeados y dividido en funciones. Obviamente es mejorable (control de errores, etc), pero sirve como prueba de concepto e introducción al uso de NLTK, matplotlib, etc.
