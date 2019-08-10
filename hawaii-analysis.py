from flask import Flask, jsonify

import numpy as np
import pandas as pd

import datetime as dt
from datetime import datetime

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

#================================================================================
# added 'sqlite:///app.db?check_same_thread=False' because of error....
# sqlalchemy.exc.ProgrammingError: (sqlite3.ProgrammingError) 
# SQLite objects created in a thread can only be used in that same thread. 
# The object was created in thread id 1000 and this is thread id 6604.
#[SQL: SELECT station.name AS station_name, station.station AS station_station 
#FROM station]
#[parameters: [{}]]
#(Background on this error at: http://sqlalche.me/e/f405)
#================================================================================
#engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
engine = create_engine("sqlite:///../Resources/hawaii.sqlite?check_same_thread=False")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Create the inspector and connect it to the engine
inspector = inspect(engine)

# Collect the names of tables within the database
inspector.get_table_names()

# Using the inspector to print the column names within the 'dow' table and its types
# Need column names and data types for query
columns = inspector.get_columns('station')
for column in columns:
    print(column["name"], column["type"])

# Using the inspector to print the column names within the 'dow' table and its types
# Need column names and data types for query
columns = inspector.get_columns('measurement')
for column in columns:
    print(column["name"], column["type"])
#Flask -- create an app
# __name__ is required; also python uses it to interpret the name of app
app =Flask(__name__)

#create routes/endpoints 
# "/" represents localhost/
# @app.route allows you to define endpoints
# within this definition, functions can be created
@app.route("/")
def home():
    return (
        "Available Routes:<br/>"
        "/api/v1.0/precipitation:<br/>"
        "/api/v1.0/stations:<br/>"
        "/api/v1.0/tobs:<br/>"
        "/api/v1.0/<start>:<br/>"
        "/api/v1.0/<start>/<end>:<br/>"
    )

#=======================================================================
# PRECIPITATION
#=======================================================================
# Create our session (link) from Python to the DB
session = Session(engine)
@app.route("/api/v1.0/precipitation")
def precipitation():
     last_tbl_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]

     last_tbl_date = datetime.strptime(last_tbl_date , '%Y-%m-%d')

     last_year = last_tbl_date - dt.timedelta(days=365)
     #print(last_year, last_tbl_date)

     sel = [Measurement.date, Measurement.prcp]

     date_precip = session.query(*sel).filter(Measurement.date >= last_year).filter(Measurement.date <= last_tbl_date).all()

     precipitation_list = [{'Date':'Inches of Rain'}]

     for date, prcp in date_precip:
         precip_dict = {}
         precip_dict[date]=prcp
         precipitation_list.append(precip_dict)
     return jsonify(precipitation_list)

#=======================================================================
# STATIONS
#=======================================================================
# Create our session (link) from Python to the DB
session = Session(engine)
@app.route("/api/v1.0/stations")
def stations():
     stations_info = session.query(Station.name, Station.station).all()
     return jsonify(stations_info)

#=======================================================================
# TOBS
#=======================================================================
# Create our session (link) from Python to the DB
session = Session(engine)
@app.route("/api/v1.0/tobs")
def tobs():
    last_tbl_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]

    last_tbl_date = datetime.strptime(last_tbl_date , '%Y-%m-%d')

    last_year = last_tbl_date - dt.timedelta(days=365)
    #print(last_year, last_tbl_date)

    sel = [Measurement.date, Measurement.tobs]

    date_precip = session.query(*sel).filter(Measurement.date >= last_year).filter(Measurement.date <= last_tbl_date).all()

    return jsonify(date_precip)
#=======================================================================
# START DATE
#=======================================================================
# Create our session (link) from Python to the DB
session = Session(engine)
@app.route("/api/v1.0/<start>")
def tempst(start):

    #start_date = datetime.strptime(start, '%Y-%m-%d')

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    temp_start = session.query(*sel).filter(Measurement.date >= start).all()
    
    #return jsonify(f'Here are the mininum temp, average temp, and maximum temp, respectively, for Hawaii from {start} to 2017-08-23:', trip)
    return jsonify(f'mininum temp, average temp, maximum temp: {start} to end date (2017-08-23)', temp_start)
    
#=======================================================================
# START AND END DATE
#=======================================================================
# Create our session (link) from Python to the DB
session = Session(engine)
@app.route("/api/v1.0/<start>/<end>")
def tempstend(start, end):

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    temp_start_end = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    return jsonify(f'mininum temp, average temp, maximum temp: {start} to {end}:', temp_start_end)

#=======================================================================
# MAIN
#=======================================================================
if __name__ == "__main__":
    app.run(debug=True)
   