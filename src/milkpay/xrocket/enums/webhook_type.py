from enum import Enum


class WebhookType(str, Enum):
    INVOICE_PAY = "invoicePay"
    SUBSCRIPTION_PAY = "subscriptionPay"
    SUBSCRIPTION_END = "subscriptionEnd"
    EXCHANGE_ORDER_COMPLETE = "exchangeOrderComplete"
