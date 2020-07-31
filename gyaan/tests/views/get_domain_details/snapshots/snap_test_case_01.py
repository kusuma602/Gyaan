# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDomainDetailsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetDomainDetailsAPITestCase.test_case body'] = {
    'domain_details': {
        'description': 'string',
        'domain_experts': [
            {
                'name': 'string',
                'user_id': 1
            }
        ],
        'domain_members_count': 1,
        'domain_name': 'string',
        'domain_posts_count': 1
    }
}
