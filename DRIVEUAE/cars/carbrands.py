from DRIVEUAE import module as ml
from DRIVEUAE import app
from DRIVEUAE import mail

# @app.route('/register',methods = ['POST', 'GET'])
@app.route("/carbrands", methods=['POST','GET'])
@ml.cross_origin()
def carbrands():
    if ml.request.method == 'POST':
        if ml.request.is_json:
            data = ml.request.get_json()
            brand = data['carbrand']
        else:
            brand = ml.request.form.get('carbrand')
        for x in ml.config.carbrands.find({"carBrand":brand}, {"carBrand":1, "numberOfBrand":1, "image":1}):
            return ml.jsonify({"status":"Success","message":"Brand Fetched", "data":{"carBrand":x['carBrand'], "numberOfBrand":x['numberOfBrand'], "image":x['image']}})
    return ml.render_template('car/carbrands.html', title='Car Brands Details')
