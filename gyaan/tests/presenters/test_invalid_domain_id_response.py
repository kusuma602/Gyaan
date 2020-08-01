from gyaan.presenters.presenter_implementation import GetDomainDetailsPresenterImplementation


def test_raise_invalid_user_id_exception_returns_http_response():
    import json

    # Arrange
    from gyaan.constants.exception_messages import INVALID_DOMAIN_ID
    expected_response = INVALID_DOMAIN_ID[0]
    expected_res_status = INVALID_DOMAIN_ID[1]
    status_code = 400
    presenter = GetDomainDetailsPresenterImplementation()

    # Act
    response = presenter.get_invalid_domain_id_response()

    # Assert
    response_content = json.loads(response.content)
    assert response_content['res_status'] == expected_res_status
    assert response_content['response'] == expected_response
    assert response_content['http_status_code'] == status_code
