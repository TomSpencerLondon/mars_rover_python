import unittest
from dataclasses import dataclass


@dataclass(frozen=True)
class Rover(object):
    facing: str

    def go(self, instruction):
        return "hello"


class MarsRoverTest(unittest.TestCase):
    def test_turn_right_N_to_E(self):
        rover = Rover('N')
        rover.go('R')
        self.assertEqual('E', rover.facing)



if __name__ == '__main__':
    unittest.main()
