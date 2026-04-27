import random as r

def fisher_yates_shuffle(arr):
    for i in range(len(arr)-1,0,-1):
        j:int = r.randint(0,i)
        arr[i], arr[j] = arr[j], arr[i]
        
