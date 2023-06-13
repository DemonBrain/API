from db import get_db

#ADMIN

def validation(username, passw):
    db = get_db()
    cursor = db.cursor()

    # Verificar si el usuario "admin" existe en la tabla Admin
    verificar = "SELECT * FROM Administrador WHERE Username = ?"
    cursor.execute(verificar, [username])
    user_exists = cursor.fetchone() is not None

    if user_exists:
        # Obtener la contraseña del usuario "admin"
        contra = "SELECT Password FROM Administrador WHERE Username = ?"
        cursor.execute(contra, [username])
        admin_password = cursor.fetchone()[0]
    
        # Comparar la contraseña ingresada con la contraseña del usuario "admin"
        if passw == admin_password:
             print("Contraseña correcta. Acceso permitido.")
             return True
        else:
             print("Contraseña incorrecta. Acceso denegado.")
             return False
    else:
        print("El usuario no existe.")
        return False 

def insert_company(company_name, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Company(company_name, company_api_key) VALUES (?, ?)"
    cursor.execute(statement, [company_name, company_api_key])
    db.commit()
    return True

def insert_location(company_id, location_name, location_country, location_city, location_meta):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Location(company_id, location_name, location_country, location_city, location_meta ) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [company_id, location_name, location_country, location_city, location_meta])
    db.commit()
    return True

def insert_sensor(location_id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Sensor(location_id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key ) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [location_id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key])
    db.commit()
    return True

def insert_sensordata(sensor_id, data_field1, data_field2, sensor_api_key):
    db = get_db()
    cursor = db.cursor()

    contra = "SELECT sensor_api_key FROM Sensor WHERE sensor_id = ?"
    cursor.execute(contra, [sensor_id])
    admin_password = cursor.fetchone()[0]

    if sensor_api_key == contra:
             statement = "INSERT INTO SensorData(sensor_id, data_field1, data_field2 )  VALUES (?, ?, ?)"
             cursor.execute(statement, [sensor_id, data_field1, data_field2])
             db.commit()
             return True
    else:
             print("Contraseña incorrecta. Acceso denegado.")
             return False

    


#Company

def all_company():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Company;"
    cursor.execute(query)
    return cursor.fetchall()

    

#LOCATION

def all_location():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Location;"
    cursor.execute(query)
    return cursor.fetchall()

def one_location():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Location LIMIT 1;"
    cursor.execute(query)
    return cursor.fetchall()

def specific_location(company_id,company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT l.* FROM Location l JOIN Company c ON l.company_id = c.ID WHERE c.company_id = ? AND c.company_api_key = ?"
    cursor.execute(query, [company_id,company_api_key])
    return cursor.fetchall()

def update_location(company_id, location_name, location_country, location_city, location_meta, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE Location SET location_name = ?, location_country = ?, location_city = ?, location_meta = ? WHERE company_id = ? AND company_id IN (SELECT ID FROM Company WHERE company_api_key = ?)"
    cursor.execute(statement, [location_name, location_country, location_city, location_meta, company_id, company_api_key])
    db.commit()
    return True

def delete_location(company_id,company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM Location WHERE company_id = ? AND company_id IN (SELECT ID FROM Company WHERE company_api_key = ?)"
    cursor.execute(statement, [company_id,company_api_key])
    db.commit()
    return True

#SENSOR

def all_sensor():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Sensor;"
    cursor.execute(query)
    return cursor.fetchall()

def one_sensor():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Sensor LIMIT 1;"
    cursor.execute(query)
    return cursor.fetchall()

def specific_sensor(company_id,company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT s.* FROM Company c JOIN Location l ON c.ID = l.company_id JOIN Sensor s ON l.company_id = s.location_id WHERE c.company_id = ? AND c.company_api_key = ? "
    cursor.execute(query, [company_id,company_api_key])
    return cursor.fetchall()

def update_sensor( sensor_id, sensor_name, sensor_category, sensor_meta, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE Sensor SET sensor_name = ?, sensor_category = ?, sensor_meta = ? WHERE location_id IN (SELECT l.company_id FROM Company c JOIN Location l ON c.ID = l.company_id WHERE c.company_api_key = ? ) AND sensor_id = ?;"
    cursor.execute(statement, [sensor_name, sensor_category, sensor_meta, company_api_key, sensor_id])
    db.commit()
    return True

def delete_sensor(sensor_id,company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM Sensor WHERE location_id IN (SELECT l.company_id FROM Company c JOIN Location l ON c.ID = l.company_id WHERE c.company_api_key = ? ) AND sensor_id = ?"
    cursor.execute(statement, [company_api_key, sensor_id])
    db.commit()
    return True


#SENSORDATA

def all_sensordata():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM SensorData;"
    cursor.execute(query)
    return cursor.fetchall()

def one_sensordata():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM SensorData LIMIT 1;"
    cursor.execute(query)
    return cursor.fetchall()

def specific_sensordata(sensor_id,sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    contra = "SELECT sensor_api_key FROM Sensor WHERE sensor_id = ?"
    cursor.execute(contra, [sensor_id])
    admin_password = cursor.fetchone()[0]

    if sensor_api_key == contra:
             statement = "SELECT * FROM SensorData WHERE sensor_id = ?"
             cursor.execute(statement, [sensor_id])
             db.commit()
             return True
    else:
            data = "error 400."
            return data


def update_sensordata( sensor_id, data_field1, data_field2, sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    contra = "SELECT sensor_api_key FROM Sensor WHERE sensor_id = ?"
    cursor.execute(contra, [sensor_id])
    admin_password = cursor.fetchone()[0]

    if sensor_api_key == contra:
             statement = "UPDATE SensorData SET data_field1 = ?, data_field2 = ? WHERE sensor_id = ?"
             cursor.execute(statement, [data_field1, data_field2, sensor_id])
             db.commit()
             return True
    else:
            data = "error 400."
            return data


def delete_sensordata(sensor_id,sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    contra = "SELECT sensor_api_key FROM Sensor WHERE sensor_id = ?"
    cursor.execute(contra, [sensor_id])
    admin_password = cursor.fetchone()[0]

    if sensor_api_key == contra:
             statement = "DELETE FROM SensorData WHERE sensor_id = ?;"
             cursor.execute(statement, [sensor_id])
             db.commit()
             return True
    else:
            data = "error 400."
            return data

