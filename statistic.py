class statistic:
    def __init__(self, letters="") -> None:
        self.letters = letters

    def statistic(self):
        """Statistic the letter in letters and draw a histogram
            the varity is a type of ls
            and it returns the statistic result as dir,
            meanwhile you can get the descending dict.
        """
        alphabet = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,
                    'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,
                    's': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0,' ': 0,
                    "'": 0,'.': 0,',': 0,';': 0
                    }
        for letter in self.letters.lower():
            if letter in alphabet.keys():
                alphabet[letter] += 1
        
        alphabet_fal = {}
        for key, value in alphabet.items():
            if value != 0:
                alphabet_fal[key] = value

        ls = sorted(alphabet_fal.items(), key=lambda x:x[1], reverse=True)

        alphabet_fal = dict(ls)

        return alphabet_fal
    
    def sum_value(self):
        """Cumulate the number of the signal"""
        try:
            return sum(self.statistic().values())
        except:
            pass

if __name__ == '__main__':
    a = 'sadfsafdfdsagfsadfasg'
    stc1 =  statistic(a)
    print(stc1.statistic().items())