# Maderito
A sumo robot for the subject ___Sistemas con Microprocesadores___ (_Microprocessor-based Systems_) of UGR with Arduino and Raspberry Pi. 

## Guía para los pines 

### Pines digitales
- 3, 9: ENABLE (MOTORES) Controlan el PWM de los motores, B los de la izquierda y A los de la derecha
- 8: echo (ultrasonidos)
- 2: trigger (ultrasonidos)
- pin 10: cny70 delante izquierda
- pin 11: cny70 delante derecha
- pin 12: cny70 detrás izquierda
- pin 13: cny70 detrás derecha

### Pines analgicos
- 4, 5, 6, 7: motores

## Algoritmo interno

1. Por reglas del juego, permanecer 3 segundos quieto. Medir distancia exacta al rival.
2. Una vez pasen los 3 segundo tenemos dos opciones:
    - Ir a por el rival con máxima potencia.
    - Quedarse esperando a que venga el rival.
      * Cuando el rival esté más cerca de una determinada distancia, esquivar.

En principio, optamos por la estrategia de esquivar al rival, por lo que la cámara irá en el lateral del robot.

## Comunicación Arduino-Raspberry Pi
La comunicación entre ambas se hará mediante el puerto serie de Arduino. En Python (Raspberry Pi) hemos usado la librería `serial`.

Hemos establecido el siguiente "protocolo" de comunicación:

* Arduino envía el carácter 'm' (_moving_) a RPi: indica que el robot se está moviendo.

* Arduino envía el carácter 's' (_stopped_) a Rpi: indica que el robot ha dejado de moverse.

* Rpi envía el carácter 'l' (_left_) a Arduino: indica que el robot debe girar a la izquierda.

* Rpi envía el carácter 'r' (_right_) a Arduino: indica que el robot debe girar a la derecha.

* Rpi envía el carácter 'q' (_quiet_) a Arduino: indica que el robot está quieto.

Los mensajes 's' y 'm' son necesarios porque mientras que el robot esté en movimiento, el algoritmo de visión por computador no funcionará correctamente. 

---

# English version

## Pin's Guide

### Digital Pins

- 3,9: ENABLE (MOTORS) Control the motors's PWM, B the left ones and A the right ones.
- 8: echo (ultrasounds)
- 2: trigger (ultrasounds)
- pin 10: cny70 front-left
- pin 11: cny70 front-right
- pin 12: cny70 back-left
- pin 13: cny70 back-right

### Analogical Pins
- 4, 5, 6, 7: motors

## Internal Algorithm

1. Because of the game's rules, stay still for 3 seconds. Measure the exact distance to the rival.
2. Once the 3 seconds have passed we have two options:
    - Go to the rival with maximum power.
    - Stay still waiting for the rival to come toward us.
        * When the rival is closer than a set distance, dodge.

At the beggining, we choosed the strategy of dodging the rival, that's why the camara will be at the lateral side of the robot.

## Comunication Arduino-Raspberry Pi

The comunication between the Arduino and the Raspberry will be performed using the serial port of the Arduino. In Python (Raspberry pi) we have used the librarby `serial`.

We have stablished the following communication's "protocol":

* Arduino sends the caracter 'm' (_moving) to Rpi: indicate that the robot is moving.

* Arduino sends the caracter 's' (_stopped_) to Rpi: indicate that the robot has stopped moving.

* Rpi sends the caracter 'l' (_left_) to Arduino: indicate that the robot must turn to the left.

* Rpi sends the caracter 'r' (_right_) to Arduino: indicate that the robot must turn to the right.

* Rip sends the caracter 'q' (_quit_) to Arduino: indicate that the robot is stand still.

The messages 's' and 'm' are necessary because while the robot is moving, the computer vision's algorithm doesn't work properly.
