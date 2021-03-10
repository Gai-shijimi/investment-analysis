from analysis.profitability.analysis_profitability import ana_pro
from analysis.PL.new_pl_phase_margin import phase_margin
from analysis.BS.new_bs_analysis import c_ratio

# ２分解と３分解

# 売上高当期利益率は phase_margin.net_profit_margin で取得できる

# 投下資本回転率は 売上高 / 総資本(= 総資産) ==  phase_margin.sales / ana_pro.total_assets

# 財務レバレッジ 総資本(= 総資産) / 純資産(総資産 - 負債) == ana_pro.total_assets / c_ratio.net_assets

net_profit_margin = phase_margin.net_profit_margin()                # new_pl_phase_margin

rate_of_rotation = phase_margin.sales / ana_pro.total_assets        # new_pl_phase_margin / analysis_profitability

leverage = ana_pro.total_assets / c_ratio.net_assets                # analysis_profitability / new_bs_analysis

print(net_profit_margin)
print(rate_of_rotation)
print(leverage)



