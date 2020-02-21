from EventHandler import *
import queue


class Airport(EventHandler):

    def __init__(self, name, runway_time_to_land, required_time_on_ground, runway_time_to_takeoff):
        self.m_in_the_air = 0
        self.m_on_the_ground = 0
        self.m_land_1, m_land_2, m_takeoff_1 = True, True, True
        self.weather = True
        self.weatherArray = [False, False, False, False, False, True, False, True, False, False]
        self.duration = 10.0
        self.old_weather_time = 0.0
        self.m_flight_time = 0
        self.m_runway_time_to_land = runway_time_to_land
        self.m_required_time_on_ground = required_time_on_ground
        self.m_runway_time_to_take_off = runway_time_to_takeoff
        self.gas_consumed_traveling = 0
        self.gas_consumed_circulating = 0
        self.m_airport_name = name
        self.m_arriving_passengers = 0
        self.m_departing_passengers = 0
        self.m_circling_time = 0

        self.arriving_queue = queue.PriorityQueue()
        self.departure_queue = queue.PriorityQueue()

    @staticmethod
    def cal_distance(airport_1, airport_2):
        a_1 = a_2 = 0
        if airport_1.m_airport_name is "LAX":
            a_1 = 0
        elif airport_1.m_airport_name is "ATL":
            a_1 = 1
        elif airport_1.m_airport_name is "NYC":
            a_1 = 2
        elif airport_1.m_airport_name is "IAH":
            a_1 = 3
        elif airport_1.m_airport_name is "CHI":
            a_1 = 4

        if airport_2.m_airport_name is "LAX":
            a_2 = 0
        elif airport_2.m_airport_name is "ATL":
            a_2 = 1
        elif airport_2.m_airport_name is "NYC":
            a_2 = 2
        elif airport_2.m_airport_name is "IAH":
            a_2 = 3
        elif airport_2.m_airport_name is "CHI":
            a_2 = 4

        matrix = [
            [0, 1946, 2451, 1379, 1745],  # LAX
            [1946, 0, 746, 689, 588],  # ATL
            [2451, 746, 0, 1416, 713],  # NYC
            [1379, 689, 1416, 0, 925],  # IAH
            [1745, 588, 713, 925, 0]  # CHI
        ]

        return matrix[a_1][a_2]
