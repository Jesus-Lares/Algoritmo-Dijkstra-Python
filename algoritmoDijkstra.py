ValoresAcumulados={'a':None,'b':None,'c':None,'d':None,'e':None,'f':None,'g':None,'z':None}

grafo= {'a':{'b':2,'f':1},
        'b':{'a':2,'c':2,'d':2,'e':4},
        'c':{'b':2,'e':3,'z':1},
        'd':{'b':2,'e':4,'f':3},
        'e':{'b':4,'c':3,'d':4,'g':7},
        'f':{'a':1,'d':3,'g':5},
        'g':{'e':7,'f':5,'z':6},
        'z':{'c':1,'g':6},
        }

def algoritmoDijkstra(inicio,final,lista,grafo):
    T=[]
    v=inicio
    #Insertamos valores en la lista de valores acumulados
    for li in lista:
        lista[li]=100
        if(inicio==li):
            lista[li]=0
        T.append(li)
    
    #Se inicia un ciclo para saber el recorrido que sume un valor minimo y este terminara hasta que el vertice final este en la lista
    while(final in T):
        #Se inicializa el for para saber cual es el minimo valor acumulado dentro de la lista de valores acumulados
        minimo=100
        for x in T:     
            if(minimo>lista[x]):
                minimo=lista[x]
                v= x

        #Eliminamos el valor v de la lista T
        T=[x for x in T if x != v] 

        #Se busca el valor mas pequeño para la lista de valores acumulados y asi encontrar la mejor ruta
        for row in grafo[v]:   
            if lista[row]>lista[v]+grafo[v][row]:
                lista[row]=lista[v]+grafo[v][row]
                print([v,row],"\tvalor:",lista[v]+grafo[v][row])

    #Se inicia a calcular la ruta empezando por el valor final hasta el inicial
    valorFinal=lista[final]
    ruta=[final]
    v=final
    while (valorFinal>0):
        for row in grafo[v]:
            if valorFinal-grafo[v][row] == lista[row]:
                valorFinal= valorFinal-grafo[v][row]
                ruta.insert(0,row)
                v=row
                break
            
    return ruta

inicio=input("Digite el valor inicial: ")
final=input("Digite el valor final: ")

ruta=algoritmoDijkstra(inicio,final,ValoresAcumulados,grafo)

print("La ruta es ",ruta, ", el tamaño de la ruta es",len(ruta))