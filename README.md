# lista-tareas
Aplicación de gestión de tareas en Python con almacenamiento en JSON desde terminal

## Administrador de Tareas en Terminal

Un programa simple en Python para gestionar tareas desde la terminal. Permite agregar, ver y completar tareas, guardando todo en un archivo JSON.

## ¿Qué hace este programa?

Este programa te permite agregar tareas nuevas con una descripción, ver todas tus tareas con su estado (completada o pendiente), marcar tareas como completadas y guardar automáticamente tus tareas en un archivo `tareas.json`.

## Cómo usarlo

Ejecuta el programa con: `python lista_tareas.py`. Verás un menú con las opciones: 1. mostrar tareas, 2. agregar tareas, 3. completar tarea y 4. salir. Presiona el número correspondiente a la acción que deseas realizar. Las tareas se muestran con su número de índice y su estado: ✅ para tareas completadas y ⬜ para tareas pendientes.

## Ejemplo de uso

Al ejecutar el programa y elegir la opción 2, te pedirá el nombre de la tarea, por ejemplo "Comprar leche". Luego al elegir la opción 1 verás "1 ⬜ Comprar leche". Si eliges la opción 3 y escribes el índice 1, la tarea se marcará como completada. Al volver a mostrar las tareas verás "1 ✅ Comprar leche". Para salir del programa elige la opción 4.

## Archivos del proyecto

El proyecto consta de dos archivos: `lista_tareas.py` que contiene todo el código del programa, y `tareas.json` que se crea automáticamente al ejecutar el programa y guarda todas tus tareas en formato JSON. No requiere librerías externas. Solo necesitas tener instalado Python 3.6 o superior.

## Lo que aprendí

Durante este proyecto practiqué:

- Funciones.
- Listas y diccionarios.
- Lectura y escritura de archivos JSON.
- Manejo de excepciones.
- Organización del código en módulos reutilizables.
