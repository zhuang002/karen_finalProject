

function renderQuote(root) {
    window.location.href = "/quote";
}

function onWizardFinish(data) {
    alert(data);
}

function requireServerData(path) {

}

class Wizard {
    constructor(onWizardFinish) {
        this.onFinish = onWizardFinish;
        this.history = new Array();
        this.history.push("/");
        this.current = 0;


        this.root=document.createElement("div");

        this.gallery = new Gallery();
        this.root.appendChild(this.gallery.getRoot());

        this.nav = document.createElement("div")
        this.root.appendChild(this.nav);
        this.nav.className = "wizardControl";

        this.back = document.createElement("button")
        this.back.innerText="BACK";
        this.back.className = "wizardControl button";
        this.back.disabled = true;
        this.back.onClick = this.goBack;
        this.nav.appendChild(this.back);
        

        let space = document.createElement("span");
        space.style.width="80px";
        this.nav.appendChild(space);

        this.next = document.createElement("button")
        this.next.innerText="NEXT";
        this.next.className = "wizardControl button";
        this.next.disabled = true;
        this.next.onClick=this.goNext;
        this.nav.appendChild(this.next);

        var data = requireServerData(this.history[this.current]);
        this.gallery.setData(data);
    }

    getRoot() {
        return this.root;
    }

    goBack() {
        if (this.current == 0) 
            return;
        this.current--;

        var data = requireServerData(this.history[this.current]);
        var newGallery = new Gallery();
        newGallery.setData(data);
        this.replaceGallery(newGallery,20);
        this.updateNavigator();
    }

    goNext() {
        if (this.current == this.history.length-1) 
            return;
        this.current++;

        var data = requireServerData(this.history[this.current]);
        var newGallery = new Gallery();
        newGallery.setData(data);
        this.replaceGallery(newGallery,-20);
        this.updateNavigator();
    }

    replaceGallery(newGallery, step) {
        this.root.replaceChild(newGallery, this.gallery);
        this.gallery = newGallery;
    }

    updateNavigator() {
        this.back.disabled = this.current == 0;
        this.next.disabled = this.current == this.history.length-1;
    }

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