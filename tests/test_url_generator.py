from minddistrict.token import TokenParams, User, UserType
from minddistrict.url import ClientRoutes, URLGenerator


class MockTokenParams(User, TokenParams):
    pass


def test_url_generator_creates_expected_url():
    url_generator = URLGenerator(
        base_url="https://test.com",
        token_generator=lambda _: "test-token",
        _route_mapping={ClientRoutes.catalogue: "catalogue"},
        _params_cls=MockTokenParams,
    )

    url = url_generator.get_url(
        ClientRoutes.catalogue,
        User(id="test-id", type=UserType.client),
    )

    expected_url = (
        "https://test.com/catalogue?userid=test-id&usertype=client&token=test-token"
    )

    assert url == expected_url
