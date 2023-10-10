from Pages.Client_Management import ClientManagement
from Pages.Dashboard import Dashboard
from Pages.Login import Login
from Pages.Portfolio_Management import PortfolioManagement
from Pages.Trade_Processing import TradeProcessing
from Pages.Trades_Settlement import TradeSettlement


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = Login(self.driver)
        self.dashboard_page = Dashboard(self.driver)
        self.client_management = ClientManagement(self.driver)
        self.trade_processing = TradeProcessing(self.driver)
        self.portfolio_management = PortfolioManagement(self.driver)
        self.trade_settlement = TradeSettlement(self.driver)
