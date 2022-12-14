from concurrent.futures import ThreadPoolExecutor
import time
import threading
import json

class Reader():
    def __init__(self, lock):
        self.lock = lock
        self.data = None

    def run(self, path):
        self.lock.acquire()
        data_json = ""
        # test for checking
        time.sleep(1)
        with open(path, mode='r') as f:
            data_json = f.read()
        print(json.loads(data_json))
        self.data = json.loads(data_json)
        self.lock.release()
        return json.loads(data_json)

if __name__ == "__main__":
    lock = threading.Lock()
    thread_pool = []
    thread_pool.append(Reader(lock).run("testpath/test.json"))
    thread_pool.append(Reader(lock).run("testpath/test.json"))
    thread_pool.append(Reader(lock).run("testpath/test.json"))

    with ThreadPoolExecutor(max_workers=3) as executor:
        for th in thread_pool:
            ret = executor.submit(th)
