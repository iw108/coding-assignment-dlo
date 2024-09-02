from hashlib import sha512
from hmac import HMAC

from pydantic import Field

from minddistrict.token import TokenGenerator, TokenParams


class MockTokenParams(TokenParams):
    a: int = Field(1, serialization_alias="c")
    b: int = 2


def test_token_generator_creates_correct_token():
    key = "test_key"
    params = MockTokenParams()

    generator = TokenGenerator(key)

    expected_token = HMAC(key.encode(), b"b2c1", sha512).hexdigest()

    assert generator(params) == expected_token
