class HuffmanTree():
    '''创建HuffmanTree
        属性：
            weight:数据类型为整形。文件中出现的次数。
    '''
    def __init__(self,symbol = None,weight = 0) -> None:
        self.symbol = symbol
        self.weight = weight
        self.code = ''
        self.leftChild = None
        self.rightChild = None
    
    def getSymbol(self):
        return self.symbol
    
    def setSymbol(self, symbol):
        self.symbol = symbol

    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        self.weight = weight

    def getCode(self):
        return self.code
    
    def setCode(self, code):
        self.code = code

    def getLeftChild(self):
        '''获取左子树'''
        return self.leftChild
    
    def getRightChild(self):
        '''获取右子树'''
        return self.rightChild
    
    def setLeftChild(self, leftChild):
        self.leftChild = leftChild

    def setRightChild(self, rightChild):
        self.rightChild = rightChild
        
    def coding(self):
        if self.getLeftChild() and self.getRightChild():
            self.getLeftChild().setCode(self.getCode() + "1")
            self.getLeftChild().coding()
            self.getRightChild().setCode(self.getCode() + "0")
            self.getRightChild().coding()
        else:
            return None
        
def builtHuffmanTree(alist):
    hTrees = []
    for (key, val) in alist.items():
        hTrees.append(HuffmanTree(key, val))
    
    while len(hTrees) > 1:
        t1 = hTrees.pop()
        t2 = hTrees.pop()
        t = HuffmanTree(None, t1.getWeight() + t2.getWeight())
        t.setLeftChild(t1)
        t.setRightChild(t2)

        if len(hTrees) > 1:
            if hTrees[len(hTrees) - 1].getWeight() < t.getWeight():
                hTrees.append(t)
            elif hTrees[0].getWeight() > t.getWeight():
                hTrees.insert(0, t)
            else:
                for i in range(len(hTrees)):
                    if hTrees[i].getWeight() >= t.getWeight():
                        hTrees.insert(i, t)
                        break
        else:
            hTrees.append(t)

    return hTrees[0]    

def preorder(huffmanTree):
    if huffmanTree:
        if huffmanTree.getSymbol() != None:
            print(f'{huffmanTree.getSymbol()} : {huffmanTree.getCode()}')
        preorder(huffmanTree.getLeftChild())
        preorder(huffmanTree.getRightChild())

if __name__ == '__main__':
    from statistic import *
    a = 'asdnjgldlaossssss'
    stc1 =  statistic(a)
    huffmanTree = builtHuffmanTree(stc1.statistic())
    huffmanTree.coding()
    preorder(huffmanTree)