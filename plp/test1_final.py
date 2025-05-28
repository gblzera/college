import threading

x = 0
lock = threading.Lock()

def incrementar():
    global x
    for _ in range(100000):
        with lock:
            x += 1

t1 = threading.Thread(target=incrementar)
t2 = threading.Thread(target=incrementar)

t1.start()
t2.start()

t1.join()
t2.join()

print(x)
