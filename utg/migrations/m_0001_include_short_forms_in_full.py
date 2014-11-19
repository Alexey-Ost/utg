# coding: utf-8

from utg.relations import *
from utg import data

# receive and return only serialized data
def migrate(word_data):

    if word_data['type'] == 1: # adjective
        migrate_forms(word_data, OLD_ADJECTIVE_CACHE, data.WORDS_CACHES[WORD_TYPE.ADJECTIVE])

    if word_data['type'] == 4: # participle
        migrate_forms(word_data, OLD_PARTICIPLE_CACHE, data.WORDS_CACHES[WORD_TYPE.PARTICIPLE])

    return word_data


def migrate_forms(word_data, old_cache, new_cache):
    old_forms = word_data['forms']
    new_forms = [u''] * len(new_cache)

    for new_key, new_index in new_cache.iteritems():
        new_forms[new_index] = old_forms[get_nearest_old_index(new_key, old_cache)]

    word_data['forms'] = new_forms


def get_nearest_old_index(new_key, old_cache):

    new_key = new_key[1:] # remove first element of the new schema, wich now is word_form

    best_index = None
    best_union = -1

    for old_key, old_index in old_cache.iteritems():
        current_union = len([1 for old, new in zip(old_key, new_key) if old == new])

        if current_union > best_union:
            best_union = current_union
            best_index = old_index

    return best_index


OLD_ADJECTIVE_CACHE = {(NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE, GRADE.POSITIVE): 132, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 16, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 41, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 37, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 33, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 73, (NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.ANIMATE, GRADE.POSITIVE): 114, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 40, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.POSITIVE): 27, (NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 113, (NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 127, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 28, (NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE, GRADE.POSITIVE): 141, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 50, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 79, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 22, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 11, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 87, (NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 110, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 43, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 44, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 26, (NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 134, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 93, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 35, (NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 125, (NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE, GRADE.POSITIVE): 111, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 17, (NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 139, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 75, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 48, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 30, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 12, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 106, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 89, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 66, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 59, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 102, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 13, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 92, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 2, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 1, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 58, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 104, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 77, (NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.INANIMATE, GRADE.POSITIVE): 123, (NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE, GRADE.POSITIVE): 135, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 95, (NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE, GRADE.POSITIVE): 129, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.POSITIVE): 63, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 90, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 107, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 62, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 61, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 18, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 97, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 85, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 52, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 68, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 7, (NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 133, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 64, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 71, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 65, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 83, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 34, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 103, (NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 116, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 74, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 39, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 19, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 55, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.POSITIVE): 99, (NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE, GRADE.POSITIVE): 126, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 4, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 5, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.POSITIVE): 45, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 98, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 23, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 88, (NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE, GRADE.POSITIVE): 108, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 20, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 69, (NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.ANIMATE, GRADE.POSITIVE): 120, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.POSITIVE): 42, (NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 143, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.POSITIVE): 24, (NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.INANIMATE, GRADE.POSITIVE): 117, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 3, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 36, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 72, (NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 115, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 91, (NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 124, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 105, (NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 128, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 101, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 31, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 10, (NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 142, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 21, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.POSITIVE): 78, (NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 119, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 8, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 14, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 15, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 38, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 86, (NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 112, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 56, (NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 137, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 76, (NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 131, (NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 130, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.POSITIVE): 9, (NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE, GRADE.POSITIVE): 138, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 82, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 51, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 67, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.POSITIVE): 6, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.POSITIVE): 96, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 70, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 80, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.POSITIVE): 81, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 94, (NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 0, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 32, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE, GRADE.POSITIVE): 57, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 54, (NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 136, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 29, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 47, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 46, (NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.POSITIVE): 60, (NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 109, (NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.POSITIVE): 84, (NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 122, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE, GRADE.SUPERLATIVE): 53, (NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE, GRADE.SUPERLATIVE): 140, (NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 121, (NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.NEUTER, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 100, (NUMBER.SINGULAR, CASE.DATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 49, (NUMBER.SINGULAR, CASE.GENITIVE, GENDER.NEUTER, ANIMALITY.ANIMATE, GRADE.COMPARATIVE): 25, (NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.INANIMATE, GRADE.COMPARATIVE): 118}


OLD_PARTICIPLE_CACHE = {(TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE): 104, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE): 157, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE): 174, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE): 129, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE): 126, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.INANIMATE): 137, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.GENITIVE, None, ANIMALITY.INANIMATE): 147, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.FEMININE, ANIMALITY.INANIMATE): 35, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.ANIMATE): 182, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE): 47, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE): 142, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE): 66, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE): 5, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE): 18, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE): 114, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.INANIMATE): 87, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE): 44, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.INANIMATE): 113, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE): 127, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE): 4, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE): 121, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE): 49, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE): 21, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.ANIMATE): 110, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.NEUTER, ANIMALITY.ANIMATE): 32, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE): 92, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.FEMININE, ANIMALITY.INANIMATE): 11, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.DATIVE, None, ANIMALITY.ANIMATE): 172, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.DATIVE, None, ANIMALITY.INANIMATE): 149, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.NEUTER, ANIMALITY.ANIMATE): 26, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE): 165, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE): 167, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.GENITIVE, None, ANIMALITY.ANIMATE): 146, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE): 6, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE): 186, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE): 176, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE): 63, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE): 116, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE): 19, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.MASCULINE, ANIMALITY.INANIMATE): 79, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.INANIMATE): 185, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.MASCULINE, ANIMALITY.INANIMATE): 73, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.DATIVE, None, ANIMALITY.INANIMATE): 125, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE): 71, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.INANIMATE): 135, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.ANIMATE): 184, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE): 189, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE): 138, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE): 179, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE): 145, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.GENITIVE, None, ANIMALITY.ANIMATE): 170, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.MASCULINE, ANIMALITY.INANIMATE): 31, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.FEMININE, ANIMALITY.ANIMATE): 58, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE): 132, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE): 65, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE): 55, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE): 45, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.NEUTER, ANIMALITY.INANIMATE): 27, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE): 90, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE): 60, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.GENITIVE, None, ANIMALITY.ANIMATE): 98, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE): 69, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE): 48, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.GENITIVE, None, ANIMALITY.INANIMATE): 99, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.ANIMATE): 136, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.ANIMATE): 158, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE): 153, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE): 22, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE): 155, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE): 96, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.FEMININE, ANIMALITY.ANIMATE): 76, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE): 94, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE): 68, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE): 37, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE): 3, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE): 139, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.INANIMATE): 39, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.DATIVE, None, ANIMALITY.ANIMATE): 124, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE): 107, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE): 51, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.ANIMATE): 86, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE): 20, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE): 117, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.FEMININE, ANIMALITY.ANIMATE): 28, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE): 131, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE): 70, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.DATIVE, None, ANIMALITY.ANIMATE): 100, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.ANIMATE): 38, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.INANIMATE): 89, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.INANIMATE): 41, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE): 0, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE): 93, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.MASCULINE, ANIMALITY.ANIMATE): 30, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE): 128, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE): 12, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.NEUTER, ANIMALITY.INANIMATE): 75, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE): 120, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE): 119, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE): 7, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE): 168, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE): 17, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE): 152, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE): 169, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.FEMININE, ANIMALITY.ANIMATE): 10, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.GENITIVE, None, ANIMALITY.INANIMATE): 123, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE): 180, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE): 141, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE): 115, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.GENITIVE, None, ANIMALITY.ANIMATE): 122, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE): 162, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.INANIMATE): 183, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE): 23, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE): 85, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.MASCULINE, ANIMALITY.INANIMATE): 25, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.INANIMATE): 161, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE): 175, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE): 190, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE): 67, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.NEUTER, ANIMALITY.INANIMATE): 15, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.GENITIVE, None, ANIMALITY.INANIMATE): 171, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE): 140, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.ANIMATE): 40, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE): 188, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.MASCULINE, ANIMALITY.ANIMATE): 54, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.DATIVE, None, ANIMALITY.INANIMATE): 101, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.NEUTER, ANIMALITY.ANIMATE): 74, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.FEMININE, ANIMALITY.INANIMATE): 59, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE): 151, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE): 1, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.ANIMATE): 112, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE): 150, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE): 52, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE): 166, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE): 108, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.DATIVE, None, ANIMALITY.INANIMATE): 173, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.FEMININE, ANIMALITY.INANIMATE): 53, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.INSTRUMENTAL, None, ANIMALITY.ANIMATE): 164, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.NEUTER, ANIMALITY.INANIMATE): 33, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.NEUTER, ANIMALITY.ANIMATE): 80, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE): 118, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE): 36, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.INANIMATE): 111, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.FEMININE, ANIMALITY.INANIMATE): 83, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE): 97, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE): 181, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.NEUTER, ANIMALITY.INANIMATE): 81, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE): 103, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.MASCULINE, ANIMALITY.ANIMATE): 78, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE): 84, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE): 95, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.INANIMATE): 159, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE): 2, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE): 191, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE): 163, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE): 154, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE): 14, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE): 46, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.FEMININE, ANIMALITY.INANIMATE): 77, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE): 109, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.NEUTER, ANIMALITY.INANIMATE): 9, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE): 187, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE): 91, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.MASCULINE, ANIMALITY.ANIMATE): 24, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE): 156, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE): 102, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.NEUTER, ANIMALITY.ANIMATE): 8, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE): 105, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, None, ANIMALITY.ANIMATE): 144, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE): 61, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.FEMININE, ANIMALITY.ANIMATE): 34, (TIME.PAST, VOICE.PASSIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.ANIMATE): 88, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE): 16, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.FEMININE, ANIMALITY.ANIMATE): 64, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE): 178, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, GENDER.FEMININE, ANIMALITY.ANIMATE): 82, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE): 130, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.MASCULINE, ANIMALITY.INANIMATE): 13, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.ANIMATE): 42, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.PREPOSITIONAL, None, ANIMALITY.INANIMATE): 143, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.NOMINATIVE, None, ANIMALITY.INANIMATE): 133, (TIME.FUTURE, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, None, ANIMALITY.INANIMATE): 177, (TIME.PAST, VOICE.ACTIVE, NUMBER.PLURAL, CASE.ACCUSATIVE, None, ANIMALITY.INANIMATE): 43, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.NEUTER, ANIMALITY.ANIMATE): 56, (TIME.PRESENT, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.PREPOSITIONAL, None, ANIMALITY.ANIMATE): 106, (TIME.PRESENT, VOICE.PASSIVE, NUMBER.PLURAL, CASE.GENITIVE, None, ANIMALITY.ANIMATE): 134, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.MASCULINE, ANIMALITY.ANIMATE): 72, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.GENITIVE, GENDER.NEUTER, ANIMALITY.INANIMATE): 57, (TIME.PAST, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.INSTRUMENTAL, GENDER.FEMININE, ANIMALITY.INANIMATE): 29, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.SINGULAR, CASE.DATIVE, None, ANIMALITY.ANIMATE): 148, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.DATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE): 62, (TIME.FUTURE, VOICE.ACTIVE, NUMBER.PLURAL, CASE.DATIVE, None, ANIMALITY.ANIMATE): 160, (TIME.PAST, VOICE.PASSIVE, NUMBER.SINGULAR, CASE.NOMINATIVE, GENDER.NEUTER, ANIMALITY.ANIMATE): 50}
