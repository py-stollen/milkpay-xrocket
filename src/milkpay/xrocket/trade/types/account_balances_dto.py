from .account_balance_dto import AccountBalanceDto
from .base import TradeXRocketObject


class AccountBalancesDto(TradeXRocketObject):
    balances: list[AccountBalanceDto]
    """Balances of you account"""
