Para la instalación y despliegue nos ubicamos en la carpeta de LAB4API (En una terminal con el comando cd), una vez ahí colocamos el siguiente comando:
uvicorn DataModel:app --reload
ya que todos los links y métodos están en ese archivo python y NO en el main.py
posteriormente colocamos en un navegador la siguiente direccion: http://127.0.0.1:8000/docs
ahí podremos ver 4 posibles links, 1 azul que es el get de prueba y 3 post que son los links del laboratorio:
/Data/predict que es el link encargado de recibir una sola linea y realizar la predicción
/Data/predict/list que es el link encargado de recibir varias lineas de datos y realizar una predicción a cada una de ellas
/Data/predict/Rcuadrado/list que es el link encargado de recibir varias lineas de datos que tienen la variable objetivo ya puesta y realizar una comparación
para calcular el r cuadrado, una métrica de desempeño. 

al clickear en cualquiera de estas,nos aparecerá un ejemplo del json que se espera, justo a la parte derecha de donde dice parameters está un botón que dice
Try it out, la undir ahí podemos modificar el json para añadir los valores que querramos ya que por defecto están en cero. una vez cambiado, presionamos el boton
azul que dice Execute.
Una vez pase esto, si deslizamos la pagina hacía abajo podremos ver el cuerpo de la respuesta, dependiendo de cada link este puede cambiar.
Esto es todo para poder correr el programa.

