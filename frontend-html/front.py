from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def form():
    return render_template('form.html')

@app.route("/addrec", methods=['POST'])
def addrec():
    if request.method == 'POST':
        try:
            Id = request.form['Id']
            nm = request.form['nm']
            nm1 = request.form['nm1']

            # You can convert request.form directly to a dictionary
            here = dict(request.form)

            print("Received data:", here)

            # Send a POST request to another endpoint
            response = requests.post('http://localhost:5000/test', json=here)

            if response.status_code == 200:
                print("Request to external endpoint successful")
            else:
                print("Request to external endpoint failed")

            return jsonify(here), 200

        except KeyError as e:
            # Handle the case where a required form field is missing
            error_message = f"Missing required field: {str(e)}"
            print(error_message)
            return jsonify({"error": error_message}), 400

    # If not a POST request, return an error
    return jsonify({"error": "Invalid request method"}), 405

if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
