class SelectPage {
    type = "Select/Menu"
    key = null;
    path = null;
    description = null;
    selections = []
}

class optionSelect {
    key = null;
    name = null;
    description = null;
    img = null;
    link = null;
}

class InputPage {
    key = null;
    path = null;
    description = null;
    inputGroups = []
    link = null;
}

class InputGroup {
    description = null;
    inputFields = []
}

class InputField {
    key = null;
    title = null;
    decription = null;
    type = "number/combo/checkbox";
    default = null;
    unit = "feet"
}


var wizardPages = [
    {
        type:"Select",
        key: "wizard1",
        path: "/select-floor",
        description: "choose which floor to customize:",
        selections: [
            {
                key: "upper-floor",
                name: "Upper Floor",
                description: null,
                img : "img/upper-floor.png",
                link: "/room-config"
            }, 
            {
                key: "main-floor",
                name: "Main Floor",
                description: null,
                img :"img/main-floor.png",
                link: ""
            },
            {
                key: "basement",
                name: "Basement",
                description: null,
                img: "img/basement.png",
                link: ""
            },
            {
                //TODO:
            }
        ]
    },
    {
        type:"Menu",
        key: "upper-room-config",
        path: "/upper-room-config",
        description: null,
        selections: [
            {
                key: "bedroom-office",
                name: "Bedroom/Office",
                description:null,
                img : "img/bedroom-office.png",
                link : "/room-dimension"
            },
            { 
                key: "bathroom",
                name: "Bathroom",
                description: null,
                img: "img/bathroom.png",
                link: "/room-dimension"
            },
            {
                key: "laundry-room",
                name: "Laundry Room",
                description: null,
                img: "img/separate-laundry-room.png",
                link: "/room-dimension"
             }
        ]
    },

    {
        key: "room-dimension",
        path: "/room-dimension",
        description: null,
        inputGroups: [
            {
                description:null,
                inputFields: [
                    { 
                        key:"width",
                        title:"width",
                        description:null,
                        type: "number",
                        default: 0,
                        unit: "feet"

                    },
                    { 
                        key:"length",
                        title:"length",
                        description:null,
                        type: "number",
                        default: 0,
                        unit: "feet"
                    }
                ]
            }
        ],
        link: "/upper-renovations"
    },
    {
        type: "Menu",
        key: "upper-customization-overview",
        path: "/upper-renovations",
        description: null,
        selections: [
            {
                key:"flooring-baseboards",
                name:"Flooring/Baseboards",
                description: null,
                img: null,
                link: "/flooring-or-baseboards"
            },
            {
                key: "closet",
                name: "Closet",
                descripion: null,
                img: null,
                link: "/closet-or-walk-in-closet"
            },
            {
                key: "wall-painting",
                name: "Wall Painting",
                description: null,
                img: null,
                link: ""
            },
            {
                key: "demolition-structural-changes",
                name: "Demolition/Structural Changes",
                description: null,
                img: null,
                link: ""
            }

        ]
    
    },

    {
        type: "Menu",
        key: "flooring-or-baseboards",
        path: "/flooring-or-baseboards",
        description: null,
        selections: [
            {
                key: "flooring",
                name: "Flooring",
                img: "img/flooring.png",
                link: "/choose-flooring-material"
            },
            {
                key: "baseboards",
                name: "Baseboards",
                img: "img/baseboards.png",
                link: "/baseboards-input-door-count"
            }

        ]
    },
    {
        key: "select-flooring-material",
        path: "/choose-flooring-material",
        description: null,
        inputGroups: [
            {
                key: "solid-hardwood-flooring",
                name: "Solid Hardwood Flooring",
                img: "img/solid-hardwood-flooring-choice.png",
                link: null
            },
            {
                key: "engineered-hardwood-flooring",
                name: "Engineered Hardwood Flooring",
                img: "img/engineered-hardwood-flooring-choice.png",
                link: null
            },
            {
                key: "laminate-flooring",
                name: "Laminate Flooring",
                img: "img/laminate-flooring-choice.png",
                link: null
            },
            {
                key: "vinyl-flooring",
                name: "Vinyl Flooring",
                img: "img/vinyl-flooring-choice.png",
                link: null
            }
        ],
        link: "/upper-renovations"
    },
    {
        key: "baseboards-input-door-count",
        path: "/baseboards-input-door-count",
        description: null,
        inputGroups: [
            {
                key: "door-count",
                title: "door count",
                description: null,
                type:"number",
                default: 1,
                unit: "integer",
                link: null
            }
        ],
        link: "/upper-renovations"
    },
    {
        type: "Select",
        key: "closet-or-walk-in-closet",
        path: "/closet-or-walk-in-closet",
        description: null,
        selections: [
            {
                key: "walk-in-closet",
                name: "Walk-in Closet",
                img: "img/walk-in-closet.png",
                link: "/walk-in-closet-dimensions"
            },
            {
                key: "closet",
                name: "Closet",
                img: "img/closet.png",
                link: ""
            }
        ]
    },
    {
        key: "walk-in-closet-dimensions",
        path: "/walk-in-closet-dimensions",
        description: null,
        inputGroups: [
            {
                key: "walk-in-closet-height",
                title: "Walk-in Closet Height",
                description: null,
                type:"number",
                default: 0,
                unit: "feet",
                link: null
            },
            {
                key: "walk-in-closet-width",
                title: "Walk-in Closet Width",
                description: null,
                type:"number",
                default: 0,
                unit: "feet",
                link: null
            },
            {
                key: "walk-in-closet-length",
                title: "Walk-in Closet Length",
                description: null,
                type:"number",
                default: 0,
                unit: "feet",
                link: null
            }
        ],
        link: "/choose-walk-in-closet-layout"
    },
    {
        type: ""
    }

]


