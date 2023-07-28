#This is the Dictionary Class

class Dictionary:
    
    def __init__(self, sw, gl, uv, gtp, aw):
        self.search_word = sw
        self.get_language = gl
        self.update_version = uv
        self.go_to_page = gtp
        self.add_word = aw

#Made a set of words with definition so its easier to have something to search
    def __init__(self):
        self.words = {
            "apple": "a fruit that grows on trees and has a red or green skin",
            "banana": "a long curved fruit with a yellow skin",
            "orange": "a round citrus fruit with a thick skin and juicy flesh"
        }
        self.version = 1.0

    def search(self, word):
       
        meaning = self.words.get(word)
        if meaning:
            print(f"The meaning of '{word}' is: {meaning}")
        else:
            print(f"'{word}' not found in the dictionary.")

    def get_language(self, word):
        print(f"The language of '{word}' is English.")

    def update_version(self):
        self.version = self.version + 1.0 
        print(f"Updated dictionary version to {self.version}.")

    def go_to_page_number(self, page_number):
        print(f"Going to page {page_number} in the dictionary...")

    def add_new_word(self, word, meaning):
        print(f"Adding '{word}': {meaning} to the dictionary...")

#Example usage:
dictionary = Dictionary()

dictionary.search("apple")
dictionary.get_language("apple")
dictionary.update_version()
dictionary.go_to_page_number(42)
dictionary.add_new_word("orange", "a round citrus fruit")
