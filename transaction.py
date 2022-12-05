import collections
class Transaction():
    def __init__(self):
        self.xid = 0
        self.queue = collections.deque()

    def start(self):
        self.xid += 1
        self.queue.append(self.xid)
        return self.xid

    def commit(self, xid):
        if self.queue[0]==xid:
            self.queue.popleft()
            return 0
        else:
            return -1

if __name__ == '__main__':
    transaction = Transaction()
    xid1 = transaction.start()
    xid2 = transaction.start()

    transaction.commit(xid1)
    transaction.commit(xid2)
