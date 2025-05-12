# 📌 Práctica de Algoritmos de Ordenamiento  

## Información General  
- **Título:** Comparación de Tiempos de Algoritmos de Ordenamiento  
- **Asignatura:** Estructura de Datos  
- **Carrera:** Computación  
- **Estudiante:** Yandri Sanchez, Mathias Añazco
- **Fecha:** 11 de mayo del 2025
- **Profesor:** Ing. Pablo Torres  

---

## 🛠️ Descripción  
Este proyecto analiza el **rendimiento** de cinco metodos de ordenamiento en Python, midiendo el tiempo que tardan en organizar arreglos de tamaños de grandes dimensiones. Se implementa en **Python** y utiliza **Matplotlib** para visualizar gráficamente los resultados.  

## Algoritmos Comparados
Los siguientes métodos de ordenamiento son evaluados:

- **Burbuja**
- **Burbuja Mejorado**
- **Selección**
- **Inserción**
- **Shell Sort**

Cada algoritmo se aplica sobre conjuntos de datos generados aleatoriamente.

## Tamaños de los Arreglos
Los experimentos se realizan con **cinco tamaños** distintos de arreglos:

- **5,000 elementos**
- **10,000 elementos**
- **30,000 elementos**
- **50,000 elementos**
- **100,000 elementos**

Para garantizar comparaciones equitativas, cada arreglo mayor conserva los primeros elementos del conjunto anterior y se expande con valores adicionales generados aleatoriamente.

## Estructura del Proyecto
El código está organizado en tres archivos principales:

- **`App.py`**: Coordina la ejecución del benchmarking, creando los arreglos de prueba, aplicando los algoritmos de ordenamiento y midiendo el tiempo de ejecución. También genera los gráficos comparativos con Matplotlib.  
- **`SorthMethods.py`**: Contiene la implementación de los algoritmos de ordenamiento, incluyendo Burbuja, Burbuja Mejorado, Selección, Inserción y Shell Sort, utilizados para evaluar el rendimiento en distintos tamaños de arreglos.  
- **`Benchmarking.py`**: Define la función para medir el tiempo de ejecución de los algoritmos, asegurando una evaluación precisa y estructurada de su eficiencia.  

## 📈 Metodología  
1. Se generaron conjuntos de datos aleatorios de diferentes tamaños, asegurando que los arreglos más grandes conservaran los primeros valores del conjunto anterior y se expandieran con elementos adicionales generados aleatoriamente.  
2. Cada conjunto de datos fue sometido a distintos algoritmos de ordenamiento, manteniendo una copia del arreglo original antes de cada ejecución para garantizar pruebas consistentes.  
3. Se midió el tiempo de ejecución de cada método, registrando los tiempos antes y después del proceso de ordenamiento mediante una medición precisa con `time.perf_counter()`.  
4. Los resultados obtenidos fueron almacenados y posteriormente visualizados mediante gráficos generados con **Matplotlib**, facilitando la comparación del rendimiento de los algoritmos.  
  

---

## 🚀 Ejecución  
Para ejecutar el proyecto:  

1. **Ejecutar el script:**  
   
   ```bash  
   python App.py  

## 📊 Gráfica de Comparación de los Metodos 
La siguiente imagen muestra la comparación visual de los tiempos de ejecución:  

![Impresiones de los tiempos de cada metodo](https://raw.githubusercontent.com/Mathias-Anazco/icc-est-u1-PracticPython/main/Impresiones.jpg)

## 🔍 Análisis de Cada Metodo  

### **Bubble Sort (Metodo Burbuja)**

#### **Conclusion**
- La comparación del algoritmo Burbuja muestra que, en términos de notación Big-O, su rendimiento está definido por ( O(n^2) ), lo que lo convierte en uno de los métodos menos eficientes para conjuntos de datos grandes. En el gráfico se observa un crecimiento exponencial en el tiempo de ejecución conforme el tamaño del arreglo aumenta, alcanzando aproximadamente 400 segundos para 100,000 elementos. Este comportamiento confirma que el ordenamiento Burbuja no es adecuado para estructuras de datos extensas, ya que su complejidad cuadrática hace que su rendimiento empeore significativamente en comparación con algoritmos más optimizados.


![Grafica de Bubble Sort](https://raw.githubusercontent.com/Mathias-Anazco/icc-est-u1-PracticPython/main/BubbleSort.jpg)

### **Bubble Optimized Sort (Metodo Burbuja Mejorado)**

#### **Conclusion**
- La comparación del algoritmo Burbuja Mejorado muestra una mejora significativa en rendimiento respecto al Burbuja tradicional. Aunque su complejidad sigue siendo ( O(n^2) ), la optimización introducida reduce el número de comparaciones innecesarias cuando el arreglo ya está parcialmente ordenado. En el gráfico se observa que, para tamaños de datos más grandes, el tiempo de ejecución es menor en comparación con el método Burbuja estándar, aunque sigue siendo considerablemente más lento que algoritmos más eficientes como Shell Sort. Esta mejora hace que Burbuja Mejorado sea una opción más viable en conjuntos de datos pequeños o casi ordenados, pero sigue siendo poco recomendable para estructuras de gran tamaño.

![Grafica de Bubble Optimized Sort](https://github.com/Mathias-Anazco/icc-est-u1-PracticPython/raw/main/BubbleOptimizedSort.jpg)

### **Selection Sort (Metodo De Seleccion)**

#### **Conclusion**
- La comparación del algoritmo Selección refleja su comportamiento característico basado en una complejidad de ( O(n^2) ). En el gráfico se observa un incremento constante en el tiempo de ejecución conforme el tamaño del arreglo aumenta, mostrando que este método se vuelve poco eficiente para conjuntos de datos grandes. Aunque el algoritmo asegura una ordenación precisa al seleccionar el elemento mínimo en cada iteración, su desempeño es considerablemente más lento en comparación con algoritmos más avanzados como Shell Sort. Para tamaños de hasta 100,000 elementos, el tiempo de ejecución se vuelve prohibitivo, lo que confirma que Selección no es una opción óptima para datos extensos.


![Grafica de Selection Sort](https://github.com/Mathias-Anazco/icc-est-u1-PracticPython/raw/main/SelectionSort.jpg)

### **Insertion Sort (Metodo De Inserccion)**

#### **Conclusion**
- El algoritmo Inserción demuestra ser eficiente en conjuntos de datos pequeños o parcialmente ordenados, debido a su forma de construcción progresiva del arreglo ordenado. Sin embargo, su complejidad ( O(n^2) ) hace que su rendimiento se vea afectado significativamente conforme el tamaño de los datos aumenta. En el gráfico se observa una tendencia de crecimiento en el tiempo de ejecución similar a otros algoritmos cuadráticos, aunque con una ligera ventaja en comparación con Burbuja y Selección. A pesar de su buen desempeño en arreglos pequeños, sigue siendo menos eficiente que métodos optimizados como Shell Sort, que logra reducir la cantidad de comparaciones y movimientos necesarios.

![Grafica de Insertion Sort](https://github.com/Mathias-Anazco/icc-est-u1-PracticPython/raw/main/InsertionSort.jpg)

### **Shell Sort (Metodo De Shell)**

#### **Conclusion**
- La comparación del algoritmo Ordenamiento de Shell destaca su superioridad respecto a los métodos de ordenamiento cuadráticos como Burbuja, Selección e Inserción. En el gráfico se observa que su crecimiento en tiempo de ejecución es más controlado, lo que refleja su eficiencia con una complejidad promedio de ( O(n \log n) ). A diferencia de los algoritmos menos optimizados, Shell Sort reduce significativamente la cantidad de comparaciones y movimientos al emplear intervalos progresivamente más pequeños. Este comportamiento lo convierte en una opción viable para manejar conjuntos de datos grandes sin que el tiempo de ejecución se incremente de manera prohibitiva.

![Grafica de Shell Sort](https://github.com/Mathias-Anazco/icc-est-u1-PracticPython/raw/main/ShellSort.jpg)


## 🔍 Análisis y Conclusiones

### **Conclusion de Yandri Sanchez**

El gráfico comparativo de los algoritmos de ordenamiento muestra una clara diferenciación en rendimiento a medida que el tamaño del arreglo aumenta. Burbuja y Burbuja Mejorado, con su complejidad (O(n^2)), presentan los tiempos de ejecución más altos, superando los 400 segundos para arreglos de 100,000 elementos, lo que evidencia su ineficiencia para conjuntos de datos grandes. Selección e Inserción mantienen una tendencia similar, aunque con una ligera mejora, permaneciendo dentro de rangos elevados de procesamiento.
Por otro lado, Shell Sort, con una complejidad de (O(n \log n)), muestra una diferencia notable en eficiencia, logrando tiempos significativamente menores en cada tamaño de prueba. En el gráfico se observa que su tiempo de ejecución se mantiene en valores mucho más reducidos en comparación con los demás algoritmos, consolidándose como la opción más óptima dentro de la prueba.
En conclusión, los métodos cuadráticos presentan un crecimiento exponencial en el tiempo de ejecución que los hace inviables para aplicaciones de gran escala, mientras que Shell Sort, con su estrategia de reducción de comparaciones, se posiciona como el algoritmo más eficiente para manejar grandes volúmenes de datos. 

### **Conclusion de Mathias Añazco**

Este proyecto compara la eficiencia de varios algoritmos de ordenamiento mediante la medición de sus tiempos de ejecución en diferentes tamaños de arreglos. Se implementaron Burbuja, Burbuja Mejorado, Selección, Inserción y Shell. 
Los resultados muestran que los algoritmos más simples como Burbuja y Selección son ineficientes en arreglos grandes, mientras que Shell Sort mejora significativamente el rendimiento al reducir la cantidad de intercambios y comparaciones necesarias.
El código ha sido estructurado en clases modulares, permitiendo una separación clara entre la generación de datos (App), la ejecución de los algoritmos (MetodosOrdenamiento) y la medición de tiempos (Benchmarking). Gracias a esta organización, el sistema permite futuras mejoras y la inclusión de nuevos métodos de ordenamiento sin afectar la estructura existente.
Este análisis ayuda a entender qué algoritmos son más rápidos y eficientes según el tipo de problema. Es importante conocer cuánto tiempo y recursos usa cada método para elegir el más adecuado en cada situación. 
El algoritmo Shell Sort es más eficiente que otros métodos básicos de ordenamiento debido a su estructura de complejidad O(n log n) en el mejor caso, lo que lo hace significativamente más rápido que Burbuja y Selección, que tienen una complejidad O(n²). 

![Grafica de Shell Sort](https://github.com/Mathias-Anazco/icc-est-u1-PracticPython/raw/main/ComparativaDeMetodos.jpg)
