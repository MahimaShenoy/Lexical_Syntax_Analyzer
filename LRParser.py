class Stack:
    def __init__(self):
        self.s = []

    def pop(self):
        return self.s.pop()

    def push(self, item):
        self.s.append(item)

    def sizeOfStack(self):
        return len(self.s)

    def peak(self):
        return self.s[len(self.s) - 1]

    def printStack(self):
        for i in range(len(self.s)):
            print(self.s[i])


def foo(string):
    global index, inpIndex, inp, s, flage

    print(string)

    if string[0] == 'r':  # do reducing
        temp = RulesTable[int(string[1:])]
        temp = temp.split("->")
        g = temp[1].split(" ")
        for i in range(len(g) * 2):
            label = s.pop()
        num = s.peak()

        s.push(temp[0])

        s.push(int(LR1Table[num][goto[temp[0]]]))
        index = (int(LR1Table[num][goto[temp[0]]]))



    else:  # do shifting
        s.push(inp[inpIndex])
        s.push(int(string[1:]))
        inpIndex += 1
        index = s.peak()


index = 0
inpIndex = 0  # input pointer
nodeNum = 0  # number of node for graphviz
flage = 1

s = Stack()

terminals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
nonterminals = ['S/', 'S', 'A', 'B', 'C', 'D', 'E', 'I', 'J', 'F', 'K', 'G', 'L', 'H']

action = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
          'm': 12, 'n': 13, 'o': 14, 'p': 15, '$': 16}
goto = {'S\'': 17, 'S': 18, 'A': 19, 'B': 20, 'C': 21, 'D': 22, 'E': 23, 'I': 24, 'J': 25, 'F': 26, 'K': 27, 'G': 28,
        'L': 29, 'H': 30}
RulesTable = []
RulesTable.append("S\->S")
RulesTable.append("S->a A")
RulesTable.append("A->B b c C d c")
RulesTable.append("B->e f g c")
RulesTable.append("C->D C")
RulesTable.append("C->D")
RulesTable.append("D->E h c")
RulesTable.append("D->F h c")
RulesTable.append("D->G")
RulesTable.append("D->H h c")
RulesTable.append("E->a I")
RulesTable.append("I->J")
RulesTable.append("I->J j I")
RulesTable.append("J->j")
RulesTable.append("J->j k l")
RulesTable.append("F->j k K")
RulesTable.append("F->j k K m K")
RulesTable.append("K->j")
RulesTable.append("K->l")
RulesTable.append("G->n f j o K g L")
RulesTable.append("L->c b c C d n c")
RulesTable.append("H->p K")
print("Grammar is :\n")

print(*RulesTable,sep="\n")
# rl(1) table
LR1Table = []
LRprinttable=[]
LRprinttable.append(['state','a  ', 'b  ', 'c  ', 'd  ', 'e  ', 'f  ', 'g  ', 'h  ', 'i  ', 'j  ', 'k  ', 'l  ', 'm  ', 'n  ', 'o  ','p  ', '$  ', 'S\ ', 'S  ', 'A  ', 'B  ', 'C  ', 'D  ', 'E  ', 'I  ', 'J  ', 'F  ', 'K  ', 'G  ', 'L  ', 'H  '])
LRprinttable.append(['    0','s2 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '  1', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['    1','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', 'acc', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['    2','   ', '   ', '   ', '   ', ' s5', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '  3', '  4', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['    3','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', 'r1 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['    4','   ', ' s6', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['    5','   ', '   ', '   ', '   ', '   ', ' s7', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['    6','   ', '   ', ' s8', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['    7','   ', '   ', '   ', '   ', '   ', '   ', ' s9', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['    8','s16', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 's17', '   ', '   ', '   ', 's18', '   ','s19', '   ', '   ', '   ', '   ', '   ', ' 10', ' 11', ' 12', '   ', '   ', ' 13', '   ', ' 14', '   ', ' 15'])
LRprinttable.append(['    9','   ', '   ', 's20', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   10','   ', '   ', '   ', 's21', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '  ', '    ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   11','s16', '   ', '   ', ' r5', '   ', '   ', '   ', '   ', '   ', 's17', '   ', '   ', '   ', 's18', '   ','s19', '   ', '   ', '   ', '   ', '   ', ' 22', ' 11', ' 12', '   ', '   ', ' 13', '   ', ' 14', '   ', ' 15'])
LRprinttable.append(['   12','   ', '   ', '   ', '   ', '   ', '   ', '   ', 's23', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   13','   ', '   ', '   ', '   ', '   ', '   ', '   ', 's24', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   14',' r8', '   ', '   ', ' r8', '   ', '   ', '   ', '   ', '   ', ' r8', '   ', '   ', '   ', ' r8', '   ',' r8', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   15','   ', '   ', '   ', '   ', '   ', '   ', '   ', 's25', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   16','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 's28', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' 26', ' 27', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   17','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 's29', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   18','   ', '   ', '   ', '   ', '   ', 's30', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   19','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' s32', '  ',' s33', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' 31', '   ', '   ', '   '])
LRprinttable.append(['   20','   ', ' r3', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   21','   ', '   ', 's34', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   22','   ', '   ', '   ', ' r4', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   23','   ', '   ', 's35', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   24','   ', '   ', 's36', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   25','   ', '   ', 's37', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   26','   ', '   ', '   ', '   ', '   ', '   ', '   ', 'r10', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   27','   ', '   ', '   ', '   ', '   ', '   ', '   ', 'r11', 's38 ', '   ', '  ', '    ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   28','   ', '   ', '   ', '   ', '   ', '   ', '   ', 'r13', ' r13', '   ', 's39', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   29','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 's41', '   ', 's42', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' 40', '   ', '   ', '   '])
LRprinttable.append(['   30','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 's43', '  ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   31','   ', '   ', '   ', '   ', '   ', '   ', '   ', 'r21', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   32','   ', '   ', '   ', '   ', '   ', '   ', '   ', 'r17', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   33','   ', '   ', '   ', '   ', '   ', '   ', '   ', 'r18', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   34','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', ' r2', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   35',' r6', '   ', '   ', ' r6', '   ', '   ', '   ', '   ', '   ', ' r6', '   ', '   ', '   ', ' r6', '   ',' r6', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   36',' r7', '   ', '   ', ' r7', '   ', '   ', '   ', '   ', '   ', ' r7', '   ', '   ', '   ', ' r7', '   ',' r7', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   37',' r9', '   ', '   ', ' r9', '   ', '   ', '   ', '   ', '   ', ' r9', '   ', '   ', '   ', ' r9', '   ',' r9', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   38','  ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 's28', '   ', '   ', '    ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' 44', ' 27', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   39','  ', '   ', '   ', '   ', '   ', '   ', '   ', '  ', '  ', '   ', '     ', 's45', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   40','  ', '   ', '   ', '   ', '   ', '   ', '   ', ' r15', '   ', '   ', '  ', '   ', ' s46', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   41','   ', '   ', '   ', '   ', '   ', '   ', '  ', ' r17', '   ', '   ', '   ', '   ', ' r17', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   42','   ', '   ', '   ', '   ', '   ', '   ', '  ', ' r18', '   ', '   ', '   ', '   ', ' r18', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   43','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 's47','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   44','   ', '   ', '   ', '   ', '   ', '   ', '   ', 'r12', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   45','   ', '   ', '   ', '   ', '   ', '  ', '   ', ' r14', ' r14', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   46','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 's32', '   ', 's33', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' 48', '   ', '   ', '   '])
LRprinttable.append(['   47','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 's50', '   ', 's51', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' 49', '   ', '   ', '   '])
LRprinttable.append(['   48','   ', '   ', '   ', '   ', '   ', '  ', '   ', ' r16', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   49','   ', '   ', '   ', '   ', '   ', '  ', 's52', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   50','   ', '   ', '   ', '   ', '   ', '  ', ' r17', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   51','   ', '   ', '   ', '   ', '   ', '   ', 'r18', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   52','   ', '   ', 's54', '   ', '   ', '   ', '  ', '   ', '   ', '    ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' 53', '   '])
LRprinttable.append(['   53',' r19', '   ', '   ', 'r19', '   ', '   ', '   ', '   ', '   ', ' r19', '  ', '   ', '  ', 'r19', '   ','r19', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   54','   ', 's55', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   55','   ', '   ', 's56', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   56','s16', 'r21', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' s17', '   ', '   ', '   ', 's18', '   ','s19', '   ', '   ', '   ', '   ', '   ', ' 57', ' 11', ' 12', '   ', '   ', ' 13', '   ', ' 14', '   ', ' 15'])
LRprinttable.append(['   57','   ', '   ', '   ', 's58', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   58','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 's59', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   59','   ', '   ', 's60', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])
LRprinttable.append(['   60','r20', '   ', '   ', 'r20', '   ', '   ', '   ', '   ', '   ', 'r20', '   ', '   ', '   ', 'r20', '   ','r20', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '])


f = open(".../Input.csv")#Give the path of Input.csv file

state = []
i = 0
for line in f:

    state = line.split(',')
    l5 = []

    for i in state:
        if i != '\n':
            l5.append(i)

    LR1Table.append(l5)
   
print("\n\nLR TABLE :\n\n")
print(*LRprinttable,sep = "\n")
print("\n\n")
# rules table

inp = input("Enter string: ")
inp += " $"
inp = inp.split(' ')

s.push(0)

temp = LR1Table[index][action[inp[inpIndex]]]
while (temp != "acc"):
    if temp == '':
        print("error")
        break
    print(temp)
    foo(temp)



    temp = LR1Table[index][action[inp[inpIndex]]] 
if(temp == "acc"):
    print("String Accepted")
