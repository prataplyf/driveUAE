from DRIVEUAE import module as ml
from DRIVEUAE import app
from DRIVEUAE import mail

# @app.route('/register',methods = ['POST', 'GET'])
@app.route("/cardetails", methods=['POST','GET'])
@ml.cross_origin()
def cardetails():
    if ml.request.method == 'POST':
        if ml.request.is_json:
            data = ml.request.get_json()
            brandname = data['brandname']
        else:
            brandname = ml.request.form.get('brandname')
        allcarsdetails = []
        for x in ml.config.allcars.find({"carBrand":brandname}, {"carBrand":1, "name":1, "image":1, "carFullDetail":1, "carType":1, "passangers":1, "luggages":1, "transmission":1, "fuel":1, "cylinder":1, "engineVolume":1, "horsepower":1, "torque":1, "fuelEcoCity":1, "fuelEcoHighway":1, "fuelEcoCombined":1, "fuelTank":1, "emissionsClass":1, "displacement":1, "rent1Day":1, "rent2+days":1, "rent4+days":1, "rent7+days":1}):
            allcarsdetails.append({"brand":x['carBrand'], "name":x['name'], "carimage":x['image'], "carFullDetail":x['carFullDetail'], "carType":x['carType'], "passangers":x['passangers'], "luggages":x['luggages'], "transmission":x['transmission'], "fuel":x['fuel'], "cylinder":x['cylinder'], "engineVolume":x['engineVolume'], "horsepower":x['horsepower'], "torque":x['torque'], "fuelEcoCity":x['fuelEcoCity'], "fuelEcoHighway":x['fuelEcoHighway'], "fuelEcoCombined":x['fuelEcoCombined'], "fuelTank":x['fuelTank'], "emissionsClass":x['emissionsClass'], "displacement":x['displacement'], "rent1Day":x['rent1Day'], "rent2+days":x['rent2+days'], "rent4+days":x['rent4+days'], "rent7+days":x['rent7+days']})
        return ml.jsonify({"status":"Success","message":"Register Successfully", "data":allcarsdetails})
    return ml.render_template('car/cardetails.html', title='Car Details')
