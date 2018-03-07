import webbrowser
import time


total_breaks = 3
break_count = 0

print("This program started! " + time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    #time.sleep(2*60*60) This would be for every 2 hours
    webbrowser.open("https://www.youtube.com/watch?v=h-_NNIX8cDA")
    break_count = break_count + 1

