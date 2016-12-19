import itertools
import collections
import re

class Vocabulary(object):

  START_TOKEN = "<s>"
  END_TOKEN = "</s>"
  UNK_TOKEN = "<unk>"

  def __init__(self, tokens, size=None):
    self.unigram_counts = collections.Counter(tokens)
    # leave space for "<s>", "</s>", and "<unk>"
    top_counts = self.unigram_counts.most_common(None if size is None else (size - 3))
    vocab = ([self.START_TOKEN, self.END_TOKEN, self.UNK_TOKEN] +
             [w for w,c in top_counts])

    # Assign an id to each word, by frequency
    self.id_to_word = dict(enumerate(vocab))
    self.word_to_id = {v:k for k,v in self.id_to_word.iteritems()}
    self.size = len(self.id_to_word)
    if size is not None:
        assert(self.size <= size)

    # Store special IDs
    self.START_ID = self.word_to_id[self.START_TOKEN]
    self.END_ID = self.word_to_id[self.END_TOKEN]
    self.UNK_ID = self.word_to_id[self.UNK_TOKEN]

  def words_to_ids(self, words):
    return [self.word_to_id.get(w, self.UNK_ID) for w in words]

  def ids_to_words(self, ids):
    return [self.id_to_word[i] for i in ids]

  def sentence_to_ids(self, words):
    return [self.START_ID] + self.words_to_ids(words) + [self.END_ID]

def canonicalize_digits(word):
    if any([c.isalpha() for c in word]): return word
    word = re.sub("\d", "DG", word)
    if word.startswith("DG"):
        word = word.replace(",", "") # remove thousands separator
    return word

def canonicalize_word(word, wordset=None, digits=True):
    word = word.lower()
    if digits:
        if (wordset != None) and (word in wordset): return word
        word = canonicalize_digits(word) # try to canonicalize numbers
    if (wordset == None) or (word in wordset): return word
    else: return "<unk>" # unknown token