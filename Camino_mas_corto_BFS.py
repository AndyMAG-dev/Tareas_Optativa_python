#Andy Martíenez-Aparicio González  #41 Grupo-21
#Tarea, camino mas corto con BFS

from collections import deque

def camino_mas_corto(laberinto, entrada, salida):
    
    movimientos = [(0, -1), (0, 1), (-1, 0), (1, 0)]    # esto son los movimientos que podemos hacer
    
    visitados = [[False]*len(laberinto[0]) for _ in range(len(laberinto))]  # creamos una matriz del mismo tamaño del laberitno pero con todo False
    
    cola = deque([([entrada], entrada)])  # creamos una cola para aplicar el BFS, inicializada con la entrada del laberinto
    
    caminos_validos = []   #lista para guardar los camino
    
    while cola:    #while que se va a repetir mientras la cola tenga elementos
        
        camino_actual, posicion_actual = cola.popleft()     #en cada iteracion sacamos un elemento de la cola
        
        if posicion_actual == salida:
            caminos_validos.append(camino_actual)          #if para comprobar si ya finalizamos
            return caminos_validos                         #si donde estamos es la salida ya concluye
        
        x_actual, y_actual = posicion_actual
        
        
        for x_mov, y_mov in movimientos:        #for para realizar todos los movimientos posibles en donde nos encontramos
            x_nueva, y_nueva = x_actual + x_mov, y_actual + y_mov
            
            #con este if berificamos si la posicion es valida
            if (0 <= x_nueva < len(laberinto) and 0 <= y_nueva < len(laberinto[0]) and not visitados[x_nueva][y_nueva] and laberinto[x_nueva][y_nueva] == 0):
              
                visitados[x_nueva][y_nueva] = True                  #si es valida lo marcamos true y_actual lo agregamos a la cola
                cola.append((camino_actual + [(x_nueva, y_nueva)], (x_nueva, y_nueva)))
    
    return caminos_validos


laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

entrada = (0, 0)
salida = (4, 4)

camino = camino_mas_corto(laberinto, entrada, salida)
print(f"camino más corto: {camino}")