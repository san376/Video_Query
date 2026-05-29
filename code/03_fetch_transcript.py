from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

video_id = "Gfr50f6ZBvo"

try:
    ytt_api = YouTubeTranscriptApi()
    transcript_obj = ytt_api.fetch(video_id)
    full_text = " ".join(chunk.text for chunk in transcript_obj)
    print(full_text)

except NoTranscriptFound:
    transcript_list = ytt_api.list(video_id)
    transcript = next(iter(transcript_list))
    transcript_obj = transcript.fetch()
    full_text = " ".join(chunk.text for chunk in transcript_obj)
    print(full_text)

except TranscriptsDisabled:
    print("No captions available for this video.")

print(transcript_obj)
