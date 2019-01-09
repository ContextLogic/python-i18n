# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import os
import os.path
import functools

from python_i18n import resource_loader, load_i18n, t
from python_i18n.resource_loader import I18nFileLoadError
from python_i18n import config
from python_i18n.config import json_available, yaml_available
from python_i18n import translations


RESOURCE_FOLDER = os.path.join(os.path.dirname(__file__), "resources")


class TestI18nLoader(unittest.TestCase):
    def setUp(self):
        self.namespace1 = "namespace.space1"
        self.namespace2 = "namespace.space2"
        self.d1 = {
            "en": {
                "test": "space1 en test"
            },
            "zh": {
                "test": "space2 zh test"
            }
        }
        self.d2 = {
            "en": {
                "test": "space2 en test"
            },
            "zh": {
                "test": "space2 zh test"
            }
        }
        load_i18n(self.d1, self.namespace1)
        load_i18n(self.d2, self.namespace2)

    def test_namespace1(self):
        t_n = functools.partial(t, _namespace=self.namespace1)
        self.assertTrue(t_n('test', locale='en') == self.d1['en']['test'])
        self.assertTrue(t_n('test', locale='zh') == self.d1['zh']['test'])
        self.assertTrue(t_n('test', locale='unknown') == 'test')
        self.assertTrue(t_n('test_unknown', locale='unknown')
                        == 'test_unknown')

    def test_namespace2(self):
        self.assertTrue(t('test', _namespace=self.namespace2, locale='en')
                        == self.d2['en']['test'])
        self.assertTrue(t('test', _namespace=self.namespace2, locale='zh')
                        == self.d2['zh']['test'])
        self.assertTrue(t('test', _namespace=self.namespace2, locale='unknown')
                        == 'test')
        self.assertTrue(t('test_unknown', _namespace=self.namespace2, locale='unknown')
                        == 'test_unknown')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestI18nLoader)
    unittest.TextTestRunner(verbosity=2).run(suite)
