# BIG DATA 2015-1 UIS #

El término Big Data se refiere a un área de conocimiento de reciente relevancia motivada por necesidades de análisis de datos a gran escala, tanto en la industria como en la academia, y que se desarrolla gracias a los avances tecnológicos y teóricos alcanzados en los últimos años. Integra procesos de aprendizaje computacional (machine learning), técnicas de cómputo y almacenamiento escalable (Hadoop, NoSQL) y equipos multidisciplinares para descubrir y extraer conocimiento latente en grandes colecciones de datos de una gran variedad y normalmente sin estructuras de datos homogéneas. 

Este curso cubre varias tecnologías y métodos usados en distintos entornos de Big Data, y aborda su integración con los sistemas y algoritmos que albergan y analizan esas grandes colecciones de datos. Ofrecerá al estudiante un contacto directo con las tecnologías principales usadas en Big Data para abordar problemas actuales y concretos.

*Contacto*: Raúl Ramos rramosp@uis.edu.co http://raulramos.org

Haz un clon de este repositorio para tener tu copia local y trabajar sobre las prácticas.

`git clone https://bitbucket.org/rramosp/20151.bigd.uis.pre.git`

Cuando hagamos quizes, este es el repositorio que deberás clonar:

`git clone https://bitbucket.org/rramosp/20151.bigd.uis.pre-quiz.git`


estamos trabajando sobre una máquina virtual con [Python Anaconda](http://continuum.io/), [mrjob](https://pythonhosted.org/mrjob/), [Hadoop](https://hadoop.apache.org/) y [Ambari](http://ambari.apache.org/). Contáctame para más información.

## Contenido

### 1. Introducción
Ley de Amdahl - Escalabilidad horizontal y vertical - Cómputo hacia los datos - Python - Estructuras de datos - Numpy - OO

[Notas 01 - Introducción a Python](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Notas%2001%20-%20Introduccion_a_Python.ipynb)
--- [Problem Set 00 - Practica](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Problem%20Set%2000%20-%20Practica-Ejemplo.ipynb)
--- [Problem Set 01 - Python](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Problem%20Set%2001%20-%20Introduccion_a_Python.ipynb)

### 2. Map-reduce
Modelos de programación - Mapreduce - Mrjob - Instrumentación - Runners - Combiners

[Notas 02 - Map reduce](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Notas%2002%20-%20Map-Reduce.ipynb) ---
[Problem Set 02A - Map reduce básico](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Problem%20Set%2002A%20-%20Map-Reduce%20I.ipynb) ---
[Problem Set 02B - Map reduce avanzado](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Problem%20Set%2002B%20-%20Map-Reduce%20II.ipynb/%3Fat%3Dmaster)

### 3. Page rank
Grafo de colecciones de documentos - Valores y vectores propios - Flujos de trabajo Map-reduce 

[Notas 03 - Page Rank](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Notas%2003%20-%20Page%20rank.ipynb) -- [Notas 03B - Flujos de trabajo map reduce](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Notas%2003B%20-%20Flujos%20de%20Tareas%20Map%20Reduce.ipynb/%3Fat%3Dmaster) --[Problem Set 03 - Page rank con Map-Reduce](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Problem%20Set%2003%20-%20Page%20Rank%20con%20Map%20Reduce.ipynb/%3Fat%3Dmaster)

### 4. Searching
Locality Sensitive Hashing - Familias de funciones LSH y distancias - Aumentación de funciones LSH

[Notas 04 - Locality Sensitive Hashing](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Notas%2004%20-%20Locality%20Sensitive%20Hashing.ipynb) -- [Problem Set 04 - LSH para distancia euclidiana](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Problem%20Set%2004%20-%20Locality%20Sensitive%20Hashing.ipynb/%3Fat%3Dmaster)

### 5. Hadoop
Arquitectura de Hadoop - Configuración y lanzamiento de jobs - integración mr-job - Jobs en Java

[Notas 05 - Intro to Hadoop](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Notas%2005%20-%20Intro%20to%20Hadoop.ipynb) -- [Problem Set 05 - Page Rank con Hadoop](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Problem%20Set%2005%20-%20Page%20Rank%20sobre%20Hadoop.ipynb)

### 6. Herramientas sobre Hadoop
PIG - HIVE

[Notas 06A - PIG](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Notas%2006A%20-%20PIG.ipynb) [Notas 06B - Hive](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Notas%2006B%20-%20HIVE.ipynb) -- [Problem Set 06A - PIG](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Problem%20Set%2006A%20-%20PIG.ipynb) [Problem Set 06B - HIVE](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Problem%20Set%2006B%20-%20HIVE.ipynb)

### 7. NoSQL
Introducción a NoSQL - Tipos de bases de datos NoSQL - Expresividad vs Escalabilidad

[Notas 07A - Cassandra](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Notas%2007A%20-%20NoSQL%20Cassandra.ipynb) -- [Problem Set 07A - Cassandra](http://nbviewer.ipython.org/urls/bitbucket.org/rramosp/20151.bigd.uis.pre/raw/master/Problem%20Set%2007A%20-%20NoSQL%20Cassandra.ipynb)

---

Calificación | Fechas
---------------- | ------------
Problem sets        40% |  Semana 6:        Talleres 1, 2 y 3 
Online Quizes      30% | Semana 7:        Exámen parcial 1
Exámenes             20% |  Semana 12:      Exámen parcial 2
Online courses    10% (*)  |  Semana 13:      Talleres resto
Extra            hasta 15% |

(*) _2 lecciones en algún curso online_

## Cursos en línea
Existe mucho material en línea acerca de Big Data y Data Science. Algunos de los ejercicios de este curso están basados en los que podrás encontrar en los siguientes cursos en línea:

* [Mining Massive Datasets](https://www.coursera.org/course/mmds), Coursera
* [Intro to Data Science](https://www.udacity.com/course/ud359), UDACITY (parte abierta)
* [Intro to Hadoop and Map-Reduce](https://www.udacity.com/course/ud617), en UDACITY (parte abierta)
* [Making Sense of Data](https://datasense.withgoogle.com/preview), en Google
* [Introduction to Data Analysis](https://class.coursera.org/datasci-001), en Coursera
* [Big Data Mini Course](http://ampcamp.berkeley.edu/big-data-mini-course/), en Berkeley

## Referencias

* [LINDYER2010] Lin, Dyer, Data intensive text processing with Map-Reduce, Morgan & Claypool Publishers [book manuscript](http://beowulf.csail.mit.edu/18.337-2012/MapReduce-book-final.pdf)
* [IBM2012] IBM, Understanding Big Data, McGraw-Hill. [download](http://www-01.ibm.com/software/data/infosphere/hadoop/mapreduce/)
* [LAM2010], Lam, Hadoop in Action, Manning [web page](http://www.manning.com/lam/)
* [WHITE2012], White, Hadoop, the definitive guide, O'Reilly [web site](http://hadoopbook.com/)
* [GATES2011], Gates, Programming Pig, O'Reilly [web site](http://chimera.labs.oreilly.com/books/1234000001811/index.html)
* [ULLMAN2013], Ullman, Rajamaran, Mining of Massive Datasets, [web site](http://infolab.stanford.edu/~ullman/mmds.html)