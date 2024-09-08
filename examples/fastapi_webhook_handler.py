from __future__ import annotations

import logging
from typing import Annotated, Any, Final

from fastapi import APIRouter, Body, Header, HTTPException, Request

from milkpay.xrocket.pay import PayXRocket
from milkpay.xrocket.pay.types import Update

router: Final[APIRouter] = APIRouter()
logger: Final[logging.Logger] = logging.getLogger(name=__name__)


@router.post("/webhook/xrocket")
async def accept_xrocket_payment(
    request: Request,
    rocket_pay_signature: Annotated[str, Header()],
    update: Annotated[Update, Body()],
) -> Any:
    xrocket: PayXRocket = request.app.state.xrocket
    if not xrocket.check_signature(
        body_text=(await request.body()).decode(),
        signature=rocket_pay_signature,
    ):
        raise HTTPException(status_code=401, detail="Invalid signature")
    logger.info("Received payment with id %d", update.data.id)
