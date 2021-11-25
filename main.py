import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/somin/Downloads/speechtotext-test-332804-89164e1e57dc.json'
speech_client = speech.SpeechClient()

# EXAMPLE 1,2. Transcribe Local Media File
# File Size <10 mbs, length < 1 minute

media_file_name_mp3 = 'audio-short.mp3'
media_file_name_wav = 'audio-short.wav'

##Step 1. Load the media files
with open(media_file_name_mp3, 'rb') as f1:
    byte_data_mp3 = f1.read()
audio_mp3 = speech.RecognitionAudio(content=byte_data_mp3)

with open(media_file_name_mp3, 'rb') as f2:
    byte_data_wav = f2.read()
audio_wav = speech.RecognitionAudio(content=byte_data_wav)

##Step 2. Configure Media Files Output
config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz = 48000,
    enable_automatic_punctuation = True,
    language_code = 'en-US'
)

config_wav = speech.RecognitionConfig(
    sample_rate_hertz = 44100,
    enable_automatic_punctuation = True,
    language_code = 'en-US',
    audio_channel_count = 2
)
##Step 3. Transcribing the RecognitionAudio Objects
response_standard_mp3 = speech_client.recognize(
    config=config_mp3,
    audio=audio_mp3
)

response_standard_wav = speech_client.recognize(
    config=config_wav,
    audio=audio_wav
)

print(response_standard_mp3)
print(response_standard_wav)

# EXAMPLE 3: Transcribing a Long media File
# media_uri = 'gs://example-stt-test1/example-long.mp3'
##Step 1. Load the media files
media_uri = 'gs://example-stt-test1/rprogramming-accent.mp3'
long_audi_wav = speech.RecognitionAudio(uri=media_uri)

##Step 2. Configure Media Files Output
config_wav_enhanced = speech.RecognitionConfig(
    sample_rate_hertz = 48000,
    enable_automatic_punctuation = True,
    language_code = 'en-US',
    use_enhanced = True,
    model = 'video'
)

##Step 3. Transcribing the RecognitionAudio Objects
operation = speech_client.long_running_recognize(
    config = config_wav_enhanced,
    audio =long_audi_wav
)

response = operation.result(timeout=150)
print(response)

for result in response.results:
    print(result.alternatives[0].transcript)
    print(result.alternatives[0].confidence)
    print()