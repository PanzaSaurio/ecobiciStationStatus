CREATE TABLE ecobici_stations (
    ecobici_stations_id INT IDENTITY(1,1),
    station_id INT,
    num_bikes_available INT,
    num_mechanical_bikes_available INT,
    num_ebikes_available INT,
    num_bikes_disabled INT,
    num_docks_available INT,
    num_docks_disabled INT,
    last_reported TIMESTAMP,
    is_charging_station BOOLEAN,
    status VARCHAR(50),
    is_installed BOOLEAN,
    is_renting BOOLEAN,
    is_returning BOOLEAN,
    traffic INT,
    PRIMARY KEY (ecobici_stations_id),
    UNIQUE (station_id, last_reported)
)
DISTKEY (station_id)
SORTKEY (last_reported);
