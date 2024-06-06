import numpy as np
import tensorflow as tf
from tensorflow.keras import models

from recording_helper import record_audio, terminate
from tf_helper import preprocess_audiobuffer

import warnings
warnings.filterwarnings('ignore')

# !! Modify this in the correct order
commands = ['down', 'left', 'no', 'right', 'up']

loaded_model = models.load_model("model/audioModel")

# Label untuk digunakan saat tidak ada input suara
default_label = [0.27428386, 0.22793025, 0.27963266, 0.088543914, 0.12960933]

# Ambang batas untuk menentukan apakah input suara kosong
SILENCE_THRESHOLD = 4800

def predict_mic():
    audio = record_audio()
    
    # Jika input suara hening (semua nilai di bawah ambang batas)
    if np.max(audio) < SILENCE_THRESHOLD:
        print("Tidak ada suara yang dideteksi. Mengatur label prediksi secara langsung.")
        percent = default_label
        command = commands[np.argmax(default_label)]
        return command
    
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    
    # Mengabaikan label 'no' dalam prediksi
    idx_no = commands.index('no')
    prediction = tf.tensor_scatter_nd_update(prediction, [[0, idx_no]], [0.0])
    
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    percent = []
    for tensor in tf.nn.softmax(prediction[0]):
        value = tensor.numpy()
        percent.append(value)
    
    print(percent)
    print("Predicted label:", command)
    return command

if __name__ == "__main__":
    while True:
        command = predict_mic()
        if command == "stop":
            terminate()
            break
