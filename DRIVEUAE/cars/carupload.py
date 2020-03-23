from DRIVEUAE import module as ml
from DRIVEUAE import app
from DRIVEUAE import mail

# @app.route('/register',methods = ['POST', 'GET'])
@app.route("/carupload", methods=['POST','GET'])
@ml.cross_origin()
def carupload():
    if ml.request.method == 'POST':
        if ml.request.is_json:
            data = ml.request.get_json()
            carbrand = data['carbrand']
            carname = data['carname']
            qty = data['qty']
            carimage = data['carimage']
            carFullDetail = data['carFullDetail']
            carType = data['carType']
            passangers = data['passangers']
            luggages = data['luggages']
            transmission = data['transmission']
            fuel = data['fuel']
            cylinder = data['cylinder']
            engineVolume = data['engineVolume']
            horsepower = data['horsepower']
            torque = data['torque']
            fuelEcoCity = data['fuelEcoCity']
            fuelEcoHighway = data['fuelEcoHighway']
            fuelEcoCombined = data['fuelEcoCombined']
            fuelTank = data['fuelTank']
            emissionsClass = data['emissionsClass']
            displacement = data['displacement']
            rent1 = data['rent1']
            rent2 = data['rent2']
            rent4 = data['rent4']
            rent7 = data['rent7']
        else:
            carbrand = ml.request.form.get('carbrand')
            carname = ml.request.form.get('carname')
            qty = ml.request.form.get('qty')
            carimage = ml.request.form.get('carimage')
            carFullDetail = ml.request.form.get('carFullDetail')
            carType = ml.request.form.get('carType')
            passangers = ml.request.form.get('passangers')
            luggages = ml.request.form.get('luggages')
            transmission = ml.request.form.get('transmission')
            fuel = ml.request.form.get('fuel')
            cylinder = ml.request.form.get('cylinder')
            engineVolume = ml.request.form.get('engineVolume')
            horsepower = ml.request.form.get('horsepower')
            torque = ml.request.form.get('torque')
            fuelEcoCity = ml.request.form.get('fuelEcoCity')
            fuelEcoHighway = ml.request.form.get('fuelEcoHighway')
            fuelEcoCombined = ml.request.form.get('fuelEcoCombined')
            fuelTank = ml.request.form.get('fuelTank')
            emissionsClass = ml.request.form.get('emissionsClass')
            displacement = ml.request.form.get('displacement')
            rent1 = ml.request.form.get('rent1')
            rent2 = ml.request.form.get('rent2')
            rent4 = ml.request.form.get('rent4')
            rent7 = ml.request.form.get('rent7')
        # add cars details into database where all cars are stored
        ml.config.allcars.insert_one({"carBrand":carbrand, "name":carname, "image":carimage, "carFullDetail":carFullDetail, "carType":carType, "passangers":passangers, "luggages":luggages, "transmission":transmission, "fuel":fuel, "cylinder":cylinder, "engineVolume":engineVolume, "horsepower":horsepower, "torque":torque, "fuelEcoCity":fuelEcoCity, "fuelEcoHighway":fuelEcoHighway, "fuelEcoCombined":fuelEcoCombined, "fuelTank":fuelTank, "emissionsClass":emissionsClass, "displacement":displacement, "rent1Day":rent1, "rent2+days":rent2, "rent4+days":rent4, "rent7+days":rent7})
        # add cars brands into database where all car brands are stored
        # add number of quantity of these car
        if carbrand in [temp['carBrand'] for temp in ml.config.carbrands.find({}, {'carBrand':1})]:
            for x in ml.config.carbrands.find({'carBrand':carbrand}, {'numberOfBrand':1}):
                new_qty = int(x['numberOfBrand']) + int(qty)
                ml.config.carbrands.update_one({"carBrand":carbrand}, {"$set" : {"numberOfBrand":new_qty}})
        else:
            ml.config.carbrands.insert_one({"carBrand":carbrand, "numberOfBrand":int(qty), "image":carimage})
        return ml.jsonify({"status":"Success","message":"Register Successfully", "data":{"name":carname,}})
    return ml.render_template('car/carupload.html', title='Car Upload')

