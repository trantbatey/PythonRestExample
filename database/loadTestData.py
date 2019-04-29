#!/usr/bin/python

import psycopg2
from config import config


def load_data():
    commands = []
    """ Commands for inserting test data """
    commands.append(
        "INSERT INTO devices (device_name, viscosity, temperature, particulate_level, is_bacteria_detected) " +
        "values ('Sidewinder Tube Skimmer', 747, 150, 'Normal', 'false') RETURNING device_id;"
    )
    commands.append(
        "INSERT INTO devices (device_name, viscosity, temperature, particulate_level, is_bacteria_detected) " +
        "values ('Zebra Tramp Oil Belt Skimmer', 900, 207, 'High', 'false') RETURNING device_id;"
    )
    commands.append(
        "INSERT INTO devices (device_name, viscosity, temperature, particulate_level, is_bacteria_detected) " +
        "values ('Smart Disk Skimmer', 630, 197, 'Normal', 'true') RETURNING device_id;"
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            print(command)
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    load_data()