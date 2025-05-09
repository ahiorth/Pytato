#%%
import sys
import unittest

from FreshStart import replace_chars

class SolutionTest(unittest.TestCase):
    '''
    Unit tests to test solution class
    '''
    def test_replace_char(self):
        self.assertEqual(replace_chars('ÅÅ'), 'AAAA')
    

if __name__ == '__main__':
    """
    NB: needs argv=['first-arg-is-ignored'] othervise only runs from commandline
    """
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    #unittest.main()    
# %%
