import json

from gyaan.presenters.presenter_implementation import GetDomainDetailsPresenterImplementation


class TestGetDomainDetialsResponse:
    def test_with_domain_dto_returns_http_response(self,
                                                   domain_details_dto,
                                                   snapshot):

        # Arrange
        presenter = GetDomainDetailsPresenterImplementation()

        # Act
        response = presenter.get_domain_details_response(
            domain_details_dto=domain_details_dto
        )

        # Assert
        response_content = json.loads(response.content)
        snapshot.assert_match(
            name="domain details response",
            value=response_content
        )
