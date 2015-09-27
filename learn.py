import threading

class IbraMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = IbraMessenger(name = 'send out messages')
y = IbraMessenger(name = 'send out messages')
x.start()
y.start()