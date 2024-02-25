Overview

This project is a Podcast Summarizer that utilizes two APIs - AssemblyAI and ListenNotes API. It allows users to enter an episode ID of a podcast, retrieves the audio file from ListenNotes API, transcribes it using AssemblyAI, and then generates a summary of the episode. The summary is displayed along with the transcript and key points.

Technologies Used

HTML
CSS
JavaScript
Python
Flask
Files

api_communication.py: This Python script handles communication with the AssemblyAI and ListenNotes APIs. It contains functions to transcribe audio, poll for transcription status, retrieve episode details, and save transcripts.
main.py: This is the main Flask application file. It routes requests and serves the HTML templates.
api_key.py: This file stores API keys for AssemblyAI and ListenNotes API. Please replace the placeholder values with your actual API keys.
Templates folder: Contains HTML template files.
index.html: The main HTML file where users interact with the application. It allows users to input the episode ID and displays the summary and transcript.
static folder: Contains CSS stylesheets.
styles.css: CSS styles for styling the HTML templates.
Setup Instructions

Install Python if not already installed.
Install Flask and requests by running:
Copy code
pip install Flask requests
Replace the placeholder API keys in api_key.py with your actual API keys.
Run main.py using Python:
css
Copy code
python main.py
Access the application through a web browser at http://localhost:5000.
Usage

Obtain the episode ID from ListenNotes website.
Enter the episode ID of the podcast you want to summarize.
Click on the "Get Episode Summary" button.
Wait for the summary to be generated. It may take a few minutes depending on the length of the episode.
Once the summary is ready, it will be displayed along with the transcript.
You can download the transcript by clicking on the "Download Transcript" link.
Note

The application may take some time to process longer episodes due to the transcription process.
Ensure a stable internet connection for smooth functioning.
Credits

AssemblyAI API: AssemblyAI
ListenNotes API: ListenNotes
License

This project is licensed under the MIT License.
