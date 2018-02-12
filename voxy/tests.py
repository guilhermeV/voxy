import unittest
import counter

class TestCounterMethods(unittest.TestCase):

    def test_base(self):
        text = 'one two three'
        result = counter.count(text)
        self.assertEqual(result, {'quantity':3,'distinct':3})
        
    def test_distinct(self):
        text = 'one two three two'
        result = counter.count(text)
        self.assertEqual(result, {'quantity':4,'distinct':3})
        
    #numbers will be counted as words
    def test_number(self):
        text = '1 2 3'
        result = counter.count(text)
        self.assertEqual(result, {'quantity':3,'distinct':3})
        
    
if __name__ == '__main__':
    unittest.main()