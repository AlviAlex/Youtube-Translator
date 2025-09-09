# 🎥 YouTube Translator (Flask + Pytube + Pydub)

This project lets you **download audio from YouTube**, **translate it into another language**, and **play back the translated audio** — all through a simple Flask + TailwindCSS web interface.

---

## 🚀 Features
- Download YouTube video audio
- Translate speech into a target language
- Listen to translated audio alongside the video
- Frontend styled with TailwindCSS + Three.js
- Flask backend (Python)

---

## 📦 Installation

### 1. Clone this repo
bash
git clone https://github.com/AlviAlex/Youtube-Translator.git

cd Youtube-Translator
2. Install Python (3.9+ recommended)
Make sure Python and pip are installed:

bash
Copy code
python --version
pip --version
3. Create and activate a virtual environment (optional but recommended)
bash
Copy code
python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate   # on Mac/Linux
4. Install required dependencies
bash
Copy code
pip install -r requirements.txt
If you don’t have a requirements.txt, install manually:

bash
Copy code
pip install flask pytube pydub googletrans==4.0.0-rc1
5. Install FFmpeg
This project needs FFmpeg for audio processing.

Download from: https://ffmpeg.org/download.html

Extract and add the /bin folder to your PATH environment variable.

Verify installation:

bash
Copy code
ffmpeg -version
ffprobe -version
▶️ Usage
Start the Flask app:

bash
Copy code
python app.py
Open your browser at:

cpp
Copy code
http://127.0.0.1:5000
Paste a YouTube link, choose a target language (like en, fr, hi, ml), and click Translate.

The app will:

Download audio from YouTube

Translate the spoken content

Play the translated audio while showing the video

🌍 Language Codes
Use the following codes when selecting translation language:

Language	Code
English	en
Hindi	hi
Malayalam	ml
French	fr
Spanish	es
German	de
Chinese	zh-cn
Japanese	ja

(Any language supported by Google Translate can be used.)

📂 Project Structure
csharp
Copy code
Youtube-Translator/
│── app.py            # Flask backend
│── templates/
│    └── index.html   # Frontend
│── static/           # Tailwind CSS, JS
│── requirements.txt  # Python dependencies
│── README.md         # Project docs
🛠️ Tech Stack
Backend: Flask, Python

Frontend: TailwindCSS, Three.js

APIs/Libraries: Pytube, Pydub, Googletrans

Audio Processing: FFmpeg
