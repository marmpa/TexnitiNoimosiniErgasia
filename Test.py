from Tree import Node
from queue import Queue
import re

marios = Node(5)
marios.AddChild(marios)

fileName = input("Dose onoma xarti: ")
#marios.PrintMap(fileName+".txt")
marios.ProcessMap(fileName)


a = {Node([2,5]),Node([2,3])}

print(Node([2,1]) in a)

#print(Node(2) in a.queue())

def RemoveDictonaryKey(d, key):
    r = dict(d)
    del r[key]
    return r

def CreatePath(state,meta,goal):
    print("Inside create path")
    #print(meta)
    actionList = list()

    while meta[state] is not None:
        #print(state.data,meta[state].data)
        state = meta[state]
        actionList.append(state.data)

    actionList.reverse()
    return actionList

def BreadthFirstSearch():
    dataTable,mapPoints = marios.CreateMapDataTable(fileName)

    openSet = Queue()
    openSetCopy = {}


    visitedNodes = set()

    root,goal = Node(mapPoints['p']),mapPoints['g']
    meta = {}
    meta[root] = (None)


    openSet.put(root)
    openSetCopy[root] = None

    while not openSet.empty():

        subRoot = openSet.get()
        openSetCopy = RemoveDictonaryKey(openSetCopy,subRoot)


        if(subRoot.data==goal):
            #return CreatePath()
            #for i,x in meta.items():
            #    print(i.data,x.data)
            #print(mapPoints['g'],"yolo")
            #print(goal,"patatatata")
            print(root.data)
            print(goal)

            t = CreatePath(subRoot,meta,Node(goal))
            t.append(goal);
            marios.PrintFinishedMap(dataTable,t)
            return t

        for (action,child) in marios.ClosebyDataPoints(subRoot,dataTable).items():

            if(child in visitedNodes):
                continue

            if(child not in openSetCopy):
                meta[child] = subRoot
                print(child.data,subRoot.data,"abga aglias")

                openSet.put(child)
                openSetCopy[child]=child
        visitedNodes.add(subRoot)

print(BreadthFirstSearch(),'yes')
