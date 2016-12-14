import collections

class Vocabulary(object):

    def __init__(self, words, size):
        word_counts = [(count, word) for word, count in collections.Counter(words).iteritems()]
        top_words = zip(*(sorted(word_counts, reverse=True)[:size]))[1]
        all_words = ['<UNK>'] + sorted(top_words)
        self.word_to_id = {word: wid for wid, word in enumerate(all_words)}
        self.id_to_word = {wid: word for word, wid in self.word_to_id.iteritems()}

    def to_id(self, word):
        return self.word_to_id.get(word, 0)

    def to_word(self, wid):
        return self.id_to_word.get(wid, '<UNK>')

    def size(self):
        return len(self.word_to_id)