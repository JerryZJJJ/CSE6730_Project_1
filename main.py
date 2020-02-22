from Airplane import *
from Event import *
from Airport import *


def main():

    landing_event = AirportEvent(AirportSim.plane1, 5, AirportSim.lax, AirportEvent.PLANE_ARRIVES, 3)
    Simulator.schedule(landing_event)

    landing_event_2 = AirportEvent(AirportSim.plane2, 5, AirportSim.lax, AirportEvent.PLANE_ARRIVES, 3)
    Simulator.schedule(landing_event_2)

    landing_event_3 = AirportEvent(AirportSim.plane3, 5, AirportSim.lax, AirportEvent.PLANE_ARRIVES, 3)
    Simulator.schedule(landing_event_3)

    landing_event_4 = AirportEvent(AirportSim.plane4, 5, AirportSim.lax, AirportEvent.PLANE_ARRIVES, 3)
    Simulator.schedule(landing_event_4)

    landing_event_5 = AirportEvent(AirportSim.plane5, 5, AirportSim.lax, AirportEvent.PLANE_ARRIVES, 3)
    Simulator.schedule(landing_event_5)

    Simulator.stop_at(1000)
    Simulator.run()

    print("Airport LAX traveling gas consumed: " + str(AirportSim.lax.gas_consumed_traveling))
    print("Airport LAX circuling gas consumed: " + str(AirportSim.lax.gas_consumed_circulating))

    print("Airport ATL traveling gas consumed: " + str(AirportSim.atl.gas_consumed_traveling))
    print("Airport ATL circuling gas consumed: " + str(AirportSim.atl.gas_consumed_circulating))

    print("Airport NYC traveling gas consumed: " + str(AirportSim.nyc.gas_consumed_traveling))
    print("Airport NYC circuling gas consumed: " + str(AirportSim.nyc.gas_consumed_circulating))

    print("Airport IAN traveling gas consumed: " + str(AirportSim.iah.gas_consumed_traveling))
    print("Airport IAN circuling gas consumed: " + str(AirportSim.iah.gas_consumed_circulating))

    print("Airport CHI traveling gas consumed: " + str(AirportSim.chi.gas_consumed_traveling))
    print("Airport CHI circuling gas consumed: " + str(AirportSim.chi.gas_consumed_circulating))

    print("Airport LAX arriving passengers: " + str(AirportSim.lax.m_arriving_passengers))
    print("Airport LAX departing passengers: " + str(AirportSim.lax.m_departing_passengers))
    print("Airport LAX total circling time: " + str(AirportSim.lax.m_circling_time))

    print("Airport ATL arriving passengers: " + str(AirportSim.atl.m_arriving_passengers))
    print("Airport ATL departing passengers: " + str(AirportSim.atl.m_departing_passengers))
    print("Airport ATL total circling time: " + str(AirportSim.atl.m_circling_time))

    print("Airport NYC arriving passengers: " + str(AirportSim.nyc.m_arriving_passengers))
    print("Airport NYC departing passengers: " + str(AirportSim.nyc.m_departing_passengers))
    print("Airport NYC total circling time: " + str(AirportSim.nyc.m_circling_time))

    print("Airport IAH arriving passengers: " + str(AirportSim.iah.m_arriving_passengers))
    print("Airport IAH departing passengers: " + str(AirportSim.iah.m_departing_passengers))
    print("Airport IAH total circling time: " + str(AirportSim.iah.m_circling_time))

    print("Airport CHI arriving passengers: " + str(AirportSim.chi.m_arriving_passengers))
    print("Airport CHI departing passengers: " + str(AirportSim.chi.m_departing_passengers))
    print("Airport CHI total circling time: " + str(AirportSim.chi.m_circling_time))

    total_sum = AirportSim.lax.m_arriving_passengers + AirportSim.atl.m_arriving_passengers + AirportSim.nyc.m_arriving_passengers + AirportSim.iah.m_arriving_passengers + AirportSim.chi.m_arriving_passengers
    print("Total passenger number: " + str(total_sum))


if __name__ == '__main__':
   main()

