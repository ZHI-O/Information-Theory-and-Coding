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
        '''插入左节点'''
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        '''插入右节点'''
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getLeftChild(self):
        '''获取左子树'''
        return self.leftChild
    
    def getRightChild(self):
        '''获取右子树'''
        return self.rightChild
    
    def setRootVal(self, obj):
        '''设置根节点'''
        self.key = obj

    def getRootVal(self):
        '''获取根节点'''
        return self.key

class BinaryHeap:
    '''构建子树二叉堆
        属性：
            heapList:子树列表
            currentsize:列表大小'''
    def __init__(self) -> None:
        self.heapList = [BinaryTree((0, 0, '0'))]
        self.currentsize = 0
    
    def insert(self, obj):
        '''插入节点'''
        self.heapList.append(obj)
        self.currentsize += 1
        self.percUp(self.currentsize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i].getRootVal()[1] < self.heapList[i // 2].getRootVal()[1]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = temp
            i //= 2
    
    def percDown(self, i):
        while (i * 2) <= self.currentsize:
            mc = self.minChild(i)
            if self.heapList[i].getRootVal()[1] > self.heapList[mc].getRootVal()[1]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc
    
    def minChild(self, i):
        if i * 2 + 1 > self.currentsize:
            return i * 2
        else:
             if self.heapList[i * 2].getRootVal()[1] < self.heapList[i * 2 + 1].getRootVal()[1]:
                 return i * 2
             else:
                 return i * 2 + 1
             
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def builtHeap(self, alist):
        i = len(alist) // 2
        self.currentsize = len(alist)
        self.heapList = [BinaryTree((0, 0, '0'))] + alist[:]
        while(i > 0):
            self.percDown(i)
            i -= 1

def builtHuffmanHeap(alpdir):
    symbols = list(BinaryTree(item) for item in alpdir.items())
    hHeap = BinaryHeap()
    hHeap.builtHeap(symbols)
    return hHeap

if __name__ == '__main__':
    dir = {'a': 12, 'b': 20, 'c': 13, 'e': 23,'f': 14}
    myHeap = builtHuffmanHeap(dir)
    for i in range(1, myHeap.currentsize + 1):
        print(myHeap.heapList[i].getRootVal())
    print(myHeap.currentsize)