class Material:
    def __init__(self, code:str, name: str, description: str, brand: str, picture: str):
        self.code =code
        self.name = name
        self.description = description
        self.brand = brand
        self.picture = picture
        self.unitprice = 0.0


class Vanity(Material):
    def __init__(self, name: str, description: str, brand: str, picture: str):
        super().__init(name, description, brand, picture)


class Toilet(Material):
    def __init__(self, name: str, description: str, brand: str, picture: str):
        super().__init(name, description, brand, picture)


class Bathtub(Material):
    def __init__(self, name: str, description: str, brand: str, picture: str):
        super().__init(name, description, brand, picture)


class Watertub(Material):
    def __init__(self, name: str, description: str, brand: str, picture: str):
        super().__init(name, description, brand, picture)


class StairStyle(Material):
    def __init__(self, name: str, description: str, brand: str, picture: str):
        super().__init(name, description, brand, picture)


class Room:
    def __init__(self, width: int = 0, length: int = 0, height: int = 8, flooring: Material = None,
                 wall_paint: Material = None, base_board: Material = None):
        self.width = width
        self.length = length
        self.height = height
        self.flooring = flooring
        self.wall_paint = wall_paint
        self.base_board = base_board


class Shower(Room):
    def __init__(self, width: int = 0, length: int = 0, height: int = 8, flooring: Material = None,
                 wall_paint: Material = None, base_board: Material = None, showerhead: Material = None,
                 door: Material = None):
        super().__init__(width, length, height, flooring, wall_paint, base_board)
        self.showerhead = showerhead
        self.door = door


class Bathroom(Room):
    def __init__(self, width: int = 0, length: int = 0, height: int = 8, flooring: Material = None,
                 wall_paint: Material = None, base_board: Material = None, vanity: Vanity = None, toilet: Toilet = None,
                 shower: Shower = None, bath_tub: Bathtub = None):
        super().__init__(width, length, height, flooring, wall_paint, base_board)
        self.vanity = vanity
        self.toilet = toilet
        self.shower = shower
        self.bath_tub = bath_tub


class Laundry(Room):
    def __init__(self, width: int = 0, length: int = 0, height: int = 8, flooring: Material = None,
                 wall_paint: Material = None, base_board: Material = None, watertub: Watertub = None):
        super().__init__(width, length, height, flooring, wall_paint, base_board)
        self.watertub = watertub


class Kitchen(Room):
    def __init__(self, width: int = 0, length: int = 0, height: int = 8, flooring: Material = None,
                 wall_paint: Material = None, base_board: Material = None):
        super().__init__(width, length, height, flooring, wall_paint, base_board)


class Foyer(Room):
    def __init__(self, width: int = 0, length: int = 0, height: int = 8, flooring: Material = None,
                 wall_paint: Material = None, base_board: Material = None, closet: Room = None):
        super().__init__(width, length, height, flooring, wall_paint, base_board)
        self.closet = closet


class DiningRoom(Room):
    def __init__(self, width: int = 0, length: int = 0, height: int = 8, flooring: Material = None,
                 wall_paint: Material = None, base_board: Material = None):
        super().__init__(width, length, height, flooring, wall_paint, base_board)


class Stair:
    def __init__(self, style: StairStyle, width: int = 0, steps: int = 0,
                 step_material: Material = None, handrail: Material = None, spindle: Material = None):
        self.style = style
        self.width = width
        self.steps = steps
        self.step_material = step_material
        self.handrail = handrail
        self.spindle = spindle


class MainFloor:
    def __init__(self, foyer: Foyer, dinning_room: Room, family_room: Room, bathroom: Bathroom,
                 living_room: Room = None,
                 stair: Stair = None, hallway: Room = None, closets: list[Room] = [], kichens: list[Room] = [], laundries: list[Laundry] = []):
        self.foyer = foyer
        self.dinning_room = dinning_room
        self.family_room = family_room
        self.bathroom = bathroom
        self.living_room = living_room
        self.stair = stair
        self.hallway = hallway
        self.closets = closets
        self.kichens = kichens
        self.laundries = laundries


class Basement:
    def __init__(self, rooms: list[Room], bathrooms: list[Room], closets: list[Room] = [], kichens: list[Room] = [], laundries: list[Laundry] = []):
        self.rooms = rooms
        self.bathrooms = bathrooms


class UpperFloor:
    def __init__(self, bedrooms: list[Room] = None, bathrooms: list[Bathroom] = None, closets: list[Room] = None, laundries: list[Laundry] = []):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.closets = closets


class Project:
    def __init__(self, upper_floor: UpperFloor = None, main_floor: MainFloor = None, basement: Basement = None,
                 laundries: list[Laundry] = [], kitchens: list[Kitchen] = []) -> None:
        self.upper_floor = upper_floor
        self.main_floor = main_floor
        self.basement = basement


class Products:
    vanity_options: list[Vanity] = []
    toilet_options: list[Toilet] = []
    bathtub_options: list[Bathtub] = []
    watertub_options: list[Watertub] = []
    stair_style_option: list[StairStyle] = []
    flooring_options: list[Material] = []
    paint_options: list[Material] = []
    baseboard_options: list[Material] = []
    tile_options: list[Material] = []
    showerhead_options: list[Material][]
    showerdoor_options: list[Material] = []
    kitchen_sink: list[Material] = []
