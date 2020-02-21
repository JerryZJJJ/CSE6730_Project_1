from SimulatorEngine import *


def get_sim():
    if Simulator.instance is None:
        Simulator.instance = SimulatorEngine()
    return Simulator.instance


class Simulator:
    instance = None
