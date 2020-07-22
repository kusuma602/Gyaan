

REQUEST_BODY_JSON = """
{
    "username": "string",
    "password": "string"
}
"""


RESPONSE_200_JSON = """
{
    "access_token": "string",
    "is_admin": true,
    "is_domain_expert": true
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_USERNAME"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_PASSWORD"
}
"""

