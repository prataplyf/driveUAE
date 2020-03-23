from DRIVEUAE import app
from DRIVEUAE import module as ml

@app.route('/')  # page that help to go on a registration page
@app.route('/home')
def home():
    return ml.render_template('index.html', title='Dashboard')