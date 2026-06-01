# Tema 4. Representación de datos

## 🗒️ Requisitos

Para realizar los ejercicios de este tema deberás haber realizado los ejercicios de los temas anteriores.

### Librerias

Para instalar las librerías necesarias para este tema debes ejecutar el siguiente comando en el terminal:

```bash
pip install -r requirements.txt
```

> Nota: El archivo 'requirements.txt' no está dentro de ninguna carpeta.

## 📝 Enunciados

Los ejercicios los encontrarás organizados por carpetas según los apartados del tema. Cada ejercicio se presentará en un fichero python, que incluirá un comentario con el enunciado del ejercicio. 

Los apartados del tema junto con los ejercicios son los siguientes:

| Apartado | Ejercicios                                                                          |
| -------- |-------------------------------------------------------------------------------------|
| a. Tipos de datos avanzados                        | [ej4a1](4a/ej4a1.py) [ej4a2](4a/ej4a2.py) [ej4a3](4a/ej4a3.py) [ej4a4](4a/ej4a4.py) |
| b. Gestión de memoria                              | [ej4b1](4b/ej4b1.py) [ej4b2](4b/ej4b2.py) [ej4b3](4b/ej4b3.py)                      |
| c. Objetos                                         | [ej4c1](4c/ej4c1.py) [ej4c2](4c/ej4c2.py) [ej4c3](4c/ej4c3.py) [ej4c4](4c/ej4c4.py) |
| d. Gestión de entrada/salida                       | [ej4d1](4d/ej4d1.py) [ej4d2](4d/ej4d2.py) [ej4d3](4d/ej4d3.py)                      |

Además, cada ejercicio irá acompañado de uno o varios tests para comprobar que tu solución es correcta. 

Cuando hayas propuesto una implementación para la función, ejecuta los tests para ver si tu solución es correcta. Si no pasa los tests, vuelve a intentarlo revisando los errores que te comentan los tests.

Una vez termines el ejercicio, deberás enviar tus cambios para que se registren en la plataforma y que puedan ser corregidos por tu profesor. 

Si tienes alguna duda sobre cómo ejecutar los tests o cómo enviar los cambios a GitHub, consulta el ejercicio del Tema 0. Si todavía tienes algun comentario o problema, puedes escribir tu consulta en la plataforma de Preguntas y Respuestas de la Escuela de Programación.

## 💻 Comandos
En la siguiente sección se presentan algunos comandos útiles para el desarrollo de la actividad. 

### Git

Con el fin de actualizar los repositorios locales con la última versión de código fuente, ejecute:

```bash
git pull
```

Para agregar los cambios realizados en los archivos, ejecute:

```bash
git add .
```

Para añadir un mensaje a los cambios realizados localmente, ejecute:

```bash
git commit -m "Mensaje"
```

Para sincronizar nuestras modificaciones con el repositorio remoto, ejecute:
```bash
git push
```

### Python

Para ejecutar las pruebas unitarias:
```bash
pytest 
```
En caso de tener algún problema, puedes probar ejecutar la función con la instrucción `python -m` delante, por ejemplo:

```bash
python -m pytest 
```
```bash
python -m pip install -r requirements.txt
```
Más información sobre cómo ejecutar las pruebas unitarias, consulte el ejercicio del tema 0.
