import unittest
import __init__
from artool.analysis.predictor import Predictor
from artool.error.custom import PredictorError


class TestPredictorModule(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def setUp(self):
        self.fj_predictor = Predictor("salary", "JDU-SS")

    def test_valid_validate_type(self):
        """_summary_
        """
        for val in ["salary","kpi","retrenchment","on-bench","promotion"]:
            with self.subTest(val=val):
                self.fj_predictor.set_type(val)
                self.assertEqual(self.fj_predictor.type, val)

    def test_invalid_validate_type(self):
        """_summary_
        """
        with self.assertRaises(PredictorError) as pe:
            self.fj_predictor.set_type("local-manager")
        the_exception = pe.exception
        self.assertEqual(the_exception.message, "Invalid Predictor type local-manager")

    def tearDown(self):
        del self.fj_predictor


if __name__ == '__main__':
    unittest.main()
