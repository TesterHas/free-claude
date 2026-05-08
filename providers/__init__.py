"""Providers package - implement your own provider by extending BaseProvider.

Concrete adapters (e.g. ``DeepSeekProvider``) live in subpackages; import them
from ``providers.deepseek`` etc. to avoid loading every adapter when the
``providers`` package is imported.
"""

from .base import BaseProvider, ProviderConfig
from .exceptions import (
    APIError,
    AuthenticationError,
    InvalidRequestError,
    ModelListResponseError,
    OverloadedError,
    ProviderError,
    RateLimitError,
    UnknownProviderTypeError,
)

__all__ = [
    "APIError",
    "AuthenticationError",
    "BaseProvider",
    "InvalidRequestError",
    "ModelListResponseError",
    "OverloadedError",
    "ProviderConfig",
    "ProviderError",
    "RateLimitError",
    "UnknownProviderTypeError",
]
