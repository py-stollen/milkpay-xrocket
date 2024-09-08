from .base import PayXRocketObject
from .withdraw_fee_network_dto import WithdrawFeeNetworkDto


class WithdrawFeeDto(PayXRocketObject):
    currency: str
    """ID of main currency for token"""
    networks: list[WithdrawFeeNetworkDto]
    """Fee for withdraw"""
