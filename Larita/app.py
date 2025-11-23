from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Temporary in-memory contacts list
contacts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    contact = {"id": len(contacts)+1, "name": name, "email": email, "phone": phone, "bookings": []}
    contacts.append(contact)
    return jsonify({"status": "success", "contact": contact})

@app.route('/contacts')
def get_contacts():
    return jsonify(contacts)

if __name__ == '__main__':
    app.run(debug=True)
