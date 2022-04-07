import os
from flask import Flask, render_template, url_for, session, redirect, request
import pickle
from data_model import Project, Room, WashRoom
import csv
from data_model import Material

app = Flask("__main__")
app.secret_key = 'TMP_SECRET_KEY'


def get_material(csvfile):
    materials = []
    with open(csvfile, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            material = Material(row[0], row[1], row[2], row[3], row[4], row[5])
            materials.append(material)
    return materials


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/clear")
def clear():
    session.pop("project_data")
    return "OK"


@app.route("/quote")
def quote():
    return redirect("/project")


@app.route("/project", methods=['GET', 'POST'])
def project_config():
    if 'project_data' in session:
        project = pickle.loads(session['project_data'])
    else:
        project = Project()
        session['project_data'] = pickle.dumps(project)
    room_type = request.form.get('room_type')
    if room_type:
        room = project.find_room_by_id(int(request.form.get('room_id')))
        room.type = request.form.get('room_type')
        room.name = request.form.get('room_name')
        room.width = int(request.form.get('room_width'))
        room.length = int(request.form.get('room_length'))
        room.height = int(request.form.get('room_height'))
        room.wall_paint = request.form.get('room_wallpaint')
        room.baseboard = request.form.get('room_baseboard')
        if isinstance(room, WashRoom):
            room.vanity = request.form.get('vanity')
            room.toilet = request.form.get('toilet')
            room.shower = request.form.get('shower')
            room.bathtub = request.form.get('bathtub')
        session['project_data'] = pickle.dumps(project)
    return render_template("/project.html", data=project)


@app.route("/project/delete/<int:room_id>")
def room_delete(room_id: int):
    project = pickle.loads(session['project_data'])
    project.delete_room(room_id)
    session['project_data'] = pickle.dumps(project)
    return redirect("/project")


@app.route("/project/edit/<string:room_id>")
def room_edit(room_id: int):
    op = "edit"
    project = pickle.loads(session['project_data'])
    room = project.get_room_by_id(room_id)
    return render_template("/room_config.html", data=room)


@app.route("/project/add/<string:floor>/<string:room_type>")
def room_config(floor: str, room_type: str):
    project = pickle.loads(session['project_data'])
    room = None
    if room_type == "washroom":
        room = WashRoom()
    else:
        room = Room()
    room.floor = floor
    room = project.add_room(room)
    session['project_data'] = pickle.dumps(project)
    vanity = get_material(os.getcwd()+url_for("static", filename="data/vanity.csv"))
    toilet = get_material(os.getcwd()+url_for("static", filename="data/toilet.csv"))
    config_data = {"room": room, "vanity": vanity, "toilet": toilet}
    return render_template("/room_config.html", data=config_data)


if __name__ == '__main__':
    app.run(debug=True)
