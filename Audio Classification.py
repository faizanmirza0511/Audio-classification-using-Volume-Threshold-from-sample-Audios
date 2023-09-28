#!/usr/bin/env python
# coding: utf-8

# In[7]:


import librosa
import librosa.display
import soundfile as sf
import numpy as np
import tempfile
import os
import shutil

# Create a temporary directory to store uploaded audio files
temp_dir = tempfile.TemporaryDirectory()

# Define a volume threshold
volume_threshold = 0.06  # Adjust this threshold as needed

# Create a function to classify audio based on volume
def classify_audio(audio_file):
    # Load the audio file
    audio, _ = librosa.load(audio_file, sr=None)
    
    # Calculate the root mean square (RMS) of the audio as a measure of volume
    rms = np.sqrt(np.mean(audio**2))
    
    # Classify audio based on volume threshold
    if rms > volume_threshold:
        return "happy"
    else:
        return "sad"

# Path to the folder containing audio files
audio_folder = "Sample Audio"  # Change this to the actual folder name

# Path to the output folders
output_folder_happy = "happy"
output_folder_sad = "sad"

# Create output folders if they don't exist
os.makedirs(output_folder_happy, exist_ok=True)
os.makedirs(output_folder_sad, exist_ok=True)

# List all audio files in the folder
audio_files = [os.path.join(audio_folder, file) for file in os.listdir(audio_folder) if file.endswith((".wav", ".mp3"))]

# Iterate through audio files, classify them, and move them to the appropriate folder
for audio_file in audio_files:
    emotion = classify_audio(audio_file)
    output_path = os.path.join(output_folder_happy if emotion == "happy" else output_folder_sad, os.path.basename(audio_file))
    
    # Copy the audio file to the appropriate folder
    shutil.copy(audio_file, output_path)
    
    display(Audio(audio_file, autoplay=True))
    print(f"Emotion: {emotion.capitalize()} - Output Path: {output_path}")

# Clean up the temporary directory
temp_dir.cleanup()

