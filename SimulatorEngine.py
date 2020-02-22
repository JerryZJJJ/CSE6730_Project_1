from EventHandler import *
from SimulatorEvent import *
import queue


class SimulatorEngine(EventHandler):
    def __init__(self):
        self.m_current_time = 0.0
        self.m_event_list = queue.PriorityQueue()
        self.m_running = False

    def run(self):
        self.m_running = True
        while self.m_running and not self.m_event_list.empty():
            ev = self.m_event_list.get()
            self.m_current_time = ev.m_time
            ev.m_handler.handle(ev)

    def handle(self, event):
        if event.m_event_type is SimulatorEvent.STOP_EVENT:
            self.m_running = False
            print("Simulator stopping at time: " + str(event.m_time))
        else:
            print("Invalid event type")

    def schedule(self, event):
        self.m_event_list.put(event)

    def stop(self):
        self.m_running = False
