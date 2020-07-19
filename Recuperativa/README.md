# Cómo ejecutar los *tests*

Junto a este README, se subieron el archivo `test_privado.py`, la carpeta `tests/` y archivos adicionales en la carpeta `datos/`. El archivo `test_privado.py` ejecuta el código de los módulos `cargar_cursos` y `consultas`, con distintos argumentos y esperando outputs específicos, los que se encuentran serializados en distintos archivos en la carpeta `tests/`.

**¿Cómo funciona?** Para poder evaluar tu tarea, coloca el archivo `test_privado.py` y las carpetas `datos/` y `test/` dentro de la carpeta `Recuperativa/` en tu repositorio personal. Una vez que ejecutas el archivo `test_privado.py`, este importa los archivos serializados dentro de `test/`, donde se almacenan los argumentos y output esperados para cada una de las funciones, además de cargar los datos de `datos/` cuando corresponda. 

**¿Por qué se usó `pickle` para serializar los archivos de *test*?** Al serializar con `json`, Python convierte tuplas y listas a un mismo tipo (*array* o arreglo), por lo que en un archivo JSON estos no se pueden distinguir, causando problemas al corregir (por ejemplo, al traducir módulos, donde hay una lista de tuplas).

> Debido a que no es fácil obtener los argumentos utilizados en cada una de las funciones, a continuación dejamos las llamadas utilizadas para evaluar cada entrega, para poder confirmar el resultado de la evaluación.

### Argumentos para cada *test*

### `traducir_modulos`

* `traducir_modulos("CLAS;TES;LAB;TER;PRA;AYU;TAL")`: (0) Sin modulos
* `traducir_modulos("AYU;CLAS#V:3;TES;TAL;LAB;PRA;TER")`: (1) Un módulo, un día
* `traducir_modulos("PRA#J,V:2;TER;TES;AYU;CLAS;TAL;LAB")`: (2) Un módulo, dos días
* `traducir_modulos("TES;AYU;CLAS;PRA;LAB#M,J:7;TER;TAL#L,M:2")`: (3) Un módulo, dos días (múltiples veces)
* `traducir_modulos("LAB;PRA;TER;TAL;TES#L,W,V:1;AYU;CLAS")`: (4) Un módulo, tres dias
* `traducir_modulos("TAL;AYU#L:5,6;CLAS;TES;PRA;LAB;TER")`: (5) Dos módulos, un dia
* `traducir_modulos("TES;LAB;TAL;TER;PRA;AYU;CLAS#V:5,6,7")`: (6) Tres módulos, un dia
* `traducir_modulos("AYU#W,J:7,8;PRA;CLAS;LAB;TER;TES;TAL")`: (7) Dos módulos, dos dias
* `traducir_modulos("TES#M,J:3,4;LAB;TER;AYU;PRA;CLAS#M,J:1,2;TAL")`: (8) Dos módulos, dos dias (múltiples veces)
* `traducir_modulos("PRA;TES;TAL#M,W,J:3,4,5;AYU;LAB;TER#M,W,J:3,4,5;CLAS")`: (9) Tres módulos, Tres dias
* `traducir_modulos("CLAS#V:3;TES#M,J:3,4;LAB#L:1;TER#J:7,8;PRA#W:2;AYU#M:1;TAL#M,J:2")`: (10) Todos los tipos de modulo

### `cargar_cursos`

* `cargar_cursos("vacio")`: (0) JSON vacío
* `cargar_cursos("sin_prerreq")`: (1) Solo un curso
* `cargar_cursos("prerreq_dcc")`: (2) Con un prerrequisito IIC
* `cargar_cursos("prerreq_dcc_2")`: (3) Con múltiples prerrequisitos IIC
* `cargar_cursos("prerreq_no_dcc")`: (4) Con un prerrequisito no IIC
* `cargar_cursos("prerreq_no_dcc_2")`: (5) Con múltiples prerrequisitos no IIC
* `cargar_cursos("prerreq_full")`: (6) Con prerrequisitos IIC y no IIC
* `cargar_cursos("2020-1")`: (7) Semestre entregado
* `cargar_cursos("2019-2")`: (8) Semestre entregado
* `cargar_cursos("2019-1")`: (9) Semestre entregado

### `filtrar_por_prerrequisitos`

En esta función, se utilizaron los cursos del semestre **2019-2**, por lo que la variable `dicc_cursos` se refiere al diccionario de cursos de ese semestre:

* `filtrar_por_prerrequisitos(dicc_curso["IIC2714"], dicc_curso)`: (0) Curso sin requisitos
* `filtrar_por_prerrequisitos(dicc_curso["IIC3113"], dicc_curso)`: (1) Curso con IIC este semestre
* `filtrar_por_prerrequisitos(nuevo_curso, dicc_curso)`: (2) Curso con IIC no este semestre, donde `nuevo_curso` es un curso (`"IIC2026"`) modificado para tener como prerrequisito solo al curso `"IIC1103"`
* `filtrar_por_prerrequisitos(dicc_curso["IIC2233"], dicc_curso)`: (3) Curso con IIC este y no este semestre
* `filtrar_por_prerrequisitos(dicc_curso["IIC3263"], dicc_curso)`: (4) Curso con IIC no este semestre y no IIC
* `filtrar_por_prerrequisitos(dicc_curso["IIC1253"], dicc_curso)`: (5) Curso con requisito no IIC
* `filtrar_por_prerrequisitos(dicc_curso["IIC2433"], dicc_curso)`: (6) Curso con todo tipo de requisitos
* `filtrar_por_prerrequisitos(dicc_curso["IIC2733"], dicc_curso)`: (7) Curso con todo tipo de requisitos

### `filtrar_por_cupos`

En esta función, se utilizaron los cursos del semestre **2020-1**, por lo que la variable `dicc_cursos` se refiere al diccionario de cursos de ese semestre:

* `filtrar_por_cupos(10, dicc_curso)`: (0) Busqueda simple
* `filtrar_por_cupos(16, dicc_curso)`: (1) Busqueda simple
* `filtrar_por_cupos(17, dicc_curso)`: (2) Apuntando al exploratorio, no debería estar en output
* `filtrar_por_cupos(25, dicc_curso)`: (3) Busqueda simple
* `filtrar_por_cupos(50, dicc_curso)`: (4) Busqueda simple
* `filtrar_por_cupos(7777, dicc_curso)`: (5) Debería ser vacío

### `filtrar_por`

En esta función, se utilizaron los cursos del semestre **2020-1**, por lo que la variable `dicc_cursos` se refiere al diccionario de cursos de ese semestre:

* `filtrar_por("llave_que_no_existe", "", dicc_curso)`: (0) Caso nulo (dict vacío)
* `filtrar_por("Nombre", "", dicc_curso)`: (1) Búsqueda vacía
* `filtrar_por("Nombre", "Inteligencia Artificial", dicc_curso)`: (2) Buscar curso simple
* `filtrar_por("Nombre", "inteligencia artificial", dicc_curso)`: (3) Buscar curso simple (solo minusculas)
* `filtrar_por("Nombre", "INTELIGENCIA artificial", dicc_curso)`: (4) Buscar curso simple (mayusculas y minusculas)
* `filtrar_por("Nombre", "CIA art", dicc_curso)`: (5) Nombre parcial
* `filtrar_por("Nombre", "nombre_no_valido", dicc_curso)`: (6) Debería ser vacío
* `filtrar_por("Profesor", "", dicc_curso)`:  (7) Busqueda vacía
* `filtrar_por("Profesor", "Luis", dicc_curso)`:  (8) Buscar nombre simple
* `filtrar_por("Profesor", "luis", dicc_curso)`:  (9) Buscar nombre simple (solo minusculas)
* `filtrar_por("Profesor", "LUIS", dicc_curso)`: (10) Buscar nombre simple (solo mayúsculas)
* `filtrar_por("Profesor", "Baier jor", dicc_curso)`: (11) Nombre parcial (profe en curso de multiples)
* `filtrar_por("Profesor", "dal gabriel", dicc_curso)`: (12) Nombre parcial (solo una sección)
* `filtrar_por("Profesor", "Hans, Garrido", dicc_curso)`: (13) Múltiples profesores
* `filtrar_por("Profesor", "profesor_no_valido", dicc_curso)`: (14) Debería ser vacío
* `filtrar_por("NRC", "", dicc_curso)`: (15) Busqueda vacía
* `filtrar_por("NRC", "15386", dicc_curso)`: (16) Buscar NRC simple
* `filtrar_por("NRC", "15", dicc_curso)`: (17) Buscar NRC parcial
* `filtrar_por("NRC", "nrc_no_valido", dicc_curso)`: (18) Debería ser vacío
* `filtrar_por("Sigla", "", dicc_curso)`: (19) Busqueda vacía
* `filtrar_por("Sigla", "IIC2233", dicc_curso)`: (20) Buscar sigla simple
* `filtrar_por("Sigla", "iic22", dicc_curso)`: (21) Buscar sigla simple (solo minusculas)
* `filtrar_por("Sigla", "Iic22", dicc_curso)`: (22) Buscar sigla simple (mayusculas y minusculas)
* `filtrar_por("Sigla", "MAT1203", dicc_curso)`: (23) Debería ser vacío
* `filtrar_por("Sigla", "sigla_no_valida", dicc_curso)`: (24) Debería ser vacío

### `filtrar_por_modulos`

En esta función, se utilizaron los cursos del semestre **2019-2**, por lo que la variable `dicc_cursos` se refiere al diccionario de cursos de ese semestre:

* `filtrar_por_modulos([("W", 6)], dicc_curso)`: (0) Busqueda simple
* `filtrar_por_modulos([("V", 1)], dicc_curso)`: (1) Busqueda simple
* `filtrar_por_modulos([("J", 4), ("J", 5)], dicc_curso)`: (2) Busqueda simple
* `filtrar_por_modulos([("M", 4), ("J", 4), ("J", 5)], dicc_curso)`: (3) Busqueda simple
* `filtrar_por_modulos([("L", 1), ("L", 2), ("L", 3), ("L", 4), ("L", 5), ("L", 6), ("L", 7), ("L", 8)], dicc_curso)`: (4) Busqueda simple
* `filtrar_por_modulos([("L", 1), ("M", 2), ("W", 3), ("V", 5), ("V", 6), ("J", 7), ("W", 8)], dicc_curso)`: (5) Busqueda simple

### `filtrar_por_cursos_compatibles`

En esta función, se utilizaron los cursos del semestre **2019-1**, por lo que la variable `dicc_cursos` se refiere al diccionario de cursos de ese semestre:

* `filtrar_por_cursos_compatibles([], dicc_curso)`: (0) Horario vacío
* `filtrar_por_cursos_compatibles(["21114"], dicc_curso)`: (1) Horario con J8
* `filtrar_por_cursos_compatibles(["10798"], dicc_curso)`: (2) Curso con secciones que no topan entre sí
* `filtrar_por_cursos_compatibles(["10747"], dicc_curso)`: (3) Todas las secciones de un curso (no debería estar en output)
* `filtrar_por_cursos_compatibles(["10760", "10754"], dicc_curso)`: (4) Horario con topes entre sí
* `filtrar_por_cursos_compatibles(nrcs, dicc_curso)`: (5) Horario con todos los nrc (debería ser vacío)