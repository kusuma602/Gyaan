from gyaan_auth.presenters.presenter_implementation import \
    LoginPresenterImplementation


def test_with_invalid_user_id_raises_exception(user_dto,
                                               user_token_dto,
                                               login_response):
    import json
    from gyaan_auth.interactors.dtos import UserWithTokensDTO

    # Arrange
    presenter = LoginPresenterImplementation()
    user_with_tokens_dto = UserWithTokensDTO(
        user_dto=user_dto,
        auth_token_dto=user_token_dto
    )

    # Act
    response = presenter.get_login_response(
        user_with_tokens_dto=user_with_tokens_dto
    )

    # Assert
    response_content = json.loads(response.content)
    assert response_content == login_response
