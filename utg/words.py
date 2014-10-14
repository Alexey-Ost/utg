# coding: utf-8
import random

from utg import relations as r
from utg import data
from utg import utils


class Properties(object):
    __slots__ = ('_data',)

    def __init__(self, *argv):
        self._data = {}
        self._update(*argv)

    def serialize(self):
        return {r.PROPERTY_TYPE.index_relation[property_type].value: property.value
                for property_type, property in self._data.iteritems()}

    @classmethod
    def deserialize(cls, data):
        return cls(*[r.PROPERTY_TYPE(int(property_type)).relation(property_value)
                     for property_type, property_value in data.iteritems()])

    def _update(self, *argv):
        for property in argv:
            if property is None:
                continue

            # optimization, replace of isinstance
            if hasattr(property, '_relation'):
                self._data[property._relation] = property
            else:
                self._data.update(property._data)


    def get_key(self, key, schema=None):
        if schema is None:
            schema = key

        value = []
        for property_group in key:
            property = self.get(property_group)

            for p in data.INVERTED_RESTRICTIONS.get(property_group, ()):

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

    def clone(self, *argv):
        return self.__class__(self, *argv)

    def __unicode__(self):
        return u'(%s)' % (u','.join(self._data[property.relation].verbose_id
                                    for property in r.PROPERTY_TYPE.records
                                    if property.relation in self._data))

    def __str__(self):
        return self.__unicode__().encode('utf-8')

    def __eq__(self, other):
        return (isinstance(other, Properties) and
                self._data == other._data)


class Word(object):
    __slots__ = ('type', 'forms', 'properties', 'patches', '_lazy__number_of_syllables', '_lazy__has_fluent_vowel')

    def __init__(self, type, forms, properties=Properties(), patches=None):
        self.type = type
        self.forms = forms
        self.properties = properties
        self.patches = {} if patches is None else patches

    def serialize(self):
        return {'type': self.type.value,
                'forms': self.forms,
                'properties': self.properties.serialize(),
                'patches': {key.value: patch.serialize() for key, patch in self.patches.iteritems()}}

    @classmethod
    def deserialize(cls, data):
        return cls(type=r.WORD_TYPE(data['type']),
                   forms=data['forms'],
                   properties=Properties.deserialize(data['properties']),
                   patches={r.WORD_TYPE(int(key)): cls.deserialize(patch_data) for key, patch_data in data['patches'].iteritems()})

    def form(self, properties):
        # we must update properties with self.properties
        # since self.properties can contain items form schema (example: NUMBER in NOUN)
        return self._form(Properties(properties, self.properties))

    def _form(self, properties):
        # here we expected correct full properties
        if (self.type.is_NOUN  and
            r.WORD_TYPE.NOUN_COUNTABLE_FORM in self.patches and
            properties.get(r.NUMBER).is_PLURAL and
            properties.is_specified(r.INTEGER_FORM)):
            return self.patches[r.WORD_TYPE.NOUN_COUNTABLE_FORM]._form(properties)

        return self.forms[data.WORDS_CACHES[self.type][properties.get_key(key=self.type.schema)]]

    def normal_form(self):
        return self.form(properties=self.properties)

    def __eq__(self, other):
        return (isinstance(other, Word) and
                self.type == other.type and
                self.properties == other.properties and
                self.forms == other.forms and
                self.patches == other.patches)

    @classmethod
    def get_forms_number(cls, type):
        return len(data.WORDS_CACHES.get(type, []))

    @classmethod
    def get_keys(cls, type):
        cache = data.WORDS_CACHES[type]
        keys = [None] * len(cache)
        for key, index in cache.iteritems():
            keys[index] = key
        return keys


    @classmethod
    def create_test_word(cls, type, prefix=u'w-', suffix=u'', only_required=False, properties=None, patches=None):
        keys = cls.get_keys(type)

        forms = []
        for key in keys:
            forms.append(prefix + u','.join(property.verbose_id for property in key if property is not None) + suffix)

        if properties is None:
            properties = Properties()

        for property_type in r.PROPERTY_TYPE.records:
            if property_type not in type.properties:
                continue

            required = type.properties[property_type]

            if not required and (only_required or random.random() > 0.5):
                continue

            properties.update(random.choice(property_type.records))

        if patches is None:
            patches = {}

        return cls(type=type, forms=forms, properties=properties, patches=patches)

    @utils.lazy_property
    def number_of_syllables(self):
        form = self.forms[0]
        return max(1, sum(form.count(char) for char in data.VOWELS))

    @utils.lazy_property
    def has_fluent_vowel(self):
        form = self.forms[0]
        base_vowels = u''.join([char for char in form if char in data.VOWELS])

        # TODO: does we need to check patches forms?

        for other_form in self.forms[1:]:
            if not other_form: # form can be unspecified
                continue
            form_vowels = u''.join([char for char in other_form if char in data.VOWELS])

            if not form_vowels.startswith(base_vowels):
                return True

        return False


class WordForm(object):
    __slots__ = ('word', 'properties', 'form_properties', '_lazy__form', '_lazy__starts_with_consonant_cluster')

    def __init__(self, word, properties=None, form_properties=None):
        self.word = word
        self.properties = word.properties if properties is None else Properties(properties, word.properties)
        self.form_properties = Properties(form_properties, word.properties) if form_properties is not None else self.properties


    @classmethod
    def get_form(cls, word, properties):
        form = word._form(properties)

        if properties.get(r.WORD_CASE).is_UPPER:
            form = form[0].upper() + form[1:]

        return form

    @utils.lazy_property
    def form(self):
        return self.get_form(self.word, self.form_properties)

    @utils.lazy_property
    def starts_with_consonant_cluster(self):
        form = self.form
        return (form[0] in data.CONSONANTS) and (len(form) == 1 or form[1] in data.CONSONANTS)


    def __eq__(self, other):
        # print self.word == other.word
        # print self.properties, other.properties
        return (self.word == other.word and
                self.properties == other.properties)
