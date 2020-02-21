class Event:
    m_next_id = 0

    def __init__(self, delay, handler, event_type):
        self.m_time = delay
        self.m_handler = handler
        self.m_event_type = event_type
        self.m_event_id = Event.m_next_id
        Event.m_next_id += 1

    def __eq__(self, other):
        return (self.m_time == other.m_time) and (self.m_event_id == other.m_event_id)

    def __lt__(self, other):
        return (self.m_time < other.m_time) or ((self.m_time == other.m_time) and (self.m_event_id < other.m_event_id))

    def __gt__(self, other):
        return (self.m_time > other.m_time) or ((self.m_time == other.m_time) and (self.m_event_id > other.m_event_id))


