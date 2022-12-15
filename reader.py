from concurrent.futures import ThreadPoolExecutor
import time
import threading
import json
import fcntl, os

class Reader():
    def __init__(self, lock):
        self.lock = lock
        self.data = None

    def run_thread_lock(self, path):
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

    def run_shared_lock(self, path):
        with open(path, 'r+') as f:
            try:
                fcntl.flock(f, fcntl.LOCK_SH)
                # test for checking
                time.sleep(1)
                data_json = f.read()
                print(json.loads(data_json))
            except IOError:
                print('shared_lock')

    def run_exclusive_lock(self, path):
        with open(path, 'r+') as f:
            try:
                fcntl.flock(f, fcntl.LOCK_EX)
                # test for checking
                time.sleep(1)
                data_json = f.read()
                print(json.loads(data_json))
            except IOError:
                print('exclusive_lock')

if __name__ == "__main__":
    lock = threading.Lock()
    thread_pool = []
    thread_pool.append(Reader(lock).run_thread_lock("testpath/test.json"))
    thread_pool.append(Reader(lock).run_thread_lock("testpath/test.json"))
    thread_pool.append(Reader(lock).run_thread_lock("testpath/test.json"))

    with ThreadPoolExecutor(max_workers=3) as executor:
        for th in thread_pool:
            ret = executor.submit(th)
