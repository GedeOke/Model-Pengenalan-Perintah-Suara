import numpy as np
import tensorflow as tf
from tensorflow.keras import models # type: ignore

from audio_precessor import preprocess_audiobuffer
from audio_recorder import AudioRecorder

import warnings
warnings.filterwarnings('ignore')

commands = ['atas', 'bawah', 'kanan', 'kiri', 'tidak_dikenal']
loaded_model = models.load_model("test.h5")
default_label = [[0.27746227, 0.08098052, 0.043101475, 0.07737855, 0.5210772]]
SILENCE_THRESHOLD = 4800

def predict_mic():
    audio_recorder = AudioRecorder()
    audio_data = audio_recorder.record_audio(duration=1)
    
    if np.max(audio_data) < SILENCE_THRESHOLD:
        print("Tidak ada suara yang dideteksi. Mengatur label prediksi secara langsung.")
        percent = default_label
        command = commands[np.argmax(default_label)]
        return command
    spec = preprocess_audiobuffer(audio_data)
    prediction = loaded_model(spec)
    prediction = prediction.numpy()
    idx_no = commands.index('tidak_dikenal')
    prediction[0, idx_no] = -np.inf
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
        
