# Observerパターン
# 第二章

# パターンの定義：
# オブジェクト間の１対多の依存関係を定義し、あるオブジェクトの状態が変化すると
# それに依存しているすべてのオブジェクトが自動的に通知され更新されるようにする

# 注釈：
# なし


# インタフェース
class Subject:
    def registerObserver(self):
        raise NotImplementedError
    
    
    def removeObserver(self):
        raise NotImplementedError


    def notifyOvservers(self):
        raise NotImplementedError


class Observer:
    def update(self, temperature, humidity, pressure):
        raise NotImplementedError 


class DisplayElement:
    def display(self):
        raise NotImplementedError 


# 実装
class WeatherData(Subject):
    def __init__(self):
        self.observer = []


    def registerObserver(self, o):
        self.observer.append(o)


    def removeObserver(self, o):
        self.observer.remove(o)


    def notifyOvservers(self):
        for o in self.observer:
            o.update(self.temperature, self.humidity, self.pressure)


    def measurementsChanged(self):
        self.notifyOvservers()


    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        self.weatherData = weatherData
        weatherData.registerObserver(self)
    

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()


    def display(self):
        messege = '現在の気象状況：温度%s度　湿度%s％' % (self.temperature, self.humidity)
        print(messege)


if __name__ == "__main__":
    weatherdata = WeatherData()
    currentconditionsdisplay = CurrentConditionsDisplay(weatherdata)
    weatherdata.setMeasurements(27, 65, 30.4)
    weatherdata.setMeasurements(28, 70, 29.2)
    weatherdata.setMeasurements(26, 90, 29.2)

