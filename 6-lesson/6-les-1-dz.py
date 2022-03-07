import time

class TrafficLight:
    __color = str

    def timer(self, sec):
        for i in range(sec, 0, -1):
            print(i)
            time.sleep(1)
            print("\n " * 10)

    def running(self):
        for i in range(2):
            TrafficLight.__color = 'red'
            print(f'{TrafficLight.__color}')
            TrafficLight.timer(self, 7)

            TrafficLight.__color = 'yellow'
            print(f'{TrafficLight.__color}')
            TrafficLight.timer(self, 2)
            
            TrafficLight.__color = 'green'
            print(f'{TrafficLight.__color}')
            TrafficLight.timer(self, 2)


svetofor = TrafficLight()
svetofor.running()
