import asyncio
import logging
from typing import Final

from milkpay.xrocket.pay import PayXRocket

PAY_KEY: Final[str] = "PAY_KEY_HERE"


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    xrocket: PayXRocket = PayXRocket(pay_key=PAY_KEY)
    try:
        for invoice in await xrocket.get_invoices():
            logging.info("Invoice #%d created at %s", invoice.id, invoice.created)
    finally:
        await xrocket.session.close()


if __name__ == "__main__":
    asyncio.run(main())
