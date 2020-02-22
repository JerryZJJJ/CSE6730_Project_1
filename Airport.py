import EventHandler
from AirportEvent import *
import Simulator
import queue
import random


class Airport(EventHandler):

    def __init__(self, name, runway_time_to_land, required_time_on_ground, runway_time_to_takeoff):
        self.m_in_the_air = 0
        self.m_on_the_ground = 0
        self.m_land_1, self.m_land_2, self.m_takeoff_1 = True, True, True
        self.weather = True
        self.weather_array = [False, False, False, False, False, True, False, True, False, False]
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
        if airport_1 is "LAX":
            a_1 = 0
        elif airport_1 is "ATL":
            a_1 = 1
        elif airport_1 is "NYC":
            a_1 = 2
        elif airport_1 is "IAH":
            a_1 = 3
        elif airport_1 is "CHI":
            a_1 = 4

        if airport_2 is "LAX":
            a_2 = 0
        elif airport_2 is "ATL":
            a_2 = 1
        elif airport_2 is "NYC":
            a_2 = 2
        elif airport_2 is "IAH":
            a_2 = 3
        elif airport_2 is "CHI":
            a_2 = 4

        matrix = [
            [0, 1946, 2451, 1379, 1745],  # LAX
            [1946, 0, 746, 689, 588],  # ATL
            [2451, 746, 0, 1416, 713],  # NYC
            [1379, 689, 1416, 0, 925],  # IAH
            [1745, 588, 713, 925, 0]  # CHI
        ]

        return matrix[a_1][a_2]

    # def handle(self, event):    # event = air event
    #     if event.m_event_type is AirportEvent.PLANE_ARRIVES:
    #         self.m_in_the_air += 1
    #         event.m_arriving_time = Simulator.get_current_time()
    #         print(Simulator.get_current_time() + ": " + event.m_plane.m_name + " arrived at " + self.m_airport_name)
    #         if (Simulator.get_current_time() - self.old_weather_time) >= self.duration:
    #             rnd = random.randint(len(self.weather_array))
    #             self.weather = self.weather_array[rnd]
    #             self.duration = 10 - (Simulator.get_current_time() - (self.old_weather_time + self.duration)) % 10
    #             self.old_weather_time = Simulator.get_current_time()
    #         if not self.weather:
    #             temp = AirportEvent(event.m_plane, 1, self, AirportEvent.PLANE_ARRIVES, 3)
    #             Simulator.schedule(temp)
    #         else:
    #             self.arriving_queue.put(event)
    #             if self.m_land_1:
    #                 self.m_land_1 = False
    #                 first_arriving_event_1 = self.arriving_queue.get()  # airport Event
    #                 print(Simulator.get_current_time() + ": " + event.m_plane.m_name + " start landing at the first landing runway of " + self.m_airport_name)
    #                 first_arriving_event_1.m_arrived_time = Simulator.get_current_time()
    #                 self.m_circling_time += first_arriving_event_1.get_wait_time()
    #
    #                 self.m_arriving_passengers += first_arriving_event_1.m_plane.m_number_passengers
    #
    #                 landed_event_1 = AirportEvent(first_arriving_event_1.m_plane, self.m_runway_time_to_land, self, AirportEvent.PLANE_LANDED, 0)
    #                 Simulator.schedule(landed_event_1)
    #
    #             elif self.m_land_2:
    #                 self.m_land_2 = False
    #                 first_arriving_event_2 = self.arriving_queue.get()  # airport Event
    #                 print(Simulator.get_current_time() + ": " + event.m_plane.m_name + " start landing at the first landing runway of " + self.m_airport_name)
    #                 first_arriving_event_2.m_arrived_time = Simulator.get_current_time()
    #                 self.m_circling_time += first_arriving_event_2.get_wait_time()
    #
    #                 self.m_arriving_passengers += first_arriving_event_2.m_plane.m_number_passengers
    #
    #                 landed_event_2 = AirportEvent(first_arriving_event_2.m_plane, self.m_runway_time_to_land, self, AirportEvent.PLANE_LANDED, 0)
    #                 Simulator.schedule(landed_event_2)
    #
    #     if event.m_event_type is AirportEvent.PLANE_TAKEOFF:
    #         if (Simulator.get_current_time() - self.old_weather_time) >= self.duration:
    #             rnd = random.randint(len(self.weather_array))
    #             self.weather = self.weather_array[rnd]
    #             self.duration = 10 - (Simulator.get_current_time() - (self.old_weather_time + self.duration)) % 10
    #             self.old_weather_time = Simulator.get_current_time()
    #         if not self.weather:
    #             temp = AirportEvent(event.m_plane, 1, self, AirportEvent.PLANE_DEPARTS, 3)
    #             Simulator.schedule(temp)
    #         else:
    #             self.departure_queue.put(event)
    #             if self.m_takeoff_1:
    #                 self.m_takeoff_1 = False
    #                 first_departure_event = self.departure_queue.get()
    #                 print(Simulator.get_current_time() + ": " + first_departure_event.m_plane.m_name + " takeoff from the first takeoff runway of" + self.m_airport_name)
    #                 takeoff_event = AirportEvent(first_departure_event.m_plane, self.m_runway_time_to_take_off, self, AirportEvent.PLANE_DEPARTS, 2)
    #                 Simulator.schedule(takeoff_event)
    #
    #     if event.m_event_type is AirportEvent.PLANE_DEPARTS:
    #         self.m_on_the_ground -= 1
    #         print(Simulator.get_current_time() + ": " + event.m_plane.m_name + " departs from " + self.m_airport_name)
    #         event.m_plane.set_number_passengers()
    #         self.m_departing_passengers += event.m_plane.m_number_passengers
    #         airport_1 = self.m_airport_name
    #         index = random.randint(len(AirportSim.airports))
    #         while AirportSim.airports[index] is self:
    #             index = random.randint(len(AirportSim.airports))
    #         destination = AirportSim.airports[index]
    #         airport_2 = destination.m_airport_name
    #         distance = Airport.cal_distance(airport_1, airport_2)
    #         speed = event.m_plane.m_speed
    #         self.m_flight_time = distance / speed
    #         temp = event.m_plane
    #
    #         self.gas_consumed_traveling += temp.cal_gas(self.m_flight_time, temp.gas_speed_traveling)
    #
    #         depart_event = AirportEvent(temp, self.m_flight_time, destination, AirportEvent.PLANE_ARRIVES, 3)  # airport event
    #         Simulator.schedule(depart_event)
    #         if self.departure_queue.qsize() is not 0:
    #             first_departure_event = self.departure_queue.get()
    #             print(Simulator.get_current_time() + ": " + first_departure_event.m_plane.m_name + " takeoff from the first takeoff runway of " + self.m_airport_name())
    #             takeoff_event = AirportEvent(first_departure_event.m_plane, self.m_runway_time_to_take_off, self, AirportEvent.PLANE_DEPARTS, 2)
    #             Simulator.schedule(takeoff_event)
    #         else:
    #             self.m_takeoff_1 = True
    #
    #     if event.m_event_type is AirportEvent.PLANE_LANDED:
    #         self.m_in_the_air -= 1
    #         self.m_on_the_ground += 1
    #         print(Simulator.get_current_time() + ": " + event.m_plane.m_name + " lands at " + self.m_airport_name)
    #         departure_event = AirportEvent(event.m_plane, self.m_required_time_on_ground, self, AirportEvent.PLANE_TAKEOFF, 2)
    #         Simulator.schedule(departure_event)
    #         runway = event.m_runway
    #         if runway == 0:
    #             self.m_land_1 = True
    #         if runway == 1:
    #             self.m_land_2 = True
    #         if self.arriving_queue.qsize() != 0:
    #             if self.m_land_1:
    #                 self.m_land_1 = False
    #                 first_arriving_event_1 = self.arriving_queue.get()
    #                 print(Simulator.get_current_time() + ": " + first_arriving_event_1.m_plane.m_name + " start landing at the first landing runway of " + self.m_airport_name)
    #                 first_arriving_event_1.m_arrived_time = Simulator.get_current_time()
    #                 self.m_circling_time += first_arriving_event_1.get_wait_time()
    #
    #                 temp_1 = event.m_plane()
    #
    #                 self.gas_consumed_circulating += temp_1.cal_gas(first_arriving_event_1.get_wait_time(), temp_1.gas_speed_circulating)
    #
    #                 print("airport" + self.m_airport_name + "circulating time1" + self.m_circling_time)
    #                 print("airport" + self.m_airport_name + "circulating gas consume" + self.gas_consumed_circulating);
    #
    #                 self.m_arriving_passengers += first_arriving_event_1.m_plane.m_number_passengers
    #
    #                 landed_event_1 = AirportEvent(first_arriving_event_1.m_plane, self.m_runway_time_to_land, self, AirportEvent.PLANE_LANDED, 0)
    #                 Simulator.schedule(landed_event_1)
    #             elif self.m_land_2:
    #                 self.m_land_2 = False
    #                 first_arriving_event_2 = self.arriving_queue.get()
    #                 print(Simulator.get_current_time() + ": " + first_arriving_event_2.m_plane.m_name + " start landing at the first landing runway of " + self.m_airport_name)
    #                 first_arriving_event_2.m_arrived_time = Simulator.get_current_time()
    #                 self.m_circling_time += first_arriving_event_2.get_wait_time()
    #
    #                 temp_2 = event.m_plane()
    #
    #                 self.gas_consumed_circulating += temp_2.cal_gas(first_arriving_event_2.get_wait_time(), temp_2.gas_speed_circulating)
    #
    #                 print("airport" + self.m_airport_name + "circulating time2" + self.m_circling_time)
    #                 print("airport" + self.m_airport_name + "circulating gas consume" + self.gas_consumed_circulating)
    #
    #                 self.m_arriving_passengers += first_arriving_event_2.m_plane.m_number_passengers
    #
    #                 landed_event_2 = AirportEvent(first_arriving_event_2.m_plane, self.m_runway_time_to_land, self,
    #                                               AirportEvent.PLANE_LANDED, 1)
    #                 Simulator.schedule(landed_event_2)
