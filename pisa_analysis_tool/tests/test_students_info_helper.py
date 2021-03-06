import unittest
import pandas as pd
import os
from pisa_analysis_tool.students_info_helper import sav_to_dataframe
from pisa_analysis_tool.students_info_helper import student2nation
from pisa_analysis_tool.students_info_helper import student2school
from pisa_analysis_tool.students_info_helper import school2nation
from pisa_analysis_tool.students_info_helper import info

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class UnitTests(unittest.TestCase):

    def test_sav_to_dataframe(self):
        """Test for file not existing"""
        with self.assertRaises(FileNotFoundError):
            sav_to_dataframe('123.sav')
        """Test for file with a wrong type"""
        with self.assertRaises(FileNotFoundError):
            sav_to_dataframe('sample.csv')
        """Test for a valid file"""
        # TODO: fix
        # file = os.path.join(THIS_DIR, os.pardir, 'data/sample.sav')
        # df = sav_to_dataframe(file)
        # self.assertTrue(len(df) == 3)

    def test_student2school(self):
        """Test for invalid student id"""
        df = pd.read_csv(os.path.join(THIS_DIR, os.pardir, 'data/sample.csv'))
        with self.assertRaises(KeyError):
            student2school(df, 0)
        with self.assertRaises(KeyError):
            student2school(df, 99999999)
        """Test for valid student id"""
        # TODO: fix
        # nID = student2school(df, 800001)
        # self.assertTrue(nID == 80000)

    def test_school2nation(self):
        """Test for id less than 97100000"""
        nID1 = school2nation(3600227)
        self.assertTrue(nID1 == 360000)
        nID2 = school2nation(7610535)
        self.assertTrue(nID2 == 760000)
        """Test for id greater than 97100000 and less than 97200000"""
        nID3 = school2nation(97100500)
        self.assertTrue(nID3 == 7240000)
        """Test for id greater than 97200000 and less than 97400000"""
        nID4 = school2nation(97311281)
        self.assertTrue(nID4 == 8400000)
        """Test for id greater than 97400000"""
        nID5 = school2nation(97400091)
        self.assertTrue(nID5 == 320100)

    def test_student2nation(self):
        """Test for id less than 97100000"""
        nID1 = student2nation(3600227)
        self.assertTrue(nID1 == 360000)
        nID2 = student2nation(7610535)
        self.assertTrue(nID2 == 760000)
        """Test for id greater than 97100000 and less than 97200000"""
        nID3 = student2nation(97100500)
        self.assertTrue(nID3 == 7240000)
        """Test for id greater than 97200000 and less than 97400000"""
        nID4 = student2nation(97311281)
        self.assertTrue(nID4 == 8400000)
        """Test for id greater than 97400000"""
        nID5 = student2nation(97400091)
        self.assertTrue(nID5 == 320100)

    def test_info(self):
        df = pd.read_csv(os.path.join(THIS_DIR, os.pardir, 'data/nations.csv'))
        """Test for invalid nation id"""
        with self.assertRaises(IndexError):
            info(df, 0)
        """Test for valid nation id"""
        res = info(df, 360000)
        self.assertEqual(('Australia', 'AUS', 'AP'), res)


if __name__ == '__main__':
    unittest.main()
