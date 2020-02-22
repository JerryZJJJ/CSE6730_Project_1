import random


class Airplane(object):

    def __init__(self, name, max_passenger, speed, volume, gas_speed_1, gas_speed_2):
        self.m_name = name
        self.m_speed = speed
        self.m_max_passengers = max_passenger
        self.gas_volume = volume
        self.gas_consumed = 0
        self.gas_speed_traveling = gas_speed_1
        self.gas_speed_circulating = gas_speed_2
        self.m_number_passengers = random.randint(0, self.m_max_passengers)

    def set_number_passengers(self):
        self.m_number_passengers = random.randint(0, self.m_max_passengers)

    def cal_gas(self, duration, speed):
        self.gas_consumed = duration * speed
        return self.gas_consumed
