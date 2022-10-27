from multiprocessing.sharedctypes import Value
import TLux_package
import unittest



class TestKayaFunction(unittest.TestCase):
    def test_kaya_function_calc_germany(self):
        actual = TLux_package.kaya_fct(82.4, 44, 5, 0.05, 'CO2')
        expected = 906.4
        self.assertEqual(actual, expected)

    def test_kaya_function_exception1(self):
        with self.assertRaises(ValueError) as exception_context:
            TLux_package.kaya_fct(pop = -82.4, gdp = 30, enInt = 5, carbInt =  0.1, output_type='CO2')
        self.assertEqual(
            str(exception_context.exception),
            'Only positive values are allowed!'
        )
    
    def test_kaya_function_exception2(self):
        with self.assertRaises(ValueError) as exception_context:
            TLux_package.kaya_fct(pop = 82.4, gdp = 30, enInt = 5, carbInt =  0.1, output_type='D')
        self.assertEqual(
            str(exception_context.exception),
            'Please provide valid output_type, either "CO2" or "C"!'
        )