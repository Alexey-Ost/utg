# coding: utf-8

from utg import words
from utg import data
from utg import exceptions
from utg import constructors
from utg import relations as r


_INVERTED_WORDS_CACHES__PROPERTIES = {}
for word_type in r.WORD_TYPE.records:
    _INVERTED_WORDS_CACHES__PROPERTIES[word_type] = [words.Properties(*key) for key in data.INVERTED_WORDS_CACHES[word_type]]


class Dictionary(object):
    __slots__ = ('_data', '_index')

    def __init__(self, words=[]):
        self._data = {}
        self._index = {word_type: {} for word_type in r.WORD_TYPE.records}

        for word in words:
            self.add_word(word)


    def add_word(self, word):
        normal_form = word.normal_form()
        if normal_form in self._index[word.type]:
            raise exceptions.DuplicateWordError(type=word.type, normal_form=normal_form)

        self._index[word.type][normal_form] = word

        for i, form in enumerate(word.forms):
            if form not in self._data:
                self._data[form] = []

            if all(word is not test_form.word for test_form in self._data[form]):
                self._data[form].append(words.WordForm(word=word, properties=_INVERTED_WORDS_CACHES__PROPERTIES[word.type][i]))


    def get_words(self, text, type=None):

        if text not in self._data:
            return []

        choices = self._data[text]

        if type:
            choices = [word for word in choices if word.word.type == type]

        return choices


    def has_words(self, text, type=None):
        return bool(self.get_words(text, type=type))

    def is_word_registered(self, type, normal_form):
        if type.is_INTEGER:
            return True
        return normal_form in self._index[type]

    def get_word(self, text, type=None):

        choices = self.get_words(text, type=type)

        if not choices:
            raise exceptions.NoWordsFoundError(text=text, type=type)

        if len(choices) > 1:
            raise exceptions.MoreThenOneWordFoundError(text=text, type=type)

        return choices[0]

    def iterwords(self):
        for type in r.WORD_TYPE.records:
            for word in self._index[type].itervalues():
                yield word
