# %%
class Array:
    def __init__(self):
        self.data = [0, 0]

    def contents(self):
        return self.data

    def size(self):
        return len(self.data)

    def isEmpty(self):
        if len(self.data) < 1:
            return True
        else:
            return False

    def at(self, index):
        return self.data[index]

    def push(self, val):
        self.data.append(val)

    def insert(self, index, item):
        self.data.insert(index, item)

    def prepend(self, item):
        self.data.insert(0, item)

    def pop(self):
        self.data.pop()

    def delete(self, index):
        del self.data[index]

    def remove(self, item):
        self.data = [x for x in self.data if x != item]

    def find(self, item):
        for i, val in enumerate(self.data):
            if val == item:
                return i
        return -1


test = Array()
test.push(1)
print(test.contents())
test.insert(1, 2)
print(test.contents())
test.prepend(0)
print(test.contents())
test.pop()
print(test.contents())
test.delete(1)
print(test.contents())
test.remove(0)
print(test.contents())
print(test.find(3))
# %%
