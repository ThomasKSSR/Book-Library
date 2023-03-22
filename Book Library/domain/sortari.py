class Sorter(object):
    
    def _identitate(self,x):
        return x
    def _negatie(self,x):
        return not x    
    def sort(self,list,key = lambda x:x,cmp = lambda x,y:x<y,reverse = False):
        pass
    
class InsertionSorter(Sorter):
    def sort(self, list, key=lambda x:x, cmp=lambda x, y:x > y, reverse=False):
        if reverse:
            operatie = self._negatie
        else:
            operatie = self._identitate
        
        for i in range(1,len(list)):
            
            while operatie(cmp(key(list[i-1]) ,key(list[i]))) and i >0:
                list[i-1], list[i] = list[i], list[i-1]
                i -= 1

class CombSorter(Sorter):
    def sort(self, list, key=lambda x:x, cmp=lambda x, y:x > y, reverse=False):
        if reverse:
            operatie = self._negatie
        else:
            operatie = self._identitate
        
        
        shrink = 1.3
        gaps = len(list)
        swapped = False
        i = 0
        while gaps > 1 or swapped:
            gaps = max(1,int(gaps/shrink))
            swapped = False
            for i in range(len(list) - gaps):
                if operatie(cmp(key(list[i]),key(list[i+gaps]))):
                    list[i],list[i+gaps] = list[i+gaps],list[i]
                    swapped = True
"""
class Sort(object):
    
    def insert_sort(self,list):
        
        for i in range(1,len(list)):
            
            while list[i-1] >list[i] and i >0:
                list[i-1], list[i] = list[i], list[i-1]
                i -= 1
    
    def comb_sort(self,list): 
        shrink = 1.3
        gaps = len(list)
        swapped = True
        i = 0
        while gaps > 1 or swapped:
            gaps = int(float(gaps)/shrink)
            swapped = False
            i = 0
            while gaps +i <len(list):
                if list[i] < list[i +gaps]:
                    list[i],list[i+gaps] = list[i+gaps], list[i]
                    swapped = True
                i += 1
    
 """                
            
        


