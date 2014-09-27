# coding: utf-8
import copy
import random

from utg import relations as r
from utg import data


class Properties(object):


    def __init__(self, *argv):
        self._data = {}
        self.update(*argv)

    def serialize(self):
        return {r.PROPERTY_TYPE.index_relation[property_type].value: property.value
                for property_type, property in self._data.iteritems()}

    @classmethod
    def deserialize(cls, data):
        return cls(*[r.PROPERTY_TYPE(int(property_type)).relation(property_value)
                     for property_type, property_value in data.iteritems()])

    def update(self, *argv):
        for property in argv:
            if property is None:
                continue

            if isinstance(property, self.__class__):
                self._data.update(property._data)
            else:
                self._data[property._relation] = property

    def get_key(self, key, schema=None):
        if schema is None:
            schema = key

        value = []
        for property_group in key:
            property = self.get(property_group)

            if property_group in data.INVERTED_RESTRICTIONS:

                for p in data.INVERTED_RESTRICTIONS[property_group]:

                    if p._relation not in schema:
                        continue

                    if self.get(p._relation) == p:
                        property = None
                        break

            value.append(property)

        return tuple(value)

    def get(self, property_group):
        if property_group in self._data:
            return self._data[property_group]
        return data.DEFAULT_PROPERTIES[property_group]

    def is_specified(self, property_group):
        return property_group in self._data

    def clone(self):
        obj = self.__class__()
        obj._data = copy.copy(self._data)
        return obj

    def __unicode__(self):
        return u'(%s)' % (u','.join(self._data[property.relation].verbose_id
                                    for property in r.PROPERTY_TYPE.records
                                    if property.relation in self._data))

    def __str__(self):
        return self.__unicode__().encode('utf-8')

    def __eq__(self, other):
        return self._data == other._data


class Word(object):

    def __init__(self, type, forms, properties):
        self.type = type
        self.forms = forms
        self.properties = properties

    def serialize(self):
        return {'type': self.type.value,
                'forms': self.forms,
                'properties': self.properties.serialize()}

    @classmethod
    def deserialize(cls, data):
        return cls(type=r.WORD_TYPE(data['type']),
                   forms=data['forms'],
                   properties=Properties.deserialize(data['properties']))

    def form(self, properties):
        real_properties = properties.clone()
        real_properties.update(self.properties)
        # print '  ', real_properties.get_key(key=self.type.schema)
        return self.forms[data.WORDS_CACHES[self.type][real_properties.get_key(key=self.type.schema)]]

    def normal_form(self):
        return self.form(properties=self.properties)

    def __eq__(self, other):
        return (self.type == other.type and
                self.properties == other.properties and
                self.forms == other.forms)

    @classmethod
    def get_forms_number(cls, type):
        return len(data.WORDS_CACHES[type])

    @classmethod
    def get_keys(cls, type):
        cache = data.WORDS_CACHES[type]
        keys = [None] * len(cache)
        for key, index in cache.iteritems():
            keys[index] = key
        return keys


    @classmethod
    def create_test_word(cls, type, prefix=u'w-', only_required=False):
        keys = cls.get_keys(type)

        forms = []
        for key in keys:
            forms.append(prefix + u','.join(property.verbose_id for property in key if property is not None))

        properties = Properties()

        for relation, required in type.properties.iteritems():
            if not required and (only_required or random.random() > 0.5):
                continue
            properties.update(random.choice(relation.records))

        return cls(type=type, forms=forms, properties=properties)


class WordForm(object):
    __slots__ = ('word', 'properties', 'form')

    def __init__(self, word, properties, form):
        self.word = word
        self.properties = properties
        self.form = form

        # properties must contain ALL valuable data
        # base word properties must redefine any other properties
        self.properties.update(word.properties) # TODO: test that line

    def __eq__(self, other):
        return (self.word == other.word and
                self.properties == other.properties and
                self.form == other.form)
