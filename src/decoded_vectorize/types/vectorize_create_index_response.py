# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .index_config import IndexConfig

__all__ = ["VectorizeCreateIndexResponse", "Error", "ErrorSource", "Message", "MessageSource", "Result"]


class ErrorSource(BaseModel):
    pointer: Optional[str] = None
    """JSON pointer to the error location"""


class Error(BaseModel):
    code: Optional[int] = None
    """Error code"""

    documentation_url: Optional[str] = None
    """URL to documentation"""

    message: Optional[str] = None
    """Error message"""

    source: Optional[ErrorSource] = None


class MessageSource(BaseModel):
    pointer: Optional[str] = None
    """JSON pointer to the message location"""


class Message(BaseModel):
    code: Optional[int] = None
    """Message code"""

    documentation_url: Optional[str] = None
    """URL to documentation"""

    message: Optional[str] = None
    """Message text"""

    source: Optional[MessageSource] = None


class Result(BaseModel):
    config: Optional[IndexConfig] = None

    description: Optional[str] = None
    """Description of the index"""

    name: Optional[str] = None
    """Name of the created index"""


class VectorizeCreateIndexResponse(BaseModel):
    errors: Optional[List[Error]] = None

    messages: Optional[List[Message]] = None

    result: Optional[Result] = None

    success: Optional[bool] = None
    """Whether the operation was successful"""
