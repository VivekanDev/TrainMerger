import unittest
from train_functions import get_max_distance, train_a_hyb_arrival, train_b_hyb_arrival, trains_merger


class TestTrainMerger(unittest.TestCase):
    
    def test_3_get_max_distance(self):
        result = get_max_distance("NDL")
        self.assertEqual(result, 700)
        result1 = get_max_distance("NJP")
        self.assertEqual(result1, 3000)
        result2 = get_max_distance("BPL")
        self.assertEqual(result2, 0)
        
    def test_1_train_a_hyb_arrival(self):
        result = train_a_hyb_arrival(['NDL', 'NDL', 'KRN', 'GHY', 'SLM', 'NJP', 'NGP', 'BLR'])
        self.assertEqual(result, ['NDL', 'NDL', 'GHY', 'NJP', 'NGP'])
        result1 = train_a_hyb_arrival(['SLM', 'BLR', 'KRN', 'HYB', 'SLM', 'NGP', 'ITJ'])
        self.assertEqual(result1, ['HYB', 'NGP', 'ITJ'])
        result2 = train_a_hyb_arrival(['SLM', 'BLR', 'KRN', 'HYB', 'SLM'])
        self.assertEqual(result2, ['HYB'])
    
    def test_2_train_b_hyb_arrival(self):
        result = train_b_hyb_arrival(['NJP', 'GHY', 'AGA', 'PNE', 'MAO', 'BPL', 'PTA'])
        self.assertEqual(result, ['NJP', 'GHY', 'AGA', 'BPL', 'PTA'])
        result1 = train_b_hyb_arrival(['SRR', 'MAO', 'NJP', 'PNE', 'PTA'])
        self.assertEqual(result1, ['NJP', 'PTA'])
        result2 = train_b_hyb_arrival(['TVC', 'SRR', 'MAQ', 'MAO', 'HYB'])
        self.assertEqual(result2, ['HYB'])
       
    def test_4_trains_merger(self):
        result = trains_merger(['NDL', 'NDL', 'GHY', 'NJP', 'NGP', 'NJP', 'GHY', 'AGA', 'BPL', 'PTA'])
        self.assertEqual(result, ['GHY', 'GHY', 'NJP', 'NJP', 'PTA', 'NDL', 'NDL', 'AGA', 'BPL', 'NGP'])
        result1 = trains_merger(['NGP', 'ITJ', 'NJP', 'PTA'])
        self.assertEqual(result1, ['NJP', 'PTA', 'ITJ', 'NGP'])
        result2 = trains_merger([])
        self.assertEqual(result2, [])
