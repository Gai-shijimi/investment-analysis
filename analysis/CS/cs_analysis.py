# キャッシュフローのパターンだけ


class CashFlow:
    def __init__(self, cf_business_activities, cf_investing_activities, cf_financing_activities):
        self.cf_business_activities = cf_business_activities        # 営業活動によるキャッシュフロー
        self.cf_investing_activities = cf_investing_activities      # 投資活動によるキャッシュフロー
        self.cf_financing_activities = cf_financing_activities      # 財務活動によるキャッシュフロー

    def pattern(self):
        if self.cf_business_activities < 0 and self.cf_investing_activities < 0 and self.cf_financing_activities > 0:
            print("新興企業です")

        elif self.cf_business_activities > 0 and self.cf_investing_activities < 0 and self.cf_financing_activities > 0:
            print("発展企業です")

        elif self.cf_business_activities > 0 and self.cf_investing_activities < 0 and self.cf_financing_activities < 0:
            print("発展企業です")

        elif self.cf_business_activities > 0 and self.cf_investing_activities > 0 and self.cf_financing_activities < 0:
            print("熟成期にある企業です")

        elif self.cf_business_activities < 0 and self.cf_investing_activities > 0 and self.cf_financing_activities > 0:
            print("衰退期にある企業です")

        elif self.cf_business_activities < 0 and self.cf_investing_activities < 0 and self.cf_financing_activities < 0:
            print("衰退期にある企業です")

        else:
            print("どこにも当てはまりません")


response1 = input("営業活動によるキャッシュフローの合計額を入れてください：")
response1 = int(response1)

response2 = input("投資活動によるキャッシュフローの合計額を入れてください：")
response2 = int(response2)

response3 = input("財務活動によるキャッシュフローの合計額を入れてください：")
response3 = int(response3)

cash_flow = CashFlow(response1, response2, response3)
print(cash_flow.pattern())c
