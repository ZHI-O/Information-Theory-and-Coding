import r_w_method
import statistic
import huffmantree
import numpy as np
import matplotlib.pyplot as plt
import six

if __name__ == '__main__':
    #创建文件读取器
    reader = r_w_method.reader('pre_img.txt','outputfile')

    #创建字符统计器
    stc = statistic.statistic(reader.reading())

    #创建huffmanTree
    myhuffmantree = huffmantree.builtHuffmanTree(stc.statistic())

    #huffmanTree进行编码
    myhuffmantree.coding()

    #输出编码结果
    dir = huffmantree.preorder(myhuffmantree)
    #print(dir[reader.reading()[0]])
    #编码后文件输出
    output = open('codefile', 'wb')
    code = ''
    for key in reader.reading():
        code = code + dir[key]
        out = 0
        while len(code)>8:
            for x in range(8):
                out = out<<1
                if code[x] == '1':
                    out = out|1
            code = code[8:]
            output.write(six.int2byte(out))
            out = 0

    # 处理剩下来的不满8位的code
    output.write(six.int2byte(len(code)))
    out = 0
    for i in range(len(code)):
        out = out<<1
        if code[i]=='1':
            out = out|1
    for i in range(8-len(code)):
        out = out<<1
    # 把最后一位给写入到文件当中
    output.write(six.int2byte(out))

    # 6. 关闭输出文件，文件压缩完毕
    output.close()

    # 文件解码
    # 将压缩后的数据恢复成01符号 
    rsl = ''
    with open('codefile', 'rb') as f:
        with open("post_img.txt","w") as out:
            s = ''
            tree = myhuffmantree
            for b in f.read()[:-2]:
                byte = str(bin(b)[2:].zfill(8))
                for s in byte:
                    if s == '1':
                        tree = tree.getLeftChild()
                    elif s == '0':
                        tree = tree.getRightChild()
                    if not tree.getLeftChild() and not tree.getRightChild():
                        rsl = chr(tree.getSymbol())
                        #print(chr(tree.getSymbol()), end='')
                        out.write(rsl)
                        tree = myhuffmantree

    # #编码速率
    # averN = 0
    # totle = sum(stc.statistic().values())

    # for symbol in stc.statistic().keys():
    #     averN += len(dir[symbol]) * (stc.statistic()[symbol] / totle)
    # print(averN)

    # # 计算信源熵
    # Hu = 0
    
    # for symbol in stc.statistic().keys():
    #     Hu += - (stc.statistic()[symbol] / totle) * np.log2((stc.statistic()[symbol] / totle))

    # print(Hu/averN)

    