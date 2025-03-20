# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from readwise_sdk import ReadwiseSDK, AsyncReadwiseSDK
from readwise_sdk._utils import parse_datetime
from readwise_sdk.types.shared import Order

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: ReadwiseSDK) -> None:
        order = client.store.orders.create()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: ReadwiseSDK) -> None:
        order = client.store.orders.create(
            id=10,
            complete=True,
            pet_id=198772,
            quantity=7,
            ship_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="placed",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: ReadwiseSDK) -> None:
        response = client.store.orders.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: ReadwiseSDK) -> None:
        with client.store.orders.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: ReadwiseSDK) -> None:
        order = client.store.orders.retrieve(
            0,
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: ReadwiseSDK) -> None:
        response = client.store.orders.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: ReadwiseSDK) -> None:
        with client.store.orders.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: ReadwiseSDK) -> None:
        order = client.store.orders.delete(
            0,
        )
        assert order is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: ReadwiseSDK) -> None:
        response = client.store.orders.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert order is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: ReadwiseSDK) -> None:
        with client.store.orders.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncReadwiseSDK) -> None:
        order = await async_client.store.orders.create()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncReadwiseSDK) -> None:
        order = await async_client.store.orders.create(
            id=10,
            complete=True,
            pet_id=198772,
            quantity=7,
            ship_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="placed",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncReadwiseSDK) -> None:
        response = await async_client.store.orders.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncReadwiseSDK) -> None:
        async with async_client.store.orders.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncReadwiseSDK) -> None:
        order = await async_client.store.orders.retrieve(
            0,
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncReadwiseSDK) -> None:
        response = await async_client.store.orders.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncReadwiseSDK) -> None:
        async with async_client.store.orders.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncReadwiseSDK) -> None:
        order = await async_client.store.orders.delete(
            0,
        )
        assert order is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncReadwiseSDK) -> None:
        response = await async_client.store.orders.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert order is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncReadwiseSDK) -> None:
        async with async_client.store.orders.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True
