


RESPONSE_200_JSON = """
[
    {
        "post_id": 1,
        "tittle": "string",
        "description": "string",
        "posted_at": "2099-12-31 00:00:00",
        "posted_by": {
            "user_id": 1,
            "name": "string"
        },
        "comments_count": 1,
        "reactions_count": 1,
        "reacted_by": [
            {
                "user_id": 1,
                "name": "string"
            }
        ],
        "domain_id": 1,
        "domain_name": "string",
        "tags": [
            {
                "tag_id": 1,
                "tag_name": "string"
            }
        ],
        "comments": [
            {
                "comment_id": 1,
                "comment_content": "string",
                "commented_at": "2099-12-31 00:00:00",
                "reactions_count": 1,
                "commented_by": {
                    "user_id": 1,
                    "name": "string"
                }
            }
        ],
        "answer": {
            "comment_id": 1,
            "comment_content": "string",
            "commented_at": "2099-12-31 00:00:00",
            "reactions_count": 1,
            "commented_by": {
                "user_id": 1,
                "name": "string"
            },
            "approved_by": {
                "user_id": 1,
                "name": "string"
            }
        }
    }
]
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_DOMAIN_ID"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_OFFSET"
}
"""

