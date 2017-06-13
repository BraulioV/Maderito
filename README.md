# Maderito
A sumo robot for the subject ___Sistemas con Microprocesadores___ (_Microprocessor-based Systems_) of UGR with Arduino and Raspberry Pi. 

## Guía para los pines 

### Pines digitales
- 3, 9: ENABLE (MOTORES) Controlan el PWM de los motores, B los de la izda y A los de la derecha
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
La comunicación entre ambas se hará mediante el puerto serial de Arduino. En Python (Raspberry Pi) hemos usado la librería `serial`.

Hemos establecido el siguiente "protocolo" de comunicación:

* Arduino envía el carácter 'm' (_moving_) a RPi: indica que el robot se está moviendo.

* Arduino envía el carácter 's' (_stopped_) a Rpi: indica que el robot ha dejado de moverse.

* Rpi envía el carácter 'l' (_left_) a Arduino: indica que el robot debe girar a la izquierda.

* Rpi envía el carácter 'r' (_right_) a Arduino: indica que el robot debe girar a la derecha.

* Rpi envía el carácter 'q' (_quiet_) a Arduino: indica que el robot está quieto.

Los mensajes 's' y 'm' son necesarios porque mientras que el robot esté en movimiento, el algoritmo de visión por computador no funcionará correctamente. 
