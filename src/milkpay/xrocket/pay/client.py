from __future__ import annotations

from hashlib import sha256
from hmac import HMAC
from typing import TYPE_CHECKING, Any, Optional, Union

from stollen import Stollen
from stollen.requests.fields import Header, RequestField

from .exceptions import PayXRocketError, UnknownAPIKeyError

if TYPE_CHECKING:
    from .types import (
        App,
        AvailableCoinsData,
        Cheque,
        FullInvoiceDto,
        InvoiceDto,
        Pagination,
        ShortChequeDto,
        Subscription,
        SubscriptionInterval,
        SubscriptionIntervalDto,
        TransferDto,
        UserSubscription,
        WithdrawalCoinResponseDto,
        WithdrawalDto,
    )


class PayXRocket(Stollen):
    pay_key: Optional[str]
    production: bool

    def __init__(
        self,
        pay_key: Optional[str] = None,
        production: bool = True,
        **stollen_kwargs: Any,
    ) -> None:
        self.pay_key = pay_key
        self.production = production

        fields: list[RequestField] = []
        if pay_key is not None:
            fields.append(Header(name="Rocket-Pay-Key", value=pay_key))

        subdomain: str = "pay" if production else "dev-pay"
        super().__init__(
            base_url=f"https://{subdomain}.xrocket.tg",
            error_message_key=["message"],
            global_request_fields=fields,
            general_error_class=PayXRocketError,
            error_codes={403: UnknownAPIKeyError},
            **stollen_kwargs,
        )

    def check_signature(self, body_text: str, signature: str) -> bool:
        if self.pay_key is None:
            raise ValueError("Pay key is not set")
        hmac: HMAC = HMAC(
            key=sha256(string=self.pay_key.encode("UTF-8")).digest(),
            msg=body_text.encode("UTF-8"),
            digestmod=sha256,
        )
        return hmac.hexdigest() == signature

    async def get_version(self) -> Optional[bool]:
        """
        Returns current version of API. You may use it as healthcheck
        """

        from .methods import GetVersion

        call: GetVersion = GetVersion()

        return await self(call)

    async def create_cheque(
        self,
        *,
        currency: str,
        cheque_per_user: Union[int, float],
        users_number: Union[int, float],
        ref_program: Union[int, float],
        password: Optional[str] = None,
        description: Optional[str] = None,
        send_notifications: Optional[bool] = None,
        enable_captcha: Optional[bool] = None,
        telegram_resources_ids: Optional[list[str]] = None,
        for_premium: Optional[bool] = None,
        linked_wallet: Optional[bool] = None,
        disabled_languages: Optional[list[str]] = None,
    ) -> Cheque:
        """
        Create multi-cheque
        """

        from .methods import CreateCheque

        call: CreateCheque = CreateCheque(
            currency=currency,
            cheque_per_user=cheque_per_user,
            users_number=users_number,
            ref_program=ref_program,
            password=password,
            description=description,
            send_notifications=send_notifications,
            enable_captcha=enable_captcha,
            telegram_resources_ids=telegram_resources_ids,
            for_premium=for_premium,
            linked_wallet=linked_wallet,
            disabled_languages=disabled_languages,
        )

        return await self(call)

    async def get_cheques(
        self,
        *,
        limit: Optional[Union[int, float]] = None,
        offset: Optional[Union[int, float]] = None,
    ) -> Pagination[ShortChequeDto]:
        """
        Get list of multi-cheques
        """

        from .methods import GetCheques

        call: GetCheques = GetCheques(
            limit=limit,
            offset=offset,
        )

        return await self(call)

    async def get_cheque(
        self,
        *,
        id_: str,
    ) -> ShortChequeDto:
        """
        Get multi-cheque info
        """

        from .methods import GetCheque

        call: GetCheque = GetCheque(
            id=id_,
        )

        return await self(call)

    async def edit_cheque(
        self,
        *,
        id_: str,
        password: Optional[str] = None,
        description: Optional[str] = None,
        send_notifications: Optional[bool] = None,
        enable_captcha: Optional[bool] = None,
        telegram_resources_ids: Optional[list[str]] = None,
        for_premium: Optional[bool] = None,
        linked_wallet: Optional[bool] = None,
        disabled_languages: Optional[list[str]] = None,
    ) -> Cheque:
        """
        Edit multi-cheque
        """

        from .methods import EditCheque

        call: EditCheque = EditCheque(
            id=id_,
            password=password,
            description=description,
            send_notifications=send_notifications,
            enable_captcha=enable_captcha,
            telegram_resources_ids=telegram_resources_ids,
            for_premium=for_premium,
            linked_wallet=linked_wallet,
            disabled_languages=disabled_languages,
        )

        return await self(call)

    async def delete_cheque(
        self,
        *,
        id_: str,
    ) -> Optional[bool]:
        """
        Delete multi-cheque
        """

        from .methods import DeleteCheque

        call: DeleteCheque = DeleteCheque(
            id=id_,
        )

        return await self(call)

    async def get_app_info(self) -> App:
        """
        Returns information about your application
        """

        from .methods import GetAppInfo

        call: GetAppInfo = GetAppInfo()

        return await self(call)

    async def transfer(
        self,
        *,
        tg_user_id: Union[int, float],
        currency: str,
        amount: Union[int, float],
        transfer_id: str,
        description: Optional[str] = None,
    ) -> TransferDto:
        """
        Make transfer of funds to another user
        """

        from .methods import Transfer

        call: Transfer = Transfer(
            tg_user_id=tg_user_id,
            currency=currency,
            amount=amount,
            transfer_id=transfer_id,
            description=description,
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
    ) -> WithdrawalDto:
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
    ) -> WithdrawalDto:
        """
        Returns withdrawal status
        """

        from .methods import GetWithdrawalStatus

        call: GetWithdrawalStatus = GetWithdrawalStatus(
            withdrawal_id=withdrawal_id,
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

    async def create_invoice(
        self,
        *,
        amount: Optional[Union[int, float]] = None,
        min_payment: Optional[Union[int, float]] = None,
        num_payments: Union[int, float],
        currency: str,
        description: Optional[str] = None,
        hidden_message: Optional[str] = None,
        comments_enabled: Optional[bool] = None,
        callback_url: Optional[str] = None,
        payload: Optional[str] = None,
        expired_in: Optional[Union[int, float]] = None,
    ) -> InvoiceDto:
        """
        Create invoice
        """

        from .methods import CreateInvoice

        call: CreateInvoice = CreateInvoice(
            amount=amount,
            min_payment=min_payment,
            num_payments=num_payments,
            currency=currency,
            description=description,
            hidden_message=hidden_message,
            comments_enabled=comments_enabled,
            callback_url=callback_url,
            payload=payload,
            expired_in=expired_in,
        )

        return await self(call)

    async def get_invoices(
        self,
        *,
        limit: Optional[Union[int, float]] = None,
        offset: Optional[Union[int, float]] = None,
    ) -> Pagination[InvoiceDto]:
        """
        Get list of invoices
        """

        from .methods import GetInvoices

        call: GetInvoices = GetInvoices(
            limit=limit,
            offset=offset,
        )

        return await self(call)

    async def get_invoice(
        self,
        *,
        id_: str,
    ) -> FullInvoiceDto:
        """
        Get invoice info
        """

        from .methods import GetInvoice

        call: GetInvoice = GetInvoice(
            id=id_,
        )

        return await self(call)

    async def delete_invoice(
        self,
        *,
        id_: str,
    ) -> Optional[bool]:
        """
        Delete invoice
        """

        from .methods import DeleteInvoice

        call: DeleteInvoice = DeleteInvoice(
            id=id_,
        )

        return await self(call)

    async def get_coins(self) -> AvailableCoinsData:
        """
        Returns available currencies
        """

        from .methods import GetCoins

        call: GetCoins = GetCoins()

        return await self(call)

    async def create_subscription(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        currency: str,
        interval: list[SubscriptionIntervalDto],
        tg_resource: Optional[str] = None,
        referral_percent: Union[int, float],
        return_url: Optional[str] = None,
    ) -> Subscription:
        """
        Create subscription
        """

        from .methods import CreateSubscription

        call: CreateSubscription = CreateSubscription(
            name=name,
            description=description,
            currency=currency,
            interval=interval,
            tg_resource=tg_resource,
            referral_percent=referral_percent,
            return_url=return_url,
        )

        return await self(call)

    async def get_subscriptions(
        self,
        *,
        limit: Optional[Union[int, float]] = None,
        offset: Optional[Union[int, float]] = None,
    ) -> Pagination[Subscription]:
        """
        Get list of subscription
        """

        from .methods import GetSubscriptions

        call: GetSubscriptions = GetSubscriptions(
            limit=limit,
            offset=offset,
        )

        return await self(call)

    async def get_subscription(
        self,
        *,
        subscription_id: str,
    ) -> Subscription:
        """
        Get subscription info
        """

        from .methods import GetSubscription

        call: GetSubscription = GetSubscription(
            subscription_id=subscription_id,
        )

        return await self(call)

    async def delete_subscription(
        self,
        *,
        subscription_id: str,
    ) -> Optional[bool]:
        """
        Delete subscription
        """

        from .methods import DeleteSubscription

        call: DeleteSubscription = DeleteSubscription(
            subscription_id=subscription_id,
        )

        return await self(call)

    async def check_subscription(
        self,
        *,
        subscription_id: str,
        user_id: Union[int, float],
    ) -> UserSubscription:
        from .methods import CheckSubscription

        call: CheckSubscription = CheckSubscription(
            subscription_id=subscription_id,
            user_id=user_id,
        )

        return await self(call)

    async def get_subscription_interval(
        self,
        *,
        subscription_id: str,
        interval_code: str,
    ) -> SubscriptionInterval:
        """
        Get subscription interval info
        """

        from .methods import GetSubscriptionInterval

        call: GetSubscriptionInterval = GetSubscriptionInterval(
            subscription_id=subscription_id,
            interval_code=interval_code,
        )

        return await self(call)

    async def edit_subscription_interval(
        self,
        *,
        subscription_id: str,
        interval_code: str,
        status: str,
    ) -> SubscriptionInterval:
        """
        Edit subscription interval
        """

        from .methods import EditSubscriptionInterval

        call: EditSubscriptionInterval = EditSubscriptionInterval(
            subscription_id=subscription_id,
            interval_code=interval_code,
            status=status,
        )

        return await self(call)

    async def delete_subscription_interval(
        self,
        *,
        subscription_id: str,
        interval_code: str,
    ) -> SubscriptionInterval:
        """
        Delete subscription interval
        """

        from .methods import DeleteSubscriptionInterval

        call: DeleteSubscriptionInterval = DeleteSubscriptionInterval(
            subscription_id=subscription_id,
            interval_code=interval_code,
        )

        return await self(call)

    async def create_subscription_interval(
        self,
        *,
        subscription_id: str,
        interval: str,
        amount: Union[int, float],
        status: str,
    ) -> SubscriptionInterval:
        """
        Create subscription interval
        """

        from .methods import CreateSubscriptionInterval

        call: CreateSubscriptionInterval = CreateSubscriptionInterval(
            subscription_id=subscription_id,
            interval=interval,
            amount=amount,
            status=status,
        )

        return await self(call)
