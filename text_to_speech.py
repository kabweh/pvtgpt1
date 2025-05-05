# ai_tutor_project/text_to_speech.py
from gtts import gTTS
from io import BytesIO

class TTS:
    @staticmethod
    def synthesize(text: str) -> bytes:
        tts = gTTS(text=text, lang="en")
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        return mp3_fp.getvalue()
