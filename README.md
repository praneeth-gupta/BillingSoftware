# Sai Krishna Opticals - Patient Management System

A comprehensive patient management and billing system for optical stores. This application helps manage patient records, track eyesight history, and generate bills.

## Features

- 👥 Patient Management
- 👁️ Eyesight History Tracking
- 💰 Bill Generation
- 🔍 Patient Search by Phone Number
- 📱 Responsive Modern UI
- 🔒 Secure Login System

## Prerequisites

Before installing the application, make sure you have:

1. Python 3.7 or higher installed
   - To check if Python is installed, open terminal/command prompt and run:
     ```bash
     python --version
     ```
   - If not installed, download from [Python's official website](https://www.python.org/downloads/)

2. Git installed (optional, for cloning the repository)
   - Download from [Git's official website](https://git-scm.com/downloads)

## Installation

### Method 1: Using Git

1. Open terminal/command prompt
2. Clone the repository:
   ```bash
   git clone https://github.com/praneeth-gupta/BillingSoftware.git
   ```
3. Navigate to the project directory:
   ```bash
   cd BillingSoftware
   ```
4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Method 2: Direct Download

1. Download the ZIP file from [GitHub](https://github.com/praneeth-gupta/BillingSoftware)
2. Extract the ZIP file to your desired location
3. Open terminal/command prompt in the extracted folder
4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### On Windows:

1. Double-click the `run_app.bat` file
   - OR open command prompt in the project directory and run:
     ```bash
     python public/app.py
     ```

### On Mac/Linux:

1. Make the run script executable:
   ```bash
   chmod +x run_app.sh
   ```
2. Run the application:
   ```bash
   ./run_app.sh
   ```
   - OR directly with Python:
     ```bash
     python3 public/app.py
     ```

3. Open your web browser and go to: http://localhost:5000

## Login Credentials

- Username: Saiopticals
- Password: venuvamsi

## Usage Guide

1. **Login**
   - Use the provided credentials to log in
   - The system will redirect you to the dashboard

2. **Search Patient**
   - Enter patient's phone number in the search box
   - Click "Search" to find existing patients

3. **Add New Patient**
   - Click "Add New Patient" button
   - Fill in required details:
     - Name
     - Phone Number (10 digits)
     - Gender
   - Add eyesight information if available:
     - Left Eye (Spherical, Cylindrical, Axis)
     - Right Eye (Spherical, Cylindrical, Axis)
     - Addition

4. **View Patient History**
   - Search for a patient
   - Click "History" button
   - View both eyesight and purchase history

5. **Generate Bill**
   - Search for a patient
   - Click "Generate Bill" button
   - Enter purchase details and amount
   - Save the bill

## Troubleshooting

1. **Application won't start**
   - Verify Python is installed correctly
   - Check if all dependencies are installed
   - Ensure no other application is using port 5000

2. **Can't log in**
   - Verify you're using the correct credentials
   - Clear browser cache and try again

3. **Database connection issues**
   - Verify internet connection
   - Check if Firebase credentials file is present

## Security Notes

1. Keep the Firebase credentials file (`patient-database-784bf-firebase-adminsdk-a1s2y-21f56bfe2f.json`) secure
2. Don't share login credentials
3. Change default credentials in production

## Support

For any issues or queries, please create an issue on the [GitHub repository](https://github.com/praneeth-gupta/BillingSoftware/issues). 