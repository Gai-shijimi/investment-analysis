from analysis.CS.cs_analysis import cash_flow

# 複利計算, 現在価値の計算, リスク調整済現在価値


class OtherFormulas:
    def __init__(self, interest_rate, duration, pv, fv, risk_f_rate, beta, past_topix_return):
        self.interest_rate = interest_rate          # 利率
        self.duration = duration                    # 経過年数
        self.pv = pv                                # 現在の金額
        self.fv = fv                                # N年後の金額
        self.risk_f_rate = risk_f_rate              # 長期国債利回り10年, 簡単に調べられる
        self.beta = beta                            # 個別企業の市場リスクに対する感応度
        self.past_topix_return = past_topix_return  # マーケットポートフォリオの利回り、つまりTOPIXリターン

    # 複利計算
    def compound_interest_of_future_values(self):
        return ((1 + self.interest_rate) ** self.duration) * self.pv

    # 現在価値の計算
    def present_values(self):
        return ((1 + self.interest_rate) ** self.duration) * self.pv / (1 + self.interest_rate) ** self.duration

    # CAPM, 株主資本コスト
    def capm_ri(self):
        return self.risk_f_rate + self.beta * (self.past_topix_return - self.risk_f_rate)

    # リスクを考慮した現在価値(リスク調整済み割引率)
    def risk_adjusted_present_values(self):
        return (cash_flow.cf_business_activities + cash_flow.cf_investing_activities) /\
               (1 + self.risk_f_rate + self.beta(self.past_topix_return - self.risk_f_rate))


interest_rate = int(input("年利率を入れてください："))

duration1 = int(input("現在の年度を入れてください："))
duration2 = int(input("基準となる年度を入れてください："))
duration = duration1 - duration2 + 1

pv = int(input("現在の株価を入れてください："))

fv = int(input("予想の株価を入れてください："))

risk_f_rate = int(input("長期国債利回り10年の値を入れてください："))

beta = int(input("個別企業の市場リスクに対する感応度を入れてください："))

past_topix_return = int(input("TOPIXリターンを入れてください："))

other_formulas = OtherFormulas(interest_rate, duration, pv, fv, risk_f_rate, beta, past_topix_return)

print(other_formulas.compound_interest_of_future_values())
print(other_formulas.present_values())
print(other_formulas.capm_ri())
print(other_formulas.risk_adjusted_present_values())










