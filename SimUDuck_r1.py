# 第一章 最初のSimUDuckアプリケーション
class Duck:
    # 鴨に関するメソッド
    def quack(self):
        pass


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
    duck = Duck()
    mallardduck = MallardDuck()
    redheadduck = RedheadDuck()
    rubberduck = RubberDuck()

    duck.display()
    mallardduck.display()
    redheadduck.display()
    rubberduck.display()
