from .pay_invoice_dto import PayInvoiceDto
from .webhook_dto import WebhookDto


class Update(WebhookDto):
    data: PayInvoiceDto
