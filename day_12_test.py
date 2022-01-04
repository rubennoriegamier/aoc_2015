import json
from unittest import TestCase, main

from day_12 import part_1, part_2


class TestDay12(TestCase):
    def test_part_1(self):
        for json_, sum_ in [('[1,2,3]', 6), ('{"a":2,"b":4}', 6), ('[[[3]]]', 3), ('{"a":{"b":4},"c":-1}', 3),
                            ('{"a":[-1,1]}', 0), ('[-1,{"a":1}]', 0), ('[]', 0), ('{}', 0)]:
            with self.subTest(json=json_):
                self.assertEqual(part_1(json.loads(json_)), sum_)

    def test_part_2(self):
        for json_, sum_ in [('[1,2,3]', 6), ('[1,{"c":"red","b":2},3]', 4), ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
                            ('[1,"red",5]', 6)]:
            with self.subTest(json=json_):
                self.assertEqual(part_2(json.loads(json_)), sum_)


if __name__ == '__main__':
    main()
