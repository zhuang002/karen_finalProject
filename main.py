import os
from flask import Flask, render_template, url_for, session, redirect, request
import pickle
from data_model import Project, Room, WashRoom, Laundry, Kitchen, materials_config
import csv
from data_model import Material
import mysql.connector
import json

app = Flask("__main__")
app.secret_key = 'TMP_SECRET_KEY'


def get_material_by_name(name):
    fname = materials_config[name]
    return get_material(fname)


def get_material(csvfile):
    materials = []
    f = os.getcwd() + "/static/data/" + csvfile
    with open(f, newline='') as csvf:
        reader = csv.reader(csvf, delimiter=',', quotechar='"')
        for row in reader:
            material = Material(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
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
    return render_template("/project.html", data=project)


@app.route("/project/delete/<int:room_id>")
def room_delete(room_id: int):
    project = pickle.loads(session['project_data'])
    project.delete_room(room_id)
    session['project_data'] = pickle.dumps(project)
    return redirect("/project")


@app.route("/project/edit/<int:room_id>")
def room_edit(room_id: int):
    project = pickle.loads(session['project_data'])
    room = project.find_room_by_id(room_id)

    config_data = {
        "room": room, "operation": "edit", 'floor': room.floor,
        "materials": {
            "room": {"wall": get_material_by_name('wall'),
                     "baseboard": get_material_by_name("baseboard")},
            "washroom": {
                "wall": get_material_by_name("w_wall"),
                "vanity": get_material_by_name("w_vanity"),
                "toilet": get_material_by_name("w_toilet"),
                "shower": get_material_by_name("w_shower"),
                "bathtub": get_material_by_name("w_bathtub"),
                "faucet": get_material_by_name("w_faucet"),
                "baseboard": get_material_by_name("w_baseboard")
            },
            "kitchen": {
                "faucet": get_material_by_name("k_faucet"),
                "rangehood": get_material_by_name("k_rangehood"),
                "watertub": get_material_by_name("k_watertub")
            },
            "laundry": {
                "watertub": get_material_by_name("l_watertub")
            }
        }
    }
    return render_template("/room_config.html", data=config_data)


@app.route("/project/add/<string:floor>")
def room_config(floor: str):
    project = pickle.loads(session['project_data'])
    room = Room()

    session['project_data'] = pickle.dumps(project)
    config_data = {
        "room": room, "operation": "add", 'floor': room.floor,
        "materials": {
            "room": {"wall": get_material_by_name('wall'),
                     "baseboard": get_material_by_name("baseboard")},
            "washroom": {
                "wall": get_material_by_name("w_wall"),
                "vanity": get_material_by_name("w_vanity"),
                "toilet": get_material_by_name("w_toilet"),
                "shower": get_material_by_name("w_shower"),
                "bathtub": get_material_by_name("w_bathtub"),
                "faucet": get_material_by_name("w_faucet"),
                "baseboard": get_material_by_name("w_baseboard")
            },
            "kitchen": {
                "faucet": get_material_by_name("k_faucet"),
                "rangehood": get_material_by_name("k_rangehood"),
                "watertub": get_material_by_name("k_watertub")
            },
            "laundry": {
                "watertub": get_material_by_name("l_watertub")
            }
        }
    }
    return render_template("/room_config.html", data=config_data)


@app.route("/project/quote/calculate")
def quote_calculate():
    project = pickle.loads(session['project_data'])
    project.calculate()
    return render_template("/calculate.html", data=project)


@app.route("/project/do/<string:operation>/<string:floor>", methods=['GET', 'POST'])
def room_doop(operation: str, floor: str):
    project = None
    if 'project_data' in session:
        project = pickle.loads(session['project_data'])
    else:
        project = Project()
        session['project_data'] = pickle.dumps(project)
    room_type = request.form.get('room_type')
    if not room_type:
        return render_template("/project.html", data=project)

    room = None
    if operation == 'add':
        if room_type == "washroom":
            room = WashRoom()
        elif room_type == "laundry":
            room = Laundry()
        elif room_type == 'kitchen':
            room = Kitchen()
        else:
            room = Room()
        room.floor = floor
        project.add_room(room)
    elif operation == 'edit':
        room = project.find_room_by_id(int(request.form.get('room_id')))

    room.type = request.form.get('room_type')
    room.name = request.form.get('room_name')
    room.width = int(request.form.get('room_width'))
    room.length = int(request.form.get('room_length'))
    room.height = int(request.form.get('room_height'))
    room.wall = request.form.get('wall')
    room.baseboard = request.form.get('baseboard')
    if isinstance(room, WashRoom):
        room.wall = request.form.get('w_wall')
        room.baseboard = request.form.get('w_baseboard')
        room.vanity = request.form.get('w_vanity')
        room.toilet = request.form.get('w_toilet')
        room.shower = request.form.get('w_shower')
        room.bathtub = request.form.get('w_bathtub')
        room.faucet = request.form.get('w_faucet')
    if isinstance(room, Laundry):
        room.watertub = request.form.get('l_watertub')
    if isinstance(room, Kitchen):
        room.watertub = request.form.get('k_watertub')
        room.faucet = request.form.get('k_faucet')
        room.rangehood = request.form.get('k_rangehood')

    session['project_data'] = pickle.dumps(project)
    return redirect("/project")


@app.route('/backend/product/<string:prod_type>')
def products_by_type(prod_type: str):
    cnx = mysql.connector.connect(host='localhost', user='emc', password='emc')
    curs = cnx.cursor(buffered=True)
    curs.execute('use emc')
    cnx.commit()

    head = "<html><body>"
    foot = "</body></html>"

    curs.execute("Select code, name, unitprice from products where type='{}'".format(prod_type))
    s = ''
    for record in curs.fetchall():
        s += record[0] + ',' + record[1] + ',' + str(record[2]) + '\n'

    return head + s + foot


@app.route('/test/grideditor')
def test_gridEditor():
    return render_template('test_grideditor.html')


@app.route('/test/update_materials')
def test_update_materials():
    jsonObj = request.json
    jsonStr = json.dumps(jsonObj)
    return jsonStr


if __name__ == '__main__':
    app.run(debug=True)
