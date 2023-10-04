import speech_recognition as sr
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds

    try:
        text = recognizer.recognize_google(audio)  # Recognize speech using Google Web Speech API
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        return f"Sorry, an error occurred: {e}"

# Call the function to recognize speech
detected_text = recognize_speech()

# Specify the directory where you want to store the text file
output_directory = "DetectedText"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Define the path to the text file
text_file_path = os.path.join(output_directory, "detected_text.txt")

# Write the detected text to the text file
with open(text_file_path, "w") as text_file:
    text_file.write(detected_text)

print("You said:", detected_text)
print(f"Detected text saved to: {text_file_path}")
