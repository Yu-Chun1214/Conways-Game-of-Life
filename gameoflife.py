import pattern
from pattern import pattern
from pattern import T,F,a,b
import time
import random
class GameofLife:
    pattern=[]
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def set_map(self,w,h):
        self.w=w
        self.h=h
        map=[]
        for i in range(h):
            map.append([F]*w)
        return map
    def set_pattern(self,type):
        if type<=3:
            if self.w<=pattern.pattern(type).w() and self.h<=pattern.pattern(type).h():
                self.w=pattern.pattern(type).w()
                self.h=pattern.pattern(type).h()
            elif self.w<=pattern.pattern(type).w():
                self.w=pattern.pattern(type).w()
            elif self.h<=pattern.pattern(type).h():
                self.h=pattern.pattern(type).h()
            posi=self.__position(self.w,self.h,pattern.pattern(type).w(),pattern.pattern(type).h())
            Map=[]
            died_cell=[b]*self.w
            for i in range(1,posi['above']+1):
                Map.append(died_cell)
            element=[]
            element=self.__pattern_manage(pattern.pattern(type).graph(),pattern.pattern(type).h(),posi['right'],posi['left'])
            for i in range(pattern.pattern(type).h()):
                Map.append(element[i])
            for i in range(posi['below']):
                Map.append(died_cell)
            self.pattern=Map
            return Map
        elif type>=4 and type<=100:
            self.pattern=pattern.pattern_maker(self.w,self.h,type,self.set_map(self.w,self.h))
            #print(self.pattern)
            return self.pattern
    def __pattern_manage(self,pattern,pattern_hight,right,left):
        pattern_cp=pattern
        for i in range(pattern_hight):
            for j in range(right):
                pattern_cp[i].insert(0,b)
            for j in range(left):
                pattern_cp[i].append(b)
        return pattern_cp
    def prin_out(self):
        for i in self.pattern:
            for j in i:
                if j==False:
                    print(" ",end =' ')
                else:
                    print('0',end=' ')
            print("\t")
        print("============generation line===========")
    def __position(self,map_w,map_h,w,h):
            left=round((map_w-w)/2)
            right=map_w-left-w
            above=round((map_h-h)/2)
            below=map_h-above-h
            posi={
                'right':right,
                'left':left,
                'above':above,
                'below':below
            }
            return posi
    def play(self,generation):
        t=0
        while t<generation:
            self.prin_out()
            time.sleep(1)
            work_pattern=[]
            for y in range(self.h):
                element=[]
                for x in range(self.w):
                    element.append(self.__count_of_life(y,x))
                work_pattern.append(element)
            self.pattern=work_pattern
            t+=1
    def __life(self,y,x):
        if x<0 or y<0 or x>=self.w or y>=self.h:
            return F
        elif self.pattern[y][x]==T:
            return T
        elif self.pattern[y][x]==F:
            return F 
    def __count_of_life(self,y,x):
        sum=0
        for i in range(y-1,y+2):
            for j in range(x-1,x+2):
                if self.__life(i,j)==T:
                    if i!=y or j!=x:
                        sum+=1
        if self.pattern[y][x]==T:
            if sum<2:
                return F
            elif sum==2 or sum==3:
                return T
            elif sum>3:
                return F
        elif self.pattern[y][x]==F:
            if sum==3:
                return T
            else:
                return F