CREATE TABLE IF NOT EXISTS reyna_mario_coderhouse.vehicle_positions (
    vehicle_positions_id INT IDENTITY(1,1),
    route_id VARCHAR(50),
    latitude FLOAT,
    longitude FLOAT,
    speed INT,
    timestamp VARCHAR(100),
    id VARCHAR(50),
    direction INT,
    agency_name VARCHAR(100),
    agency_id INT,
    route_short_name VARCHAR(50),
    tip_id VARCHAR(50),
    trip_headsign VARCHAR(100),
    PRIMARY KEY (vehicle_positions_id),
    UNIQUE (id, timestamp)
)
DISTKEY (id)
SORTKEY (timestamp);