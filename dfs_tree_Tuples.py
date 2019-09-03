import sys

Root = None
List = []

class Node:

    def __init__(self,Parent=-1,Child=-1):
        self.Parent = Parent
        self.Child = Child
        self.data = (self.Parent,self.Child)

    def Print_Node(self):
        print(self.data,end = ' ')

    def Transform(self,lst):
        self.data = tuple(lst)
        List.append(self)
    def setNchild(self,n):
        self.Nchild = n



if __name__ == '__main__':
    inputs = sys.stdin.readlines()
    for ip in inputs:
        if Root is None:
            Root = Node(-1,ip[0])
            List.append(Root)
            lst = list(Root.data)
            for _ in range(1, len(ip) - 1):
                    n1 = Node(ip[0],ip[_])
                    n1.Print_Node()
                    List.append(lst.append(n1))
                    n1.Transform(lst)
        else:
            Q = [Root]
            while Q:
                temp = Q.pop(0)
                i = 0
                lst = list(Root.data)
                for _ in range(1, len(ip) - 1):
                    n1 = Node(ip[0], ip[_])
                    n1.Print_Node()
                    List.append(lst.append(n1))
                    n1.Transform(lst)
                i += 1
        n1.setNchild(len(ip)-2)
        print("No of CHilds: ",n1.Nchild)
