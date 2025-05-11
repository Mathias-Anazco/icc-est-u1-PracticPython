from Benchmarking import Benchmarking
from SorthMethods import SorthMethods
import matplotlib.pyplot as plt
import random

class App:
    
    def __init__(self):
        self.sizes = [5000, 10000, 30000, 50000, 100000]
        self.arreglos = self.crear_arreglos()
        self.metodosOrden = SorthMethods()
        self.methods = {
            "Burbuja": self.metodosOrden.sortByBubble,
            "Burbuja Mejorado": self.metodosOrden.sortByBubbleOptimized,
            "Selección": self.metodosOrden.sortBySelection,
            "Inserción": self.metodosOrden.sortByInsertion,
            "Shell": self.metodosOrden.sortByShell
        }
        self.resultados = []
    
    def crear_arreglos(self):
        arreglos = []
        base_array = [random.randint(1, 100000) for _ in range(self.sizes[-1])]

        for i, size in enumerate(self.sizes):
            if i == 0:
                arreglos.append(base_array[:size])
            else:
                nuevos_valores = [random.randint(1, 100000) for _ in range(size - self.sizes[i-1])]
                arreglos.append(arreglos[i-1] + nuevos_valores)

        return arreglos
    def ejecutar_pruebas(self):
        for i, arreglo in enumerate(self.arreglos):
            tam = self.sizes[i]
            for nombre, metodo in self.methods.items():
                arreglo_copia = arreglo.copy()
                tiempo = Benchmarking.medir_tiempo(metodo, arreglo_copia)
                self.resultados.append((tam, nombre, tiempo))
                
    def imprimir_resultados(self):
        for tam, nombre, tiempo in self.resultados:
            print(f"Tamaño: {tam}, Algoritmo: {nombre}, Tiempo: {tiempo:.6f} segundos")
            
    def generar_graficos(self):
        """Genera gráficos de rendimiento para cada método y un gráfico comparativo general."""
        plt.figure(figsize=(10, 6))
        datos_por_metodo = {}

        for tam, nombre, tiempo in self.resultados:
            if nombre not in datos_por_metodo:
                datos_por_metodo[nombre] = {"sizes": [], "tiempos": []}
            datos_por_metodo[nombre]["sizes"].append(tam)
            datos_por_metodo[nombre]["tiempos"].append(tiempo)
            
        for nombre, datos in datos_por_metodo.items():
            plt.figure(figsize=(8, 5))
            plt.plot(datos["sizes"], datos["tiempos"], marker="o", linestyle="-", label=nombre)
            plt.xlabel("Tamaño del arreglo")
            plt.ylabel("Tiempo de ejecución (s)")
            plt.title(f"Rendimiento del algoritmo {nombre}")
            plt.legend()
            plt.grid()
            plt.show()
            
             # Gráfico combinado
        plt.figure(figsize=(10, 6))
        for nombre, datos in datos_por_metodo.items():
            plt.plot(datos["sizes"], datos["tiempos"], marker="o", linestyle="-", label=nombre)
        
        plt.xlabel("Tamaño del arreglo")
        plt.ylabel("Tiempo de ejecución (s)")
        plt.title("Comparación de algoritmos de ordenamiento")
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    app = App()
    app.ejecutar_pruebas()
    app.imprimir_resultados()
    app.generar_graficos()