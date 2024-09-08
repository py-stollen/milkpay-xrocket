
###############
milkpay-xrocket
###############

**milkpay** is a set of lightweight crypto payment system SDKs.
**⚠️ This SDK still in beta! ⚠️**

Installation
------------

..  code-block:: bash

    pip install -U milkpay-xrocket

Simple example
--------------

.. code-block:: python

    import asyncio
    import logging
    from typing import Final

    from milkpay.xrocket.pay import PayXRocket


    PAY_KEY: Final[str] = "YOUR_PAY_KEY_HERE"


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


Support
-------
❤️ My TON Address: `UQBTR4X8Cg-qJ3jkMLbuhe7DkqSNAfddNj8kvOHZtLHtR8YQ`

