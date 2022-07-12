import sys
import traceback
from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
import numpy as np
import pickle


gpu_devices = tf.config.experimental.list_physical_devices('GPU')
for device in gpu_devices:
    tf.config.experimental.set_memory_growth(device, True)

app = Flask(__name__)

model = tf.keras.models.load_model('model_clean_v1.hdf5')    


labels = ['CWE-119', 'CWE-120', 'CWE-469', 'CWE-476', 'CWE-other']

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def Pipeline( X_test ):
    list_tokenized_test = tokenizer.texts_to_sequences(X_test)
    X_test_pad = pad_sequences(list_tokenized_test,  maxlen=500, padding='post', dtype = float)
    return X_test_pad



@app.route('/predict', methods=['POST']) 
def predict():
        try:
            instance_json = request.get_json() #capture the json from POST
            instance_json =  json.loads(instance_json)
            input_data = instance_json["instance"]
            x_test = np.array( [input_data, ] )
            x_test = Pipeline(x_test)
            #print(x_test)

            #print(len(instance_json["instance"][0]))
            #print(instance_json["instance"][0])
            #print(instance_json[0]["instace"])
            prediction = model.predict(x_test)
            confidences = {labels[i]: float(prediction[i][0][1]) for i in range(5)}
            print(confidences)
            return jsonify({'prediction': confidences})

        except Exception as e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})

@app.route('/do') 
def do():
    return "hoal"

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 80

    app.run(host='0.0.0.0', port=port, debug=True)
