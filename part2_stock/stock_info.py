import pandas as pd
import yfinance as yf


class Stock:
    def __init__(self, ticker) -> None:
        # 주식 티커 설정
        self.ticker = ticker

        try:
            # 티커 데이터 가져오기
            self.stock = yf.Ticker(self.ticker)
            # 데이터가 없는 경우 None 처리
            if not self.stock.info:
                self.stock = None
        except Exception as e:
            print(f"Error fetching data for ticker {self.ticker}: {e}")
            self.stock = None

    def 금융정보(self):
        if not self.stock:
            return {"error": f"No data available for ticker {self.ticker}"}
        try:
            return {
                'info': self.stock.info,
                'income_statement': self.stock.quarterly_income_stmt,
                'balance_sheet': self.stock.quarterly_balance_sheet,
                'cash_flow': self.stock.quarterly_cash_flow,
                'history': self.stock.history(period='1mo'),
            }
        except Exception as e:
            return {"error": f"Failed to retrieve financial data: {e}"}
        
    def report_support(self):
        """
        금융 전문가의 분석을 보조할 지표들
        """
        if not self.stock:
            return f"No data available for ticker {self.ticker}"

        def is_float(x):
            try:
                float(x)
                return True
            except ValueError:
                return False
            except TypeError:
                return False

        try:
            stock = self.stock
            info = pd.DataFrame.from_dict(stock.info, orient='index', columns=['Value'])
            info = info[info['Value'].apply(is_float)]

            return f'''
            ### Financials
            {info.to_markdown()}

            #### Quarterly Income Statement
            {stock.quarterly_income_stmt.loc[['Total Revenue', 'Gross Profit', 'Operating Income', 'Net Income']].to_markdown()}"""

            #### Quarterly Balance Sheet
            {stock.quarterly_balance_sheet.loc[['Total Assets', 'Total Liabilities Net Minority Interest', 'Stockholders Equity']].to_markdown()}"""

            #### Quarterly Cash Flow
            {stock.quarterly_cash_flow.loc[['Operating Cash Flow', 'Investing Cash Flow', 'Financing Cash Flow']].to_markdown()}"""
            '''
        except Exception as e:
            return f"Error generating report: {e}"