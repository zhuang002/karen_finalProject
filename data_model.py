from typing import List


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


class WashRoom(Room):
    def __init__(self) -> None:
        super().__init__()
        self.type = "washroom"
        self.vanity = None
        self.toilet = None
        self.shower = None
        self.bathtub = None


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

    def add_room(self, room: Room) -> Room:
        room.id = self.id_count
        self.id_count += 1
        rooms = getattr(self, room.floor)
        rooms.append(room)
        return room

    def delete_room(self, room_id:int) -> None:
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

    def update_room(self, room:Room):
        self.delete_room(room.id)
        self.add_room(room)

    def find_room_by_id(self, room_id:int) -> Room:
        for room in self.main_floor:
            if room.id == room_id:
                return room
        for room in self.upper_floor:
            if room.id == room_id:
                return room
        for room in self.basement:
            if room.id == room_id:
                return room


class Material:
    def __init__(self, code:str, name: str, description: str, brand: str, picture: str, price: float):
        self.code =code
        self.name = name
        self.description = description
        self.brand = brand
        self.picture = picture
        self.unitprice = price
