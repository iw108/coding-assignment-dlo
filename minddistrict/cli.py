"""Cli app."""

from typing import Annotated

import typer

from .token import TokenGenerator, User, UserType
from .url import ClientRoutes, ProfessionalRoutes, URLGenerator

app = typer.Typer()


BASE_URL = "https://ca-isnaitic.minddistrict.dev"


@app.command()
def get_professional_url(
    route: ProfessionalRoutes,
    user_id: Annotated[str, typer.Option()],
    secret_key: Annotated[str, typer.Option(envvar="DLO_KEY")],
    base_url: Annotated[str, typer.Option()] = BASE_URL,
):
    user = User(
        id=user_id,
        type=UserType.provider,
    )

    url_generator = URLGenerator(
        base_url=base_url,
        token_generator=TokenGenerator(secret_key),
    )

    print(url_generator.get_url(route, user))


@app.command()
def get_client_url(
    route: ClientRoutes,
    user_id: Annotated[str, typer.Option()],
    secret_key: Annotated[str, typer.Option(envvar="DLO_KEY")],
    base_url: Annotated[str, typer.Option()] = BASE_URL,
):
    user = User(
        id=user_id,
        type=UserType.client,
    )

    url_generator = URLGenerator(
        base_url=base_url,
        token_generator=TokenGenerator(secret_key),
    )

    print(url_generator.get_url(route, user))


if __name__ == "__main__":
    app()
