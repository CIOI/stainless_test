# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from decoded_vectorize import DecodedVectorize, AsyncDecodedVectorize
from decoded_vectorize.types import VectorizeCreateIndexResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVectorize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_index(self, client: DecodedVectorize) -> None:
        vectorize = client.vectorize.create_index(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        )
        assert_matches_type(VectorizeCreateIndexResponse, vectorize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_index_with_all_params(self, client: DecodedVectorize) -> None:
        vectorize = client.vectorize.create_index(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
            description="This is my example index.",
        )
        assert_matches_type(VectorizeCreateIndexResponse, vectorize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_index(self, client: DecodedVectorize) -> None:
        response = client.vectorize.with_raw_response.create_index(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vectorize = response.parse()
        assert_matches_type(VectorizeCreateIndexResponse, vectorize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_index(self, client: DecodedVectorize) -> None:
        with client.vectorize.with_streaming_response.create_index(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vectorize = response.parse()
            assert_matches_type(VectorizeCreateIndexResponse, vectorize, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVectorize:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_index(self, async_client: AsyncDecodedVectorize) -> None:
        vectorize = await async_client.vectorize.create_index(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        )
        assert_matches_type(VectorizeCreateIndexResponse, vectorize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_index_with_all_params(self, async_client: AsyncDecodedVectorize) -> None:
        vectorize = await async_client.vectorize.create_index(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
            description="This is my example index.",
        )
        assert_matches_type(VectorizeCreateIndexResponse, vectorize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_index(self, async_client: AsyncDecodedVectorize) -> None:
        response = await async_client.vectorize.with_raw_response.create_index(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vectorize = await response.parse()
        assert_matches_type(VectorizeCreateIndexResponse, vectorize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_index(self, async_client: AsyncDecodedVectorize) -> None:
        async with async_client.vectorize.with_streaming_response.create_index(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vectorize = await response.parse()
            assert_matches_type(VectorizeCreateIndexResponse, vectorize, path=["response"])

        assert cast(Any, response.is_closed) is True
