# region imports
from AlgorithmImports import *
# endregion

class TrailingStopOrderAlgorithm(QCAlgorithm):
    trailingAmount = 0.01

    def Initialize(self):
        self.SetStartDate(2021, 7, 1)
        self.SetEndDate(2021, 7, 9)
        self.SetCash(100000)

        self.symbol = self.AddEquity("SPY", dataNormalizationMode = DataNormalizationMode.Raw).Symbol

    def OnData(self, data):
        if not self.Portfolio.Invested:
            quantity = 1 if self.Time.day % 2 == 0 else -1
            
            self.MarketOrder(self.symbol, quantity)
            self.TrailingStopOrder(self.symbol, -quantity, self.trailingAmount, True)
