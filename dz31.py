from threading import Thread





def red_color():
    for i in Svetofor:
        print(i)
Svetofor = "Red"

def yellow_color():
    for y in Svetofor1:
        print(y)
Svetofor1 = "Yellow"
def green_color():
    for g in Svetofor2:
        print(g)
Svetofor2 = "Green"
t1 = Thread(target=red_color())
t1.start()
t2 = Thread(target=yellow_color())
t2.start()
t3 = Thread(target=green_color())
t3.start()

