# 投下資本回転率とその分解

from analysis.BS.new_bs_analysis import c_ratio
from analysis.PL.new_pl_phase_margin import phase_margin


# 使用総資本回転率
def turnover_ratio_of_total_liabilities():
    return phase_margin.sales / c_ratio.total_assets


# 営業債権(売上債権)回転率
def turnover_rate_of_receivables():
    return phase_margin.sales / c_ratio.t_n_a_r


# 棚卸資産回転率
def turnover_rate_of_inventory():
    return phase_margin.sales / c_ratio.inventory_assets


# 有形固定資産回転率
def turnover_rate_of_tangible_fixed_assets():
    return phase_margin.sales / c_ratio.tangible_fixed_assets


# 営業債権回転日数
def date_of_turnover_rate_of_receivables():
    return c_ratio.t_n_a_r / phase_margin.sales * 365


# 棚卸資産回転日数
def date_of_turnover_rate_of_inventory():
    return c_ratio.inventory_assets / phase_margin.sales * 365


# 営業プロセス
def date_of_process_of_operating():
    return (c_ratio.t_n_a_r + c_ratio.inventory_assets) / phase_margin.sales * 365


# CCC, キャッシュコンバージョンサイクル
def cash_conversion_cycle():
    return c_ratio.working_capital() / phase_margin.sales * 365


print("使用総資本回転率は、", turnover_ratio_of_total_liabilities())
print("営業債権（売上債権回転率）は、", turnover_rate_of_receivables())
print("棚卸資産回転率は、", turnover_rate_of_inventory())
print("有形固定資産回転率は、", turnover_rate_of_tangible_fixed_assets())
print("営業プロセスは", date_of_process_of_operating())
print("キャッシュコンバージョンサイクルは", cash_conversion_cycle())





