import math
import time


class Node:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0

    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1


class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0

    def insert(self, key):
        new_tree = Node(key)
        self.trees.append(new_tree)
        if self.least is None or key < self.least.key:
            self.least = new_tree
        self.count = self.count + 1

    def getMin(self):
        if self.least is None:
            return None
        return self.least.key

    def extractMin(self, c):
        smallest = self.least
        # c += 1
        if smallest is not None:
            # c += 1
            for child in smallest.children:
                # c += 1
                self.trees.append(child)
                # c += 2
            self.trees.remove(smallest)
            # c += 2
            if not self.trees:
                # c += 1
                self.least = None
                # c += 1
            else:
                self.least = self.trees[0]
                c = self.consolidate(c)
                # c += 4
            self.count = self.count - 1
            # c += 3
            return smallest.key, c

    def consolidate(self, c):
        aux = (floor_log2(self.count) + 1) * [None]
        # c += 7
        while self.trees:
            # c += 1
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            # c += 4
            while aux[order] is not None:
                # c += 1
                y = aux[order]
                # c += 1
                if x.key > y.key:
                    x, y = y, x
                    # c += 4
                x.add_at_end(y)
                # c += 6
                aux[order] = None
                order = order + 1
                # c += 2
            aux[order] = x
            # c += 1

        self.least = None
        # c += 1
        for k in aux:
            # c += 1
            if k is not None:
                self.trees.append(k)
                # c += 3
                if (self.least is None
                        or k.key < self.least.key):
                    self.least = k
                    # c += 8
        # return c


def floor_log2(x):
    return math.frexp(x)[1] - 1


fInsert = open("timeInsert", 'w')
fGet = open("timeGet", "w")
fExtract = open("timeExtract", "w")
fExtractIter = open("IterExtract", "w")

for i in range(1, 101):
    filename = f"text{i}.txt"

    heap = FibonacciHeap()

    sumTime = 0
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        for j in range(n):
            key = int(file.readline().strip())
            startTimeInsert = time.perf_counter_ns()
            heap.insert(key)
            endTimeInsert = time.perf_counter_ns()
            sumTime += (endTimeInsert - startTimeInsert)

    fInsert.write(str(sumTime / n) + "\n")

    startTimeGet = time.perf_counter_ns()
    heap.getMin()
    endTimeGet = time.perf_counter_ns()
    fGet.write(str(endTimeGet - startTimeGet) + "\n")

    startTimeExtract = time.perf_counter_ns()
    # _, iterations = heap.extractMin(0)
    # время нужно считать до подсчета итераций
    heap.extractMin(0)
    endTimeExtract = time.perf_counter_ns()
    # fExtractIter.write(str(iterations // 100) + "\n")
    fExtract.write(str(endTimeExtract - startTimeExtract) + "\n")

fInsert.close()
fGet.close()
fExtract.close()
fExtractIter.close()

# heap = FibonacciHeap()
# heap.insert(1)
# heap.insert(3)
# heap.insert(2)
# heap.insert(4)
# heap.insert(0)
#
# print("Минимум:", heap.getMin())
# heap.extractMin(0)
# print("Минимум:", heap.getMin())
