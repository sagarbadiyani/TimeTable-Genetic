course_section_capacity_df = None
tt_parsed_df = None

section_time_map = {}

course_list_all = ['BITS F110 P', 'CHEM F110 P', 'PHY F110 P', 'MATH F113 L', 'MATH F113 T', 'BIO F110 P', 'BITS F112 L', 'ME F110 P', 'PHY F111 L', 'PHY F111 T', 'BIO F111 L' , 'BIO F111 T' , 'MATH F111 L', 'MATH F111 T', 'CHEM F111 L', 'CHEM F111 T']
course_list_pure_eg = ['BITS F110 P', 'CHEM F110 P', 'PHY F110 P', 'MATH F113 T', 'MATH F113 L']
course_list_pure_ws = ['BIO F110 P', 'BITS F112 L', 'ME F110 P', 'PHY F111 T', 'PHY F111 L']
course_list_common = ['BIO F111 L', 'BIO F111 T', 'MATH F111 L', 'MATH F111 T', 'CHEM F111 L', 'CHEM F111 T']
course_list_eg = course_list_pure_eg + course_list_common
course_list_ws = course_list_pure_ws + course_list_common

field_eg = []
field_ws = []

for i in range(20):
    field_eg.append([])
    field_ws.append([])


class Slot:
    def __init__(self, day, start_time):
        self.day = day
        self.start_time = start_time

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def __lt__(self, other):
        return str(self) < str(other)

    def __str__(self):
        return self.day + ' ' + str(self.start_time)


class Section:
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
