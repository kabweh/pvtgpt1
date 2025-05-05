# ai_tutor_project/tts_component.py
import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
from text_to_speech import TTS

class TTSProcessor(AudioProcessorBase):
    def recv(self, frame):
        # placeholder for future streaming TTS
        return frame

def voice_playback(text: str):
    audio_bytes = TTS.synthesize(text)
    st.audio(audio_bytes, format='audio/mp3')
