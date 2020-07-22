# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03SigninUserAPITestCase::test_case status'] = 200

snapshots['TestCase03SigninUserAPITestCase::test_case body'] = {
    'access_token': 'user access token',
    'is_admin': True,
    'is_domain_expert': False
}

snapshots['TestCase03SigninUserAPITestCase::test_case header_params'] = {
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
        '82'
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

snapshots['TestCase03SigninUserAPITestCase::test_case token response'] = {
    'access_token': 'user access token',
    'is_admin': True,
    'is_domain_expert': False
}
