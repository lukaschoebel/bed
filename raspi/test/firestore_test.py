import unittest
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("../../secrets/firestore-creds.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class FirestoreTest(unittest.TestCase):
    def test_set2store(self):
        # reference to the firestore document
        doc_ref = db.collection(u'current_measure').document(u'0')
        doc_ref.set({
            u'duration': 999,
            u'infestation': 999,
            u'notes': 'hi from test!',
            u'status': 'completed'
        })

        doc = doc_ref.get()
        notes = doc.to_dict()['notes']

        self.assertEqual(notes, 'hi from test!')

    def test_updateStore(self):
        # reference to the firestore document
        doc_ref = db.collection(u'current_measure').document(u'0')
        doc_ref.update({
            u'notes': 'updated test msg!'
        })

        doc = doc_ref.get()
        notes = doc.to_dict()['notes']

        self.assertEqual(notes, 'updated test msg!')


if __name__ == '__main__':
    unittest.main()