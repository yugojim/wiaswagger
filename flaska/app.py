from flask import Flask, render_template, send_from_directory
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def swagger_ui():
    return render_template('swagger_ui.html')

@app.route('/yaml')
@cross_origin()
def yamldownload():
    return send_from_directory(app.root_path, 'openapi.yaml')
   
@app.route('/Patient')
@cross_origin()
def DischargeSummary():
    return send_from_directory(app.root_path, 'Patient.json')

if __name__ == '__main__':
   app.run(debug=False, port=5000)