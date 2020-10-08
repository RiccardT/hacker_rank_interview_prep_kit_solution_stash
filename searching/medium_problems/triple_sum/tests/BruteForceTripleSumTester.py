from unittest import TestCase, main
import os

from searching.medium_problems.triple_sum.triple_sum_brute_force import triple_sum_brute_force


current_path = os.path.dirname(__file__)
test_resources_path = current_path + "/test_resources/"


class BruteForceTripleSumTester(TestCase):

    functionality_test_data: dict = {
        "test_0": {
            "a": [1, 3, 5],
            "b": [2, 3],
            "c": [1, 2, 3],
            "expected": 8
        },
        "test_1": {
            "a": [1, 4, 5],
            "b": [2, 3, 3],
            "c": [1, 2, 3],
            "expected": 5
        },
        "test_2": {
            "a": [1, 3, 5, 7],
            "b": [5, 7, 9],
            "c": [7, 9, 11, 13],
            "expected": 12
        },
        "test_3": {
            "a": [3, 5, 7],
            "b": [3, 6],
            "c": [4, 6, 9],
            "expected": 4
        },
    }

    def test_functionality_0(self):
        test_data = self.get_functionality_test_data("test_0")
        a: list = test_data["a"]
        b: list = test_data["b"]
        c: list = test_data["c"]

        expected: int = test_data["expected"]
        actual: int = triple_sum_brute_force(a, b, c)
        self.assertEqual(expected, actual)

    def test_functionality_1(self):
        test_data = self.get_functionality_test_data("test_1")
        a: list = test_data["a"]
        b: list = test_data["b"]
        c: list = test_data["c"]

        expected: int = test_data["expected"]
        actual: int = triple_sum_brute_force(a, b, c)
        self.assertEqual(expected, actual)

    def test_functionality_2(self):
        test_data = self.get_functionality_test_data("test_2")
        a: list = test_data["a"]
        b: list = test_data["b"]
        c: list = test_data["c"]

        expected: int = test_data["expected"]
        actual: int = triple_sum_brute_force(a, b, c)
        self.assertEqual(expected, actual)

    def test_functionality_3(self):
        test_data = self.get_functionality_test_data("test_3")
        a: list = test_data["a"]
        b: list = test_data["b"]
        c: list = test_data["c"]

        expected: int = test_data["expected"]
        actual: int = triple_sum_brute_force(a, b, c)
        self.assertEqual(expected, actual)

    def get_functionality_test_data(self, test_name: str) -> dict:
        functionality_test_data: dict = self.functionality_test_data[test_name]
        return functionality_test_data


if __name__ == "__main__":
    main()

