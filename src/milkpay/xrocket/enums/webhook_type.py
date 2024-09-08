from enum import StrEnum


class WebhookType(StrEnum):
    INVOICE_PAY = "invoicePay"
    SUBSCRIPTION_PAY = "subscriptionPay"
    SUBSCRIPTION_END = "subscriptionEnd"
    EXCHANGE_ORDER_COMPLETE = "exchangeOrderComplete"
