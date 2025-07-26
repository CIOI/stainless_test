# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .index_config_param import IndexConfigParam

__all__ = ["VectorizeCreateIndexParams"]


class VectorizeCreateIndexParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account identifier"""

    config: Required[IndexConfigParam]

    name: Required[str]
    """Name of the index"""

    description: str
    """Optional description of the index"""
