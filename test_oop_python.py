from oop_python import *
import unittest


class TestoopPython(unittest.TestCase):
    def test_case1(self):
        name = 'Dhoni'
        team = 'CSK'
        p1 = player(name,team)
        self.assertTrue(p1.getPlayerName()=='Dhoni')

    def test_case2(self):
        name = 'Dhoni'
        team = 'CSK'
        p1 = player(name,team)
        self.assertTrue(p1.getTeam()=='CSK')


if __name__ == '__main__':
    unittest.main()