from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mission(db.Model):
    __tablename__ = 'mission'

    mission_id = db.Column(db.Integer, primary_key=True)
    mission_date = db.Column(db.Date)
    theater_of_operations = db.Column(db.String(100))
    country = db.Column(db.String(100))
    air_force = db.Column(db.String(100))
    unit_id = db.Column(db.String(100))
    aircraft_series = db.Column(db.String(100))
    callsign = db.Column(db.String(100))
    mission_type = db.Column(db.String(100))
    takeoff_base = db.Column(db.String(255))
    takeoff_location = db.Column(db.String(255))
    takeoff_latitude = db.Column(db.String(15))
    takeoff_longitude = db.Column(db.Numeric(10, 6))
    target_id = db.Column(db.String(100))
    target_country = db.Column(db.String(100))
    target_city = db.Column(db.String(100))
    target_type = db.Column(db.String(100))
    target_industry = db.Column(db.String(255))
    target_priority = db.Column(db.String(5))
    target_latitude = db.Column(db.Numeric(10, 6))
    target_longitude = db.Column(db.Numeric(10, 6))
    altitude_hundreds_of_feet = db.Column(db.Numeric(7, 2))
    airborne_aircraft = db.Column(db.Numeric(4, 1))
    attacking_aircraft = db.Column(db.Integer)
    bombing_aircraft = db.Column(db.Integer)
    aircraft_returned = db.Column(db.Integer)
    aircraft_failed = db.Column(db.Integer)
    aircraft_damaged = db.Column(db.Integer)
    aircraft_lost = db.Column(db.Integer)
    high_explosives = db.Column(db.String(255))
    high_explosives_type = db.Column(db.String(255))
    high_explosives_weight_pounds = db.Column(db.String(25))
    high_explosives_weight_tons = db.Column(db.Numeric(10, 2))
    incendiary_devices = db.Column(db.String(255))
    incendiary_devices_type = db.Column(db.String(255))
    incendiary_devices_weight_pounds = db.Column(db.Numeric(10, 2))
    incendiary_devices_weight_tons = db.Column(db.Numeric(10, 2))
    fragmentation_devices = db.Column(db.String(255))
    fragmentation_devices_type = db.Column(db.String(255))
    fragmentation_devices_weight_pounds = db.Column(db.Numeric(10, 2))
    fragmentation_devices_weight_tons = db.Column(db.Numeric(10, 2))
    total_weight_pounds = db.Column(db.Numeric(10, 2))
    total_weight_tons = db.Column(db.Numeric(10, 2))
    time_over_target = db.Column(db.String(8))
    bomb_damage_assessment = db.Column(db.String(255))
    source_id = db.Column(db.String(100))

    def __init__(self, mission_date, theater_of_operations, country, air_force, unit_id, aircraft_series, callsign, mission_type, takeoff_base,
                 takeoff_location, takeoff_latitude, takeoff_longitude, target_id, target_country, target_city, target_type, target_industry,
                 target_priority, target_latitude, target_longitude, altitude_hundreds_of_feet, airborne_aircraft, attacking_aircraft,
                 bombing_aircraft, aircraft_returned, aircraft_failed, aircraft_damaged, aircraft_lost, high_explosives, high_explosives_type,
                 high_explosives_weight_pounds, high_explosives_weight_tons, incendiary_devices, incendiary_devices_type, incendiary_devices_weight_pounds,
                 incendiary_devices_weight_tons, fragmentation_devices, fragmentation_devices_type, fragmentation_devices_weight_pounds,
                 fragmentation_devices_weight_tons, total_weight_pounds, total_weight_tons, time_over_target, bomb_damage_assessment, source_id):
        self.mission_date = mission_date
        self.theater_of_operations = theater_of_operations
        self.country = country
        self.air_force = air_force
        self.unit_id = unit_id
        self.aircraft_series = aircraft_series
        self.callsign = callsign
        self.mission_type = mission_type
        self.takeoff_base = takeoff_base
        self.takeoff_location = takeoff_location
        self.takeoff_latitude = takeoff_latitude
        self.takeoff_longitude = takeoff_longitude
        self.target_id = target_id
        self.target_country = target_country
        self.target_city = target_city
        self.target_type = target_type
        self.target_industry = target_industry
        self.target_priority = target_priority
        self.target_latitude = target_latitude
        self.target_longitude = target_longitude
        self.altitude_hundreds_of_feet = altitude_hundreds_of_feet
        self.airborne_aircraft = airborne_aircraft
        self.attacking_aircraft = attacking_aircraft
        self.bombing_aircraft = bombing_aircraft
        self.aircraft_returned = aircraft_returned
        self.aircraft_failed = aircraft_failed
        self.aircraft_damaged = aircraft_damaged
        self.aircraft_lost = aircraft_lost
        self.high_explosives = high_explosives
        self.high_explosives_type = high_explosives_type
        self.high_explosives_weight_pounds = high_explosives_weight_pounds
        self.high_explosives_weight_tons = high_explosives_weight_tons
        self.incendiary_devices = incendiary_devices
        self.incendiary_devices_type = incendiary_devices_type
        self.incendiary_devices_weight_pounds = incendiary_devices_weight_pounds
        self.incendiary_devices_weight_tons = incendiary_devices_weight_tons
        self.fragmentation_devices = fragmentation_devices
        self.fragmentation_devices_type = fragmentation_devices_type
        self.fragmentation_devices_weight_pounds = fragmentation_devices_weight_pounds
        self.fragmentation_devices_weight_tons = fragmentation_devices_weight_tons
        self.total_weight_pounds = total_weight_pounds
        self.total_weight_tons = total_weight_tons
        self.time_over_target = time_over_target
        self.bomb_damage_assessment = bomb_damage_assessment
        self.source_id = source_id
