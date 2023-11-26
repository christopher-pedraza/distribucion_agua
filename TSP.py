import random
import Graph

'''
graph[id] = {
            "x": float(x),
            "y": float(y),
            "fuente": True if fuente == "1" else False,
            "vecinos": [],
            "sector": None,
            "oficina": False,
            "esMasLejano": False,
        }
'''

test_case={}
# obten el grafo
graph=Graph.create_graph("grafos/FOS.txt")[0]



for id_,dictionary in graph.items():
    test_case[id_]={}
    for vecino in dictionary["vecinos"]:
        # vecino es diccionario
        test_case[id_][vecino["id"]]=vecino["longitud"]

print("---1")
print("GRAPH:",graph)
print("TC",test_case)
#print("TEST CASE:", test_case)

'''
test_case={
    1: {2: 22, 3: 15, 4: 12, 5: 20, 6: 25},
    2: {4: 22, 5: 24, 6: 19},
    3: {1: 15, 2: 18, 4: 14, 5: 17, 6: 22},
    4: {1: 12, 2: 22, 3: 14,7:12},
    5: {2: 24, 7:2,4: 16, 6: 11},
    6: {1:22,3: 22, 4: 21, 5: 11},
    7: {4:17}
}
'''


def vibe_check(my_items,temp,prev):
    my_items.sort(key=lambda x: x[1])

    i=0
    while ((random.randrange(0,9)>temp) or my_items[i][0]==prev) and i<len(my_items)-1:
        i+=1
    #print("VIBE:",prev,my_items[i])
    return my_items[i]



def S_builder(temp):
    visited=set()
    visited.add(1)
    S=[(1,0),(1,0)]

    testing=[]


    iterations=0
    # n node travels
    while len(visited)<len(test_case):
        my_items=[]
        old_items=[]



        for node,cost in test_case[S[-1][0]].items():
            if node not in visited:
                my_items.append((node,cost))
            old_items.append((node,cost))


        #my items list of (node,cost)

        #Hay al menos un nodo no visitado adyacente al nodo actual: 
        if my_items:
            #llevame al nodo no visitado con menor costo, a menos que la suerte/temperatura 
            # indique que uno con 
            #mayor peso
            S.append(vibe_check(my_items,temp,S[-2][0]))
            visited.add(S[-1][0])
            testing.append(S[-1][0])
        
        #Si no hay un nodo no visitado, regresate a uno
        else:
            S.append(vibe_check(old_items,temp,S[-2][0]))
            testing.append(S[-1][0])
        
        #print("jump:", iterations,"---",S, "set:", len(visited),"\n")
        iterations+=1
        '''
        if iterations>60:
            listy=[]
            for i in range(1,21):
                if i not in visited:
                    listy.append(i)
            print("not visited:" , listy , "\n")
            sys.exit()
        '''

    #Salimos del while anterior cuando solo falta regresar a home.
    while S[-1][0] != 1:
        old_items=[]
        for node,cost in test_case[S[-1][0]].items():
            old_items.append((node,cost))
            #Hay un camino a home
            if node==1:
                S.append((node,cost))
                break
        
        #escogemos un movimiento repetido al asar.    
        if S[-1][0] != 1:
            S.append(vibe_check(old_items,temp,S[-2][0]))




    #Regresamos la respuesta.
    total_cost=0
    for s in S:
        total_cost+=s[1]

    return [S,total_cost]
        

def monte_carlo(temp,temp_cut,temp_min,best_so_far):
    while temp>temp_min:
        current=S_builder(temp)
        if current[1]<best_so_far[1]:
            best_so_far=current
        temp=temp-temp_cut
    return best_so_far

best_so_far=S_builder(7)



print("very low budget",monte_carlo(7,1,5,best_so_far)[1])
print("low budget",monte_carlo(7,1,2,best_so_far)[1])
print("medium budget",monte_carlo(7,0.5,1,best_so_far)[1])
print("great budget: ",monte_carlo(7,0.2,0.5,best_so_far)[1])
print("ultra budget: ",monte_carlo(7,0.01,0.5,best_so_far)[1])
print("meta budget",monte_carlo(7,0.002,0.02,best_so_far)[1])
print("budget royale",monte_carlo(7,0.001,0.01,best_so_far)[1])

