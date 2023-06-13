from flask import Flask, jsonify, request
from db import create_tables
import controladores
app = Flask(__name__)

@app.route('/hola', methods=["GET"])
def hola():
    return jsonify("holaa")

#Admin

@app.route("/<username>/<passw>/company", methods=["POST"])
def insert_company(username,passw):
    game_details = request.get_json()
    company_name = game_details["name"]
    company_api_key = game_details["api_key"]
    valid = controladores.validation(username,passw)

    if valid:
        result = controladores.insert_company(company_name, company_api_key)
        return jsonify(result)
    else:
        return jsonify(valid)

@app.route("/<username>/<passw>/company", methods=["GET"])
def get_all_company(username,passw):
    valid = controladores.validation(username,passw)

    if valid:
        todas = controladores.all_company()
        return jsonify(todas)
    else:
        return jsonify(valid)


@app.route("/<username>/<passw>/location", methods=["POST"])
def insert_location(username,passw):
    game_details = request.get_json()
    company_id = game_details["company_id"]
    location_name = game_details["name"]
    location_country = game_details["country"]
    location_city = game_details["city"]
    location_meta = game_details["meta"]
    valid = controladores.validation(username,passw)

    if valid:
        result = controladores.insert_location(company_id, location_name, location_country, location_city, location_meta)
        return jsonify(result)
    else:
        return jsonify(valid)    
    
@app.route("/<username>/<passw>/sensor", methods=["POST"])
def insert_sensor(username,passw):
    game_details = request.get_json()
    location_id = game_details["location_id"]
    sensor_id = game_details["id"]
    sensor_name = game_details["name"]
    sensor_category = game_details["category"]
    sensor_meta = game_details["meta"]
    sensor_api_key = game_details["api_key"]
    valid = controladores.validation(username,passw)

    if valid:
        result = controladores.insert_sensor(location_id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key)
        return jsonify(result)
    else:
        return jsonify(valid)    

@app.route("/<username>/<passw>/sensordata", methods=["POST"])
def insert_sensordata(username,passw):
    game_details = request.get_json()
    sensor_id = game_details["sensor_id"]
    data_field1 = game_details["field1"]
    data_field2 = game_details["field2"]
    sensor_api_key = game_details["api_key"]
    valid = controladores.validation(username,passw)

    if valid:
        result = controladores.insert_sensordata(sensor_id, data_field1, data_field2,sensor_api_key)
        return jsonify(result)
    else:
        return jsonify(valid)    


#Location Endpoint Muestra todo, muestra uno, edita, elimina. (GET, GET, PUT, DELETE)

@app.route('/location', methods=["GET"])
def get_all_location():
    todas = controladores.all_location()
    return jsonify(todas)

@app.route('/location/one', methods=["GET"])
def get_one_location():
    todas = controladores.one_location()
    return jsonify(todas)

@app.route('/location/<company_api_key>/<id>', methods=["GET"])
def get_specific_location(company_api_key,id):
    todas = controladores.specific_location(id,company_api_key)
    return jsonify(todas)

@app.route("/location/<company_api_key>", methods=["PUT"])
def update_location(company_api_key):
    location_details = request.get_json()
    company_id = location_details["id"]
    location_name = location_details["name"]
    location_country = location_details["country"]
    location_city = location_details["city"]
    location_meta = location_details["meta"]
    result = controladores.update_location(company_id, location_name, location_country, location_city, location_meta, company_api_key)
    return jsonify(result)

@app.route("/location/<company_api_key>", methods=["DELETE"])
def delete_location(company_api_key):
    location_details = request.get_json()
    company_id = location_details["id"]
    result = controladores.delete_location(company_id,company_api_key)
    return jsonify(result)

#Sensor Endpoint Muestra todo, muestra uno, edita, elimina. (GET, GET, PUT, DELETE)

@app.route('/sensor', methods=["GET"])
def get_all_sensor():
    todas = controladores.all_sensor()
    return jsonify(todas)

@app.route('/sensor/one', methods=["GET"])
def get_one_sensor():
    todas = controladores.one_sensor()
    return jsonify(todas)

@app.route('/sensor/<company_api_key>/<company_id>', methods=["GET"])
def get_specific_sensor(company_api_key,company_id):
    todas = controladores.specific_sensor(company_id,company_api_key)
    return jsonify(todas)

@app.route("/sensor/<company_api_key>", methods=["PUT"])
def update_sensor( sensor_id, sensor_name, sensor_category, sensor_meta, company_api_key):
    location_details = request.get_json()
    sensor_id = location_details["id"]
    sensor_name = location_details["name"]
    sensor_category = location_details["category"]
    sensor_meta = location_details["meta"]
    result = controladores.update_sensor( sensor_id, sensor_name, sensor_category, sensor_meta, company_api_key)
    return jsonify(result)

@app.route("/sensor/<company_api_key>", methods=["DELETE"])
def delete_sensor(company_api_key):
    location_details = request.get_json()
    sensor_id = location_details["id"]
    result = controladores.delete_sensor(sensor_id,company_api_key)
    return jsonify(result)


#SensorData Endpoint Muestra todo, muestra uno, edita, elimina. (GET, GET, PUT, DELETE)

@app.route('/sensordata', methods=["GET"])
def get_all_sensordata():
    todas = controladores.all_sensordata()
    return jsonify(todas)

@app.route('/sensordata/one', methods=["GET"])
def get_one_sensordata():
    todas = controladores.one_sensordata()
    return jsonify(todas)

@app.route('/sensordata/<sensor_id>', methods=["GET"])
def get_specific_sensordata():
    game_details = request.get_json()
    sensor_id = game_details["id"]
    sensor_api_key = game_details["api_key"]
    todas = controladores.specific_sensordata(sensor_id,sensor_api_key)
    return jsonify(todas)

@app.route("/sensordata", methods=["PUT"])
def update_sensordata(  sensor_id, data_field1, data_field2):
    location_details = request.get_json()
    sensor_id = location_details["id"]
    data_field1 = location_details["field1"]
    data_field2 = location_details["field2"]
    sensor_api_key = location_details["api_key"]
    result = controladores.update_sensordata( sensor_id, data_field1, data_field2, sensor_api_key)
    return jsonify(result)

@app.route("/sensordata", methods=["DELETE"])
def delete_sensordata(sensor_id):
    location_details = request.get_json()
    sensor_id = location_details["id"]
    sensor_api_key = location_details["api_key"]
    result = controladores.delete_sensordata(sensor_id,sensor_api_key)
    return jsonify(result)


@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response




if __name__ == "__main__":
      create_tables()

      app.run(host='0.0.0.0', port=8000, debug=False)
