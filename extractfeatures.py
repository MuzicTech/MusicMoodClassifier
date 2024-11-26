import os
import pandas as pd

# Directory of the dataset
DATASET_DIR = "dataset/"

# Define moods and initialize list to store data
moods = ["Happy", "Sad", "Energetic", "Calm"]
data = []

# Loop through each mood directory and each file
for mood in moods:
    folder_path = os.path.join(DATASET_DIR, mood)
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3") or filename.endswith(".wav"):
            file_path = os.path.join(folder_path, filename)
            features = extract_features(file_path)
            features["mood"] = mood
            data.append(features)

# Convert to DataFrame
df = pd.DataFrame(data)
print(df.head())

