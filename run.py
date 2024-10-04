import datetime
from num import Generator
from difflib import SequenceMatcher

def run():
    
    intro = input("...Press Enter to begin...") 
    generator = Generator(9, True, 4, 18)
    while True:
        example = next(generator)
        start = datetime.datetime.now()
        answer = input(example + "\n")
        
        time = round((datetime.datetime.now() - start).total_seconds(), 2) # seconds
        result = check(example, answer)
        kph = round(len(answer) / time * 60 * 60, 2)
        input(f">Accuracy: {int(result*100)}% \n>Time: {time} s \n>KPH: {kph} \n...Press Enter to continue...")

def check(a, b):
    s = SequenceMatcher(None, a, b)
    return round(s.ratio(), 2)
        
run()