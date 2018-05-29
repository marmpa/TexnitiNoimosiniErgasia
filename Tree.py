import re

class Node(object):
    def __init__(self, data=None,parent=None):
        self.data = data
        self.mapFolder = "maps/"
        self.children = []
        self.parent = parent

    def __eq__(self,other):
        if isinstance(self,other.__class__):
            return self.data == other.data
        return False
    def __hash__(self):
        try:
            return hash(tuple(self.data))
        except Exception as e:
            return hash(self.data)


    def AddChild(self, obj):
        obj.parent=self
        self.children.append(obj)




    def CreateMapDataTable(self,fileName):
        table = {}
        points = {}
        try:
            lineCount = None

            fileName = fileName.strip()
            pattern = re.compile("\w+\.txt$",re.IGNORECASE)#Το pattern που βρίσκει αν υπάρχει .txt στο τέλος
            if(not pattern.match(fileName)):#Αν δεν υπάρχει τότε το προσθέτει στο τέλος
                fileName += ".txt"

            with open(self.mapFolder+fileName,"r") as file:
                for lineCounter,line in enumerate(file):
                    table[lineCounter+1] = {}

                    for i,char in enumerate(line):
                        if(char!="\n"):
                            if(char.lower() in ['g','p']):
                                points[char.lower()] = [lineCounter+1,i+1]
                            table[lineCounter+1][i+1] = char


        except Exception as e:
            print(e)


        return table,points

    def ProcessMap(self,fileName):
        pass


    def DevProcessMap(self,fileName):
        dataTable,mapPoints = self.CreateMapDataTable(fileName)
        start,end = [0,0],[0,0]
        try:
            start,end = mapPoints['p'],mapPoints['g']
        except Exception as e:
            print(e)



    def PrintMap(self,fileName):
        try:
            with open(self.mapFolder+fileName,"r") as file:
                for line in file:
                    print(len(line)-line.count("\n"))
                    for char in line:
                        print(char,end="")

        except Exception as e:
            print(e)

    def PrintFinishedMap(self,table,points):
        for i,v in table.items():
            for k,l in v.items():
                if(l.lower() in ['g','p']):
                    print(l,end="")
                elif([i,k] in points):
                    print(".",end="")
                else:
                    print(l,end="")
            print()
    def ClosebyDataPoints(self,point,Table):
        point = point.data
        rows,columns = len(Table),len(Table[1])

        points = {}

        if((point[0]+1)<rows):
            if(not Table[point[0]+1][point[1]]=='%'):
                points[0] = Node([point[0]+1,point[1]])

        if((point[1]+1)<columns):
            if(not Table[point[0]][point[1]+1]=='%'):
                points[1] = Node([point[0],point[1]+1])

        if((point[0]-1)>=0):
            if(not Table[point[0]-1][point[1]]=='%'):
                points[2] = Node([point[0]-1,point[1]])

        if((point[1]-1)>=0):
            if(not Table[point[0]][point[1]-1]=='%'):
                points[3] = Node([point[0],point[1]-1])

        return points
    def ClosebyDataPointsN(self,point,Table,visited):
        point = point.data
        rows,columns = len(Table),len(Table[1])

        points = {}

        if((point[0]+1)<rows):
            if(not Table[point[0]+1][point[1]]=='%' and not Node([point[0]+1,point[1]]) in visited):
                points[0] = Node([point[0]+1,point[1]])

        if((point[1]+1)<columns):
            if(not Table[point[0]][point[1]+1]=='%'  and not Node([point[0],point[1]+1]) in visited):
                points[1] = Node([point[0],point[1]+1])

        if((point[0]-1)>=0):
            if(not Table[point[0]-1][point[1]]=='%'  and not Node([point[0]-1,point[1]]) in visited):
                points[2] = Node([point[0]-1,point[1]])

        if((point[1]-1)>=0):
            if(not Table[point[0]][point[1]-1]=='%'  and not Node([point[0]+1,point[1]]) in visited):
                points[3] = Node([point[0],point[1]-1])

        return points

    def ListToNodeList(self,list):
        a = []
        for x in list:
            a.append(Node(x))
        return a



#kato deksia pano aristera
