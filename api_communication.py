import requests
import json
import time
from api_key import API_KEY_ASSEMBLYAI, API_KEY_LISTENNOTES


#2
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'
headers_assemblyai = {
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}

listennotes_episode_endpoint = 'https://listen-api.listennotes.com/api/v2/episodes'
headers_listennotes = {
    'X-ListenAPI-Key': API_KEY_LISTENNOTES,
}

def get_episode_audio_url(episode_id):
    url = f"{listennotes_episode_endpoint}/{episode_id}"
    response = requests.get(url, headers=headers_listennotes)
    response.raise_for_status()  # Raise an exception for bad status codes
    data = response.json()

    episode_title = data['title']
    thumbnail = data['thumbnail']
    podcast_title = data['podcast']['title']
    audio_url = data['audio']
    return audio_url, thumbnail, podcast_title, episode_title

def transcribe(audio_url, auto_chapters):
    transcript_request = {
        'audio_url': audio_url,
        'auto_chapters': auto_chapters
    }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers_assemblyai)
    transcript_response.raise_for_status()  # Raise an exception for bad status codes
    transcript_id = transcript_response.json()['id']
    return transcript_id

def poll(transcript_id):
    polling_endpoint = f"{transcript_endpoint}/{transcript_id}"
    polling_response = requests.get(polling_endpoint, headers=headers_assemblyai)
    polling_response.raise_for_status()  # Raise an exception for bad status codes
    return polling_response.json()

def get_transcription_result_url(audio_url, auto_chapters):
    transcript_id = transcribe(audio_url, auto_chapters)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']

        print("waiting for 60 seconds")
        time.sleep(60)

def save_transcript(episode_id):
    audio_url, thumbnail, podcast_title, episode_title = get_episode_audio_url(episode_id)
    data, error = get_transcription_result_url(audio_url, auto_chapters=True)
    
    if data:
        filename = f"{episode_id}.txt"
        with open(filename, 'w') as f:
            f.write(data['text'])

        filename = f"{episode_id}_chapters.json"
        with open(filename, 'w') as f:
            chapters = data['chapters']
            episode_data = {
                'chapters': chapters,
                'audio_url': audio_url,
                'thumbnail': thumbnail,
                'podcast_title': podcast_title,
                'episode_title': episode_title
            }
            json.dump(episode_data, f, indent=4)
            print('Transcript saved')
            return True
    elif error:
        print("Error:", error)
        return False

