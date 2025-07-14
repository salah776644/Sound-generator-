import json
import time
import uuid
import requests
import random
from flask import Flask, render_template_string, request, jsonify, Response

app = Flask(__name__)

VOICES_PER_PAGE = 15

def Fix():
    try:
        url = "https://ai-voice.nyc3.cdn.digitaloceanspaces.com/data/data.json"
        headers = FOU()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('voices', [])
    except requests.exceptions.RequestException as e:
        return []

def Fox():
    Id_B7E1 = uuid.uuid4().hex
    start_time = str(int(time.time() * 1000))
    Id_B7E9 = uuid.uuid4().hex + ":APA91b"
    return Id_B7E1, start_time, Id_B7E9

def FOU():
    return {
        'User-Agent': "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.100 Mobile Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/json",
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': "?1",
        'origin': "http://localhost",
        'x-requested-with': "com.leonfiedler.voiceaj",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "http://localhost/",
        'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        'priority': "u=1, i"
    }

def ABC():
    try:
        U0 = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser"
        P0 = {'key': "AIzaSyDk5Vr0fvGX3AF3mNfMghP6Q-ECoBYT7aE"}
        P1 = json.dumps({"clientType": "CLIENT_TYPE_ANDROID"})
        B7E_com = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Build/RKQ1.201004.002)",
            'Connection': "Keep-Alive", 'Accept-Encoding': "gzip", 'Content-Type': "application/json",
            'X-Android-Package': "com.leonfiedler.voiceai", 'X-Android-Cert': "F6D71619262E74DC6BADD005D596BA9EC6543814",
            'Accept-Language': "ar-EG, en-US", 'X-Client-Version': "Android/Fallback/X23000000/FirebaseCore-Android",
            'X-Firebase-GMPID': "1:444011263758:android:acbabc2d1f24666531495f",
            'X-Firebase-Client': "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA"
        }
        O0O = requests.post(U0, params=P0, data=P1, headers=B7E_com)
        O0O.raise_for_status()
        data_signup = O0O.json()
        token2 = data_signup['idToken']
        Cc0 = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo"
        T0T = json.dumps({"idToken": token2})
        R0R = requests.post(Cc0, params=P0, data=T0T, headers=B7E_com)
        R0R.raise_for_status()
        D0 = R0R.json()
        Id_B7E2 = D0['users'][0]['localId']
        C9 = D0['users'][0]['createdAt']
        return token2, Id_B7E2, C9
    except requests.exceptions.RequestException as e:
        return None, None, None

def EFG(Id_B7E2, token2, Id_B7E1):
    try:
        url = "https://api.getvoices.ai/api/v1/user"
        payload = json.dumps({
            "uid": Id_B7E2, "isNew": True, "uuid": f"android_{Id_B7E1}",
            "platform": "android", "appVersion": "1.10.1"
        })
        headers = FOU()
        headers['authorization'] = token2
        requests.post(url, data=payload, headers=headers)
    except requests.exceptions.RequestException as e:
        pass

def HIG(Id_B7E2, token2, C9, Id_B7E1, Id_B7E9, B7E, text, ff, bb):
    try:
        url = "https://connect.getvoices.ai/api/v1/text2speech/stream"
        payload = json.dumps({
            "voiceId": B7E, "text": text, "deviceId": Id_B7E1, "uid": Id_B7E2,
            "lang": "ar", "platform": "android", "voice": bb, "voiceCategory": ff,
            "subscribed": 50000, "startTime": C9, "translate": None, "fcmToken": Id_B7E9,
            "appVersion": "1.10.1"
        })
        headers = FOU()
        headers['authorization'] = token2
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        return None

LANDING_PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#03DAC8">
    <title>SALAH_VICO_AI - تحويل النص إلى صوت</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --space-blue: #0a1128;
            --midnight-blue: #001f54;
            --cobalt-blue: #034078;
            --electric-blue: #1282a2;
            --light-blue: #4cc9f0;
            --neon-blue: #00f5d4;
            --dark-bg: #0a0a14;
            --card-bg: rgba(16, 22, 58, 0.8);
            --card-border: rgba(0, 247, 212, 0.15);
            --text-color: #f0f8ff;
            --text-secondary: #a0c8ff;
            --accent-color: #00f5d4;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Tajawal', sans-serif;
            background: linear-gradient(135deg, var(--dark-bg) 0%, var(--space-blue) 70%);
            color: var(--text-color);
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }
        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 10% 20%, rgba(0, 245, 212, 0.05) 0%, transparent 20%),
                radial-gradient(circle at 90% 80%, rgba(0, 247, 212, 0.05) 0%, transparent 20%),
                radial-gradient(circle at 50% 30%, rgba(10, 17, 40, 0.3) 0%, transparent 30%);
            z-index: -1;
        }
        .particle {
            position: absolute;
            border-radius: 50%;
            background: rgba(76, 201, 240, 0.1);
            z-index: -1;
            animation: float 15s infinite linear;
        }
        .hero {
            text-align: center;
            padding: 3rem 1.5rem;
            max-width: 900px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
            width: 100%;
        }
        .app-logo {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 1.5rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }
        .app-logo-icon {
            width: 100px;
            height: 100px;
            background: linear-gradient(135deg, var(--electric-blue), var(--neon-blue));
            border-radius: 25px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            box-shadow: 0 0 40px rgba(0, 245, 212, 0.4);
            animation: pulse 3s infinite;
        }
        .app-name {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(to right, var(--light-blue), var(--neon-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 1px;
            margin: 10px 0;
            text-shadow: 0 0 25px rgba(76, 201, 240, 0.3);
        }
        .app-tagline {
            color: var(--text-secondary);
            font-size: 1.8rem;
            margin-top: -0.5rem;
            text-shadow: 0 0 15px rgba(160, 200, 255, 0.3);
        }
        .hero p {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            line-height: 1.7;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            color: var(--text-secondary);
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2.5rem;
            max-width: 1200px;
            margin: 3rem auto;
            padding: 0 1.5rem;
            width: 100%;
        }
        .feature-card {
            background: var(--card-bg);
            border-radius: 25px;
            padding: 2.5rem;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 1px solid var(--card-border);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
            z-index: 1;
        }
        .feature-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(0, 245, 212, 0.1), transparent);
            transform: rotate(30deg);
            transition: 0.5s;
            z-index: -1;
        }
        .feature-card:hover::before {
            left: 50%;
        }
        .feature-card:hover {
            transform: translateY(-15px);
            box-shadow: 0 20px 50px rgba(0, 245, 212, 0.25);
            border: 1px solid var(--accent-color);
        }
        .feature-icon {
            font-size: 4.5rem;
            margin-bottom: 2rem;
            color: var(--neon-blue);
            text-shadow: 0 0 30px rgba(0, 245, 212, 0.6);
            animation: float 6s ease-in-out infinite;
        }
        .feature-card h3 {
            font-size: 2.2rem;
            margin-bottom: 1.5rem;
            color: var(--text-color);
        }
        .feature-card p {
            font-size: 1.3rem;
            color: var(--text-secondary);
            line-height: 1.7;
        }
        .cta-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            background: linear-gradient(135deg, var(--electric-blue), var(--neon-blue));
            color: #0a1128;
            padding: 1.5rem 3.5rem;
            border: none;
            border-radius: 60px;
            font-size: 1.8rem;
            font-weight: 700;
            text-decoration: none;
            margin-top: 3rem;
            cursor: pointer;
            transition: all 0.4s ease;
            box-shadow: 0 10px 35px rgba(0, 245, 212, 0.4);
            position: relative;
            overflow: hidden;
            animation: pulse-button 2s infinite alternate;
        }
        .cta-button:hover {
            transform: translateY(-8px);
            box-shadow: 0 15px 45px rgba(0, 245, 212, 0.6);
        }
        .cta-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            transition: 0.5s;
        }
        .cta-button:hover::before {
            left: 100%;
        }
        .cta-button i {
            font-size: 2.5rem;
            transition: transform 0.3s ease;
        }
        .cta-button:hover i {
            transform: scale(1.3);
        }
        .footer {
            margin-top: 4rem;
            text-align: center;
            padding: 2.5rem;
            font-size: 1.3rem;
            color: var(--text-secondary);
            width: 100%;
            border-top: 1px solid rgba(0, 245, 212, 0.1);
        }
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0px); }
        }
        @keyframes pulse {
            0% { transform: scale(1); box-shadow: 0 0 40px rgba(0, 245, 212, 0.4); }
            50% { transform: scale(1.05); box-shadow: 0 0 60px rgba(0, 245, 212, 0.6); }
            100% { transform: scale(1); box-shadow: 0 0 40px rgba(0, 245, 212, 0.4); }
        }
        @keyframes pulse-button {
            0% { box-shadow: 0 10px 35px rgba(0, 245, 212, 0.4); }
            100% { box-shadow: 0 10px 45px rgba(0, 245, 212, 0.6), 0 0 40px rgba(0, 245, 212, 0.4); }
        }
        .icon-3d {
            transform: perspective(600px) rotateY(15deg) rotateX(10deg);
            text-shadow: 4px 4px 15px rgba(0, 0, 0, 0.4);
            transition: transform 0.4s ease;
        }
        .icon-3d:hover {
            transform: perspective(600px) rotateY(-15deg) rotateX(-10deg);
        }
        @media (max-width: 1200px) { .app-logo-icon { width: 90px; height: 90px; font-size: 2.8rem; } .app-name { font-size: 3rem; } .app-tagline { font-size: 1.6rem; } .hero p { font-size: 1.4rem; } .feature-card { padding: 2rem; } .feature-icon { font-size: 4rem; } .feature-card h3 { font-size: 2rem; } .feature-card p { font-size: 1.2rem; } .cta-button { padding: 1.3rem 3rem; font-size: 1.6rem; } }
        @media (max-width: 992px) { .app-logo-icon { width: 85px; height: 85px; font-size: 2.5rem; } .app-name { font-size: 2.7rem; } .app-tagline { font-size: 1.5rem; } .hero p { font-size: 1.3rem; } .features { grid-template-columns: 1fr; gap: 2.2rem; } .cta-button { padding: 1.2rem 2.5rem; font-size: 1.5rem; } }
        @media (max-width: 768px) { .app-logo { flex-direction: column; gap: 1rem; } .app-logo-icon { width: 80px; height: 80px; font-size: 2.3rem; } .app-name { font-size: 2.5rem; } .app-tagline { font-size: 1.4rem; } .hero p { font-size: 1.2rem; } .feature-card { padding: 1.8rem; border-radius: 22px; } .feature-icon { font-size: 3.5rem; } .feature-card h3 { font-size: 1.8rem; } .feature-card p { font-size: 1.1rem; } .cta-button { padding: 1.1rem 2.2rem; font-size: 1.4rem; } .footer { padding: 2rem; font-size: 1.2rem; } }
        @media (max-width: 576px) { body { padding: 15px; } .hero { padding: 2rem 1rem; } .app-logo-icon { width: 75px; height: 75px; font-size: 2rem; } .app-name { font-size: 2.2rem; } .app-tagline { font-size: 1.3rem; } .hero p { font-size: 1.1rem; } .feature-card { padding: 1.5rem; border-radius: 20px; } .feature-icon { font-size: 3rem; margin-bottom: 1.5rem; } .feature-card h3 { font-size: 1.6rem; } .cta-button { padding: 1rem 2rem; font-size: 1.3rem; } .footer { padding: 1.5rem; font-size: 1.1rem; } }
        @media (max-width: 480px) { .app-name { font-size: 2rem; } .app-tagline { font-size: 1.2rem; } .hero p { font-size: 1rem; } .feature-card { padding: 1.3rem; } .feature-icon { font-size: 2.8rem; } .feature-card h3 { font-size: 1.5rem; } .feature-card p { font-size: 1rem; } .cta-button { padding: 0.9rem 1.8rem; font-size: 1.2rem; } .footer { padding: 1.2rem; font-size: 1rem; } }
    </style>
</head>
<body>
    <div id="particles-container"></div>
    <section class="hero">
        <div class="app-logo">
            <div class="app-logo-icon icon-3d"> <i class="fas fa-microphone-alt"></i> </div>
            <div>
                <h1 class="app-name">SALAH_VICO_AI</h1>
                <p class="app-tagline">تقنية الذكاء الاصطناعي لتحويل النص إلى صوت</p>
            </div>
        </div>
        <p>استخدم أحدث تقنيات الذكاء الاصطناعي لتحويل النص إلى صوت طبيعي بأكثر من 50 شخصية صوتية مختلفة. اجعل محتواك ينبض بالحياة ويصل إلى جمهورك بطريقة فريدة ومؤثرة.</p>
        <a href="/app" class="cta-button"> <i class="fas fa-play icon-3d"></i> ابدأ الرحلة الآن </a>
    </section>
    <section class="features">
        <div class="feature-card">
            <div class="feature-icon icon-3d"> <i class="fas fa-users"></i> </div>
            <h3>أصوات متعددة</h3>
            <p>مجموعة واسعة من الأصوات الطبيعية التي تناسب مختلف المحتويات والفئات المستهدفة</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon icon-3d"> <i class="fas fa-bolt"></i> </div>
            <h3>سرعة فائقة</h3>
            <p>تحويل النص إلى صوت في ثوانٍ معدودة دون تأخير، حتى مع النصوص الطويلة</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon icon-3d"> <i class="fas fa-volume-up"></i> </div>
            <h3>جودة عالية</h3>
            <p>أصوات طبيعية وواضحة بجودة استوديو احترافية</p>
        </div>
    </section>
    <footer class="footer">
        <p><i class="fas fa-code icon-3d"></i> تم التطوير بواسطة <strong>صلاح أحمدين</strong> &copy; 2025 جميع الحقوق محفوظة</p>
    </footer>
    <script>
        function createParticles() {
            const container = document.getElementById('particles-container');
            const particleCount = window.innerWidth < 768 ? 50 : 100;
            for (let i = 0; i < particleCount; i++) {
                const particle = document.createElement('div');
                particle.classList.add('particle');
                const size = Math.random() * 12 + 3;
                const posX = Math.random() * 100;
                const posY = Math.random() * 100;
                const duration = Math.random() * 20 + 15;
                const delay = Math.random() * 10;
                const color = `rgba(${Math.floor(Math.random()*100)}, ${Math.floor(Math.random()*200+55)}, ${Math.floor(Math.random()*255)}, ${Math.random()*0.2+0.1})`;
                particle.style.width = `${size}px`;
                particle.style.height = `${size}px`;
                particle.style.top = `${posY}%`;
                particle.style.left = `${posX}%`;
                particle.style.background = color;
                particle.style.animationDuration = `${duration}s`;
                particle.style.animationDelay = `${delay}s`;
                container.appendChild(particle);
            }
        }
        function setup3DIcons() {
            const icons = document.querySelectorAll('.icon-3d');
            icons.forEach(icon => {
                icon.addEventListener('mousemove', (e) => {
                    const rect = icon.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    const centerX = rect.width / 2;
                    const centerY = rect.height / 2;
                    const rotateY = 15 * ((x - centerX) / centerX);
                    const rotateX = -10 * ((y - centerY) / centerY);
                    icon.style.transform = `perspective(600px) rotateY(${rotateY}deg) rotateX(${rotateX}deg)`;
                });
                icon.addEventListener('mouseleave', () => {
                    icon.style.transform = 'perspective(600px) rotateY(15deg) rotateX(10deg)';
                });
            });
        }
        document.addEventListener('DOMContentLoaded', () => { createParticles(); setup3DIcons(); });
    </script>
</body>
</html>
"""

APP_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#03DAC8">
    <title>SALAH_VICO_AI - لوحة التحكم</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --dark-bg: #0a0a14; --space-blue: #0a1128; --card-bg: #10163a; --card-border: rgba(0, 245, 212, 0.2);
            --text-color: #f0f8ff; --text-secondary: #a0c8ff; --accent-color: #00f5d4; --accent-hover: #99fff2;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Tajawal', sans-serif; background: linear-gradient(135deg, var(--dark-bg) 0%, var(--space-blue) 100%);
            color: var(--text-color); display: flex; justify-content: center; align-items: flex-start; min-height: 100vh; padding: 20px;
        }
        .container {
            width: 100%; max-width: 900px; background: var(--card-bg); border: 1px solid var(--card-border);
            border-radius: 20px; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5); backdrop-filter: blur(10px);
            padding: 1.5rem; animation: fadeIn 0.8s ease-out;
        }
        header { text-align: center; margin-bottom: 2rem; border-bottom: 1px solid var(--card-border); padding-bottom: 1.5rem; }
        header .logo { display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 0.5rem; }
        header .logo i { font-size: 2rem; color: var(--accent-color); }
        header h1 {
            font-size: 2rem; font-weight: 700; background: linear-gradient(90deg, var(--text-color), var(--accent-color));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        header p { font-size: 1rem; color: var(--text-secondary); }
        h2 { font-size: 1.4rem; color: var(--accent-color); margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.7rem; }
        .hidden { display: none !important; }
        .voice-grid {
            display: grid; grid-template-columns: repeat(auto-fill, minmax(110px, 1fr)); gap: 1rem; margin-bottom: 2rem;
        }
        .voice-card {
            background: rgba(0,0,0,0.2); border: 1px solid transparent; border-radius: 12px; padding: 1rem;
            text-align: center; cursor: pointer; transition: transform 0.3s, background 0.3s, border-color 0.3s;
        }
        .voice-card:hover { transform: translateY(-5px); background: rgba(0, 245, 212, 0.1); border-color: var(--card-border); }
        .voice-card img { width: 70px; height: 70px; border-radius: 50%; object-fit: cover; margin-bottom: 0.75rem; border: 2px solid var(--accent-color); }
        .voice-card span { font-size: 0.9rem; font-weight: 500; display: block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .pagination { display: flex; justify-content: center; gap: 1rem; }
        .pagination a {
            padding: 0.6rem 1.2rem; background: rgba(0,0,0,0.3); color: var(--text-secondary); text-decoration: none;
            border-radius: 8px; font-weight: 500; transition: background 0.3s, color 0.3s;
        }
        .pagination a:hover { background: var(--accent-color); color: var(--dark-bg); }
        .section-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }
        .selected-voice-display {
            display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem; background: rgba(0,0,0,0.2);
            padding: 0.75rem 1rem; border-radius: 10px; border-left: 4px solid var(--accent-color);
        }
        .selected-voice-display img { width: 40px; height: 40px; border-radius: 50%; }
        .selected-voice-display span { font-weight: 700; font-size: 1.1rem; }
        textarea {
            width: 100%; height: 150px; padding: 1rem; border-radius: 10px; border: 1px solid var(--card-border);
            font-size: 1rem; font-family: 'Tajawal', sans-serif; resize: vertical; background: rgba(0,0,0,0.2);
            color: var(--text-color); transition: border-color 0.3s, box-shadow 0.3s;
        }
        textarea:focus { border-color: var(--accent-color); outline: none; box-shadow: 0 0 15px rgba(0, 245, 212, 0.2); }
        .button {
            display: inline-flex; align-items: center; justify-content: center; gap: 0.7rem; padding: 0.8rem 1.5rem;
            border-radius: 8px; font-size: 1rem; font-weight: 700; cursor: pointer; transition: transform 0.2s, box-shadow 0.2s;
            border: none;
        }
        .button.primary { background: var(--accent-color); color: var(--dark-bg); width: 100%; margin-top: 1rem; }
        .button.primary:hover { background: var(--accent-hover); box-shadow: 0 0 20px rgba(0, 245, 212, 0.4); transform: translateY(-3px); }
        .button.secondary { background: transparent; border: 1px solid var(--text-secondary); color: var(--text-secondary); }
        .button.secondary:hover { background: rgba(255,255,255,0.1); color: var(--text-color); border-color: var(--text-color); }
        .loader { text-align: center; margin-top: 1.5rem; }
        .loader .spinner {
            border: 4px solid rgba(255, 255, 255, 0.2); border-top: 4px solid var(--accent-color);
            border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: auto;
        }
        .loader p { margin-top: 0.5rem; font-size: 0.9rem; color: var(--text-secondary); }
        audio { width: 100%; margin-top: 1.5rem; border-radius: 8px; }
        .modal-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(10, 10, 20, 0.85); backdrop-filter: blur(5px);
            display: flex; justify-content: center; align-items: center; z-index: 1000;
            animation: fadeIn 0.3s ease;
        }
        .modal-content {
            background: var(--card-bg); border: 1px solid var(--card-border);
            border-radius: 15px; padding: 2rem; width: 90%; max-width: 450px;
            text-align: center; position: relative;
            box-shadow: 0 5px 30px rgba(0, 245, 212, 0.2);
        }
        .modal-content .close-btn {
            position: absolute; top: 10px; left: 15px;
            background: none; border: none; font-size: 2rem;
            color: var(--text-secondary); cursor: pointer; transition: color 0.3s;
        }
        .modal-content .close-btn:hover { color: var(--text-color); }
        .modal-content h3 { font-size: 1.5rem; color: var(--accent-color); margin-bottom: 0.5rem; }
        .modal-content p { color: var(--text-secondary); margin-bottom: 1.5rem; }
        .social-links { display: flex; flex-direction: column; gap: 1rem; margin-bottom: 1.5rem; }
        .social-btn {
            display: flex; align-items: center; justify-content: center; gap: 10px;
            padding: 0.8rem; text-decoration: none; border-radius: 8px;
            font-size: 1.1rem; font-weight: 700; transition: transform 0.2s;
        }
        .social-btn i { font-size: 1.3rem; }
        .social-btn.telegram { background: #2AABEE; color: white; }
        .social-btn.facebook { background: #1877F2; color: white; }
        .social-btn:hover { transform: scale(1.05); }
        .countdown { color: var(--text-secondary); font-size: 0.9rem; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        @media (max-width: 600px) {
            body { padding: 10px; } .container { padding: 1rem; }
            header h1 { font-size: 1.5rem; } h2 { font-size: 1.2rem; }
            .voice-grid { grid-template-columns: repeat(auto-fill, minmax(90px, 1fr)); gap: 0.75rem; }
            .voice-card { padding: 0.75rem; } .voice-card img { width: 60px; height: 60px; }
            .section-header { flex-direction: column; align-items: flex-start; gap: 0.75rem; }
        }
    </style>
</head>
<body>
    <div id="ad-modal" class="modal-overlay hidden">
        <div class="modal-content">
            <button id="close-ad-btn" class="close-btn">&times;</button>
            <h3>تابع المطور صلاح أحمدين</h3>
            <p>للحصول على آخر التحديثات والأدوات الحصرية.</p>
            <div class="social-links">
                <a href="https://t.me/DesignerSalahAhmadyn" target="_blank" class="social-btn telegram">
                    <i class="fab fa-telegram"></i> تليجرام
                </a>
                <a href="https://www.facebook.com/share/19PSU6vHWu/" target="_blank" class="social-btn facebook">
                    <i class="fab fa-facebook"></i> فيسبوك
                </a>
            </div>
            <div class="countdown">سيستمر التوليد خلال <span id="ad-countdown">10</span> ثوانٍ...</div>
        </div>
    </div>
    <div class="container">
        <header>
            <a href="/" style="text-decoration: none; color: inherit;">
                <div class="logo">
                    <i class="fas fa-microphone-alt"></i>
                    <h1>SALAH_VICO_AI</h1>
                </div>
            </a>
            <p>حوّل النص إلى صوت واقعي باستخدام الذكاء الاصطناعي</p>
        </header>
        <main id="main-content">
            <section id="voice-selection-section">
                <h2><i class="fas fa-users"></i>1. اختر شخصية صوتية</h2>
                <div class="voice-grid">
                    {% for voice in voices %}
                    <div class="voice-card" onclick='selectVoice({{ voice | tojson | safe }})'>
                        <img src="https://ai-voice.nyc3.cdn.digitaloceanspaces.com/voice_images/{{ voice.image_ios.split("/")[-1] if voice.image_ios else "" }}" 
                             alt="{{ voice.name }}"
                             onerror="this.onerror=null;this.src='https://ui-avatars.com/api/?name={{ voice.name[0] | urlencode }}&background=0a1128&color=00f5d4&size=70';">
                        <span>{{ voice.name }}</span>
                    </div>
                    {% endfor %}
                </div>
                <div class="pagination">
                    {% if page > 1 %}
                        <a href="/app?page={{ page - 1 }}"><i class="fas fa-arrow-right"></i> السابق</a>
                    {% endif %}
                    {% if voices|length == 15 %}
                        <a href="/app?page={{ page + 1 }}">التالي <i class="fas fa-arrow-left"></i></a>
                    {% endif %}
                </div>
            </section>
            <section id="text-input-section" class="hidden">
                <div class="section-header">
                    <h2><i class="fas fa-keyboard"></i>2. أدخل النص والصوت</h2>
                    <button id="back-btn" class="button secondary"><i class="fas fa-arrow-left"></i> تغيير</button>
                </div>
                <div class="selected-voice-display">
                    <img id="selected-voice-img" src="" alt="Selected Voice">
                    <span id="selected-voice-name"></span>
                </div>
                <form id="tts-form">
                    <input type="hidden" id="selected-voice-data" name="voice_data">
                    <textarea id="text-input" name="text" required maxlength="6000">مرحبا بكم في موقع SALAH_VICO_AI هذا الموقع الخ.... 
تم تطوير هذا الموقع بواسطة المطور صلاح أحمدين</textarea>
                    <button type="submit" class="button primary"><i class="fas fa-volume-up"></i> توليد الصوت</button>
                </form>
                <div id="loader" class="loader hidden">
                    <div class="spinner"></div>
                    <p>جاري التحويل...</p>
                </div>
                <audio id="audio-player" class="hidden" controls></audio>
            </section>
        </main>
        <footer>
            <p><i class="fas fa-code"></i> تم التطوير بواسطة <strong>صلاح أحمدين</strong> &copy; 2025</p>
        </footer>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const voiceSelectionSection = document.getElementById('voice-selection-section');
            const textInputSection = document.getElementById('text-input-section');
            const ttsForm = document.getElementById('tts-form');
            const loader = document.getElementById('loader');
            const audioPlayer = document.getElementById('audio-player');
            const backBtn = document.getElementById('back-btn');
            const adModal = document.getElementById('ad-modal');
            const closeAdBtn = document.getElementById('close-ad-btn');
            const adCountdownSpan = document.getElementById('ad-countdown');
            let countdownInterval;
            let generationHasStarted = false;

            window.selectVoice = function(voiceData) {
                voiceSelectionSection.classList.add('hidden');
                textInputSection.classList.remove('hidden');
                textInputSection.style.animation = 'fadeIn 0.5s';
                document.getElementById('selected-voice-name').innerText = voiceData.name;
                const imgElement = document.getElementById('selected-voice-img');
                const defaultAvatar = `https://ui-avatars.com/api/?name=${encodeURIComponent(voiceData.name[0])}&background=0a1128&color=00f5d4&size=40`;
                imgElement.src = voiceData.image_ios ? `https://ai-voice.nyc3.cdn.digitaloceanspaces.com/voice_images/${voiceData.image_ios.split('/').pop()}` : defaultAvatar;
                imgElement.onerror = () => { imgElement.src = defaultAvatar; };
                document.getElementById('selected-voice-data').value = JSON.stringify(voiceData);
                window.scrollTo({ top: 0, behavior: 'smooth' });
            };
            
            backBtn.addEventListener('click', () => {
                textInputSection.classList.add('hidden');
                voiceSelectionSection.classList.remove('hidden');
                voiceSelectionSection.style.animation = 'fadeIn 0.5s';
                audioPlayer.classList.add('hidden');
                audioPlayer.src = '';
            });
            
            const proceedWithGeneration = async () => {
                if (generationHasStarted) return;
                generationHasStarted = true;
                clearInterval(countdownInterval);
                adModal.classList.add('hidden');
                loader.classList.remove('hidden');
                audioPlayer.classList.add('hidden');
                audioPlayer.src = '';
                try {
                    const text = document.getElementById('text-input').value;
                    const voiceData = document.getElementById('selected-voice-data').value;
                    const response = await fetch('/generate', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ text: text, voice_data: voiceData })
                    });
                    if (!response.ok) {
                        const errorData = await response.json();
                        throw new Error(errorData.error || 'حدث خطأ في استجابة الخادم');
                    }
                    const audioBlob = await response.blob();
                    const audioUrl = URL.createObjectURL(audioBlob);
                    audioPlayer.src = audioUrl;
                    audioPlayer.classList.remove('hidden');
                    audioPlayer.play();
                } catch (error) {
                    alert(`فشل توليد الصوت: ${error.message}`);
                } finally {
                    loader.classList.add('hidden');
                }
            };

            ttsForm.addEventListener('submit', (e) => {
                e.preventDefault();
                const text = document.getElementById('text-input').value;
                if (!text.trim()) { alert('الرجاء إدخال نص.'); return; }
                
                generationHasStarted = false;
                adModal.classList.remove('hidden');
                let countdown = 10;
                adCountdownSpan.textContent = countdown;
                
                countdownInterval = setInterval(() => {
                    countdown--;
                    adCountdownSpan.textContent = countdown;
                    if (countdown <= 0) {
                        proceedWithGeneration();
                    }
                }, 1000);
            });
            
            closeAdBtn.addEventListener('click', proceedWithGeneration);
        });
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def landing_page():
    return render_template_string(LANDING_PAGE)

@app.route('/app', methods=['GET'])
def app_page():
    try:
        page = int(request.args.get('page', 1))
        if page < 1: page = 1
    except ValueError:
        page = 1
    
    all_voices = Fix()
    if not all_voices:
        return "<h1>لا يمكن جلب الأصوات حاليًا. يرجى المحاولة مرة أخرى لاحقًا.</h1>", 500
        
    start_idx = (page - 1) * VOICES_PER_PAGE
    end_idx = start_idx + VOICES_PER_PAGE
    paginated_voices = all_voices[start_idx:end_idx]

    return render_template_string(APP_TEMPLATE, voices=paginated_voices, page=page)

@app.route('/generate', methods=['POST'])
def generate_audio():
    try:
        data = request.get_json()
        text = data.get('text')
        voice_data_str = data.get('voice_data')
        
        if not text or not voice_data_str:
            return jsonify({"error": "بيانات غير مكتملة."}), 400

        if len(text) > 6000:
            return jsonify({"error": "النص يتجاوز الحد المسموح به (6000 حرف)."}), 400
            
        B7E = json.loads(voice_data_str)
        ff = B7E.get('category') 
        bb = B7E.get('7847383702:AAEjFGjND24DEp6qZcVl_SEMo6ASixxkzW8')
        
        Id_B7E1, start_time, Id_B7E9 = Fox()
        token2, Id_B7E2, C9 = ABC()
        
        if not (token2 and Id_B7E2 and C9):
            return jsonify({"error": "فشل في عملية المصادقة."}), 500
            
        EFG(Id_B7E2, token2, Id_B7E1)
        audio_data = HIG(Id_B7E2, token2, C9, Id_B7E1, Id_B7E9, B7E['voiceId'], text, ff, bb)
        
        if audio_data:
            return Response(audio_data, mimetype='audio/mpeg')
        else:
            return jsonify({"error": "فشل في توليد الملف الصوتي من المصدر."}), 500

    except Exception as e:
        return jsonify({"error": f"حدث خطأ داخلي في الخادم: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5065, debug=False)
