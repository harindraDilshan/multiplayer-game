import threading

def fun1():
    count = 0
    for i in range(4):
        count += 1
        print(f"Count in fun 1 : {count}")


def fun2():
    count = 0
    for i in range(10):
        count += 1
        print(f"Count in fun 2 : {count}")


t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)

t1.start()
t2.start()

t1.join()
t2.join()