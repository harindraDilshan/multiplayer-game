import threading
import time

done = True

def worker(text):
    counter = 0
    while done:
        counter += 1
        print(f"Counter is : {counter} text is : {text}")
        time.sleep(1)

# Get user input
def user_in():
    input("Enter your input : ")
    global done
    done = False


# I need both function work togather. Normally after user_in() then begin worker()
# user_in()
# worker()

'''
This is a daemon thred. If a thred is damon, when execute any other therd daemon thred ended automatically.
threading.Thread(target=worker, daemon=True).start()

pass arguments via thread.
threading.Thread(target=worker, args=("ABC",))

To wait unti thread is over
t1.join()

'''

t1 = threading.Thread(target=worker, args=("ABC",))
t2 = threading.Thread(target=worker, args=("XYZ",))

t1.start()
t2.start()

t1.join()
t2.join()

user_in()