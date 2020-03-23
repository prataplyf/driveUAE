from DRIVEUAE import app
from werkzeug.serving import run_simple

if __name__ == "__main__":
    # app.run(debug=True, use_reloader=True,ssl_context="adhoc")  # ssl_context=('cert.pem', 'key.pem')
    # pip install pyopenssl
    run_simple('localhost', 5000, app, use_reloader= True, use_debugger = True, use_evalex=True)