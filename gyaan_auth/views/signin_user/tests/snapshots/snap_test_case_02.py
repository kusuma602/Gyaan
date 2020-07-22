# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02SigninUserAPITestCase::test_case status'] = 400

snapshots['TestCase02SigninUserAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_PASSWORD',
    'response': 'Invalid Password, try with Valid Password'
}

snapshots['TestCase02SigninUserAPITestCase::test_case header_params'] = {
    'allow': (
        'Allow',
        'POST, OPTIONS'
    ),
    'content-language': (
        'Content-Language',
        'en'
    ),
    'content-length': (
        'Content-Length',
        '116'
    ),
    'content-type': (
        'Content-Type',
        'text/html; charset=utf-8'
    ),
    'vary': (
        'Vary',
        'Accept-Language, Origin, Cookie'
    ),
    'x-frame-options': (
        'X-Frame-Options',
        'SAMEORIGIN'
    )
}

snapshots['TestCase02SigninUserAPITestCase::test_case exception message'] = 'INVALID_PASSWORD'
