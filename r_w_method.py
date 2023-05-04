class reading:
    def reading(self, addr):
        '''Reading the text
            You should add the address as varity
        '''
        try:
            with open(addr) as text:
                contents = text.read()
            return contents
        except FileNotFoundError:
            print("Please write the right address.")
 
    def writing(self, addr):
        '''Writing the text
            You should add the address as varity
        '''
        try:
            pass
        except:
            pass
        finally:
            pass