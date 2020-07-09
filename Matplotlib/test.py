import threading

T1 = threading.Thread(target=input_)
T1.start()
def input_():
    input("hello: ")
def df():
    time.sleep(5)
    print(, end="\r")