from urllib.parse import quote

from loguru import logger

DEBUG = True
SQLALCHEMY_DATABASE_URI = f'mysql://sa:{quote("12345")}@10.128.43.117/apitest'
# SQLALCHEMY_DATABASE_URI = f'mssql://sa:{quote("123456789aA")}@Banana\\SQLEXPRESS/treasury?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# logger.add('logs/{time}.log', level='DEBUG', rotation='00:00')


class Config():
    """Contain all the data that is required to run use cases.
    Required parameters must be provided in any case,
    while optionals used only in specific use cases and should be provided accordingly.
    """

    def __init__(self) -> None:
        self.cms_api_url: str = "wss://democmsapi.cqg.com:443"

        # Brokerage specific data that can be obtained from CAST.
        self.brokerage_id: str = ""  # Without prefix.
        self.profile_sales_series_id: str = ""  # With 'S' prefix.

        # REQUIRED PARAMETERS
        # Authentication data.
        self.username: str = "APIBalanceCMS"
        self.password: str = "1Password!"
        self.client_app_id: str = "SacombankCMS"  # Provided by CQG.
        self.private_label: str = ""  # Provided by CQG.
        self.client_version: str = ""

        # Additional data for use cases.
        self.email: str = ""

        # OPTIONAL PARAMETERS
        # External authentication data (external_auth case).
        self.external_auth_service_id: int = 0  # Provided by CQG when required.
        self.external_auth_partner_id: str = "0"  # Provided by CQG when required.
