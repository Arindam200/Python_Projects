
import datetime
from flask import *
from werkzeug.utils import secure_filename
import tensorflow as tf
import cv2
import wget
import os
import numpy as np
from firebase_admin import credentials, initialize_app, storage, firestore

cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": "explore-ai-hackathon",
        "private_key_id": "6559ad087a8ce2f4d0e2fd71d5081d1dda3405b4",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCs65e9HQCtmszl\nqqqssncMEUVh/5yqtdYR3wwnl3E79pcJGWZC/pTCx7Ukqkoiou6WppCAqBVdeEwd\n05axuF8A8O2j5f6OgS2XusaI5WIoNJ5nzzMQSy9raE2GgwOg0M7K3Pu9ClMrZYub\nn+6vP+Cj+jwd3hme5GC91IU90fQBJojnpViRnAAwo2iQOUEWQW6nzb2KteqCyvUv\nxtQi61ctsf/S05FEuHybhmBtsCPUJCEk8gKE6UyXKvzv9ADEJBAnX1YePNRz9pC2\nQnm+PV40qK5wJGujtKMpqVm+hcOPhkxfTfBYHkzFOBgVVdJaQsI8MhQE/A3CXrsB\nWxh9lgQPAgMBAAECggEAQWxbeyoLdSNx7Vz+eRuGjhLEwPigcjgc96L/qsUSCwFX\nkJJDDgrbBrzfbLFfHi6t/WKknoC5oKUgi1JgG/ppO2ZsSsv8XTdDpDn+3pGG6zZJ\nTnZm1/3SQZ1zY3aTO1d1PeyQ9CuBXxRq1yUR/c05tWC6OQSsheDbN0c+aC7U1k/5\naJ/i/QhAElSmTiS+WFm6axPYGgNnSdY5HY+usucuI9wHMDv+2UIg/QLezLBabDvi\ndV2WaNzB6JjnZAM8SqCNnZS7HTWCw11uCd1y2oKgvJuc+ZdHu9hBUZWBr054jzmY\nR2Onoy7twBuHVMpfRI2M8MXTQXOkGhwIrYXDhUs/gQKBgQDqrcgeRpAaYEWf3vwp\nbUtAK/+DQrMwe0kB+gI5jJL66nQpqLTEQHaxIdrexdML3MQtnX/ig8c3WERztfSP\n722KkedNeyVkb33gLlqiAbLHG/FvrSegIdF4hU+kdTJurKdETnoEM/fth+pTrwuW\ntk3iFYCOSU35ILzVrKy4R4BfgQKBgQC8oWpXV4LDF4p02tCRKZFEgKUhG0j572pW\nqEtInt00Z5pAEfBEhlRy1U5cd2d8knHnTWa4BFzrVHW900nxq9MXnI7mf/i885Ar\nGtvf2hhmMo84uEH7HgeEbNPKw2J/5Vei9rPVcHz8DAG9EN+of0KZIDpDq1O/CK3r\nvI0Jp9YrjwKBgCpu5cJjq+a5BZ3Uqe+rrXGbAwZu5wubHyZWWFSjkGgCQKLPuG/L\n4CpDHtotFu4MKwS8d8UzYrAlK6toeSIVfs8RdqtR2v8AEdiZSRYGDJdn/A3fV0zj\nEIckQ7RO5KGSYmQ9dF6SLwAqFTqwaf4EVKzOioIvywOC4eIY6NohQ5sBAoGAFDvk\nYlYayr6dtYc7VDb3RDfgfrqki1rpNz56ROH1rIdofnLuKQuXx3GmJDkSusQiv8MH\nv7mIFh5LOv+NMQVTcXbzxTn4/pvJ3TXWXB7S+zN1NYpeWYeRGt1pophu2nVJf0uj\nYsPcRFUtYpCKzVJJXI+ecF/Sbe2Kan0hS+XbDXUCgYEAulIdO008flTgdIbkSniv\nx7kmgJQmzTI8u8EIlSBfyrxf8WY7anDq65qcZKMeANmHLTeEEXoe5p4FAJ596Y8Y\nlmSjb6MyCofYvI2uY5QnZ5kskqk4iOJrrx8QC/EUSzgxknR0fsQC1i9978v/7sB2\nA+q0sqs4G1Yo5yDXFxHPIGE=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-1grld@explore-ai-hackathon.iam.gserviceaccount.com",
        "client_id": "111224561641513910775",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1grld%40explore-ai-hackathon.iam.gserviceaccount.com"
    }

)
initialize_app(cred, {'storageBucket': "explore-ai-hackathon.appspot.com"})
db = firestore.client()
collection = db.collection(u"trees")
bucket = storage.bucket()

model = tf.keras.models.load_model("./imageclassifier.h5")


def newmain(PATH=""):
    img = cv2.imread(PATH)
    resize = tf.image.resize(img, (256, 256))
    yhat = model.predict(np.expand_dims(resize/255, 0))
    if yhat > 0.5:
        return True
    else:
        return False


print("\033[96m\033[1m\033[4m model Trained \033[0m")

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return """
    <body style='text-align: center;'>
        <h1 style=''>AiModelTest</h1>
        <form method="post" action="/" enctype = "multipart/form-data">
            <input name="file" type="file"/>
            <button>Submit</button>
        </form>
    </body>
    """


@app.route('/', methods=['POST'])
def third():
    try:
        if 'file' in request.files and request.files['file'] and request.files['file'].filename != '':
            file = request.files['file']
            uid = 123456789

            filename = secure_filename(file.filename)
            file.save(filename)
            result = newmain(filename)
            # File Uplode to firebase storage
            blob = bucket.blob(filename)
            blob.upload_from_filename(f"/{filename}")
            blob.make_public()
            dateNow = datetime.datetime.now()
            collection.document(f"{uid}").collection(u"trees").document(f"{int(filename.split('.')[0])}").set({
                'timeNow': dateNow,
                "index": int(filename.split(".")[0]),
                'treeImageUrl': blob.public_url
            })

            os.remove(filename)
            return jsonify({"result": result})
        else:
            return jsonify({"error": "file not found"})
    except Exception as e:
        return jsonify({"error": e})


if __name__ == "__main__":
    app.run(port=8080, debug=True, host="0.0.0.0", threaded=True,
            use_reloader=True, passthrough_errors=True)
