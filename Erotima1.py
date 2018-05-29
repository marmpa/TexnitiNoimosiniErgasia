from Tree import Node
from queue import Queue
import re

from pptree import print_tree

marios = Node(5)
marios.AddChild(marios)

fileName = input("Dose onoma xarti: ")
#marios.PrintMap(fileName+".txt")
marios.ProcessMap(fileName)


a = {Node([2,5]),Node([2,3])}

print(Node([2,1]) in a)
dataTable,mapPoints = marios.CreateMapDataTable(fileName)

#print(Node(2) in a.queue())
def PrintNode(node):
    #print(node)
    try:
        for x in node:
            print(x.data)
    except Exception:
        for x in node:
            print(x)
def SetToList(oSet):
    a = []
    for x in oSet:
        a.append(x)
    return a
def NodeToList(oSet):
    a=[]
    for x in oSet:
        a.append(x.data)
    return a

def RemoveDictonaryKey(d, key):
    r = dict(d)
    del r[key]
    return r

def PrintTreeView(Tree,depth=0):
    if(len(Tree.children)==0):
        return (int)(100/depth)
    if Tree:
        for x in Tree.children:
            if x.data is not None:
                print(PrintTreeView(x,depth+10),x.data,end="")
        print()
    return 1*depth

def PrintSubRoot(subRoot,num=0):
    #print("hello",num)
    if subRoot:

        for x in subRoot.children:
            #print("geia")
            PrintSubRoot(x,num+1)
            print("  Child",x.data,"gaol",num,"Parent",subRoot.data)
            #for y in x.children:
            #    print("   ",y.data,"gaol")
    else:
        print("Parent",subRoot.data)
def FindPath(meta,start):
    print("Inside create path2")

    actionList = list()

    while meta is not None:
        actionList.append(meta.data)
        meta = meta.parent

    actionList.reverse()
    print("steps:",len(actionList))
    return actionList


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
    metaNodes = set()

    root,goal = Node(mapPoints['p']),mapPoints['g']

    visitedNodes.add(root)
    metaNodes.add(root)
    head = root


    openSet.put(root)
    openSetCopy[root] = None

    while not openSet.empty():


        subRoot = openSet.get()
        meta = subRoot
        openSetCopy = RemoveDictonaryKey(openSetCopy,subRoot)

        if(subRoot.data==goal):
            #return CreatePath()
            #print(mapPoints['g'],"yolo")
            #print(goal,"patatatata")
            #print(root.data)
            #print(goal)
            #meta.AddChild(subRoot)
            t = FindPath(meta,root)
            print("Lisi Breadth First!")
            marios.PrintFinishedMap(dataTable,t)
            #PrintSubRoot(head)
            #t = CreatePath(subRoot,meta,Node(goal))
            #t.append(goal);
            #marios.PrintFinishedMap(dataTable,t)
            #PrintTreeView(root)
            #return t
            return visitedNodes

        #print("fores",subRoot.data)
        for (action,child) in marios.ClosebyDataPoints(subRoot,dataTable).items():

            #print(action,child.data,"terastiaabga",len(marios.ClosebyDataPoints(subRoot,dataTable).items()))
            if(child in visitedNodes):
                continue

            if(child not in openSetCopy):


                if(child not in metaNodes):
                    #for i in metaNodes:
                        #print(i.data,"visited","child",child.data)
                    #print("parent:",subRoot.data,"child:",child.data)
                    meta.AddChild(child)
                    metaNodes.add(child)



                #metaNodes.add(child)

                #print("    child",child.data,"parent",subRoot.data,"yahoo")

                openSet.put(child)
                openSetCopy[child]=child
        visitedNodes.add(subRoot)
        #meta = subRoot
def DepthFirstSearch():
    dataTable,mapPoints = marios.CreateMapDataTable(fileName)

    openSet = []
    visitedNodes = set()
    metaNodes = set()

    root,goal = Node(mapPoints['p']),mapPoints['g']



    openSet.append(root)
    metaNodes.add(root)

    while openSet:
        subRoot = openSet.pop()
        meta = subRoot

        if(subRoot.data==goal):
            t= FindPath(meta,root)
            print("Lisi Depth First!")
            marios.PrintFinishedMap(dataTable,t)
            return visitedNodes
        for (action,child) in marios.ClosebyDataPoints(subRoot,dataTable).items():
            if(child in visitedNodes):
                continue

            if(child not in openSet):
                    openSet.append(child)
                    meta.AddChild(child)
        visitedNodes.add(subRoot)

    return visitedNodes


m = DepthFirstSearch()
n = BreadthFirstSearch()
a=SetToList(m)
a=NodeToList(a)
b=SetToList(n)
b=NodeToList(b)
print()
print("Ta visited","#"*len(dataTable))
print()
marios.PrintFinishedMap(dataTable,a)
print()
marios.PrintFinishedMap(dataTable,b)
