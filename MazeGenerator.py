ans = input("Dose xarti:")
table = {}

symbol="%"

with open("maps/"+ans+".txt","r") as file:
    for lineCounter,line in enumerate(file):
        table[lineCounter+1] = {}

        for i,char in enumerate(line):
            if(char!="\n"):
                if(char.lower() in ['+','-','|']):
                    table[lineCounter+1][i+1] = symbol
                else:
                    table[lineCounter+1][i+1] = " "

                if(lineCounter+1==1 or lineCounter+1==len(line) or i+1==1 or i+1>=201):
                    table[lineCounter+1][i+1] = symbol



with open("maps/"+ans+"Pr"+".txt","w") as file:
    for lineCounter,line in table.items():
        print(line)
        print("\n"*5)
        file.write(''.join(str(i) for e,i in line.items())+'\n')
