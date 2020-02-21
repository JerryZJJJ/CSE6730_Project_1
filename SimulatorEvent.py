from Event import *

STOP_EVENT = 0


class SimulatorEvent(Event):
    def __init__(self, delay, handler, event_type):
        super().__init__( delay, handler, event_type)
