import json

import psycopg2
from database.config import config

class Device:
    def __init__(self, device_name, viscosity, temperature, particulate_level, is_bacteria_detected):
        self.device_name = device_name
        self.viscosity = viscosity
        self.temperature = temperature
        self.particulate_level = particulate_level
        self.is_bacteria_detected = is_bacteria_detected

    @staticmethod
    def toDevice(data):
        device_name = data['device_name']
        viscosity = data['viscosity']
        temperature = data['temperature']
        if (data['particulate_level'] == 2):
            particulate_level = 'Elevated'
        elif (data['particulate_level'] == 3):
            particulate_level = 'High'
        else:
            particulate_level = 'Normal'
        if (data['is_bacteria_detected'].lower() == "true"):
            is_bacteria_detected = True
        else:
            is_bacteria_detected = False
        device = Device(device_name, viscosity, temperature, particulate_level, is_bacteria_detected)
        return device

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def read_all_devices():
        commands = []
        """ Read devices data """
        commands.append(
            "SELECT * FROM devices; "
        )
        conn = None
        deviceItems = []
        try:
            # read the connection parameters
            params = config('database/database.ini')
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            print("read_all_devices")
            # create table one by one
            for command in commands:
                print(command)
                cur.execute(command)
            device_records = cur.fetchall()
            for row in device_records:
                # skip the device id row @ row[0]
                device = Device(row[1], row[2], row[3], row[4], row[5])
                deviceItems.append(device.toJSON())

            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return deviceItems


