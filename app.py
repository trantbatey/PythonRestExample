from flask import Flask
from flask_restplus import Api, Resource, fields
from zebra_api.Device import Device


app = Flask(__name__)
api = Api(app)
'''
deviceItems = []
Sidewinder = Device('Sidewinder Tubs Skimmer', 747, 150, 'Normal', False)
deviceItems.append(Sidewinder.toJSON())
'''
deviceItems = Device.read_all_devices()
print("deviceItems: ")
print(deviceItems)
Device = api.model('Device.py', {'device_name': fields.String('The Device Name'),
                              'viscosity': fields.Integer('The viscosity of the lubricant'),
                              'temperature': fields.Integer('The temperature of the lubricant'),
                              'particulate_level': fields.Integer('1=Normal, 2=Elevated, 3=High, ' +
                                                                  'The level of particulates in the lubricant'),
                              'is_bacteria_detected': fields.Boolean(False)})


@api.route('/zebra_api/device')
class DeviceItem(Resource):
    def get(self):
        return deviceItems

    @api.expect(Device)
    def post(self):
        print(api.payload)
        d = {}
        d['device_name'] = api.payload['device_name'];
        d['viscosity'] = api.payload['viscosity'];
        d['temperature'] = api.payload['temperature'];
        d['particulate_level'] = api.payload['particulate_level'];
        d['is_bacteria_detected'] = api.payload['is_bacteria_detected'];
        from zebra_api.Device import Device
        device = Device.toDevice(d)
        deviceItems.append(device.toJSON())
        return {'result': 'Device added'}, 201


if __name__ == '__main__':
    app.run(debug=True)

