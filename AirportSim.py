from AirportEvent import *
from Event import *
from Airport import *
from Airplane import *
import Simulator


# def main():
#
#     landing_event = AirportEvent(AirportSim.plane1, 5, AirportSim.lax, AirportEvent.PLANE_ARRIVES, 3)
#     Simulator.schedule(landing_event)
#
#     landing_event_2 = AirportEvent(AirportSim.plane2, 5, AirportSim.lax, AirportEvent.PLANE_ARRIVES, 3)
#     Simulator.schedule(landing_event_2)
#
#     landing_event_3 = AirportEvent(AirportSim.plane3, 5, AirportSim.lax, AirportEvent.PLANE_ARRIVES, 3)
#     Simulator.schedule(landing_event_3)
#
#     landing_event_4 = AirportEvent(AirportSim.plane4, 5, AirportSim.lax, AirportEvent.PLANE_ARRIVES, 3)
#     Simulator.schedule(landing_event_4)
#
#     landing_event_5 = AirportEvent(AirportSim.plane5, 5, AirportSim.lax, AirportEvent.PLANE_ARRIVES, 3)
#     Simulator.schedule(landing_event_5)
#
#     Simulator.stop_at(1000)
#     Simulator.run()
#
#     print("Airport LAX traveling gas consumed: " + AirportSim.lax.gas_consumed_traveling)
#     print("Airport LAX circuling gas consumed: " + AirportSim.lax.gas_consumed_circulating)
#
#     print("Airport ATL traveling gas consumed: " + AirportSim.atl.gas_consumed_traveling)
#     print("Airport ATL circuling gas consumed: " + AirportSim.atl.gas_consumed_circulating)
#
#     print("Airport NYC traveling gas consumed: " + AirportSim.nyc.gas_consumed_traveling)
#     print("Airport NYC circuling gas consumed: " + AirportSim.nyc.gas_consumed_circulating)
#
#     print("Airport IAN traveling gas consumed: " + AirportSim.iah.gas_consumed_traveling)
#     print("Airport IAN circuling gas consumed: " + AirportSim.iah.gas_consumed_circulating)
#
#     print("Airport CHI traveling gas consumed: " + AirportSim.chi.gas_consumed_traveling)
#     print("Airport CHI circuling gas consumed: " + AirportSim.chi.gas_consumed_circulating)
#
#     print("Airport LAX arriving passengers: " + AirportSim.lax.m_arriving_passengers())
#     print("Airport LAX departing passengers: " + AirportSim.lax.m_departing_passengers())
#     print("Airport LAX total circling time: " + AirportSim.lax.m_circling_time())
#
#     print("Airport ATL arriving passengers: " + AirportSim.atl.m_arriving_passengers())
#     print("Airport ATL departing passengers: " + AirportSim.atl.m_departing_passengers())
#     print("Airport ATL total circling time: " + AirportSim.atl.m_circling_time())
#
#     print("Airport NYC arriving passengers: " + AirportSim.nyc.m_arriving_passengers())
#     print("Airport NYC departing passengers: " + AirportSim.nyc.m_departing_passengers())
#     print("Airport NYC total circling time: " + AirportSim.nyc.m_circling_time())
#
#     print("Airport IAH arriving passengers: " + AirportSim.iah.m_arriving_passengers())
#     print("Airport IAH departing passengers: " + AirportSim.iah.m_departing_passengers())
#     print("Airport IAH total circling time: " + AirportSim.iah.m_circling_time())
#
#     print("Airport CHI arriving passengers: " + AirportSim.chi.m_arriving_passengers())
#     print("Airport CHI departing passengers: " + AirportSim.chi.m_departing_passengers())
#     print("Airport CHI total circling time: " + AirportSim.chi.m_circling_time())
#
#     total_sum = AirportSim.lax.m_arriving_passengers() + AirportSim.atl.m_arriving_passengers() + AirportSim.nyc.m_arriving_passengers() + AirportSim.iah.m_arriving_passengers() + AirportSim.chi.m_arriving_passengers()
#     print("Total passenger number: " + total_sum)
#
#
# class AirportSim(object):
#     lax = Airport("LAX", 0.5, 2, 0.3)
#     atl = Airport("ATL", 0.5, 2, 0.3)
#     nyc = Airport("NYC", 0.5, 2, 0.3)
#     iah = Airport("IAH", 0.5, 2, 0.3)
#     chi = Airport("CHI", 0.5, 2, 0.3)
#
#     plane1 = Airplane("plane1", 506, 640, 1000, 2, 1)
#     plane2 = Airplane("plane2", 147, 583, 1000, 2, 1)
#     plane3 = Airplane("plane3", 314, 562, 1000, 2, 1)
#     plane4 = Airplane("plane4", 277, 541, 1000, 2, 1)
#     plane5 = Airplane("plane5", 290, 567, 1000, 2, 1)
#     plane6 = Airplane("plane6", 506, 640, 1000, 2, 1)
#     plane7 = Airplane("plane7", 147, 583, 1000, 2, 1)
#     plane8 = Airplane("plane8", 314, 562, 1000, 2, 1)
#     plane9 = Airplane("plane9", 277, 541, 1000, 2, 1)
#     plane10 = Airplane("plane10", 290, 567, 1000, 2, 1)
#
#     airplanes = [plane1, plane2, plane3, plane4, plane5, plane6, plane7, plane8, plane9, plane10]
#     airports = [lax, atl, nyc, iah, chi]


# def main():
#     lax = Airport("LAX", 0.5, 2, 0.3)
#     atl = Airport("ATL", 0.5, 2, 0.3)
#     nyc = Airport("NYC", 0.5, 2, 0.3)
#     iah = Airport("IAH", 0.5, 2, 0.3)
#     chi = Airport("CHI", 0.5, 2, 0.3)
#
#     plane1 = Airplane("plane1", 506, 640, 1000, 2, 1)
#     plane2 = Airplane("plane2", 147, 583, 1000, 2, 1)
#     plane3 = Airplane("plane3", 314, 562, 1000, 2, 1)
#     plane4 = Airplane("plane4", 277, 541, 1000, 2, 1)
#     plane5 = Airplane("plane5", 290, 567, 1000, 2, 1)
#     plane6 = Airplane("plane6", 506, 640, 1000, 2, 1)
#     plane7 = Airplane("plane7", 147, 583, 1000, 2, 1)
#     plane8 = Airplane("plane8", 314, 562, 1000, 2, 1)
#     plane9 = Airplane("plane9", 277, 541, 1000, 2, 1)
#     plane10 = Airplane("plane10", 290, 567, 1000, 2, 1)
#
#     airplanes = [plane1, plane2, plane3, plane4, plane5, plane6, plane7, plane8, plane9, plane10]
#     airports = [lax, atl, nyc, iah, chi]
#
#     landing_event = AirportEvent(plane1, 5, lax, AirportEvent.PLANE_ARRIVES, 3)
#     Simulator.schedule(landing_event)
#
#     landing_event_2 = AirportEvent(plane2, 5, lax, AirportEvent.PLANE_ARRIVES, 3)
#     Simulator.schedule(landing_event_2)
#
#     landing_event_3 = AirportEvent(plane3, 5, lax, AirportEvent.PLANE_ARRIVES, 3)
#     Simulator.schedule(landing_event_3)
#
#     landing_event_4 = AirportEvent(plane4, 5, lax, AirportEvent.PLANE_ARRIVES, 3)
#     Simulator.schedule(landing_event_4)
#
#     landing_event_5 = AirportEvent(plane5, 5, lax, AirportEvent.PLANE_ARRIVES, 3)
#     Simulator.schedule(landing_event_5)
#
#     Simulator.stop_at(1000)
#     Simulator.run()
#
#     print("Airport LAX traveling gas consumed: " + lax.gas_consumed_traveling)
#     print("Airport LAX circuling gas consumed: " + lax.gas_consumed_circulating)
#
#     print("Airport ATL traveling gas consumed: " + atl.gas_consumed_traveling)
#     print("Airport ATL circuling gas consumed: " + atl.gas_consumed_circulating)
#
#     print("Airport NYC traveling gas consumed: " + nyc.gas_consumed_traveling)
#     print("Airport NYC circuling gas consumed: " + nyc.gas_consumed_circulating)
#
#     print("Airport IAN traveling gas consumed: " + iah.gas_consumed_traveling)
#     print("Airport IAN circuling gas consumed: " + iah.gas_consumed_circulating)
#
#     print("Airport CHI traveling gas consumed: " + chi.gas_consumed_traveling)
#     print("Airport CHI circuling gas consumed: " + chi.gas_consumed_circulating)
#
#     print("Airport LAX arriving passengers: " + lax.m_arriving_passengers())
#     print("Airport LAX departing passengers: " + lax.m_departing_passengers())
#     print("Airport LAX total circling time: " + lax.m_circling_time())
#
#     print("Airport ATL arriving passengers: " + atl.m_arriving_passengers())
#     print("Airport ATL departing passengers: " + atl.m_departing_passengers())
#     print("Airport ATL total circling time: " + atl.m_circling_time())
#
#     print("Airport NYC arriving passengers: " + nyc.m_arriving_passengers())
#     print("Airport NYC departing passengers: " + nyc.m_departing_passengers())
#     print("Airport NYC total circling time: " + nyc.m_circling_time())
#
#     print("Airport IAH arriving passengers: " + iah.m_arriving_passengers())
#     print("Airport IAH departing passengers: " + iah.m_departing_passengers())
#     print("Airport IAH total circling time: " + iah.m_circling_time())
#
#     print("Airport CHI arriving passengers: " + chi.m_arriving_passengers())
#     print("Airport CHI departing passengers: " + chi.m_departing_passengers())
#     print("Airport CHI total circling time: " + chi.m_circling_time())
#
#     total_sum = lax.m_arriving_passengers() + atl.m_arriving_passengers() + nyc.m_arriving_passengers() + iah.m_arriving_passengers() + chi.m_arriving_passengers()
#     print("Total passenger number: " + total_sum)


# if __name__ == '__main__':
#    main()

def main():
    lax = Airport("LAX", 0.5, 2, 0.3)
    print(lax.m_airport_name)

