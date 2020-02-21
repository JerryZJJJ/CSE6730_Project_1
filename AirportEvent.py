from Event import *


class AirportEvent(Event):

    PLANE_ARRIVES, PLANE_LANDED, PLANE_DEPARTS, PLANE_TAKEOFF = 0, 1, 2, 3

    def __init__(self, plane, delay, handler, event_type, runway):
        super().__init__(delay, handler, event_type)
        self.m_plane = plane
        self.m_next_handler = None
        self.m_arriving_time = 0
        self.m_arrived_time = 0
        self.m_runway = runway

    def get_wait_time(self):
        return self.m_arrived_time - self.m_arriving_time
