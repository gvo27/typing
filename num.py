import random

class IterObj:
    def __init__(self):
        pass
    
    def __iter__(self):
        return self
    
    def __next__(self) -> str:
        pass

class Number(IterObj):
    def __init__(self, max_len: int = 9, complex: bool = True, max_dec: int = 5):
        self.complex = complex
        self.max_len = max_len
        self.max_dec = max_dec
    
    def __next__(self) -> str:
        num = self.rand()
        if self.complex:
            return f"{num:,}"
        else:
            return f"{int(num)}"
    
    def rand(self) -> float:
        length = random.randint(self.max_len//2, self.max_len)
        if length < 1:
            return 0
        dec = random.randint(2, self.max_dec) 
        return round(random.uniform(0, 10**length), dec) 
    
class Sentence(IterObj):
    def __init__(self, num_words: int = 3, word_size: int = 9, complex_words: bool = True):
        self.length = num_words
        self.num = Number(max_len=word_size, complex=complex_words)
    
    def __next__(self) -> str:
        result = ""
        for _ in range(self.length):
            n = next(self.num)
            result += n + ' '
        return result