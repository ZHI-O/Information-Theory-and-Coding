import r_w_method
import statistic
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #创建文件读取器
    reader = r_w_method.reading()

    #创建字符统计器
    stc = statistic.statistic(reader.reading("test.txt"))

    #用numpy库进行数据处理
    arry = np.array(list(stc.statistic().values()))

    #图像绘制
    arry = arry / stc.sum_value()
    plt.figure()
    plt.plot(arry, '*')
    plt.show()

    print(type(arry))

    