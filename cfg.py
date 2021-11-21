course_section_capacity_df = None
tt_parsed_df = None


class Slot:
    day = str()
    startTime = int()

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def __lt__(self, other):
        return str(self) < str(other)

    def __str__(self):
        return self.day + ' ' + str(self.startTime)


class Section:
    name = str()
    timing = [Slot()]
    capacity = int()
    allotted = int()

    def __init__(self, name, capacity, timing):
        self.name = name
        self.capacity = capacity
        self.timing = sorted(timing)

    def __eq__(self, other):
        return str(self.timing) == str(other.timing)

    def __lt__(self, other):
        return str(self.timing) < str(other.timing)

    def __repr__(self):
        return str(self) + "\n"

    def __str__(self):
        times = ["{} {}".format(x.day, x.startTime) for x in self.timing]
        times = " ".join(times)
        return "Name: {} | Capacity: {} | Time: {}".format(self.name, self.capacity, times)
