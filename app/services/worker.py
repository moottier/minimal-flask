from queue import Queue
from urllib import request
from threading import Thread

class HttpGetWorker(Thread):
    def __init__(self, queue: Queue):
        super().__init__()
        super().start()
        self.queue = queue
        self.responses = []
        self.work()

    def work(self):
        while True:
            url = self.queue.get()
            if not url:
                break
            response = request.urlopen(url)
            self.responses.append(response)
            self.queue.task_done()
