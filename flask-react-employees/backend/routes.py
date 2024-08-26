from flask import jsonify, request
from models import Employee
from app import app, db


@app.route("/api/employees" , methods = ["GRT"])
def get_amployees() :
    # employees = Employee.query.all()
    # json_emps = [emp.to_json() for emp in employees]

    return "hello" # jsonify(json_emps)


@app.route("/" , methods = ["GRT"])
def home() :
    return "home"