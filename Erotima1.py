from Tree import Node
from queue import Queue
from queue import PriorityQueue
import re
import itertools
from heapq import heappop, heappush

from pptree import print_tree

marios = Node(5)
marios.AddChild(marios)

fileName = input("Dose onoma xarti: ")
#marios.PrintMap(fileName+".txt")
marios.ProcessMap(fileName)


a = {Node([2,5]),Node([2,3])}

print(Node([2,1]) in a)
dataTable,mapPoints = marios.CreateMapDataTable(fileName)

def Finddubl(node,a=None,num=0):
    if a is None:
        a = set()
        a.add(node)
    if node:
        for x in node.children:
            if(x in a):
                print("Diplotipo to " ,x.data," riza ", num)
            a.add(x)
            Finddubl(x,a,num+1)


def PrintFatherOfFather(node):

    while node.parent is not None:
        print("pateras",node.data," kai pateras",node.parent)
        node = node.parent
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

def VisitedNodesToDataForDisplaying(oSet):
    tx = SetToList(oSet)
    return NodeToList(tx)

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

            t = FindPath(meta,root)
            print("Lisi Breadth First!")
            marios.PrintFinishedMap(dataTable,t)
            return visitedNodes

        #print("fores",subRoot.data)
        for (action,child) in marios.ClosebyDataPoints(subRoot,dataTable).items():

            #print(action,child.data,"terastiaabga",len(marios.ClosebyDataPoints(subRoot,dataTable).items()))
            if(child in visitedNodes):
                continue

            if(child not in openSetCopy):


                if(child not in metaNodes):
                    meta.AddChild(child)
                    metaNodes.add(child)

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

#temporary
goal = mapPoints['g']
def CallDepthFirstSearchRecurs():
    dataTable,mapPoints = marios.CreateMapDataTable(fileName)
    root,goal = Node(mapPoints['p']),mapPoints['g']


    def DepthFirstSearchRecurs(subRoot=None,visitedNodes=None,meta=None,metaNodes=None,itter=1):
        if visitedNodes is None:
            visitedNodes = set()

        if metaNodes is None:
            metaNodes=set()
        if subRoot is None:
            subRoot=Node(mapPoints['p'])
            meta=subRoot
        else:
            if meta is None:
                meta=subRoot
            else:
                pass

        visitedNodes.add(subRoot)
        meta=subRoot

        if(subRoot.data==goal):
            return subRoot

        for(action,child) in marios.ClosebyDataPoints(subRoot,dataTable).items():
            if(child not in visitedNodes):
                t = visitedNodes.copy()
                if(child not in metaNodes):
                    #print(child.data,"child.data")
                    metaNodes.add(child)
                    meta.AddChild(child)
                if(itter!=1):
                    ans = DepthFirstSearchRecurs(child,visitedNodes,meta,metaNodes,itter+1)
                    if((not type(ans)==tuple)and(ans is not None)):
                        return ans
                elif(itter==1):
                    ans = DepthFirstSearchRecurs(child,visitedNodes,meta,metaNodes,itter+1)
                    if((not type(ans)==tuple)and(ans is not None)):
                        return visitedNodes,ans,meta

        #print(itter)
        return None

        ty,tx,tz = DepthFirstSearchRecurs()
        trx = FindPath(tx,tz)
        print("Lisi Depth First Search!")
        marios.PrintFinishedMap(dataTable,trx)

def IterativeDeepening():

    def DepthFirstIterativeDeepeningSearch(subRoot=None,visitedNodes=None,meta=None,metaNodes=None,itter=1,depth=0):


        if visitedNodes is None:
            visitedNodes = set()

        if metaNodes is None:
            metaNodes=set()
        if subRoot is None:
            subRoot=Node(mapPoints['p'])
            meta=subRoot
        else:
            if meta is None:
                meta=subRoot
            else:
                pass

        visitedNodes.add(subRoot)
        meta=subRoot

        if(depth==0 and subRoot.data==goal):
            return subRoot
        if(depth==0):
            return None

        for(action,child) in marios.ClosebyDataPoints(subRoot,dataTable).items():
            if(child not in visitedNodes):
                t = visitedNodes.copy()
                if(child not in metaNodes):
                    #print(child.data,"child.data")
                    metaNodes.add(child)
                    meta.AddChild(child)
                if(itter!=1):
                    ans = DepthFirstIterativeDeepeningSearch(child,visitedNodes,meta,metaNodes,itter+1,depth-1)
                    if((not type(ans)==tuple)and(ans is not None)):
                        return ans
                elif(itter==1):
                    ans = DepthFirstIterativeDeepeningSearch(child,visitedNodes,meta,metaNodes,itter+1,depth-1)
                    if((not type(ans)==tuple)and(ans is not None)):
                        return visitedNodes,ans,meta
        return None

    for depth in itertools.count():
        answer=DepthFirstIterativeDeepeningSearch(depth=depth)

        if(answer is not None):
            ty,tx,tz = IterativeDeepening()
            trx = FindPath(tx,tz)
            print("Lisi Iterative Deepening First!")
            marios.PrintFinishedMap(dataTable,trx)
            return answer[0],answer[1],answer[2]


def BestFirstSearch():
    dataTable,mapPoints = marios.CreateMapDataTable(fileName)
    root,goal = Node(mapPoints['p']),mapPoints['g']

    searchPriorityQueue = PriorityQueue()
    visitedNodes = set()
    metaNodes = set()

    searchPriorityQueue.put([0,root])
    visitedNodes.add(root)

    while not searchPriorityQueue.empty():
        subRoot = searchPriorityQueue.get()[1]

        if(subRoot not in metaNodes):
            metaNodes.add(subRoot)
            if subRoot.parent is not None:
                meta = subRoot.parent
                meta.AddChildOnce(subRoot)

        if(subRoot.data == goal):
            t=FindPath(meta,root)
            print("Best First Search")
            marios.PrintFinishedMap(dataTable,t)
            Finddubl(root)
            return visitedNodes
        else:
            for(action,child) in marios.ClosebyDataPoints(subRoot,dataTable).items():
                if(child not in visitedNodes):
                    #exei lathos bazo panta to addchild gia kathe paidi
                    if(child.parent is None):
                        child.AddParentOnly(subRoot)
                    visitedNodes.add(child)
                    #t = VisitedNodesToDataForDisplaying(visitedNodes)
                    #marios.PrintFinishedMap(dataTable,t)
                    #print(child.data,"Apostasi:",marios.ManhattanPointDistance(child,goal),end="")
                    searchPriorityQueue.put([marios.ManhattanPointDistance(child,goal),child])



def AStartSearch():
    dataTable,mapPoints = marios.CreateMapDataTable(fileName)
    root,goal = Node(mapPoints['p']),mapPoints['g']

    searchPriorityQueue = []
    visitedNodes = set()
    metaNodes = set()

    heappush(searchPriorityQueue,[0+marios.ManhattanPointDistance(root,goal),0,root])

    while searchPriorityQueue:
        _, cost,subRoot = heappop(searchPriorityQueue)

        if(subRoot not in metaNodes):
            metaNodes.add(subRoot)

            if subRoot.parent is not None:
                meta = subRoot.parent
                meta.AddChildOnce(subRoot)


        if(subRoot.data == goal):
            t = FindPath(meta,root)
            print("Best First Search")
            marios.PrintFinishedMap(dataTable,t)
            return visitedNodes
        if subRoot in visitedNodes:
            continue
        visitedNodes.add(subRoot)
        #t = VisitedNodesToDataForDisplaying(visitedNodes)
        #marios.PrintFinishedMap(dataTable,t)


        for(action,child) in marios.ClosebyDataPoints(subRoot,dataTable).items():
            if(child not in searchPriorityQueue):
                if(child.parent is None):
                    child.AddParentOnly(subRoot)
                heappush(searchPriorityQueue,[cost + marios.ManhattanPointDistance(root,goal),cost + 1,child])

root=Node(mapPoints['p'])
ans = AStartSearch()
print()
t = VisitedNodesToDataForDisplaying(ans)
marios.PrintFinishedMap(dataTable,t)
BestFirstSearch()
"""
ty,tx,tz = IterativeDeepening()
trx = FindPath(tx,tz)
print("Lisi IterativeDeepening First!")
marios.PrintFinishedMap(dataTable,trx)
print()

#DepthFirstSearch()
n = BreadthFirstSearch()
ty,tx,tz = DepthFirstSearchRecurs()
print("yaaaaaaaaaas")
#print_tree(tz,nameattr='data')
trx = FindPath(tx,tz)
print("Lisi DepthFirstSearch First!")
marios.PrintFinishedMap(dataTable,trx)
#print()

"""
"""
m = DepthFirstSearch()
n = BreadthFirstSearch()
a=SetToList(m)
a=NodeToList(a)
b=SetToList(n)
b=NodeToList(b)
print()
print("Ta visited","#"*len(dataTable))
print()
#marios.PrintFinishedMap(dataTable,a)
print()
#marios.PrintFinishedMap(dataTable,b)
"""
