import unittest

from mars_rover import Rover


class MarsRoverTest(unittest.TestCase):
    def test_turn_right_N_to_E(self):
        rover = Rover('N')
        rover = rover.go('R')
        self.assertEqual('E', rover.facing)

    def test_turn_right_E_to_S(self):
        rover = Rover('E')
        rover = rover.go('R')
        self.assertEqual('S', rover.facing)

    def test_turn_right_S_to_W(self):
        rover = Rover('S')
        rover = rover.go('R')
        self.assertEqual('W', rover.facing)


if __name__ == '__main__':
    unittest.main()
