class InterestCoverageRatio:
    def __init__(self, operating_profit, interest_income, dividends_income, equity_in_net_income_of_affiliates,
                 interest_expense, effective_tax_rate):
        self.operating_profit = operating_profit                # 営業利益
        self.interest_income = interest_income                  # 受取利息
        self.dividends_income = dividends_income                # 受取配当金
        self.e_i_n_i_o_a = equity_in_net_income_of_affiliates   # 持分法による投資損益
        self.interest_expense = interest_expense                # 支払利息
        self.effective_tax_rate = effective_tax_rate            # 実効税率

    # 事業利益
    def business_interest(self):
        return self.operating_profit + self.interest_income + self.dividends_income + self.e_i_n_i_o_a

    # インタレストカバレッジレシオ
    def interest_coverage_ratio(self):
        return (self.operating_profit + self.interest_income + self.dividends_income + self.e_i_n_i_o_a)\
               / self.interest_expense

    # 税引後営業利益
    def net_operating_profit_after_taxes(self):
        return self.operating_profit * (1 - self.effective_tax_rate)


n1 = input("営業利益の数字を入れてください：")
n1 = int(n1)

n2 = input("受取利息の数字を入れてください\n"
           "(もし受取利息と受取配当金が合計されている場合は合計額を入れてください)：")
n2 = int(n2)

n3 = input("受取配当金の数字を入れてください\n"
           "(もし受取利息と受取配当金の合計額をすでに記入している場合は0と記入してください)：")
n3 = int(n3)

n4 = input("持分法による投資損益の数字を記入してください\n"
           "(もし金額に△がついている場合はマイナスをつけて数字を記入してください)：")
n4 = int(n4)

n5 = input("支払利息の数字を入れてください：")
n5 = int(n5)

n6 = input("実効税率の数字を入れてください。この数字は調べてください。：")
n6 = int(n6)

inter_ratio = InterestCoverageRatio(n1, n2, n3, n4, n5, n6)
print("事業利益は", inter_ratio.business_interest(), "です。")
print("インタレストカバレッジレシオは", inter_ratio.interest_coverage_ratio(), "です。")


