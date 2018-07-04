# Strategyパターン
# 第一章 SimUDuckアプリケーションをインタフェースを使用して実装

# パターンの定義：
# 一連のアルゴリズムを定義し、それぞれをカプセル化し交換可能とする

# 注釈：
# Pythonの場合はインタフェースがないので今回は通常のClassで実装した
# 抽象クラスはABCパッケージで定義可能だがダックタイピングの考え方などによりJavaとは作法が異なる為
# 現実的にはDuckクラスとインタフェースに対する実装があればよい？

# インタフェース
class FlyBehavior():
    def fly(self):
        raise NotImplementedError


class QuackBehavior():
    def quack(self):
        raise NotImplementedError


# インタフェースに対する実装
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("飛んでいます！！")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("飛べません")


class Quack(QuackBehavior):
    def quack(self):
        print("ガーガー")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<<沈黙>>")


class Squack(QuackBehavior):
    def quack(self):
        print("キューキュー")


# Duckクラスは継承で機能を追加で実装しない
class Duck():
    # 鴨に関するメソッド

    flybehavior = FlyWithWings()
    quackbehavior = Quack()

    def __init__(self):
        pass
    

    def setflybehavior(self, flybehavior):
        self.flybehavior = flybehavior


    def setquackbehavior(self, quackbehavior):
        self.quackbehavior = quackbehavior


    def performfly(self):
        self.flybehavior.fly()

    
    def performquake(self):
        self.quackbehavior.quack()


    def swim(self):
        pass


    def display(self):
        pass


class MallardDuck(Duck):
    def display(self):
        # マガモの表示
        pass


class RedheadDuck(Duck):
    def display(self):
        # アメリカホシハジロの表示
        pass


class RubberDuck(Duck):
    def display(self):
        # ゴムの鴨の表示
        pass


if __name__ == "__main__":
    mallardduck = MallardDuck()
    mallardduck.performquake()
    mallardduck.performfly()

    rubberduck = RubberDuck()
    rubberduck.setquackbehavior(Squack())
    rubberduck.setflybehavior(FlyNoWay())
    rubberduck.performquake()
    rubberduck.performfly()

