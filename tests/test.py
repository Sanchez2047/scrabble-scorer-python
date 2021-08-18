import unittest, re, types

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from scrabble_scorer import *

class TestScrabbleScorer(unittest.TestCase):

	## transform tests ##

	def test_transform_returns_an_object(self):
		transformed_obj = transform(OLD_POINT_STRUCTURE)
		self.assertIs(type(transformed_obj), dict)

	def test_transform_returns_a_dict_that_is_not_empty(self):
		transformed_obj = transform(OLD_POINT_STRUCTURE)
		self.assertNotEqual(transformed_obj.keys(), {}.keys())
		self.assertNotEqual(len(transformed_obj.keys()), 0)

	# is there a better way to write this one?
	def test_transform_returns_a_dict_with_letter_keys(self):
		transformed_obj = transform(OLD_POINT_STRUCTURE)
		letter_keys = list(transformed_obj.keys())
		letters_ex = re.findall('[a-z]', str(letter_keys))
		self.assertEqual(len(letters_ex), len(letter_keys))

	def test_transform_returns_a_dict_with_integer_values(self):
		transformed_obj = transform(OLD_POINT_STRUCTURE)
		int_vals = transformed_obj.values()
		for val in int_vals:
			self.assertEqual(type(val), int)

	## new_point_structure tests ##

	def test_new_point_structure_contains_correct_key_value_pairs(self):
		sample = {
			"a": 1,
			"e": 1,
			"i": 1,
			"o": 1,
			"u": 1,
			"l": 1,
			"n": 1,
			"r": 1,
			"s": 1,
			"t": 1,
			"d": 2,
			"g": 2,
			"b": 3,
			"c": 3,
			"m": 3,
			"p": 3,
			"f": 4,
			"h": 4,
			"v": 4,
			"w": 4,
			"y": 4,
			"k": 5,
			"j": 8,
			"x": 8,
			"q": 10,
			"z": 10
		}
		self.assertTrue(sample == new_point_structure)

	## simple_scorer tests ##

	def test_simple_scorer_function_exists(self):
		self.assertEqual(type(simple_scorer), types.FunctionType)

	def test_simple_scorer_returns_an_integer_score(self):
		self.assertEqual(type(simple_scorer('foo')), int)

	def test_simple_scorer_returns_a_score_equal_to_the_length_of_its_input(self):
		self.assertEqual(simple_scorer('foo'), 3)
		self.assertEqual(simple_scorer(''), 0)

	## vowel_bonus_scorer tests ##

	def test_vowel_bonus_scorer_function_exists(self):
		self.assertEqual(type(vowel_bonus_scorer), types.FunctionType)

	def test_vowel_bonus_scorer_returns_an_integer_score(self):
		self.assertEqual(type(vowel_bonus_scorer('foo')), int)

	def test_vowel_bonus_scorer_returns_three_points_per_vowel(self):
		self.assertEqual(vowel_bonus_scorer('a'), 3)
		self.assertEqual(vowel_bonus_scorer('e'), 3)
		self.assertEqual(vowel_bonus_scorer('i'), 3)
		self.assertEqual(vowel_bonus_scorer('o'), 3)
		self.assertEqual(vowel_bonus_scorer('u'), 3)

		self.assertEqual(vowel_bonus_scorer('ae'), 6)
		self.assertEqual(vowel_bonus_scorer('aei'), 9)

	def test_vowel_bonus_scorer_returns_one_point_per_consonant(self):
		self.assertEqual(vowel_bonus_scorer('foo'), 7)
		self.assertEqual(vowel_bonus_scorer('bar'), 5)

	## scrabble_scorer tests ##

	def test_scrabble_scorer_function_exists(self):
		self.assertEqual(type(scrabble_scorer), types.FunctionType)

	def test_scrabble_scorer_returns_an_integer_score(self):
		self.assertEqual(type(scrabble_scorer('foo')), int)

	def test_scrabble_scorer_uses_new_point_structure_to_score_a_word(self):
		self.assertEqual(scrabble_scorer('foo'), 6)
		self.assertEqual(scrabble_scorer('bar'), 5)
		self.assertEqual(scrabble_scorer('baz'), 14)

	## scoring_algorithms tests ##

	def test_scoring_algorithms_is_a_tuple_of_three_scoring_objects(self):
		self.assertEqual(type(scoring_algorithms), tuple)
		self.assertEqual(len(scoring_algorithms), 3)

	def test_scoring_algorithms_contain_three_scoring_objects(self):
		self.assertTrue(scoring_algorithms[0]['scoring_function'] == simple_scorer)
		self.assertTrue(scoring_algorithms[1]['scoring_function'] == vowel_bonus_scorer)
		self.assertTrue(scoring_algorithms[2]['scoring_function'] == scrabble_scorer)

if __name__ == '__main__':
	unittest.main()