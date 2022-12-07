# Hackathon, Manejo Visual

## Introducción

El objetivo de la competencia es crear una función de Python que maneje un Turtlebot basado en un feed de video.
![competencia](/assets/challenge.jpg "data workflow")

### Información y plantilla

Se provee una [plantilla](template.py) con una función de ayuda. También se provee [videos](videos) e [imágenes](images) de prueba grabadas con la cámara del robot.

![ robot ](/assets/camera_placement.jpg "Posición de la cámara desde el piso")

### Grupos

Los grupos pueden tener 6 integrantes o menos. Se les asignará un número en el proceso de inscripción.

## Competencia

### Recorrido

![ recorrido ](/assets/track.jpg "Un recorrido posible")

El recorrido será aproximadamente ⅛ del círculo central de UdeSA, la línea de partida y llegada estarán marcadas en el piso con cinta de papel blanca de 25mm.

### Prueba

El robot se lo inicia en una posición aleatoria en el tercio central de la pasarela y con un ángulo aleatorio de hasta 30° con el camino. Se enciende el robot detras de la linea de largada y se toma el tiempo desde que cruza la largada hasta la llegada. Si alguna de las ruedas del robot se salise del cemento o se queda trabado se termina la prueba.

### Puntaje

Si el vehículo pasa la línea de llegada sin tocar el pasto su puntaje será:

```python
puntaje = tiempo_de_recorrido[s]
```

En caso contrario

```python
puntaje = largo_pista[m] x 21 - dist_recorrida[m]
```

El puntaje más **bajo** gana la competencia

## Entregable

Se debe crear una función de la forma:

``` python
def visual_driver_group_x(image: np.ndarray):
    # YOUR CODE HERE
    return linear_vel_x, angular_vel_z
```

Recibe una imagen BGR como un numpy.ndarray de la forma: (480, 640, 3)

Debe devolver un comando de velocidad lineal y angular en m/s y Rad/s respectivamente.
El nombre de la función debe indicar el número de grupo.

![ driving ](/assets/robot.gif  "Driving with simple heuristic" )

### Ensayos

1 hora después de que se presente la consigna y hasta 10 minutos antes de la entrega se le dará tiempo para hacer pruebas a los grupos. Tendrán un slot de 5 minutos para pruebas y la precedencia de grupos estará dada por una cola donde luego de haber hecho pruebas pasan al final del orden de prioridad.

## Entrega

El entregable será un único archivo .py de menos de 500 líneas de código, que contenga la función pedida y todas las funciones auxiliares que hagan falta. Se puede asumir que las funciones provistas en la plantilla por la organización estarán presentes y no hace falta entregarlas. La entrega se hace por mail a: *aichallenge@udesa.edu.ar* antes de las 15:00hs detallando en el asunto del mail el número de grupo.

### Módulos

Se pueden usar las librerías estándar de Python y otras librerías comunes como: Numpy, CV2 v4.2.0, Pandas, etc.
Si se quiere usar alguna librería menos usual, testear que funcione en la computadora del robot.

## Links útiles

- Plataforma Kobuki: <http://kobuki.yujinrobot.com/about2/>
- Cámara: <https://www.logitech.com/es-ar/products/webcams/c925e-business-webcam.960-001075.html#specs>
