class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        matches = []
        sorted_word = sorted(self.word)  # Sort the letters of the original word

        for candidate in possible_anagrams:
            if sorted_word == sorted(candidate):  # Compare sorted letters
                matches.append(candidate)  # If they match, add to results
        
        return matches
