"""Functionality related to generating urls."""

import urllib.parse
from enum import StrEnum, auto
from typing import Callable, Mapping

from .token import DLOTokenParams, TokenParams, User


class ClientRoutes(StrEnum):
    """Enum defining professional routes."""

    catalogue = auto()
    conversations = auto()


class ProfessionalRoutes(StrEnum):
    """Enum defining professional routes."""

    catalogue = auto()
    clients = auto()
    clients_all = auto()
    configuration = auto()
    professionals = auto()
    tasks = auto()


RouteMappingT = Mapping[ClientRoutes | ProfessionalRoutes, str]


ROUTE_MAPPING: RouteMappingT = {
    ProfessionalRoutes.catalogue: "catalogue",
    ProfessionalRoutes.configuration: "configuration",
    ProfessionalRoutes.clients: "c/",
    ProfessionalRoutes.clients_all: "c/@@all",
    ProfessionalRoutes.professionals: "p/",
    ProfessionalRoutes.tasks: "tasks",
    ClientRoutes.catalogue: "catalogue",
    ClientRoutes.conversations: "conversations",
}


class URLGenerator:
    """Class used to generate DLO authenticated urls."""

    def __init__(
        self,
        base_url: str,
        token_generator: Callable[[TokenParams], str],
        *,
        _route_mapping: RouteMappingT = ROUTE_MAPPING,
        _params_cls: type[TokenParams] = DLOTokenParams,
    ):
        self.base_url = base_url
        self.token_generator = token_generator

        self.route_mapping = _route_mapping
        self.params_cls = _params_cls

    def get_url(
        self,
        route_key: ProfessionalRoutes | ClientRoutes,
        user: User,
    ) -> str:
        """Get DLO authenticated url for given route."""
        route_url = self._get_route_url(route_key)
        query_params = self._get_query_params(user)
        return f"{route_url}?{query_params}"

    def _get_route_url(self, route_key: ProfessionalRoutes | ClientRoutes):
        route = self.route_mapping[route_key]
        return f"{self.base_url}/{route}"

    def _get_query_params(self, user: User) -> str:
        token_params = self.params_cls(**user.model_dump())

        query_params = urllib.parse.urlencode(
            {
                **token_params.model_dump(
                    mode="json",
                    by_alias=True,
                    exclude_none=True,
                ),
                "token": self.token_generator(token_params),
            }
        )
        return query_params
