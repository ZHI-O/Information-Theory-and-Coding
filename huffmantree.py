class BinaryTree:
    '''构建二叉树类

        Attributes:
            rootObj: 节点所表示的对象,其中一号元素为value，二号元素为weight，三号元素为code
            leftChild: 左节点
            rightChild: 右节点
    '''
    def __init__(self, rootObj) -> None:
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    def isEmpty(self):
        return self.stack == []
    
    def size(self):
        return len(self.stack)

class BinaryHeap:
    '''构建子树二叉堆
        属性：
            heapList:子树列表
            currentsize:列表大小'''
    def __init__(self) -> None:
        self.heapList = [None]
        self.currentsize = 0
    
    def insert(self, obj):
        self.heapList.append(obj)
        self.currentsize += 1
        self.percUp(self.currentsize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i].getRootVal()[1] > self.heapList[i // 2].getRootVal()[1]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = temp
            i //= 2

def builtHuffmanHeap(alpdir):
    symbols = list(alpdir.items())
    hHeap = BinaryHeap()
    for symbol in symbols:
        hHeap.insert(BinaryTree(symbol))

    return hHeap

if __name__ == '__main__':
    dir = {'a': 12, 'b': 20, 'c': 13, 'e': 23,'f': 14}
    myHeap = builtHuffmanHeap(dir)
    print(myHeap.currentsize)