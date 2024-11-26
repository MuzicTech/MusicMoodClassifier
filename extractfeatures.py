import librosa
import numpy as np

def extract_features(file_path):
    y, sr = librosa.load(file_path)
    features = {
        "tempo": librosa.beat.tempo(y, sr=sr)[0],
        "energy": np.mean(librosa.feature.rms(y=y)),
        "valence": np.mean(librosa.feature.mfcc(y=y, sr=sr)),
        "chroma_stft": np.mean(librosa.feature.chroma_stft(y=y, sr=sr)),
        "mfcc": np.mean(librosa.feature.mfcc(y=y, sr=sr).T, axis=0),
    }
    return features
