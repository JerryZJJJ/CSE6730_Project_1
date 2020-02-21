from Event import *


def main():
    exp1 = Event(0, 2, 2)
    exp2 = Event(1, 2, 2)

    print(exp1.m_event_id)
    print(exp2.m_event_id)
    print(exp1 > exp2)


if __name__ == "__main__":
    main()
