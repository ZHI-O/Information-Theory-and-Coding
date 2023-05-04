class statistic:
    def __init__(self, characters="") -> None:
        self.characters = characters

    def statistic(self):
        """Statistic the letter in letters and draw a histogram
            the varity is a type of ls
            and it returns the statistic result as dir,
            meanwhile you can get the descending dict.
        """
        dir = {}

        for character in self.characters:
            if character in dir.keys():
                dir[character] += 1
            else:
                dir[character] = 1

        ls = sorted(dir.items(), key=lambda x:x[1], reverse=True)

        dir_fal = dict(ls)

        return dir_fal
    
    def sum_value(self):
        """Cumulate the number of the signal"""
        try:
            return sum(self.statistic().values())
        except:
            pass

if __name__ == '__main__':
    a = 'aaaassss'
    stc1 =  statistic(a)
    print(stc1.statistic().items())