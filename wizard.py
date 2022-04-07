from flask import render_template


class HtmlComponent:
    def __init__(self, key: str, name: str, desc: str, next: str = None, skip: bool = False) -> None:
        self.key = key
        self.name = name
        self.description = desc
        self.next = None
        self.skip = False

    def __str__(self) -> str:
        pass

    def getNext(self):
        return self.next


class SelectOptionCtrl(HtmlComponent):
    def __init__(self, key: str, name: str, desc: str, next: str = None, skip: bool = False, img: str = None) -> None:
        super().__init__(key, name, desc, next, skip)
        self.img = img

    def __str__(self) -> str:
        pass


class SelectCtrl(HtmlComponent):
    def __init__(self, key: str, name: str, desc: str, next: str = None, skip: bool = False, selections: list[SelectOptionCtrl] = []) -> None:
        super().__init__(key, name, desc, next, skip)
        self.selections: list[SelectOptionCtrl] = selections

    def __str__(self) -> str:
        return super().__str__()


class SelectMulCtrl(SelectCtrl):
    def __init__(self, key: str, name: str, desc: str, next: str = None, skip: bool = False, selections: list[SelectOptionCtrl] = []) -> None:
        super().__init__(key, name, desc, next, skip, selections)

    def __str__(self) -> str:
        return super().__str__()


class SelectSingleCtrl(SelectCtrl):
    def __init__(self, key: str, name: str, desc: str, next: str = None, skip: bool = False, selections: list[SelectOptionCtrl] = []) -> None:
        super().__init__(key, name, desc, next, skip, selections)

    def __str__(self) -> str:
        return super().__str__()


class InputFieldCtrl(HtmlComponent):
    def __init__(self, key: str, name: str, desc: str, next: str = None, skip: bool = False, tp: type = int) -> None:
        super().__init__(key, name, desc, next, skip)
        self.tp: type = tp


class InputGroupCtrl(HtmlComponent):
    def __init__(self, key: str, name: str, desc: str, next: str = None, skip: bool = False, fields: list[InputFieldCtrl] = []) -> None:
        super().__init__(key, name, desc, next, skip)
        self.inputFields: list[InputFieldCtrl] = fields

    def __str__(self) -> str:
        return super().__str__()


class InputCtrl(HtmlComponent):
    def __init__(self, key: str, name: str, desc: str, next: str = None, skip: bool = False, groups: list[InputGroupCtrl] = []) -> None:
        super().__init__(key, name, desc, next, skip)
        self.inputGroups: list[InputGroupCtrl] = groups

    def __str__(self) -> str:
        pass


class Wizard:
    def __init__(self):
        self._pages = {
            "select-floor":
            {
                "type": "SelectMulti",
                "key": "select-floor",
                "description": "choose which floor to customize:",
                "next-link": "upper-room-config",
                "skip": False,
                "selections": [
                    {
                        "key": "upper-floor",
                        "name": "Upper Floor",
                        "description": None,
                        "img": "img/upper-floor.png",
                        "link": None
                    },
                    {
                        "key": "main-floor",
                        "name": "Main Floor",
                        "description": None,
                        "img": "img/main-floor.png",
                        "link": None
                    },
                    {
                        "key": "basement",
                        "name": "Basement",
                        "description": None,
                        "img": "img/basement.png",
                        "link": None
                    },
                ]

            },
            "upper-room-config":
            {
                "type": "Input",
                "key": "upper-room-config",
                "description": "Please input the number of rooms",
                "next-link": "room-dimension",
                "skip": False,
                "inputGroups": [
                    {
                        "name": None,
                        "description": None,
                        "repeat": 1,
                        "inputFields": [
                            {
                                "key": "bedroom_number",
                                "name": "Bedrooms",
                                "description": "Please input the total number of bedrooms",
                                "type": "Number",
                                "default": "2",
                                "unit": None
                            },
                            {
                                "key": "bathroom_number",
                                "name": "Bathrooms",
                                "description": "Please input the total number of bathrooms",
                                "type": "Number",
                                "default": "2",
                                "unit": None
                            },
                            {
                                "key": "laundry_number",
                                "name": "Landries",
                                "description": "Please input the total number of laundries",
                                "type": "Number",
                                "default": "1",
                                "unit": None
                            }
                        ]
                    }
                ]
            },
            "room-dimension":
            {
                "type": "Input",
                "key": "room-dimension",
                "description": None,
                "skip": False,
                "next-link": "upper-renovation",
                "inputGroupsRepeat": [
                    {
                        "Name": "Room",
                        "description": "Room Dimension",
                        "repeat": 1,
                        "inputFields": [
                            {
                                "key": "width",
                                "title": "width",
                                "description": None,
                                "type": "number",
                                "default": 0,
                                "unit": "feet"

                            },
                            {
                                "key": "length",
                                "title": "length",
                                "description": None,
                                "type": "number",
                                "default": 0,
                                "unit": "feet"
                            }
                        ]
                    }
                ],
            },
            "upper-renovations":
            {
                "type": "Input",
                "key": "upper-renovations",
                "description": None,
                "selections": [
                    {
                        "key": "flooring-baseboards",
                        "name": "Flooring/Baseboards",
                        "description": None,
                        "img": None,
                        "link": "flooring-or-baseboards"
                    },
                    {
                        "key": "closet",
                        "name": "Closet",
                        "description": None,
                        "img": None,
                        "link": "closet-or-walk-in-closet"
                    },
                    {
                        "key": "wall-painting",
                        "name": "Wall Painting",
                        "description": None,
                        "img": None,
                        "link": ""
                    },
                    {
                        "key": "demolition-structural-changes",
                        "name": "Demolition/Structural Changes",
                        "description": None,
                        "img": None,
                        "link": ""
                    }

                ]

            },
            "flooring-or-baseboards":
            {
                "type": "Menu",
                "key": "flooring-or-baseboards",
                "description": None,
                "selections": [
                    {
                        "key": "flooring",
                        "name": "Flooring",
                        "img": "img/flooring.png",
                        "link": "choose-flooring-material"
                    },
                    {
                        "key": "baseboards",
                        "name": "Baseboards",
                        "img": "img/baseboards.png",
                        "link": "baseboards-input-door-count"
                    }

                ]
            },
            "choose-flooring-material":
            {
                "type": "Input",
                "key": "choose-flooring-material",
                "description": None,
                "inputGroups": [
                    {
                        "key": "solid-hardwood-flooring",
                        "name": "Solid Hardwood Flooring",
                        "img": "img/solid-hardwood-flooring-choice.png",
                        "link": None
                    },
                    {
                        "key": "engineered-hardwood-flooring",
                        "name": "Engineered Hardwood Flooring",
                        "img": "img/engineered-hardwood-flooring-choice.png",
                        "link": None
                    },
                    {
                        "key": "laminate-flooring",
                        "name": "Laminate Flooring",
                        "img": "img/laminate-flooring-choice.png",
                        "link": None
                    },
                    {
                        "key": "vinyl-flooring",
                        "name": "Vinyl Flooring",
                        "img": "img/vinyl-flooring-choice.png",
                        "link": None
                    }
                ],
                "link": "upper-renovations"
            },
            "baseboards-input-door-count":
            {
                "type": "Input",
                "key": "baseboards-input-door-count",
                "description": None,
                "inputGroups": [
                    {
                        "key": "door-count",
                        "title": "door count",
                        "description": None,
                        "type": "number",
                        "default": 1,
                        "unit": "integer",
                        "link": None
                    }
                ],
                "link": "upper-renovations"
            },
            "closet-or-walk-in-closet":
            {
                "type": "Select",
                "key": "closet-or-walk-in-closet",
                "description": None,
                "selections": [
                    {
                        "key": "walk-in-closet",
                        "name": "Walk-in Closet",
                        "img": "img/walk-in-closet.png",
                        "link": "walk-in-closet-dimensions"
                    },
                    {
                        "key": "closet",
                        "name": "Closet",
                        "img": "img/closet.png",
                        "link": ""
                    }
                ]
            },
            "walk-in-closet-dimensions":
            {
                "type": "Input",
                "key": "walk-in-closet-dimensions",
                "description": None,
                "inputGroups": [
                    {
                        "key": "walk-in-closet-height",
                        "title": "Walk-in Closet Height",
                        "description": None,
                        "type": "number",
                        "default": 0,
                        "unit": "feet",
                        "link": None
                    },
                    {
                        "key": "walk-in-closet-width",
                        "title": "Walk-in Closet Width",
                        "description": None,
                        "type": "number",
                        "default": 0,
                        "unit": "feet",
                        "link": None
                    },
                    {
                        "key": "walk-in-closet-length",
                        "title": "Walk-in Closet Length",
                        "description": None,
                        "type": "number",
                        "default": 0,
                        "unit": "feet",
                        "link": None
                    }
                ],
                "link": "choose-walk-in-closet-layout"
            }

        }

    def render_page(self, page_key: str) -> str:
