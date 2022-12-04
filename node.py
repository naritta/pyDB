
class Node():
    def __init__(self, content):
        self.content = content
        self.relations = {}

    def has(self, node):
        self.relations[node.content.__class__.__name__] = node

    def find(self, type):
        if type in self.relations:
            return self.relations[type].content
        else:
            return None

if __name__ == '__main__':
    class Job():
        def __init__(self, name):
            self.name = name

    class Person():
        def __init__(self, name):
            self.name = name

    taro = Node(Person("Taro"))
    student = Node(Job("student"))

    taro.has(student)
    print(taro.find("Job").name)
