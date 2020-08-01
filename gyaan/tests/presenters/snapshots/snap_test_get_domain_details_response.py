# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetDomainDetialsResponse.test_with_domain_dto_returns_http_response domain details response'] = {
    'description': 'domain_1 description',
    'domain_book_marks_count': 4,
    'domain_experts': [
        {
            'is_admin': False,
            'is_domain_expert': False,
            'name': 'user_1',
            'user_id': 1
        },
        {
            'is_admin': False,
            'is_domain_expert': False,
            'name': 'user_2',
            'user_id': 2
        }
    ],
    'domain_members_count': 3,
    'domain_name': 'domain_1',
    'domain_posts_count': 2
}
