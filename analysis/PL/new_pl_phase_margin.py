# Plの基本分析
from analysis.PL.new_pl_interest_coverage_ratio import inter_ratio


class PhaseMargin:
    def __init__(self, sales, gross_profit, ordinary_income, net_income):  # 営業利益はある
        self.sales = sales                          # 売上高
        self.gross_profit = gross_profit            # 総利益
        self.ordinary_income = ordinary_income      # 経常利益
        self.net_income = net_income                # 当期純利益

    # 売上高総利益率
    def gross_profit_margin(self):
        return self.gross_profit / self.sales * 100

    # 売上高営業利益率
    def operating_profit_margin(self):
        return inter_ratio.operating_profit / self.sales * 100

    # 売上高経常利益率
    def ordinary_income_to_net_sales_ratio(self):
        return self.ordinary_income / self.sales * 100

    # 売上高当期利益率
    def net_profit_margin(self):
        return self.net_income / self.sales * 100


n1 = input("売上高の数字を入れてください：")
n2 = input("売上総利益の数字を入れてください：")
n3 = input("経常利益の数字を入れてください：")
n4 = input("当期利益の数字を入れてください：")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)

phase_margin = PhaseMargin(n1, n2, n3, n4)

print("売上高総利益率は", phase_margin.gross_profit_margin(), "%です。")
print("売上高営業利益率は", phase_margin.operating_profit_margin(), "%です。")
print("売上高経常利益率は", phase_margin.ordinary_income_to_net_sales_ratio(), "%です。")
print("売上高当期利益率は", phase_margin.net_profit_margin(), "%です")


