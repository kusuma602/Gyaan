from gyaan_auth.presenters.presenter_implementation import \
        LoginPresenterImplementation


def test_raise_invalid_username_exception_returns_http_response():
    import json
    from gyaan_auth.constants.exception_messages import INVALID_USERNAME

    # Arrange
    presenter = LoginPresenterImplementation()
    status_code = 404

    # Act
    response = presenter.raise_invalid_username_exception()

    # Assert
    response_content = json.loads(response.content)
    assert response_content['response'] == INVALID_USERNAME[0]
    assert response_content['res_status'] == INVALID_USERNAME[1]
    assert response_content['http_status_code'] == status_code
