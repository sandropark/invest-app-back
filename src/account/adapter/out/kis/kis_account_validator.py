from src.account.domain.account_info import AccountInfo
from src.common.domain.exception import ExeptionType, InvestAppException
from src.common.domain.type import BrokerType


class KisAccountValidator:
    def validate(self, account_info: AccountInfo) -> None:
        if account_info.broker_type != BrokerType.KIS:
            return

        if account_info.login_id is None or account_info.url_base is None or account_info.product_code is None or account_info.number is None:
            raise InvestAppException(
                ExeptionType.INVALID_ACCOUNT_INFO,
                f"KIS 계좌는 다음 항목이 필수입니다. number, product_code, url_base, login_id",
            )
