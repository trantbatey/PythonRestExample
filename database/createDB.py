#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    commands = []
    """ create tables in the PostgreSQL database for devices"""
    commands.append(
        "CREATE TABLE devices ( " +
        "device_id SERIAL PRIMARY KEY, " +
        "device_name VARCHAR(255) NOT NULL, " +
        "viscosity INTEGER DEFAULT 0 NOT NULL, " +
        "temperature INTEGER DEFAULT 0 NOT NULL, " +
        "particulate_level VARCHAR(12) DEFAULT  'Normal' NOT NULL, " +
        "is_bacteria_detected BOOLEAN DEFAULT false NOT NULL, " +
        "UNIQUE(device_name) ) "
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
    create_tables()