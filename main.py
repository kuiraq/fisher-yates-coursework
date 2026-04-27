import random as r

def fisher_yates_shuffle(arr):
    for i in range(len(arr)-1,0,-1):
        j:int = r.randint(0,i)
        print(f"Swapping index {arr[i]} and {arr[j]}") 
        arr[i], arr[j] = arr[j], arr[i]
        
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print("Before shuffle: ", arr)
    fisher_yates_shuffle(arr)
    print("After shuffle: ", arr)