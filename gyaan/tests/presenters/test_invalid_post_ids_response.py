from gyaan.exceptions import InvalidPostIds
from gyaan.presenters.presenter_implementation import GetPostsPresenterImplementation


def test_raise_invalid_user_id_exception_returns_http_response(snapshot):
    import json

    # Arrange
    presenter = GetPostsPresenterImplementation()
    invalid_post_ids = [1, 2, 3]
    err_obj = InvalidPostIds(invalid_post_ids=invalid_post_ids)

    # Act
    response = presenter.return_invalid_posts_response(err_obj)

    # Assert
    response_content = json.loads(response.content)
    snapshot.assert_match(
        name="Invalid post ids response",
        value=response_content
    )
