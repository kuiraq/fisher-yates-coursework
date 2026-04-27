import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as r

original_arr = list(range(1, 16))
arr = original_arr.copy()
def fisher_yates_generator(arr):
    for i in range(len(arr)-1,0,-1):
        j:int = r.randint(0,i)
        arr[i], arr[j] = arr[j], arr[i]
        yield arr, i, j

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,5))
fig.suptitle('Fisher-Yates Shuffle Visualization', fontsize=15)

ax1.set_title('Original Array')
ax1.bar(range(len(original_arr)), original_arr, color='lightgray')

ax2.set_title('Shuffling Process')
ax2.bar(range(len(arr)), arr, color='skyblue')

bars = ax2.bar(range(len(arr)), arr, color='skyblue')

def update(frame):
    current_arr, idx_i, idx_j = frame
    
    for bar, height in zip(bars, current_arr):
        bar.set_height(height)
        bar.set_color('skyblue')

    bars[idx_i].set_color('red')
    bars[idx_j].set_color('red')

    return bars

ani = animation.FuncAnimation(fig, update, frames=fisher_yates_generator(arr), interval=1960, repeat=False)

plt.show()