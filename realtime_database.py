import pyrebase

config = {
    "apiKey": "your_key",
    "authDomain": "your_project.firebaseapp.com",
    "databaseURL": "https://your_project-default-rtdb.firebaseio.com",
    "storageBucket": "your_project.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

def log_data(rpm):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    db.child("drill_data").push({"time": timestamp, "rpm": rpm})

# In update_gui(), after rpm = get_drill_data():
log_data(rpm)
