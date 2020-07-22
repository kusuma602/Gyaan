from gyaan_auth.presenters.presenter_implementation import \
        LoginPresenterImplementation


def test_raise_invalid_password_exception_returns_http_response():
    import json
    from gyaan_auth.constants.exception_messages import INVALID_PASSWORD

    # Arrange
    presenter = LoginPresenterImplementation()
    status_code = 400

    # Act
    response = presenter.raise_invalid_password_exception()

    # Assert
    response_content = json.loads(response.content)
    assert response_content['response'] == INVALID_PASSWORD[0]
    assert response_content['res_status'] == INVALID_PASSWORD[1]
    assert response_content['http_status_code'] == status_code
