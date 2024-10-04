import datetime
from num import Sentence
from difflib import SequenceMatcher

def run():
    
    NUMBER_OF_WORDS = 7
    COMMAS_AND_DECIMALS = True
    
    intro = input("Press Enter to begin.") 
    generator = Sentence(num_words=NUMBER_OF_WORDS, complex_words=COMMAS_AND_DECIMALS)
    while True:
        example = next(generator)
        start = datetime.datetime.now()
        answer = input(example + "\n")
        
        time = round((datetime.datetime.now() - start).total_seconds(), 2) # seconds
        result = check(example, answer)
        kph = round(len(answer) / time * 60 * 60, 2)
        input(f"Accuracy: {int(result*100)}% \nTime: {time} s \nKPH: {kph} \nPress Enter to continue.")

def check(a, b):
    s = SequenceMatcher(None, a, b)
    return round(s.ratio(), 2)
        
run()