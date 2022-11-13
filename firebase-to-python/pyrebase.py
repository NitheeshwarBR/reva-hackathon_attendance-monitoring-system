import setup

# config = {
#   "apiKey": "AIzaSyCve3wQd5wgxBa5DWhLEduP1JEomDVdjjk",
#   "authDomain": "gold-fart-e5696.firebaseapp.com",
#   "databaseURL": "https://gold-fart-e5696-default-rtdb.firebaseio.com/",
#   "projectId": "gold-fart-e5696",
#   "storageBucket": "gold-fart-e5696.appspot.com",
#   "messagingSenderId": "563942008737",
#   "appId": "1:563942008737:web:74c8782b0c46d7180d8de0",
#   "measurementId": "G-8B611KMBH6"
# }

config = {
    "apiKey": "AIzaSyDmN8cGvMwOri3zc4ALySvLKwcgVcqLYLY",
    "authDomain": "gandu-a52a3.firebaseapp.com",
    "projectId": "gandu-a52a3",
    "databaseURL": "https://console.firebase.google.com/u/0/project/gandu-a52a3/database/gandu-a52a3-default-rtdb/data/~2F",
    "storageBucket": "gandu-a52a3.appspot.com",
    "messagingSenderId": "329022795247",
    "appId": "1:329022795247:web:04ca2ef64a59f3e7fcda1a",
    "measurementId": "G-B92RP9SL4V"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

data = {"test": "parsssing object"}

database.push(data)
