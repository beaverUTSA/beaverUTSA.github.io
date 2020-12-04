import unittest
import ddiQuestion2

class TestPortExclusions(unittest.TestCase):
    
    def test_single_ranges(self):
        self.assertEqual(ddiQuestion2.apply_port_exclusions([[8000, 9000]],[[8080, 8080]]),[[8000, 8079], [8081, 9000]])
    
    def test_unordered1_example(self):
        self.assertEqual(ddiQuestion2.apply_port_exclusions([[80, 80], [22, 23], [8000, 9000]],[[1024, 1024], [8080, 8080]]),[[22, 23], [80, 80], [8000, 8079], [8081, 9000]])
    
    def test_unordered2_example(self):
        self.assertEqual(ddiQuestion2.apply_port_exclusions([[8000, 9000], [80, 80], [22, 23]],[[1024, 1024], [8080, 8080]]),[[22, 23], [80, 80], [8000, 8079], [8081, 9000]])    

    def test_nested_exclusions_example(self):
        self.assertEqual(ddiQuestion2.apply_port_exclusions([[1,65535]],[[1000,2000], [500, 2500]]),[[1, 499], [2501, 65535]])    

    def test_unjoined_inclusions_example(self):
        self.assertEqual(ddiQuestion2.apply_port_exclusions([[1,1], [3, 65535], [2, 2]],[[1000, 2000], [500, 2500]]),[[1, 499], [2501, 65535]])
    
    def test_empty_inclusions_example(self):
        self.assertEqual(ddiQuestion2.apply_port_exclusions([],[[8080, 8080]]), [])
    
if __name__ == '__main__':
    unittest.main()