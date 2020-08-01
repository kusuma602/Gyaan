# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_raise_invalid_user_id_exception_returns_http_response Invalid post ids response'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_POST_IDS',
    'response': 'Invalid Post ID, try with valid post ids Invalid user ids: [1, 2, 3]'
}
