# PLの趨勢比の基本分析

print("趨勢比とは、過去の項目(例：2015年の売上高)から現在(例：2020年の売上高)の項目の伸び率を見るものです。\n"
      "企業のPLの時系列的な変化を観察することができます")


class TrendRatio:
    def __init__(self, past_item, current_item):
        self.past_item = past_item
        self.current_item = current_item

    def trend_ratio(self):
        return (self.current_item / self.past_item - 1) * 100


n1 = input("過去(例：2015年)の何か項目(例：売上高)の金額を入れてください：")
n1 = int(n1)

n2 = input("現在(例：2020)の上記と同じ項目(例：売上高)の金額を入れてください：")
n2 = int(n2)

trend_ratio = TrendRatio(n1, n2)

print("伸び率は", trend_ratio.trend_ratio(), "%です。マイナスの場合は何か原因があるはずです。")







