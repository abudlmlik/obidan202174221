graph1={
    'S':['B','A'],
    'A':['D','C'],
    'B':['G','D'],
    'C':[],
    'D':['G','C'],
    'G':[]
}
def dfspath(graph1,start,goal):
    stack=[[start]]
    visited=[]
    while stack:
        print("stack:",stack)
        path=stack.pop(0)
        node=path[-1]
        if node== goal:
            return print("this is the path:",path)
        children=graph1[node]
        for child in children:
            if child not in visited:
                newpath=path+[child]
                stack.insert(0,newpath)
                visited.append(child)
dfspath(graph1,'S','G')
           