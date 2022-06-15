

function renderQuote(root) {
    window.location.href = "/quote";
}


function renderHome(root) {

    root.innerHTML="<div style='padding:20;text-align:center;vertical-align:middle'>"
        +"<b style='font-size:20; font-family:sans-serif'>WELCOME TO EMC MILLWORK & CONSTRUCTION LTD</b>"
        +"</div>";

    let gallery = new Gallery();
    root.appendChild(gallery.getRoot());

    const infos = [
        {
            image : "img/home_pic1.jpg",
            title : "BEST HOUSE RENOVATION",
            text : "What might be right for you may not be to right for some. Now the world don't move to the som beat of just one drumu sathsa."
        },

        {
            image : "img/home_pic2.jpg",
            title : "DESIGN AND BUILD",
            text : "What might be right for you may not be to right for some. Now the world don't move to the som beat of just one drumu sathsa."
        },

        {
            image : "img/home_pic1.jpg",
            title : "BEST HOUSE RENOVATION",
            text : "What might be right for you may not be to right for some. Now the world don't move to the som beat of just one drumu sathsa."
        },

        {
            image : "img/home_pic2.jpg",
            title : "DESIGN AND BUILD",
            text : "What might be right for you may not be to right for some. Now the world don't move to the som beat of just one drumu sathsa."
        }
    ]
    
    gallery.setData(infos);
    

}

class Gallery {
    
    constructor () {
        this.root = document.createElement("div");
        this.root.className="gallery";
    }
    

    add(art) {
        this.root.appendChild(art.getRoot());
    }

    getRoot() {
        return this.root;
    }

    setData(infos) {
        for (var i=0;i<infos.length;i++) {
            var info = infos[i];
            var textPicture = new TextPicture(info,280,360);
            this.add(textPicture);
        }
    }
}

class TextPicture {
    constructor(info, width,height) {
        this.root = document.createElement("div")
        this.root.style.margin=20;
        this.root.style.display="inline-block";

        var container = document.createElement("div");
        container.style.height=height;
        container.style.width=width;
        container.className = "textPicture";
        this.root.appendChild(container)

        var picDiv = document.createElement("div");
        picDiv.style.width=width;
        picDiv.style.height="auto";
        container.appendChild(picDiv);

        var img = document.createElement("img")
        img.style.width=width;
        img.style.height = "auto";
        img.src='static/'+info.image;
        picDiv.appendChild(img);

        var title = document.createElement("div");
        title.className="textPicture tp_title";
        title.innerText=info.title;
        container.appendChild(title);

        var text = document.createElement("div")
        text.className="tp_text";
        text.innerText=info.text;
        container.append(text);
    }

    getRoot() {
        return this.root;
    }
}


function renderServices() {
    content.innerHTML="<div>This is services</div>"
}

function renderProjects() {
    content.innerHTML ="<div>This is projects</div>"
}

function chooseMaterial(type, matEle) {
    for (var i=0; i< matEle.parentElement.children.length;i++) {
        div = matEle.parentElement.children[i];
        div.className = "material_selection";
    }
    matEle.parentElement.parentElement.children[1].value = matEle.getAttribute('prodcode');
    matEle.className = 'material_selected';
}

function onChangeRoomType(eleSelect) {
    hideAllEquipments();
    var roomtype = eleSelect.value;
    if (roomtype!='washroom')
        document.getElementById("room_panel").style.display="";
    if (roomtype=='washroom' || roomtype=='laundry' || roomtype=='kitchen')
        document.getElementById(roomtype+"_panel").style.display="";
}

function hideAllEquipments() {
    document.getElementById("room_panel").style.display="none";
    document.getElementById("washroom_panel").style.display="none";
    document.getElementById("laundry_panel").style.display="none";
    document.getElementById("kitchen_panel").style.display="none";
}

