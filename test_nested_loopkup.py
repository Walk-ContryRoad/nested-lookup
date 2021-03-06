from unittest import TestCase

from nested_lookup import nested_lookup

class TestNestedLookup(TestCase):

    def setUp(self):
        self.subject_dict = {'a':1,'b':{'d':100},'c':{'d':200}}

    def test_nested_lookup(self):
        results = nested_lookup('d', self.subject_dict)
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100,200}, set(results))

    def test_nested_lookup_wrapped_in_list(self):
        results = nested_lookup('d', [{}, self.subject_dict, {}])
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100,200}, set(results))

    def test_nested_lookup_wrapped_in_list_in_dict_in_list(self):
        results = nested_lookup('d', [{}, {'H' : [self.subject_dict]} ])
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100,200}, set(results))

    def test_nested_lookup_wrapped_in_list_in_list(self):
        results = nested_lookup('d', [ {}, [self.subject_dict, {}] ])
        self.assertEqual(2, len(results))
        self.assertIn(100, results)
        self.assertIn(200, results)
        self.assertSetEqual({100,200}, set(results))


