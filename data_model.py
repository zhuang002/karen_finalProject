from typing import List
import csv


class Room:
    def __init__(self) -> None:
        self.id: int = 0
        self.type = 'bedroom'
        self.floor = 'upper_floor'
        self.name: str = None
        self.width: int = 0
        self.length: int = 0
        self.height: int = 0
        self.wall_paint: str = None
        self.baseboard: str = None
        self.cost = 0

    def calculate(self):
        self.cost = 0
        area = self.length * self.width
        unit_price = get_unit_price('baseboard.csv', self.baseboard)
        self.cost += area * unit_price

        area = (self.length + self.width) * self.height * 2
        unit_price = get_unit_price('wall_paint.csv', self.wall_paint)
        self.cost += area * unit_price


class WashRoom(Room):
    def __init__(self) -> None:
        super().__init__()
        self.type = "washroom"
        self.vanity = None
        self.toilet = None
        self.shower = None
        self.bathtub = None

    def calculate(self):
        super().calculate()

        self.cost += get_unit_price('Vanity-Sheet1.csv', self.vanity)
        self.cost += get_unit_price('Toilets-Sheet1.csv', self.toilet)
        self.cost += get_unit_price('Showerheads-Sheet1.csv', self.shower)
        self.cost += get_unit_price('Bathtubs-Sheet1.csv', self.bathtub)


class Laundry(Room):
    def __init__(self) -> None:
        super().__init__()
        self.watertub = None

    def calculate(self):
        super().calculate()
        self.cost += get_unit_price('watertub.csv', self.watertub)


class Stair:
    def __init__(self) -> None:
        self.style: str = None
        self.width: int = 0
        self.steps: int = 0
        self.step_material: str = None
        self.handrail: str = None
        self.spindle: str = None


class Project:
    def __init__(self) -> None:
        self.id_count: int = 1
        self.main_floor: List[Room] = []
        self.upper_floor: List[Room] = []
        self.basement: List[Room] = []
        self.stairs: List[Stair] = []
        self.cost = 0
        self.main_floor_cost = 0
        self.upper_floor_cost = 0
        self.basement_cost = 0

    def add_room(self, room: Room) -> Room:
        room.id = self.id_count
        self.id_count += 1
        rooms = getattr(self, room.floor)
        rooms.append(room)
        return room

    def delete_room(self, room_id: int) -> None:
        for room in self.main_floor:
            if room.id == room_id:
                self.main_floor.remove(room)
                return None
        for room in self.upper_floor:
            if room.id == room_id:
                self.upper_floor.remove(room)
                return None
        for room in self.basement:
            if room.id == room_id:
                self.basement.remove(room)
                return None

    def update_room(self, room: Room):
        self.delete_room(room.id)
        self.add_room(room)

    def find_room_by_id(self, room_id: int) -> Room:
        for room in self.main_floor:
            if room.id == room_id:
                return room
        for room in self.upper_floor:
            if room.id == room_id:
                return room
        for room in self.basement:
            if room.id == room_id:
                return room

    def calculate(self):
        self.cost = 0
        self.main_floor_cost = 0
        self.upper_floor_cost = 0
        self.basement_cost = 0
        for room in self.main_floor:
            room.calculate()
            self.cost += room.cost
            self.main_floor_cost += room.cost

        for room in self.upper_floor:
            room.calculate()
            self.cost += room.cost
            self.upper_floor_cost += room.cost

        for room in self.basement:
            room.calculate()
            self.cost += room.cost
            self.basement_cost += room.cost



class Material:
    def __init__(self, code: str, ref: str,  name: str, description: str, brand: str, picture: str, price: float):
        self.code = code
        self.ref = ref
        self.name = name
        self.description = description
        self.brand = brand
        self.picture = picture
        self.unitprice = price


def get_unit_price(file: str, code: str):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if row[0] == code:
                return row[5]
    return 0
