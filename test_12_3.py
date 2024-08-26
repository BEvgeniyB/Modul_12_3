#-*- coding: utf-8 -*-
from pprint import pprint

import runner_and_tournament as rt
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(condition=is_frozen, reason="Тесты в этом кейсе заморожены")
    def test_walk(self):
        runn = rt.Runner(name='Спортсмен № 1',speed=10)
        for i in range(10):
            runn.walk()
        self.assertEqual(runn.distance,100)

    @unittest.skipIf(condition=is_frozen, reason="Тесты в этом кейсе заморожены")
    def test_run(self):
        runn = rt.Runner(name='Спортсмен № 2',speed=8)
        for i in range(1, 11):
            runn.run()
        #self.assertEqual(runn.distance, 160)
        self.assertEqual(runn.distance, 160)

    @unittest.skipIf(condition=is_frozen, reason="Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = rt.Runner(name='Спортсмен № 1',speed=10)
        runner2 = rt.Runner(name='Спортсмен № 2',speed=8)
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance,runner2.distance)

class TournamentTest(unittest.TestCase):
    all_results = None
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rt.Runner(name="Усэйн", speed=10)
        self.runner2 = rt.Runner(name="Андрей", speed=9)
        self.runner3 = rt.Runner(name="Ник", speed=3)

    @unittest.skipIf(condition=is_frozen, reason="Тесты в этом кейсе заморожены")
    def test_running1(self):
        running1 = rt.Tournament(90,self.runner1, self.runner3)
        result = running1.start()
        self.all_results[1] = {}
        for k,v in result.items():
            self.all_results[1][k] = str(v)
        res = self.all_results[1]
        last_result =res [max(res)]
        self.assertTrue(last_result == self.runner3,msg=f'{last_result}  fnd {self.runner3}')

    @unittest.skipIf(condition=is_frozen, reason="Тесты в этом кейсе заморожены")
    def test_running2(self):
        running2 = rt.Tournament(90,self.runner2, self.runner3)
        result = running2.start()
        self.all_results[2] = {}
        for k,v in result.items():
            self.all_results[2][k] = str(v)
        res = self.all_results[2]
        last_result = res[max(res)]
        self.assertTrue(last_result == self.runner3,msg=f'{last_result}  fnd {self.runner3}')

    @unittest.skipIf(condition=is_frozen,reason="Тесты в этом кейсе заморожены")
    def test_running3(self):
        running3 = rt.Tournament(2, self.runner1, self.runner2, self.runner3)
        result = running3.start()
        self.all_results[3] = {}
        for k, v in result.items():
            self.all_results[3][k] = str(v)
        res = self.all_results[3]
        last_result = res[max(res)]
        self.assertTrue(last_result == self.runner3, msg=f'{last_result}  and {self.runner3}')

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            pprint(v)


if __name__ == '__main__':
    unittest.main()
