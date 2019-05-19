import threading

x=0
def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1
def square():
    print('Execution of thread :')
    for i in range(100000):
        increment()

def main_task():
    sqt = threading.Thread(target=square, args=[])
    cubet = threading.Thread(target=square, args=[])
    sqt.start()
    cubet.start()
    sqt.join()
    cubet.join()

if __name__=='__main__':

    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))