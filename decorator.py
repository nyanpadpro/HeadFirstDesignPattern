# Decoratorパターン
# 第三章

# パターンの定義：
# オブジェクトに付加的な責務を動的に付与する。
# サブクラス化の代替となる、柔軟な機能拡張手段を提供する。

# 注釈：
# なし


# 抽象クラス、インタフェース
class Beverage:
    def __init__(self):
        self.description = '不明な飲み物'


    def getDescription(self):
        return self.description


    def cost(self):
        raise NotImplementedError


class CondimentDecorator(Beverage):
    def getDescription(self):
        raise NotImplementedError


# 実装
class Espresso(Beverage):
    def __init__(self):
        self.description = 'エスプレッソ'

    
    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        self.description = 'ハウスブレンドコーヒー'

    
    def cost(self):
        return .89


# ↓デコレータ
class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage


    def getDescription(self):
        return self.beverage.getDescription() + '、モカ'


    def cost(self):
        return .20 + self.beverage.cost()


if __name__ == "__main__":
    beverage = Espresso()
    messege = "%s $%s" % (beverage.getDescription(), beverage.cost())
    print(messege)

    beverage2 = HouseBlend()
    beverage2 = Mocha(beverage2)    # デコレータMochaでラップ
    beverage2 = Mocha(beverage2)    # デコレータMochaでもういちどラップ
    messege = "%s $%s" % (beverage2.getDescription(), beverage2.cost())
    print(messege)