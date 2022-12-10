import collections

class BufferTable:
    def __init__(self):
        self.tables = collections.defaultdict(list)

    def append(self, table_name, id):
        self.tables[table_name].append(id)

if __name__ == '__main__':
    bf = BufferTable()
    bf.append("tableA", 1)
