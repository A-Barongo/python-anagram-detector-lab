# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word=word.lower()
    def match(self,word_array):
        
        return [w for w in word_array if sorted(w.lower())==sorted(self.word)]