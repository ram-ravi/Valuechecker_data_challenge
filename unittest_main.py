from main import process
from main import binary_search
from main import converter
from main import hash_process
from main import hash_converter
from main import hash_search

import unittest


class TestMain(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([], 3), -1)
        self.assertEqual(binary_search([1, 2], 3), -1)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4], 4), 3)

    def test_converter(self):
        self.assertEqual(converter({1: 23}, 1463), 23)
        self.assertEqual(converter({1: 87, 34: 42}, 59849), None)
        self.assertEqual(converter({5673: 27, 3323: 43, 567: 98}, 567378), 27)
        self.assertEqual(converter({134365: 232, 3522: 42}, 13436575), 232)
        self.assertEqual(converter({1: 2, 3: 4}, 438469), None)

    def test_process(self):
        self.assertEqual(process({'op A': {1: 23}, 'op B': {146: 78, 87: 124, 495: 59}}, 1463), ['op A'])
        self.assertEqual(process({'op C': {1: 87, 34: 42}}, 59849), 'NO OPERATOR FOUND FOR THIS NUMBER: 59849')
        self.assertEqual(process({'op D': {5673: 27, 3323: 43, 567: 98}}, 567378), ['op D'])
        self.assertEqual(process({'op E': {134365: 232, 3522: 42}}, 13436575), ['op E'])
        self.assertEqual(process({'op F': {1: 2, 3: 4, 438: 67},
                                  'op G': {12: 34, 438: 56, 4384: 67}}, 438469), ['op F', 'op G'])

    # def test_hash_search(self):
    #     self.assertEqual(hash_search({1: 23}, 1463), 23)
    #     self.assertEqual(hash_search({1: 87, 34: 42}, 59849), None)
    #     self.assertEqual(hash_search({5673: 27, 3323: 43, 567: 98}, 567378), 27)
    #     self.assertEqual(hash_search({134365: 232, 3522: 42}, 13436575), 232)
    #     self.assertEqual(hash_search({1: 2, 3: 4}, 438469), None)

    def test_hash_converter(self):
        self.assertEqual(hash_converter({1: 23}, 1463), 23)
        self.assertEqual(hash_converter({1: 87, 34: 42}, 59849), None)
        self.assertEqual(hash_converter({5673: 27, 3323: 43, 567: 98}, 567378), 27)
        self.assertEqual(hash_converter({134365: 232, 3522: 42}, 13436575), 232)
        self.assertEqual(hash_converter({1: 2, 3: 4}, 438469), None)

    def test_hash_process(self):
        self.assertEqual(hash_process({'op A': {1: 23}, 'op B': {146: 78, 87: 124, 495: 59}}, 1463), ['op A'])
        self.assertEqual(hash_process({'op C': {1: 87, 34: 42}}, 59849), 'NO OPERATOR FOUND FOR THIS NUMBER: 59849')
        self.assertEqual(hash_process({'op D': {5673: 27, 3323: 43, 567: 98}}, 567378), ['op D'])
        self.assertEqual(hash_process({'op E': {134365: 232, 3522: 42}}, 87364), 'NO OPERATOR FOUND FOR THIS NUMBER: '
                                                                                 '87364')
        self.assertEqual(hash_process({'op F': {1: 2, 3: 4, 438: 67},
                                       'op G': {12: 34, 438: 56, 4384: 67}}, 438469), ['op F', 'op G'])


if __name__ == '__main__':
    unittest.main()
