# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import vectorize_create_index_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.index_config_param import IndexConfigParam
from ..types.vectorize_create_index_response import VectorizeCreateIndexResponse

__all__ = ["VectorizeResource", "AsyncVectorizeResource"]


class VectorizeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VectorizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CIOI/stainless_test#accessing-raw-response-data-eg-headers
        """
        return VectorizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CIOI/stainless_test#with_streaming_response
        """
        return VectorizeResourceWithStreamingResponse(self)

    def create_index(
        self,
        *,
        account_id: str,
        config: IndexConfigParam,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorizeCreateIndexResponse:
        """
        Creates a new Vectorize Index by calling Cloudflare Vectorize API

        Args:
          account_id: Cloudflare account identifier

          name: Name of the index

          description: Optional description of the index

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/vectorize/indexes",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "config": config,
                    "name": name,
                    "description": description,
                },
                vectorize_create_index_params.VectorizeCreateIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorizeCreateIndexResponse,
        )


class AsyncVectorizeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVectorizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CIOI/stainless_test#accessing-raw-response-data-eg-headers
        """
        return AsyncVectorizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CIOI/stainless_test#with_streaming_response
        """
        return AsyncVectorizeResourceWithStreamingResponse(self)

    async def create_index(
        self,
        *,
        account_id: str,
        config: IndexConfigParam,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorizeCreateIndexResponse:
        """
        Creates a new Vectorize Index by calling Cloudflare Vectorize API

        Args:
          account_id: Cloudflare account identifier

          name: Name of the index

          description: Optional description of the index

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/vectorize/indexes",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "config": config,
                    "name": name,
                    "description": description,
                },
                vectorize_create_index_params.VectorizeCreateIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorizeCreateIndexResponse,
        )


class VectorizeResourceWithRawResponse:
    def __init__(self, vectorize: VectorizeResource) -> None:
        self._vectorize = vectorize

        self.create_index = to_raw_response_wrapper(
            vectorize.create_index,
        )


class AsyncVectorizeResourceWithRawResponse:
    def __init__(self, vectorize: AsyncVectorizeResource) -> None:
        self._vectorize = vectorize

        self.create_index = async_to_raw_response_wrapper(
            vectorize.create_index,
        )


class VectorizeResourceWithStreamingResponse:
    def __init__(self, vectorize: VectorizeResource) -> None:
        self._vectorize = vectorize

        self.create_index = to_streamed_response_wrapper(
            vectorize.create_index,
        )


class AsyncVectorizeResourceWithStreamingResponse:
    def __init__(self, vectorize: AsyncVectorizeResource) -> None:
        self._vectorize = vectorize

        self.create_index = async_to_streamed_response_wrapper(
            vectorize.create_index,
        )
