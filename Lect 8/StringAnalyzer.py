from string import punctuation


class Analyzer:
    def __init__(self, s):
        for c in punctuation:
            s = s.replace(c, '')    # replaces a specified phrase with another specified phrase
            s = s.lower()           # converts all uppercase characters in a string into lowercase characters
            self.words = s.split()  # Split a string into a list where each word is a list item

    # how many words are in the string
    def number_of_words(self):
        return len(self.words)

    # how many start with a given string
    def starts_with(self, s):
        return len([w for w in self.words if w[:len(s)] == s])

    # how many are of a given length
    def number_with_length(self, n):
        return len([w for w in self.words if len(w) == n])


s = 'This is a test of the class.'
analyzer = Analyzer(s)
print(analyzer.words)
print('Number of words:', analyzer.number_of_words())
print('Number of words starting with "t":', analyzer.starts_with('t'))
print('Number of 2-letter words:', analyzer.number_with_length(2))