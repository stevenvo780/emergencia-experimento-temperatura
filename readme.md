# Simulación de Propiedades Emergentes: La Temperatura

## Descripción General

Este script de Python tiene como objetivo demostrar cómo la temperatura puede ser considerada una propiedad emergente en un sistema de partículas. La simulación se basa en el concepto de que la temperatura es el resultado de las interacciones entre partículas individuales, en lugar de ser simplemente una propiedad que puede ser deducida de las partículas individualmente.

## Fórmulas Matemáticas

La "temperatura" en esta simulación se calcula usando la desviación estándar (sigma) de las velocidades (v) de las partículas:

\`\`\`
sigma = sqrt(sum((v_i - v_avg)^2) / n)
\`\`\`

Donde `n` es el número de partículas y `v_avg` es la velocidad media.

### Colisiones

Cuando dos partículas colisionan, sus nuevas velocidades se determinan a partir de la velocidad media de ambas, añadiendo una fluctuación aleatoria:

\`\`\`
new_speed1 = (speed1 + speed2) / 2 + fluctuation
new_speed2 = (speed1 + speed2) / 2 - fluctuation
\`\`\`

Donde `fluctuation` es un número aleatorio entre -2 y 2.

## Irreductibilidad

La irreductibilidad de las propiedades emergentes se refiere a la idea de que ciertas características de un sistema no pueden ser completamente explicadas o predichas mediante el análisis de sus componentes individuales. En este caso, la temperatura es una propiedad emergente porque cambia como resultado de las interacciones entre las partículas, y no puede ser simplemente deducida o predicha observando las partículas individualmente.

## Ejecución

El script comienza generando un sistema de 100 partículas con velocidades aleatorias. Luego, realiza 1000 colisiones aleatorias entre estas partículas y calcula la "temperatura" tanto antes como después de estas colisiones para demostrar cómo esta propiedad puede cambiar como resultado de las interacciones entre partículas.
