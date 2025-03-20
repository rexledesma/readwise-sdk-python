# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .orders import (
    OrdersResource,
    AsyncOrdersResource,
    OrdersResourceWithRawResponse,
    AsyncOrdersResourceWithRawResponse,
    OrdersResourceWithStreamingResponse,
    AsyncOrdersResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.store_inventory_response import StoreInventoryResponse

__all__ = ["StoreResource", "AsyncStoreResource"]


class StoreResource(SyncAPIResource):
    @cached_property
    def orders(self) -> OrdersResource:
        return OrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> StoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/readwise-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/readwise-sdk-python#with_streaming_response
        """
        return StoreResourceWithStreamingResponse(self)

    def inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StoreInventoryResponse:
        """Returns a map of status codes to quantities"""
        return self._get(
            "/store/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreInventoryResponse,
        )


class AsyncStoreResource(AsyncAPIResource):
    @cached_property
    def orders(self) -> AsyncOrdersResource:
        return AsyncOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/readwise-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/readwise-sdk-python#with_streaming_response
        """
        return AsyncStoreResourceWithStreamingResponse(self)

    async def inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StoreInventoryResponse:
        """Returns a map of status codes to quantities"""
        return await self._get(
            "/store/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreInventoryResponse,
        )


class StoreResourceWithRawResponse:
    def __init__(self, store: StoreResource) -> None:
        self._store = store

        self.inventory = to_raw_response_wrapper(
            store.inventory,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithRawResponse:
        return OrdersResourceWithRawResponse(self._store.orders)


class AsyncStoreResourceWithRawResponse:
    def __init__(self, store: AsyncStoreResource) -> None:
        self._store = store

        self.inventory = async_to_raw_response_wrapper(
            store.inventory,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        return AsyncOrdersResourceWithRawResponse(self._store.orders)


class StoreResourceWithStreamingResponse:
    def __init__(self, store: StoreResource) -> None:
        self._store = store

        self.inventory = to_streamed_response_wrapper(
            store.inventory,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithStreamingResponse:
        return OrdersResourceWithStreamingResponse(self._store.orders)


class AsyncStoreResourceWithStreamingResponse:
    def __init__(self, store: AsyncStoreResource) -> None:
        self._store = store

        self.inventory = async_to_streamed_response_wrapper(
            store.inventory,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        return AsyncOrdersResourceWithStreamingResponse(self._store.orders)
