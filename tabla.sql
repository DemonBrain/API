CREATE TABLE IF NOT EXISTS Administrador (
    Username VARCHAR(255),
    Password VARCHAR(255),
    PRIMARY KEY (Username)
);

CREATE TABLE IF NOT EXISTS Company (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name VARCHAR(255),
    company_api_key VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Location (
    company_id INTEGER,
    location_name VARCHAR(255),
    location_country VARCHAR(255),
    location_city VARCHAR(255),
    location_meta VARCHAR(255),
    PRIMARY KEY (company_id, location_name),
    FOREIGN KEY (company_id) REFERENCES Company(ID)
);

CREATE TABLE IF NOT EXISTS Sensor (
    location_id INTEGER,
    sensor_id INTEGER,
    sensor_name VARCHAR(255),
    sensor_category VARCHAR(255),
    sensor_meta VARCHAR(255),
    sensor_api_key INTEGER,
    PRIMARY KEY (location_id, sensor_id)
);

CREATE TABLE IF NOT EXISTS SensorData (
    sensor_id INTEGER,
    data_field1 INTEGER,
    data_field2 VARCHAR(255),
    PRIMARY KEY (sensor_id),
    FOREIGN KEY (sensor_id) REFERENCES Sensor(sensor_id)
);

-- Crear el usuario administrador
INSERT or REPLACE INTO Administrador(Username, Password) VALUES ('admin', 'password');

