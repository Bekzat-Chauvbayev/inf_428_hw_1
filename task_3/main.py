import math
import unittest

def convert_hour_to_cyclic(hour):
    radians = (hour % 24) * (2 * math.pi / 24)
    return math.sin(radians), math.cos(radians)

def cyclic_time_difference(hour1, hour2):
    sin1, cos1 = convert_hour_to_cyclic(hour1)
    sin2, cos2 = convert_hour_to_cyclic(hour2)
    return math.acos(sin1 * sin2 + cos1 * cos2) * (24 / (2 * math.pi))

class TestCyclicTimeConversion(unittest.TestCase):
    def test_same_time(self):
        self.assertAlmostEqual(cyclic_time_difference(5, 5), 0.0)

    def test_across_midnight(self):
        self.assertAlmostEqual(cyclic_time_difference(23, 1), 2.0, delta=0.01)

    def test_opposite_times(self):
        self.assertAlmostEqual(cyclic_time_difference(0, 12), 12.0, delta=0.01)

    def test_random_time_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(6, 18), 12.0, delta=0.01)

    def test_half_day_difference(self):
        self.assertAlmostEqual(cyclic_time_difference(3, 15), 12.0, delta=0.01)

if __name__ == '__main__':
    unittest.main()
