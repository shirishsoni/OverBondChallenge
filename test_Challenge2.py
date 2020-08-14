from unittest import TestCase

from Challenge2 import interpolateYield


class Test(TestCase):
    def test_print_output(self):
        result = interpolateYield(gYield1=4.8, gYield2=5.5, gTerm1=12.0, gTerm2=16.3, cTerm=15.2)
        self.assertEqual(5.32, result)
