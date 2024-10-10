from typing import Union

from pydantic import Field

from .base import PayXRocketObject
from .set import Set
from .tg_resource import TgResource


class Cheque(PayXRocketObject):
    id: Union[int, float]
    """Cheque ID"""
    currency: str
    total: Union[int, float]
    """Total amount of cheque (this amount is charged from balance)"""
    per_user: Union[int, float] = Field(alias="perUser")
    """Amount of cheque per user"""
    users: Union[int, float]
    """Number of users that can activate your cheque"""
    password: str
    """Cheque password"""
    description: str
    """Cheque description"""
    send_notifications: bool = Field(alias="sendNotifications")
    """send notifications about cheque activation to application cheque webhook or not"""
    captcha_enabled: bool = Field(alias="captchaEnabled")
    """enable / disable cheque captcha"""
    ref_program_percents: Union[int, float] = Field(alias="refProgramPercents")
    """percentage of cheque that rewarded for referral program"""
    ref_reward_per_user: Union[int, float] = Field(alias="refRewardPerUser")
    """amount of referral user reward"""
    state: str
    """Active - cheque created and has unclaimed activations. Completed - cheque totally activated."""
    link: str
    tg_resources: list[TgResource] = Field(alias="tgResources")
    activations: Union[int, float]
    """How many times cheque is activated"""
    ref_rewards: Union[int, float] = Field(alias="refRewards")
    """How many times referral reward is payed"""
    disabled_languages: Set = Field(alias="disabledLanguages")
    """Disable languages"""
    for_premium: bool = Field(alias="forPremium")
    """Only users with Telegram Premium can activate this cheque"""
    for_new_users_only: bool = Field(alias="forNewUsersOnly")
    """Only new users can activate this cheque"""
    linked_wallet: bool = Field(alias="linkedWallet")
    """Only users with connected wallets can activate this cheque"""
