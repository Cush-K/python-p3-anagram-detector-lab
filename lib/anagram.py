words = [
    'enlists',
    'google',
    'inlets',
    'banana'
    ]

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        sorted_word = sorted(self.word)
        matching_words = []

        for word in word_list:
            if sorted(word) == sorted_word:
               matching_words.append(word)
        
        return matching_words
                   

word = Anagram("babies")
print(word.match(words))