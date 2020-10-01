from jobs import Job
from data import Data
from job_statistics import Stats
import unittest


class test_job_functions(unittest.TestCase):
    
    def test_job_seeker(self):
        result_1 = Job("random_input")
        answer_1 = result_1.job_seeker()
        result_2 = Job("testing123")
        answer_2 = result_2.job_seeker()
        
        self.assertIsInstance(answer_1, float)
        self.assertIsInstance(answer_2, float)
    
    
    def net_change(self):
        result_3 = Stats("Python")
        answer_3 = result_3.net_change()
        
        self.assertIsInstance(answer_3, str)
        