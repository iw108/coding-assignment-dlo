"""Functionality related to generating tokens."""

from datetime import UTC, datetime
from enum import StrEnum
from hashlib import sha512
from hmac import new
from uuid import UUID, uuid4

from pydantic import AwareDatetime, BaseModel, Field


def now() -> datetime:
    return datetime.now(tz=UTC)


class UserType(StrEnum):
    provider = "careprovider"
    client = "client"


class TokenParams(BaseModel):
    pass


class User(BaseModel):
    id: str = Field(..., serialization_alias="userid")
    type: UserType = Field(..., serialization_alias="usertype")


class DLOTokenParams(User, TokenParams):
    timestamp: AwareDatetime = Field(default_factory=now)
    nonce: UUID = Field(default_factory=uuid4)


class TokenGenerator:
    """Class to generate DLO tokens."""

    def __init__(self, key: str):
        self.key = key

    def __call__(self, params: TokenParams) -> str:
        """Generate token from token params."""
        params_as_dict = params.model_dump(
            mode="json",
            exclude_none=True,
            by_alias=True,
        )
        message = "".join(
            f"{key}{value}" for key, value in sorted(params_as_dict.items())
        )
        return new(self.key.encode(), message.encode(), sha512).hexdigest()
