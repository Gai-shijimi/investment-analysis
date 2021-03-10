class CurrentRatio:
    def __init__(self, cash, trading_securities, trade_notes_accounts_receivable, inventory_assets,
                 current_assets, total_assets, trade_payable, current_liabilities, debt_sum, investment_and_loan,
                 tangible_fixed_assets, intangible_fixed_assets):
        self.cash = cash                                        # 現金・預金及び現金同等物
        self.tra_sec = trading_securities                       # 流動資産の項目にある有価証券(売買目的有価証券)
        self.t_n_a_r = trade_notes_accounts_receivable          # 受取手形と売掛金
        self.inventory_assets = inventory_assets                # 棚卸資産
        self.c_assets = current_assets                          # 流動資産の合計
        self.total_assets = total_assets                        # 資産合計
        self.trade_payable = trade_payable                      # 支払手形および買掛金の合計
        self.c_liabilities = current_liabilities                # 流動負債の合計
        self.debt_sum = debt_sum                                # 負債合計
        self.invest_and_loan = investment_and_loan              # 投資および貸付金合計
        self.tangible_fixed_assets = tangible_fixed_assets      # 有形固定資産合計
        self.intangible_fixed_assets = intangible_fixed_assets  # 無形固定資産

    # 流動比率
    def current_ratio(self):
        return self.c_assets / self.c_liabilities * 100

    # 当座比率
    def quick_assets_ratio(self):
        return (self.cash + self.t_n_a_r + self.tra_sec) / self.c_liabilities * 100

    # 運転資本
    def working_capital(self):
        return self.t_n_a_r + self.inventory_assets + self.trade_payable

    # 純資産
    def net_assets(self):
        return self.total_assets - self.debt_sum

    # 負債・純資産比率
    def d_s_t_e_ratio(self):
        return self.debt_sum / (self.total_assets - self.debt_sum) * 100

    # 固定資産比率
    def fixed_ratio(self):
        return (self.invest_and_loan + self.tangible_fixed_assets + self.intangible_fixed_assets) / \
               (self.total_assets - self.debt_sum) * 100


num1 = input("現金・預金及び現金同等物の金額を記入してください：")
num1 = int(num1)

num2 = input("流動資産の項目にある有価証券の金額の数字を入れてください：")
num2 = int(num2)

num3 = input("受取手形と売掛金が含まれてる項目の金額を記入してください：")
num3 = int(num3)

num4 = input("棚卸資産の金額を入れてください：")
num4 = int(num4)

num5 = input("流動資産の合計額の数字を記入してください：")
num5 = int(num5)

num6 = input("資産合計の数字を記入してください：")
num6 = int(num6)

num7 = input("支払手形および買掛金の合計額を記入してください：")
num7 = int(num7)

num8 = input("流動負債の合計額の数字を記入してください：")
num8 = int(num8)

num9 = input("負債合計の数字を記入してください：")
num9 = int(num9)

num10 = input("投資および貸付金合計の数字を記入してください：")
num10 = int(num10)

num11 = input("有形固定資産合計を記入してください：")
num11 = int(num11)

num12 = input("無形固定資産を記入してください：")
num12 = int(num12)

num = num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12

# 1470073, 1324538, 1091242, 653278, 5246612, 20981586, 492124, 6079815, 16536095, 11724651, 777053, 917966


c_ratio = CurrentRatio(num)

print(c_ratio.current_ratio())
print(c_ratio.quick_assets_ratio())
print(c_ratio.working_capital())
print(c_ratio.d_s_t_e_ratio())
print(c_ratio.fixed_ratio())
