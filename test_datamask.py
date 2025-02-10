from distutils.command.config import config
import unittest
import datamask


class TestDataMask(unittest.TestCase):
    def test_isZipcode(self):
        result = datamask.isZipCode(config['General']['Zip'])
        self.assertEqual(result,True)
        
if __name__ == '__main__':
    unittest.main()
    