from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from stollen import Stollen
from stollen.requests.fields import Header, RequestField

from .exceptions import TradeXRocketError, UnknownAPIKeyError

if TYPE_CHECKING:
    from .types import (
        AccountBalanceDto,
        AccountBalancesDto,
        CryptoCurrenciesResponseDto,
        ExchangeOrderDto,
        FiatCurrenciesDto,
        LastTradesResponseDto,
        OrderBookFullDto,
        OrderEstimateDto,
        Pagination,
        PairDto,
        RateCryptoCryptoDto,
        RateCryptoFiatDto,
        TimeSeriesDto,
        UserFeesResponseDto,
        WithdrawalCoinResponseDto,
        WithdrawalResponseDto,
    )


class TradeXRocket(Stollen):
    trade_key: Optional[str]
    production: bool

    def __init__(
        self,
        trade_key: Optional[str] = None,
        production: bool = True,
        **stollen_kwargs: Any,
    ) -> None:
        self.trade_key = trade_key
        self.production = production

        fields: list[RequestField] = []
        if trade_key is not None:
            fields.append(Header(name="Rocket-Exchange-Key", value=trade_key))

        subdomain: str = "trade" if production else "dev-trade"
        super().__init__(
            base_url=f"https://{subdomain}.xrocket.tg",
            error_message_key=["message"],
            global_request_fields=fields,
            general_error_class=TradeXRocketError,
            error_codes={403: UnknownAPIKeyError},
            **stollen_kwargs,
        )

    async def get_version(self) -> Optional[bool]:
        """
        Returns current version of API. You may use it as healthcheck
        """

        from .methods import GetVersion

        call: GetVersion = GetVersion()

        return await self(call)

    async def get_balances(self) -> AccountBalancesDto:
        """
        Returns current balances of you account
        """

        from .methods import GetBalances

        call: GetBalances = GetBalances()

        return await self(call)

    async def get_fees(self) -> UserFeesResponseDto:
        """
        Returns current user fees
        """

        from .methods import GetFees

        call: GetFees = GetFees()

        return await self(call)

    async def get_balance(
        self,
        *,
        coin: str,
    ) -> AccountBalanceDto:
        """
        Returns current balance of you account for coin
        """

        from .methods import GetBalance

        call: GetBalance = GetBalance(
            coin=coin,
        )

        return await self(call)

    async def get_withdrawal_fees(
        self,
        *,
        currency: Optional[str] = None,
    ) -> list[WithdrawalCoinResponseDto]:
        """
        Returns withdrawal fees
        """

        from .methods import GetWithdrawalFees

        call: GetWithdrawalFees = GetWithdrawalFees(
            currency=currency,
        )

        return await self(call)

    async def withdrawal(
        self,
        *,
        network: str,
        address: str,
        currency: str,
        amount: Union[int, float],
        withdrawal_id: str,
        comment: Optional[str] = None,
    ) -> WithdrawalResponseDto:
        """
        Make withdrawal of funds to external wallet
        """

        from .methods import Withdrawal

        call: Withdrawal = Withdrawal(
            network=network,
            address=address,
            currency=currency,
            amount=amount,
            withdrawal_id=withdrawal_id,
            comment=comment,
        )

        return await self(call)

    async def get_withdrawal_status(
        self,
        *,
        withdrawal_id: str,
    ) -> WithdrawalResponseDto:
        """
        Returns withdrawal status
        """

        from .methods import GetWithdrawalStatus

        call: GetWithdrawalStatus = GetWithdrawalStatus(
            withdrawal_id=withdrawal_id,
        )

        return await self(call)

    async def get_pairs(self) -> list[PairDto]:
        """
        Returns available pairs on Rocket Exchange
        """

        from .methods import GetPairs

        call: GetPairs = GetPairs()

        return await self(call)

    async def get_pair(
        self,
        *,
        pair: str,
    ) -> PairDto:
        """
        Return pair by base/quote coin on Rocket Exchange
        """

        from .methods import GetPair

        call: GetPair = GetPair(
            pair=pair,
        )

        return await self(call)

    async def get_available_fiat_currencies(self) -> FiatCurrenciesDto:
        """
        Returns available fiat currencies for exchange rates
        """

        from .methods import GetAvailableFiatCurrencies

        call: GetAvailableFiatCurrencies = GetAvailableFiatCurrencies()

        return await self(call)

    async def get_available_crypto_currencies(self) -> CryptoCurrenciesResponseDto:
        """
        Returns available crypto currencies for exchange rates
        """

        from .methods import GetAvailableCryptoCurrencies

        call: GetAvailableCryptoCurrencies = GetAvailableCryptoCurrencies()

        return await self(call)

    async def get_crypto_rate_in_fiat(
        self,
        *,
        crypto: str,
        fiat: str,
    ) -> RateCryptoFiatDto:
        """
        Returns rate crypto currency in fiat
        """

        from .methods import GetCryptoRateInFiat

        call: GetCryptoRateInFiat = GetCryptoRateInFiat(
            crypto=crypto,
            fiat=fiat,
        )

        return await self(call)

    async def get_crypto_rate_in_crypto(
        self,
        *,
        base: str,
        quote: str,
    ) -> RateCryptoCryptoDto:
        """
        Returns rate crypto currency in crypto
        """

        from .methods import GetCryptoRateInCrypto

        call: GetCryptoRateInCrypto = GetCryptoRateInCrypto(
            base=base,
            quote=quote,
        )

        return await self(call)

    async def get_time_series(
        self,
        *,
        pair: str,
        start_date: str,
        end_date: str,
        period: str,
    ) -> TimeSeriesDto:
        """
        Get timeseries for pair
        """

        from .methods import GetTimeSeries

        call: GetTimeSeries = GetTimeSeries(
            pair=pair,
            start_date=start_date,
            end_date=end_date,
            period=period,
        )

        return await self(call)

    async def get_order_book(
        self,
        *,
        pair: str,
    ) -> OrderBookFullDto:
        """
        Returns full order book for pair
        """

        from .methods import GetOrderBook

        call: GetOrderBook = GetOrderBook(
            pair=pair,
        )

        return await self(call)

    async def get_order_book_compact(
        self,
        *,
        pair: str,
    ) -> OrderBookFullDto:
        """
        Returns full order book for pair
        """

        from .methods import GetOrderBookCompact

        call: GetOrderBookCompact = GetOrderBookCompact(
            pair=pair,
        )

        return await self(call)

    async def get_orders(
        self,
        *,
        limit: Optional[Union[int, float]] = None,
        offset: Optional[Union[int, float]] = None,
        only_active: bool,
    ) -> Pagination[ExchangeOrderDto]:
        """
        Get list of exchange orders
        """

        from .methods import GetOrders

        call: GetOrders = GetOrders(
            limit=limit,
            offset=offset,
            only_active=only_active,
        )

        return await self(call)

    async def create_order(
        self,
        *,
        pair: str,
        type_: str,
        execute_type: str,
        rate: Optional[Union[int, float]] = None,
        amount: Union[int, float],
        currency: str,
    ) -> ExchangeOrderDto:
        """
        Execute order
        """

        from .methods import CreateOrder

        call: CreateOrder = CreateOrder(
            pair=pair,
            type=type_,
            execute_type=execute_type,
            rate=rate,
            amount=amount,
            currency=currency,
        )

        return await self(call)

    async def get_orders_by_pair(
        self,
        *,
        pair: str,
        limit: Optional[Union[int, float]] = None,
        offset: Optional[Union[int, float]] = None,
        only_active: bool,
    ) -> Pagination[ExchangeOrderDto]:
        """
        Get list of exchange orders by pair
        """

        from .methods import GetOrdersByPair

        call: GetOrdersByPair = GetOrdersByPair(
            pair=pair,
            limit=limit,
            offset=offset,
            only_active=only_active,
        )

        return await self(call)

    async def get_order(
        self,
        *,
        id_: str,
    ) -> ExchangeOrderDto:
        """
        Get exchange order
        """

        from .methods import GetOrder

        call: GetOrder = GetOrder(
            id=id_,
        )

        return await self(call)

    async def cancel_order(
        self,
        *,
        id_: str,
    ) -> Optional[bool]:
        """
        Cancel exchange order
        """

        from .methods import CancelOrder

        call: CancelOrder = CancelOrder(
            id=id_,
        )

        return await self(call)

    async def get_order_estimate(
        self,
        *,
        pair_id: Union[int, float],
        type_: str,
        execute_type: str,
        rate: Union[int, float],
        amount: Union[int, float],
        currency: str,
    ) -> OrderEstimateDto:
        """
        Returns order estimate
        """

        from .methods import GetOrderEstimate

        call: GetOrderEstimate = GetOrderEstimate(
            pair_id=pair_id,
            type=type_,
            execute_type=execute_type,
            rate=rate,
            amount=amount,
            currency=currency,
        )

        return await self(call)

    async def get_last_trades(
        self,
        *,
        pair: str,
        limit: Optional[Union[int, float]] = None,
    ) -> list[LastTradesResponseDto]:
        """
        Get last trades by pair
        """

        from .methods import GetLastTrades

        call: GetLastTrades = GetLastTrades(
            pair=pair,
            limit=limit,
        )

        return await self(call)
