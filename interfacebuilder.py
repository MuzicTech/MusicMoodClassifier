song_path = input("Enter the path to the song file: ")
features = extract_features(song_path)
mood_prediction = clf.predict([features])
print("Predicted Mood:", mood_prediction[0])
