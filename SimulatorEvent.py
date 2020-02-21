from Event import *


class SimulatorEvent(Event):
    STOP_EVENT = None

    def __init__(self, delay, handler, event_type):
        super().__init__(delay, handler, event_type)
