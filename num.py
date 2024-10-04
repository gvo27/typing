import random

class IterObj:
    def __init__(self):
        pass
    
    def __iter__(self):
        return self
    
    def __next__(self) -> str:
        pass

class Number(IterObj):
    def __init__(self, max_len: int = 9, comma: bool = True, max_dec: int = 4): 
        super().__init__()
        self.comma = comma
        self.max_len = max_len
        self.max_dec = max_dec
    
    def __next__(self) -> str:
        num = self.rand()
        if self.comma:
            return f"{num:,}"
        else:
            return f"{num}"
    
    def rand(self) -> float:
        length = random.randint(self.max_len//2, self.max_len)
        if length < 1:
            return 0
        result = random.uniform(0, 10**length)
        if self.max_dec == 0:
            return int(result)
        dec = random.randint(1, self.max_dec) 
        return round(result, dec) 
    
class Sentence(IterObj):
    def __init__(self, iterator: IterObj, num_words: int = 3):
        super().__init__()
        self.iterator = iterator
        self.len = num_words
    
    def __next__(self) -> str:
        result = ""
        for _ in range(self.len):
            n = next(self.iterator)
            result += n + ' '
        return result

class Generator(IterObj):
    def __init__(self, word_size: int, thousandth_comma: bool, decimal_places: int, sent_size: int):
        super().__init__()
        self.num = Number(max_len=word_size, comma=thousandth_comma, max_dec= decimal_places)
        self.sent = Sentence(iterator=self.num, num_words=sent_size)
                
    def __next__(self) -> str:
        return next(self.sent)