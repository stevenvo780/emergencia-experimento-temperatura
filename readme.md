# Simulación de Propiedades Emergentes: La Temperatura

## Descripción General

Este script de Python tiene como objetivo demostrar cómo la temperatura puede ser considerada una propiedad emergente en un sistema de partículas. La simulación se basa en el concepto de que la temperatura es el resultado de las interacciones entre partículas individuales, en lugar de ser simplemente una propiedad que puede ser deducida de las partículas individualmente.

## Fórmulas Matemáticas

La "temperatura" en esta simulación se calcula usando la desviación estándar (\( \sigma \)) de las velocidades (\( v \)) de las partículas:

\[
\sigma = \sqrt{\frac{\sum_{i=1}^{n} (v_i - \bar{v})^2}{n}}
\]

Donde \( n \) es el número de partículas y \( \bar{v} \) es la velocidad media.

### Colisiones

Cuando dos partículas colisionan, sus nuevas velocidades se determinan a partir de la velocidad media de ambas, añadiendo una fluctuación aleatoria:

\[
\text{new\_speed1} = \frac{\text{speed1} + \text{speed2}}{2} + \text{fluctuation}
\]
\[
\text{new\_speed2} = \frac{\text{speed1} + \text{speed2}}{2} - \text{fluctuation}
\]

Donde \( \text{fluctuation} \) es un número aleatorio entre -2 y 2.

## Irreductibilidad

La irreductibilidad de las propiedades emergentes se refiere a la idea de que ciertas características de un sistema no pueden ser completamente explicadas o predichas mediante el análisis de sus componentes individuales. En este caso, la temperatura es una propiedad emergente porque cambia como resultado de las interacciones entre las partículas, y no puede ser simplemente deducida o predicha observando las partículas individualmente.

En términos más filosóficos, esto resalta la naturaleza holística del sistema: el sistema como un todo tiene propiedades y comportamientos que no son aparentes cuando se examinan solo sus partes.

## Ejecución

El script comienza generando un sistema de 100 partículas con velocidades aleatorias. Luego, realiza 1000 colisiones aleatorias entre estas partículas y calcula la "temperatura" tanto antes como después de estas colisiones para demostrar cómo esta propiedad puede cambiar como resultado de las interacciones entre partículas.
