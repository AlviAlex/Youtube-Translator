# app.py

import os
import uuid
from flask import Flask, render_template, request, jsonify, send_file
from pydub import AudioSegment
import whisper
from deep_translator import GoogleTranslator
from gtts import gTTS
import yt_dlp

app = Flask(__name__)
os.makedirs("audios", exist_ok=True)

# Set ffmpeg path for pydub
AudioSegment.converter = r"C:\Users\Alvin\Downloads\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\Users\Alvin\Downloads\ffmpeg-8.0-essentials_build\bin\ffprobe.exe"

# Load Whisper once (CPU-friendly tiny model)
model = whisper.load_model("tiny")

# Supported languages for user convenience
LANGUAGES = {
    "ml": "Malayalam",
    "hi": "Hindi",
    "ta": "Tamil",
    "en": "English",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
}

@app.route("/")
def index():
    return render_template("index.html", languages=LANGUAGES)

@app.route("/translate", methods=["POST"])
def translate_audio():
    data = request.form
    yt_url = data.get("yt_url")
    target_lang = data.get("target_lang")

    if not yt_url or target_lang not in LANGUAGES:
        return jsonify({"error": "Invalid input"}), 400

    try:
        # 1️⃣ Download audio
        temp_audio_file = f"audios/temp_{uuid.uuid4().hex}.mp3"
        ydl_opts = {'format': 'bestaudio/best', 'outtmpl': temp_audio_file, 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])

        # 2️⃣ Convert to WAV
        wav_file = temp_audio_file.replace(".mp3", ".wav")
        audio = AudioSegment.from_file(temp_audio_file)
        audio.export(wav_file, format="wav")

        # 3️⃣ Transcribe using Whisper
        result = model.transcribe(wav_file)
        english_text = result["text"].strip()

        # 4️⃣ Translate to target language
        translated_text = GoogleTranslator(source='auto', target=target_lang).translate(english_text)

        # 5️⃣ Convert to speech
        output_file = f"audios/translated_{target_lang}_{uuid.uuid4().hex}.mp3"
        tts = gTTS(translated_text, lang=target_lang)
        tts.save(output_file)

        # 6️⃣ Clean temp files
        os.remove(temp_audio_file)
        os.remove(wav_file)

        return jsonify({"audio_file": output_file, "text": translated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/audios/<filename>")
def serve_audio(filename):
    return send_file(os.path.join("audios", filename), as_attachment=False)

if __name__ == "__main__":
    app.run(debug=True)
