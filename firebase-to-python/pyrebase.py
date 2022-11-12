import pyrebase

config = {
  "apiKey": "AIzaSyCve3wQd5wgxBa5DWhLEduP1JEomDVdjjk",
  "authDomain": "gold-fart-e5696.firebaseapp.com",
  "databaseURL": "https://gold-fart-e5696-default-rtdb.firebaseio.com/",
  "projectId": "gold-fart-e5696",
  "storageBucket": "gold-fart-e5696.appspot.com",
  "messagingSenderId": "563942008737",
  "appId": "1:563942008737:web:74c8782b0c46d7180d8de0",
  "measurementId": "G-8B611KMBH6"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

data = {"test": "parsssing object"}

database.push(data)