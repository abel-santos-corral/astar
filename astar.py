import heapq

class Nodo:
    def __init__(self, estado, padre=None, costo=0, heuristica=0):
        self.estado = estado
        self.padre = padre
        self.costo = costo
        self.heuristica = heuristica
        self.f = costo + heuristica
    
    def __lt__(self, otro):
        return self.f < otro.f

def heuristica(estado):
    heuristica_valores = {
        (4,3,2,1): 6,
        (4,3,1,2): 5,
        (4,1,3,2): 4,
        (1,4,3,2): 3,
        (1,3,4,2): 2,
        (1,3,2,4): 1,
        (1,2,3,4): 0
    }
    return heuristica_valores.get(tuple(estado), 10)

def generar_sucesores(nodo):
    estado = nodo.estado
    sucesores = []
    for i in range(len(estado) - 1):
        nuevo_estado = estado[:]
        nuevo_estado[i], nuevo_estado[i+1] = nuevo_estado[i+1], nuevo_estado[i]
        nuevo_nodo = Nodo(nuevo_estado, nodo, nodo.costo + 1, heuristica(nuevo_estado))
        sucesores.append(nuevo_nodo)
    return sucesores

def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo.estado)
        nodo = nodo.padre
    return camino[::-1]

def busqueda_Astar():
    estado_inicial = [4,3,2,1]
    objetivo = [1,2,3,4]
    nodo_inicial = Nodo(estado_inicial, None, 0, heuristica(estado_inicial))
    frontera = []
    heapq.heappush(frontera, nodo_inicial)
    explorados = set()
    
    while frontera:
        nodo_actual = heapq.heappop(frontera)
        if nodo_actual.estado == objetivo:
            return reconstruir_camino(nodo_actual)
        explorados.add(tuple(nodo_actual.estado))
        for sucesor in generar_sucesores(nodo_actual):
            if tuple(sucesor.estado) not in explorados:
                heapq.heappush(frontera, sucesor)
    return None

resultado = busqueda_Astar()
print("Camino encontrado:", resultado)
