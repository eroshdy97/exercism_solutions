class Garden:
    plants_dict = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }
    def __init__(self, diagram, students = None):
        self.diagram = diagram.split("\n")
        if students is not None:
            self.students = sorted(students)
        else:
            self.students = [
                "Alice",
                "Bob",
                "Charlie",
                "David",
                "Eve",
                "Fred",
                "Ginny",
                "Harriet",
                "Ileana",
                "Joseph",
                "Kincaid",
                "Larry"
            ]

    def plants(self, name):
        index = [i for i, x in enumerate(self.students) if x == name][0]
        res = [
            Garden.plants_dict[self.diagram[0][index*2]],
            Garden.plants_dict[self.diagram[0][index*2+1]],
            Garden.plants_dict[self.diagram[1][index*2]],
            Garden.plants_dict[self.diagram[1][index*2+1]]
        ]
        return res

