# Integrador-Concurrente-Trenes

<div align= "center"><img src= "https://funkypotato.com/images/2015/12/train-traffic-control.jpg" height="300" width="800"></div>

# Problema a resolver

En el centro de control de circulaciòn de trenes, hay una interfaz que se encarga de:<br>  
- Zonas de vias compartidas en donde hay que controlar la entrada de trenes por uno y otro lado.<br>

Estos tramos, están vacíos u ocupados con un tren. Cuando un tren quiere entrar y hay otro dentro, queda esperando hasta que la vía esté libre. Cuando un tren sale, este se lo notifica a los trenes que estén esperando. Las salidas de estos se van alternando si los dos tramos estan ocupados.

Como ya imaginamos esta interfaz tiene muchos años, y su actualizaciòn ha quedado en el pasado. Por consecuencia de esta negligencia todo la red de trenes, es una constante irregularidad y ha habido multiples reclamos de los pasajeros.<br>
Es por eso que te pedimos que hagas un nuevo diseño para que los trenes funcionen correctamente, y lo mas importante que no se generen accidentes mayores.

# Porque es necesaria y beneficiosa la concurrencia en este problema

Es necesaria porque permite sincronizar el cruce de trenes en estos tramos, si no la tendrìamos ocurririan accidentes y demoras.<br>
La concurrencia da el beneficio de optimizar de los recursos utilizados y actualiza un sistema antiguo que no tiene mucha dedicaciòn. 

# Ejemplo de porque se necesita la programaciòn concurrente en los contoles de circulacion de trenes
https://www.mcaleerlaw.com/estadisticas-de-accidentes-de-tren.html
