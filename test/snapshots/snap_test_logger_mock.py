# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestClass::test_logger 1'] = '''hi
there'''

snapshots['TestClass::test_logger_with_decorator 1'] = '''hi
there'''
