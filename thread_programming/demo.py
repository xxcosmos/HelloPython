import threading
import time
import os


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('thread {},@number:{}'.format(self.name, i))
            time.sleep(1)


def main():
    print("start main threading")
    threads = [MyThread() for i in range(3)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    print("End main threading")


if __name__ == '__main__':
    main()
