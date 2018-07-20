import random
T=a=True
F=b=False
pattern1=[
    [a,a,a],
    [a,b,b],
    [b,a,b]
]
pattern2=[
    [b,a,b,b,a],
    [a,b,b,b,b],
    [a,b,b,b,b],
    [a,a,a,a,a]
]
pattern3=[
    [F,F,T,T,F,F,F,F,F,T,T,F,F],
    [F,F,F,T,T,F,F,F,T,T,F,F,F],
    [T,F,F,T,F,T,F,T,F,T,F,F,T],
    [T,T,T,F,T,T,F,T,T,F,T,T,T],
    [F,T,F,T,F,T,F,T,F,T,F,T,F],
    [F,F,T,T,T,F,F,F,T,T,T,F,F],
    [F,F,F,F,F,F,F,F,F,F,F,F,F],
    [F,F,T,T,T,F,F,F,T,T,T,F,F],
    [F,T,F,T,F,T,F,T,F,T,F,T,F],
    [T,T,T,F,T,T,F,T,T,F,T,T,T],
    [T,F,F,T,F,T,F,T,F,T,F,F,T],
    [F,F,F,T,T,F,F,F,T,T,F,F,F],
    [F,F,T,T,F,F,F,F,F,T,T,F,F]
]
'''
pattern=[
    [3,3,pattern1],
    [5,4,pattern2],
    [13,13,pattern3]
]
'''
#pattern=[
#   [w,h,pattern_]
# ]

#def pattern_maker(w,h,percentage):
#'''
class picture:
    __w=0
    __h=0
    __graph=[]
    def __init__(self,w,h,map):
        self.__w=w
        self.__h=h
        self.__graph=map
    def graph(self):
        return self.__graph
    def w(self):
        return self.__w
    def h(self):
        return self.__h  

class cPattern:
    __pattern=[]
    def __init__(self):
        self.__pattern=[picture(3,3,pattern1),picture(5,4,pattern2),picture(13,13,pattern3)]

    def pattern(self,type):
        if type<=3:
            return self.__pattern[type-1]
    
    def pattern_maker(self,w,h,percentage,Map):
        coordinate=self.__position_maker(w,h)
        print('w{:0}*h{:1}*percentage{:2}*0.01={:3}'.format(w,h,percentage,w*h*percentage*0.01))
        amount=round(w*h*percentage*0.01)
        coordinate=random.sample(coordinate,amount)
        for i in range(amount):
            x=coordinate[i][1]
            y=coordinate[i][0]
            Map[y][x]=T
        self.__pattern.append([w,h,Map])
        return Map
    def __position_maker(self,w,h):
            coordinate=[]
            for i in range(h):
                for j in range(w):
                    element=[i,j]
                    coordinate.append(element)
            return coordinate


pattern=cPattern()
print(pattern.pattern(1).graph())