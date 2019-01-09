import unittest

from python_i18n.tests.translation_tests import TestTranslationFormat

from python_i18n.tests.loader_tests import TestFileLoader
from python_i18n.tests.i18n_tests import TestI18nLoader


def suite():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(TestFileLoader))
    suite.addTest(unittest.makeSuite(TestTranslationFormat))
    suite.addTest(unittest.makeSuite(TestI18nLoader))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    runner.run(test_suite)
