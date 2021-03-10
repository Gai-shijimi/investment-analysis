from analysis.other.other_formulas import other_formulas


class TheoreticalValue:
    def __init__(self, div, stock_price, past_stock_price, net_income_of_parents, shareholder_equity,
                 net_operating_profit_after_tax,):
        self.div = div                                      # 配当金
        self.stock_price = stock_price                      # 現在の株価
        self.past_stock_price = past_stock_price            # 基準となる株価
        self.net_income_of_parent = net_income_of_parents   # 親会社株主に帰属する当期純利益
        self.shareholder_equity = shareholder_equity        # 株主資本

    # 投資収益率
    def ret_r(self):
        return (self.div + self.stock_price - self.past_stock_price) / self.past_stock_price

    # DDM(割引配当モデル), (配当額一定, 割引率一定, ゼロ成長の場合),
    # 企業の株価がわかる
    # しかし、残余利益モデルを使った方が良い！
    def dividend_discount_model(self):
        return self.div / (self.div + self.stock_price - self.past_stock_price) / self.past_stock_price

    # RIM(残余利益モデル) DDMの配当の部分を会計情報にしたバージョン
    def residual_income_model(self):  # 親会社株主に帰属する当期純利益 - 期待利益 (= 株主資本コスト * 株主資本簿価)
        return self.shareholder_equity + \
               (self.net_income_of_parent - (other_formulas.capm_ri() * self.shareholder_equity)) /\
               other_formulas.capm_ri()

    # EVA 経済的付加価値

    # 株価収益率
    def price_earning_ratio(self):
        return 1 / other_formulas.capm_ri()

    # 時価簿価比率

    # Ohlson modelの線形情報モデル


div = int(input("配当金を入れてください："))
stock_price = int(input("現在の株価を入れてください："))
past_stock_price = int(input("基準となる株価を入れてください。（過去の株価です）："))
net_income_of_parents = int(input("親会社に帰属する当期純利益の額を入れてください："))
shareholder_equity = int(input("当社株主に帰属する資本合計の額を入れてください："))

theoretical_values = TheoreticalValue(div, stock_price, past_stock_price, net_income_of_parents, shareholder_equity)

print(theoretical_values.ret_r())
print(theoretical_values.dividend_discount_model())
print(theoretical_values.residual_income_model())
print(theoretical_values.price_earning_ratio())






