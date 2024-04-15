# Imports
#-------------------------------------------------------------------------------
import pyrebase



firebaseConfig = {  
  "apiKey": "AIzaSyCOrIxG0BiKk-ZOcqDAJZfJTeoi4GRj3aY",
  "authDomain": "detection-c518c.firebaseapp.com",
  "projectId": "detection-c518c",
  "storageBucket": "detection-c518c.appspot.com",
  "messagingSenderId": "530554266561",
  "appId": "1:530554266561:web:0642d368fcec03ee488540",
  "measurementId": "G-GFFVFEQD80",
  "databaseURL": "https://detection-c518c-default-rtdb.asia-southeast1.firebasedatabase.app/"
}



firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
current=""
previous=""

def name(data1):
  if data1 is not None:
    global current
    global previous
    if data1 != current:
      data = {"current": f"{data1}"}
      db.child("current").set(data)
      if current!=previous:
          data2 = {"previous": f"{current}"}
          db.child("previous").set(data2)
          previous = current
      current = data1



