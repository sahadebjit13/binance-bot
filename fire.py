import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('crypto-trading-3600f-201fe095fde0.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

def target():
    ref = db.collection('settings').document('data').get()
    return ref.to_dict()