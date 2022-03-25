from flask import render_template


class Wizard:
    def __init__(self):
        self._pages = {
            "select-floor":
            {
                "type": "Select",
                "key": "select-floor", 
                "description": "choose which floor to customize:",
                "selections": [
                    {
                        "key": "upper-floor",
                        "name": "Upper Floor",
                        "description": None,
                        "img": "img/upper-floor.png",
                        "link": "upper-room-config"
                    },
                    {
                        "key": "main-floor",
                        "name": "Main Floor",
                        "description": None,
                        "img": "img/main-floor.png",
                        "link": ""
                    },
                    {
                        "key": "basement",
                        "name": "Basement",
                        "description": None,
                        "img": "img/basement.png",
                        "link": ""
                    },
                    
                ]
            },
            "upper-room-config":
            {
                "type": "Menu",
                "key": "upper-room-config",
                "description": None,
                "selections": [
                    {
                        "key": "bedroom-office",
                        "name": "Bedroom/Office",
                        "description": None,
                        "img": "img/bedroom-office.png",
                        "link": "room-dimension"
                    },
                    {
                        "key": "bathroom",
                        "name": "Bathroom",
                        "description": None,
                        "img": "img/bathroom.png",
                        "link": "room-dimension"
                    },
                    {
                        "key": "laundry-room",
                        "name": "Laundry Room",
                        "description": None,
                        "img": "img/separate-laundry-room.png",
                        "link": "room-dimension"
                    }
                ]
            },
            "room-dimension":
            {
                "type": "Input",
                "key": "room-dimension",
                "description": None,
                "inputGroups": [
                    {
                        "description": "Room Dimension",
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
                "link": "upper-renovations"
            },
            "upper-renovations":
            {
                "type": "Menu",
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
        page = self._pages[page_key]
        tp = page["type"]
        if tp == "Select" or tp == "Menu":
            return render_template("select_page.html", data=page)
        elif tp == "Input":
            return render_template("input_page.html", data=page)


