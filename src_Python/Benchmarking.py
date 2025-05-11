import time

class Benchmarking:
    
    @staticmethod
    def medir_tiempo( metodo, arreglo):
        inicio = time.perf_counter()
        metodo(arreglo)
        fin = time.perf_counter()
        return fin - inicio
