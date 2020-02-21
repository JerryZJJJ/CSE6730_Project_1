from Event import *
from Airport import *


def main():
    exp1 = Event(0, 2, 2)
    exp2 = Event(1, 2, 2)
    exp3 = Event(1, 2, 3)

    print(exp1.m_event_id)
    print(exp2.m_event_id)
    print(exp3.m_event_id)

    airport1 = Airport("LAX", 0, 0, 0)
    airport2 = Airport("CHI", 0, 0, 0)
    print(Airport.cal_distance(airport1, airport2))


if __name__ == "__main__":
    main()
