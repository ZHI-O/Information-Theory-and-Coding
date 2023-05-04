class reader:
    def __init__(self, inputname='', outputname='') -> None:
        #读入文件名
        self.inputname = inputname
        #写入文件名
        self.outputname = outputname
        
    #进行读操作
    def reading(self):
        '''Reading the text
            You should add the address as varity
        '''
        try:
            #以二进制方式打开文件
            with open(self.inputname, 'rb') as text:
                contents = text.read()
            return contents
        except FileNotFoundError:
            print("Please write the right address.")
 
    def writing(self):
        '''Writing the text
            You should add the address as varity
        '''
        try:
            #进行文件写操作
            with open(self.outputname, 'w') as outputfile:
                pass
        except:
            pass
        finally:
            pass

if __name__ == '__main__':
    reader = reader(inputname='test.txt',outputname='outputfile.txt')
    print(reader.reading())
    reader.writing()