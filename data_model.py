from typing import List
import csv
import os

materials_config = {
    "wall": "Washroom Floor_Wall Tile-Sheet1.csv",
    "baseboard": "Hardwood Flooring-Sheet1.csv",
    "w_wall": "Washroom Floor_Wall Tile-Sheet1.csv",
    "w_baseboard": "Washroom Floor_Wall Tile-Sheet1.csv",
    "w_vanity": "Vanity-Sheet1.csv",
    "w_toilet": "Toilets-Sheet1.csv",
    "w_shower": "Showerheads-Sheet1.csv",
    "w_bathtub": "Bathtubs-Sheet1.csv",
    "w_faucet": "Washroom Faucet-Sheet1.csv",
    "l_watertub": "Kitchen Sink-Sheet1.csv",
    "k_watertub": "Kitchen Sink-Sheet1.csv",
    "k_faucet": "Kitchen Faucets-Sheet1.csv",
    "k_rangehood": "Range Hoods-Sheet1.csv"
}


class Room:
    def __init__(self) -> None:
        self.id: int = 0
        self.type = 'bedroom'
        self.floor = 'upper_floor'
        self.name: str = None
        self.width: int = 0
        self.length: int = 0
        self.height: int = 0
        self.wall = None
        self.baseboard = None
        self.cost = 0

    def calculate(self):
        self.cost = 0
        area = self.length * self.width
        unit_price = get_unit_price('baseboard', self.baseboard)
        self.cost += area * unit_price


#        area = (self.length + self.width) * self.height * 2
#        unit_price = get_unit_price('wall', self.wall)
#        self.cost += area * unit_price


class WashRoom(Room):
    def __init__(self) -> None:
        super().__init__()
        self.type = "washroom"
        self.vanity = None
        self.toilet = None
        self.shower = None
        self.bathtub = None
        self.faucet = None

    def calculate(self):
        self.cost = 0
        area = self.length * self.width
        unit_price = get_unit_price('w_wall', self.baseboard)
        self.cost += area * unit_price

        area = (self.length + self.width) * self.height * 2
        unit_price = get_unit_price('w_baseboard', self.wall)
        self.cost += area * unit_price

        self.cost += get_unit_price('w_vanity', self.vanity)
        self.cost += get_unit_price('w_toilet', self.toilet)
        self.cost += get_unit_price('w_shower', self.shower)
        self.cost += get_unit_price('w_bathtub', self.bathtub)
        self.cost += get_unit_price('w_faucet', self.bathtub)


class Laundry(Room):
    def __init__(self) -> None:
        super().__init__()
        self.type = "laundry"
        self.watertub = None

    def calculate(self):
        super().calculate()
        self.cost += get_unit_price('l_watertub', self.watertub)


class Kitchen(Room):
    def __init__(self):
        super().__init__()
        self.faucet = None
        self.watertub = None
        self.rangehood = None

    def calculate(self):
        super().calculate()
        self.cost += get_unit_price('k_faucet', self.faucet)
        self.cost += get_unit_price('k_watertub', self.watertub)
        self.cost += get_unit_price('k_rangehood', self.rangehood)


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
        self.paint_cost = 0

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
        self.wall_area = 0
        for room in self.main_floor:
            room.calculate()
            self.cost += room.cost
            self.main_floor_cost += room.cost
            if not isinstance(room, WashRoom):
                self.wall_area += (room.width + room.length)*2*room.height

        for room in self.upper_floor:
            room.calculate()
            self.cost += room.cost
            self.upper_floor_cost += room.cost
            if not isinstance(room, WashRoom):
                self.wall_area += (room.width + room.length) * 2 * room.height

        for room in self.basement:
            room.calculate()
            self.cost += room.cost
            self.basement_cost += room.cost
            if not isinstance(room, WashRoom):
                self.wall_area += (room.width + room.length) * 2 * room.height

        self.paint_cost = self.wall_area*85.0/400
        self.cost += self.paint_cost


class Material:
    def __init__(self, code: str, ref: str,  name: str, description: str, brand: str, picture: str, price: float):
        self.code = code
        self.ref = ref
        self.name = name
        self.description = description
        self.brand = brand
        self.picture = picture
        self.unitprice = price


def get_unit_price(name: str, code: str):
    f = os.getcwd() + "/static/data/" + materials_config[name]
    with open(f, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if row[0] == code:
                return float(row[6])
    return 0
