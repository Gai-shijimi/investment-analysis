# 成長性の分析


# 幾何平均
class GeometricMean:
    def __init__(self, y, current_v, base_v):
        self.year = y
        self.current_values = current_v
        self.base_values = base_v

    # 幾何平均成長率
    def geometric_mean_growth_ratio(self):
        return ((self.current_values / self.base_values) ** (1 / self.year) - 1) * 100


year1 = int(input("調べたい年度を入れてください："))
year2 = int(input("どこの年から調べたいか、ベースとなる年度を入れてください："))
year = int(year1 - year2 + 1)

current_values = input("調べたい年度の、調べたい項目の数字を入れてください：")
current_values = int(current_values)

base_values = input("ベースとなる年度の、一つ前で入力した同じ項目の数字を入れてください：")
base_values = int(base_values)

geometric_mean = GeometricMean(year, current_values, base_values)
print(geometric_mean.geometric_mean_growth_ratio())



