# 収益性の分析 ROE, ROA
from analysis.PL.new_pl_interest_coverage_ratio import inter_ratio
from analysis.BS.new_bs_analysis import c_ratio


class AnalysisProfitability:
    def __init__(self, total_assets, debt_sum, minority_interests, share_option, current_net_income,
                 short_term_loans_receivable, investment_and_other, construction_in_progress_accounts):
        self.total_assets = total_assets                                # 総資産
        self.debt_sum = debt_sum                                        # 負債合計
        self.minority_interests = minority_interests                    # 少数株主持分
        self.share_option = share_option                                # 新株予約権
        self.current_net_income = current_net_income                    # 当期純利益
        self.s_term_loans_receivable = short_term_loans_receivable      # 短期貸付金
        self.investment_and_other = investment_and_other                # 投資その他資産
        self.const_in_pro_acc = construction_in_progress_accounts       # 建設仮勘定(未使用資産)

    # 自己資本
    def equity_capital(self):
        return self.total_assets - self.debt_sum - self.minority_interests - self.share_option

    # ROE 自己資本当期利益率
    def roe(self):
        return self.current_net_income / (self.total_assets - self.debt_sum -
                                          self.minority_interests - self.share_option) * 100

    # ROA 使用総資本事業利益率
    def roa(self):
        return inter_ratio.business_interest() / self.total_assets * 100

    # 経営資本
    def operating_capital(self):
        return self.total_assets - (c_ratio.cash + c_ratio.tra_sec +
                                    self.s_term_loans_receivable + self.investment_and_other)\
                                    - self.const_in_pro_acc

    # return on operating capital 経営資本営業利益率
    def return_on_operating_capital(self):
        return inter_ratio.operating_profit / \
               (self.total_assets - (c_ratio.cash + c_ratio.tra_sec +
                                     self.s_term_loans_receivable + self.investment_and_other)
                - self.const_in_pro_acc) * 100


r1 = input("総資産（資産の合計額）を入れてください：")
r1 = int(r1)

r2 = input("負債の合計額を入れてください：")
r2 = int(r2)

r3 = input("少数株主持分の数字を入れてください：")
r3 = int(r3)

r4 = input("新株予約権の数字を入れてください")
r4 = int(r4)

r5 = input("当期純利益を入れてください")
r5 = int(r5)

r6 = input("短期貸付金を入れてください")
r6 = int(r6)

r7 = input("投資その他資産の金額を入れてください。\n"
           "（おそらく流動資産合計の少し下にあります）：")
r7 = int(r7)

r8 = input("建設仮勘定の金額を入れてください")
r8 = int(r8)

ana_pro = AnalysisProfitability(r1, r2, r3, r4, r5, r6, r7, r8)

print(ana_pro.roe())
print(ana_pro.roa())
print(ana_pro.return_on_operating_capital())


















