class coder:
    def __init__(self, dict1={}) -> None:
        self.dict1 = dict1

    def coding(self):
        """"""
        #创建字典副本用于编码
        dict_cp = self.dict1.copy()
        for key in self.dict1.keys():
            dict_cp[key] = ""


        return dict_cp


    def decoding(selc, content):
        pass

if __name__ in '__main__':
    coder = coder({'a': 10, 'b': 10})
    print(coder.coding())
