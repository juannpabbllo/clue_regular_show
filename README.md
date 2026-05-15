# Clue: Un Show Más

¡Bienvenido a **Clue: Un Show Más**! Un videojuego de deducción y misterio desarrollado completamente en Python utilizando la biblioteca gráfica `Tkinter`. 

En este juego de un solo jugador, asumes el rol de un detective en el parque. Papaleta ha sido hallado sin vida y tu deber es descubrir **quién fue, dónde ocurrió y qué arma se usó**. Tienes que investigar las coartadas de los personajes, revisar las locaciones y analizar las armas para llegar a la verdad. ¡Pero cuidado! Si te equivocas en tu acusación, Benson te despedirá de inmediato.

---

## Características

* **Interfaz Gráfica Personalizada (GUI):** Desarrollada con Tkinter, utilizando una paleta de colores moderna y atractiva.
* **Pistas Dinámicas:** El sistema de pistas cambia dependiendo de a quién o qué estés investigando. ¡No hay pistas directas, tendrás que usar tu lógica!
* **Visualización de Evidencia:** Muestra imágenes y descripciones de los sospechosos, armas y locaciones seleccionadas.
* **Sistema de Rejugabilidad:** Un botón de "Jugar de Nuevo" que reinicia el tablero, limpiando el registro y sorteando un nuevo caso aleatorio sin necesidad de cerrar el programa.
* **Pantallas de Resolución Épicas:** Ventanas emergentes de victoria o derrota que revelan la historia completa de cómo ocurrió el crimen.

---

## Tecnologías y Requisitos

Este proyecto está escrito en **Python 3**. Hace uso de las siguientes bibliotecas:
* `tkinter` (Viene instalada por defecto con Python).
* `Pillow` (Fork de PIL, necesario para el redimensionamiento y manejo de imágenes).
* `random` y `os` (Bibliotecas estándar de Python).

### Requisitos previos
Asegúrate de tener Python instalado en tu sistema. Además, necesitarás instalar la biblioteca `Pillow` ejecutando el siguiente comando en tu terminal:

```bash
pip install Pillow
