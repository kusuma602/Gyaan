# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDomainPostsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetDomainPostsAPITestCase.test_case body'] = [
    {
        'answer': {
            'approved_by': {
                'name': 'string',
                'user_id': 1
            },
            'comment_content': 'string',
            'comment_id': 1,
            'commented_at': '2099-12-31 00:00:00',
            'commented_by': {
                'name': 'string',
                'user_id': 1
            },
            'reactions_count': 1
        },
        'comments': [
            {
                'comment_content': 'string',
                'comment_id': 1,
                'commented_at': '2099-12-31 00:00:00',
                'commented_by': {
                    'name': 'string',
                    'user_id': 1
                },
                'reactions_count': 1
            }
        ],
        'comments_count': 1,
        'description': 'string',
        'domain_id': 1,
        'domain_name': 'string',
        'post_id': 1,
        'posted_at': '2099-12-31 00:00:00',
        'posted_by': {
            'name': 'string',
            'user_id': 1
        },
        'reacted_by': [
            {
                'name': 'string',
                'user_id': 1
            }
        ],
        'reactions_count': 1,
        'tags': [
            {
                'tag_id': 1,
                'tag_name': 'string'
            }
        ],
        'tittle': 'string'
    }
]
