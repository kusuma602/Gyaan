from gyaan_auth.presenters.presenter_implementation import \
    GetUserDtoPresenterImplementation
from gyaan_auth.exceptions import InvalidUserIds


def test_raise_invalid_user_id_exception_returns_http_response():
    import json

    # Arrange
    presenter = GetUserDtoPresenterImplementation()
    invalid_user_ids = [1, 2, 3]
    err_obj = InvalidUserIds(invalid_user_ids)
    expected_response = {
        'http_status_code': 400,
        'res_status': 'INVALID_PASSWORD',
        'response':
            'Invalid Password, try with Valid Password Invalid user ids: [1, 2, 3]'
    }

    # Act
    response = presenter.raise_invalid_user_ids_exception(err_obj)

    # Assert
    response_content = json.loads(response.content)
    assert response_content == expected_response
