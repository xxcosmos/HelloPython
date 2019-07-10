import threading, time

balance = 0
lock = threading.Lock()


def change_balance(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000):
        # lock.acquire()
        try:
            change_balance(n)
        finally:
            pass
            # lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(7,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
