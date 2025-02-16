from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore
import os
from datetime import datetime
import uuid
from functools import wraps

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Initialize Firebase
cred = credentials.Certificate("patient-database-784bf-firebase-adminsdk-a1s2y-21f56bfe2f.json")
if not len(firebase_admin._apps):
    firebase_admin.initialize_app(cred)
db = firestore.client()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def login():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == "Saiopticals" and password == "venuvamsi":
        session['user'] = username
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'Invalid credentials'})

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/search_patient', methods=['POST'])
@login_required
def search_patient():
    phone = request.json.get('phone')
    if not phone:
        return jsonify({'success': False, 'message': 'Phone number required'})
    
    patients = db.collection("Patients").where("phone", "==", phone).get()
    results = []
    for doc in patients:
        patient = doc.to_dict()
        results.append({
            'serial': doc.id,
            'name': patient.get('name'),
            'phone': patient.get('phone'),
            'gender': patient.get('gender')
        })
    return jsonify({'success': True, 'patients': results})

@app.route('/api/patient/<serial>/history')
@login_required
def get_patient_history(serial):
    eyesight_records = db.collection("EyesightHistory").where("serial_number", "==", serial).get()
    purchase_records = db.collection("PurchaseHistory").where("serial_number", "==", serial).get()
    
    eyesight_history = []
    for record in eyesight_records:
        data = record.to_dict()
        eyesight_history.append({
            'date': data.get('date_of_visit'),
            'r_spherical': data.get('r_spherical'),
            'r_cylindrical': data.get('r_cylindrical'),
            'r_axis': data.get('r_axis'),
            'l_spherical': data.get('l_spherical'),
            'l_cylindrical': data.get('l_cylindrical'),
            'l_axis': data.get('l_axis'),
            'addition': data.get('addition')
        })
    
    purchase_history = []
    for record in purchase_records:
        data = record.to_dict()
        purchase_history.append({
            'date': data.get('date_of_visit'),
            'details': data.get('purchase_details'),
            'amount': data.get('bill_amount')
        })
    
    return jsonify({
        'success': True,
        'eyesight_history': eyesight_history,
        'purchase_history': purchase_history
    })

@app.route('/api/add_patient', methods=['POST'])
@login_required
def add_patient():
    data = request.json
    name = data.get('name', '').strip().lower()
    phone = data.get('phone', '').strip()
    
    if not name or not phone or len(phone) != 10:
        return jsonify({'success': False, 'message': 'Invalid input data'})
    
    try:
        patient_key = f"{phone}_{name}"
        query = db.collection("Patients").where("patient_key", "==", patient_key).get()
        
        if query:
            serial_number = query[0].id
        else:
            serial_number = str(uuid.uuid4())[:8]
            while db.collection("Patients").document(serial_number).get().exists:
                serial_number = str(uuid.uuid4())[:8]
            
            patient_data = {
                "name": name,
                "phone": phone,
                "gender": data.get('gender'),
                "serial_number": serial_number,
                "patient_key": patient_key
            }
            db.collection("Patients").document(serial_number).set(patient_data)
        
        # Save eyesight data
        eyesight_data = {
            "serial_number": serial_number,
            "date_of_visit": datetime.now().strftime("%Y-%m-%d"),
            "r_spherical": data.get('r_spherical'),
            "r_cylindrical": data.get('r_cylindrical'),
            "r_axis": data.get('r_axis'),
            "l_spherical": data.get('l_spherical'),
            "l_cylindrical": data.get('l_cylindrical'),
            "l_axis": data.get('l_axis'),
            "addition": data.get('addition')
        }
        db.collection("EyesightHistory").document(serial_number).set(eyesight_data)
        
        return jsonify({
            'success': True,
            'serial_number': serial_number,
            'message': 'Patient added successfully'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/generate_bill', methods=['POST'])
@login_required
def generate_bill():
    data = request.json
    serial_number = data.get('serial_number')
    
    bill_data = {
        'serial_number': serial_number,
        'date_of_visit': datetime.now().strftime("%Y-%m-%d"),
        'bill_amount': data.get('amount'),
        'purchase_details': data.get('details')
    }
    
    try:
        db.collection("PurchaseHistory").document(serial_number).set(bill_data)
        return jsonify({'success': True, 'message': 'Bill saved successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True) 