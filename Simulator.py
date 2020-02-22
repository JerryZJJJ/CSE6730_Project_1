from SimulatorEngine import *


def get_sim():
    if Simulator.instance is None:
        Simulator.instance = SimulatorEngine()
    return Simulator.instance


def stop_at(time):
    stop_event = SimulatorEvent(time, get_sim(), SimulatorEvent.STOP_EVENT)
    schedule(stop_event)


def run():
    get_sim().run()


def get_current_time():
    return get_sim().m_current_time


def schedule(event):
    event.m_time = event.m_time + get_sim().m_current_time
    get_sim().schedule(event)


class Simulator:
    instance = None
