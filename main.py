import r_w_method
import statistic
import huffmantree
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #创建文件读取器
    reader = r_w_method.reader('test.txt')

    #创建字符统计器
    x = reader.reading()
    stc = statistic.statistic(reader.reading())

    #创建huffmanTree
    myhuffmantree = huffmantree.builtHuffmanTree(stc.statistic())

    #huffmanTree进行编码
    myhuffmantree.coding()

    #输出编码结果
    dir = huffmantree.preorder(myhuffmantree)

    #编码速率
    averN = 0
    totle = sum(stc.statistic().values())

    for symbol in stc.statistic().keys():
        averN += len(dir[symbol]) * (stc.statistic()[symbol] / totle)
    print(averN)

    # 计算信源熵
    Hu = 0
    
    for symbol in stc.statistic().keys():
        Hu += - (stc.statistic()[symbol] / totle) * np.log2((stc.statistic()[symbol] / totle))

    print(Hu/averN)