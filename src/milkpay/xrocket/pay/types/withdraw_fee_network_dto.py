from pydantic import Field

from .base import PayXRocketObject
from .withdraw_fee_network_fee_dto import WithdrawFeeNetworkFeeDto


class WithdrawFeeNetworkDto(PayXRocketObject):
    network_code: str = Field(alias="networkCode")
    """Network code for withdraw"""
    fee_withdraw: WithdrawFeeNetworkFeeDto = Field(alias="feeWithdraw")
    """Withdraw fee params"""
