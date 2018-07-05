# Factory Methodパターン
# 第四章

# パターンの定義：
# オブジェクト作成のためのインタフェースを定義する。
# どのクラスをインスタンス化するかはサブクラスに決定させる。

# 注釈：
# なし


# ピザStoreクラス
class PizzaStore:
    def createPizza(self, type):
        raise NotImplementedError


    def orderPizza(self, type):
        pizza = self.createPizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYStylePizzaStore(PizzaStore):
    def createPizza(self, type):
        if type == "チーズ":
            return NYStylePizza()
        elif type == "野菜":
            # チーズ以外のFactory部分は割愛
            #return NYStyleVeggiePizza()
            pass
        else:
            pass


# ピザクラス
class Pizza:
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []


    def prepare(self):
        print("%sを下処理 %s" % (self.name, self.name))
        print("生地をこねる.....")
        print("ソースを追加.....")
        print("トッピングを追加：")
        for topping in self.toppings:
            print(topping)
        

    def bake(self):
        print("350度で2分間焼く")

    
    def cut(self):
        print("ピザを扇状に切り分ける")

    
    def box(self):
        print("PizzaStoreの正式な箱にピザを入れる")


class NYStylePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NYスタイルのソース＆チーズピザ"
        self.dough = "薄いクラスト生地"
        self.sauce = "マリナラソース"
        self.toppings.append("粉レッジャーノチーズ")


if __name__ == "__main__":
    nypizzastore = NYStylePizzaStore()
    nypizzastore.orderPizza("チーズ")


