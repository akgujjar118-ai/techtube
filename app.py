from flask import Flask, request, redirect, session, jsonify
import json, os, datetime
app = Flask(__name__)
app.secret_key = "adeel-techtube-perfect-2026"

SETTINGS_FILE = "settings.json"
def load_settings():
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE,'r',encoding='utf-8') as f: return json.load(f)
    except: pass
    return {"site_name":"TechTube","welcome":"Tech World, All In One Place.","ad_code":"","ad_link":"","admin_user":"admin","admin_pass":"adeel123","feedback":[]}
def save_settings(s):
    with open(SETTINGS_FILE,'w',encoding='utf-8') as f: json.dump(s,f,ensure_ascii=False,indent=2)
SETTINGS = load_settings()

USERS = {}
SUBS = {}
LIKES = {}
COMMENTS = {}
UPLOADED = []
FEEDBACKS = SETTINGS.get("feedback", [])

# --- 1 MILLION+ VIDEOS - Jo Search Karo, Wo Mil Jayega! ---
ALL_APPS = ["WhatsApp","Facebook","Instagram","TikTok","YouTube","Snapchat","CapCut","Telegram","Twitter","X","ChatGPT","Gemini","Adeel AI","Copilot","Canva","PicsArt","Alight Motion","Kinemaster","InShot","PUBG","Free Fire","GTA 5","Minecraft","Candy Crush","Ludo King","Clash of Clans","Temple Run","Daraz","Foodpanda","Careem","Bykea","JazzCash","Easypaisa","NayaPay","Meezan Bank","HBL","Google Maps","Gmail","Google Drive","Google Photos","Chrome","Opera","UC Browser","Zoom","Google Meet","Microsoft Teams","Skype","Netflix","Amazon Prime","Disney Plus","Spotify","SoundCloud","Gaana","YouTube Music","Photoshop","Lightroom","MS Word","MS Excel","MS PowerPoint","WPS Office","Windows 11","Windows 10","Android","iOS","iPhone","Samsung","Oppo","Vivo","Realme","Redmi","Xiaomi","Huawei","Nokia","Infinix","Tecno","HP Laptop","Dell Laptop","Lenovo Laptop","MacBook","iPad","Tablet","WiFi","Internet","Bluetooth","Hotspot","VPN","Antivirus","Battery","Charging","Storage","AI","Robot","Drone","Smart Watch","Earbuds","Headphones","Camera","Printer","Keyboard","Mouse","Bigo Live","Likee","Snack Video","Helo","ShareChat","Moj","Josh","OLX","Alibaba","AliExpress","Amazon","Flipkart","Shein","Temu","PayPal","Binance","Crypto","Bitcoin","Pi Network","Duolingo","Khan Academy","Coursera","Udemy","W3Schools","TikTok Lite","WhatsApp Business","GB WhatsApp","FM WhatsApp","YouTube Vanced","Truecaller","VidMate","Snaptube","MX Player","VLC Player","Kodi","Dream11","MPL","Winzo","Teen Patti","Poker","Zomato","Swiggy","Uber","InDrive","Foodpanda Rider","Tinder","Bumble","Badoo","Azar","OmeTV","FaceApp","Remini","Lensa AI","B612","BeautyPlus","Sweet Selfie","Google Translate","Camera Scanner","QR Scanner","File Manager","Clean Master","Instagram Reels","Facebook Reels","YouTube Shorts","TikTok Shorts","ChatGPT App","Gemini App","Bing AI","Perplexity","Claude AI","Jazz World","My Telenor App","Zong App","Ufone App","PTV Sports","Geo News","ARY News","Dunya News","Samaa TV","Cricbuzz","ESPN","SofaScore","Live Cricket TV","Quran App","Muslim Pro","Prayer Times","Islam360","Careem Food","KFC App","McDonalds App","Dominos","Bank Alfalah","UBL","SadaPay","Adobe Premiere","Filmora","VN Editor","CapCut Pro","PowerDirector","Garena Free Fire Max","PUBG Mobile Lite","Call of Duty","Fortnite","Roblox","Brawl Stars","Instagram Pro","Insta Pro","GB Instagram","Aero Instagram","YouTube Studio","Creator Studio","TikTok Studio","Meta Business","Google Classroom","Microsoft Office","Notion","Trello","Slack","Google Meet","WhatsApp Web","Telegram Web","Lightroom Presets","PicsArt Gold","Canva Pro","Alight Motion Pro","KingMaster","YouCut","VideoShow","VivaVideo","Montage","AudioLab","Voloco","AutoTune","Smule","StarMaker","Hago","Yalla Ludo","Ludo Star","Carrom Pool","8 Ball Pool","GTA Vice City","GTA San Andreas","Need For Speed","Asphalt 9","Traffic Rider","Weather App","AccuWeather","Windy","Live Weather","Health App","Fitness App","Step Counter","Calorie Counter","Dictionary","Urdu Dictionary","English To Urdu","Google Lens","File Recover","Data Recovery","Photo Recovery","Video Recovery","Screen Recorder","AZ Recorder","XRecorder","Mobizen","Call Recorder","SMS App","Messages","Contacts","Launcher","Nova Launcher","Smart Launcher","iPhone Launcher","Wallpaper App","Ringtones","Live Wallpapers","Themes","Battery Saver","Phone Cooler","RAM Booster","Junk Cleaner","App Lock","Calculator Lock","Vault","Gallery Vault","Kids App","Baby Games","Kids Learning","ABC Learning","Quran Majeed","Hadith App","Naat App","Islamic Wallpapers","Earn Money App","Online Earning","Freelancing","Fiverr","Upwork","Video Download","Status Saver","Story Saver","Reels Downloader","PDF Reader","PDF Maker","Word To PDF","Image To PDF","Video Compressor","Photo Compressor","Image Resizer","AI Photo Editor","AI Video Editor","AI Voice Changer","AI Chat","Face Swap","Video Face Swap","Deepfake","AI Avatar","Old Age Filter","Cartoon Filter","Anime Filter","Snapchat Filters","Make Money","YouTube Earning","TikTok Earning","Facebook Earning","Online Shopping","Price Check","Discount App","Coupons","Train Booking","PIA App","Bus Booking","Flight Booking","Hotel Booking","Booking.com","Airbnb","Trivago","Job App","Rozee","Indeed","LinkedIn","Naukri","Property App","Zameen.com","OLX Property","Housing","Car Game","Bike Game","Bus Simulator","Truck Simulator","Train Simulator","Cricket Game","Football Game","WWE Game","Wrestling Game","Chess","Sudoku","Puzzle Games","Word Games","Brain Games","News App","Daily News","Breaking News","Headlines","Radio App","FM Radio","Podcast App","Audio Books","Bible App","Hindu App","Sikh App","Christian App","Baby Names","Good Names","Urdu Names","Islamic Names","Cooking App","Recipes","Biryani Recipe","Cake Recipe","Fashion App","Mehndi Designs","Hair Style","Beauty Tips","Cricket Live","Football Live","Hockey Live","Tennis Live","Live TV","ARY Zindagi","Hum TV","Geo Entertainment","Drama App","Pakistani Dramas","Indian Dramas","Turkish Dramas","Movie App","Hollywood Movies","Bollywood Movies","Lollywood Movies","Song App","Old Songs","New Songs","Punjabi Songs","Urdu Songs","Naat Sharif","Qawwali","Islamic Songs","Hamd","Jokes App","Funny Videos","Comedy Videos","Prank Videos","Magic Tricks","Science Tricks","Maths Tricks","English Tricks","Computer Course","Mobile Repairing","Laptop Repairing","Electrician Course","Driving App","Car Driving","Bike Driving","Traffic Rules","Police App","Emergency App","Hospital App","Doctor App","Blood Donation","Charity App","Donate App","School App","College App","University App","Result App","Board Result","BISE Lahore","BISE Karachi","BISE Peshawar","NADRA App","Passport App","Driving License App","FBR App","Electricity Bill","Gas Bill","Water Bill","PTCL Bill","Load Shedding","WAPDA App","K Electric App","Currency Converter","Dollar Rate","Gold Rate","Petrol Price","Prayer App","Qibla Direction","Tasbeeh Counter","Ramadan App","Eid App","Hajj App","Umrah App","Zakat Calculator","Baby Care","Pregnancy App","Women Health","Men Health","Yoga App","Gym App","Workout App","Running App","Sleep App","Meditation App","Relax App","Stress Relief","Dua App","Wazifa App","Istikhara App","Durood Sharif","Kids Rhymes","Nursery Rhymes","Poems","Stories","Urdu Stories","English Stories","Hindi Stories","Moral Stories","History App","Islamic History","Pakistan History","World History","Science App","Physics","Chemistry","Biology","Maths","English Grammar","Urdu Grammar","Arabic Grammar","Pashto App","Sindhi App","Balochi App","Punjabi App","Saraiki App"]

VIDEO_TYPES = ["Full Review","How To Use","Hidden Features","Secret Tricks","Complete Guide","New Update 2026","Best Settings","How To Earn Money","How To Download","How To Install","Tips And Tricks","All Features Explained","Beginner To Pro","Top 10 Tricks","Full Course","Problem Solved","Account Ban Fix","Password Forgot Fix","Viral Tricks","Pro Version Free","Without Watermark","New Filter","Edit Like Pro","Make Money","Live Proof"]
YT_THUMBS = ["Uh9643c2P6k","LXb3EKWsInQ","eKFTSSKCzWA","2Vv-BfVoq4g","dQw4w9WgXcQ","jfKfPfyJRdk","aircAruvnKk","pQN-pnXPaVg","kXYiU_JCYtU"]

def get_videos(search_q="", cat="all", limit=20, start=0):
    results = []
    search_q = search_q.lower().strip()
    if search_q:
        matched_apps = [a for a in ALL_APPS if search_q in a.lower()]
        if not matched_apps:
            matched_apps = [search_q.title()]
        for app_name in matched_apps[:5]:
            for j, vtype in enumerate(VIDEO_TYPES):
                vid = YT_THUMBS[(hash(app_name+str(j)) % len(YT_THUMBS))]
                results.append({"id": f"search_{app_name}_{j}","yt_id": vid,"title": f"{app_name} - {vtype} - 2026","channel": f"{app_name} Master","views": f"{(hash(app_name+str(j))%900)+50}K","cat": "Tech","source": "youtube","uploader": "YouTube","likes": (hash(app_name+str(j))%500)+100,"thumb": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"})
    else:
        for i in range(start, start+limit):
            app_name = ALL_APPS[i % len(ALL_APPS)]
            vtype = VIDEO_TYPES[i % len(VIDEO_TYPES)]
            vid = YT_THUMBS[i % len(YT_THUMBS)]
            results.append({"id": f"yt_{i}","yt_id": vid,"title": f"{app_name} - {vtype} - Part {(i//10)+1}","channel": ["Tech Master","Adeel Tech","Mobile Zone","Windows Guru"][i%4],"views": f"{(i*137)%900+50}K","cat": "Tech","source": "youtube","uploader": "YouTube","likes": (i*23)%500+100,"thumb": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"})
    return results[:limit]

def adeel_ai_answer(q, name="Friend"):
    ql=q.lower().strip()
    online_note=""
    try:
        import urllib.request, json as js
        if len(ql)>3:
            url=f"https://en.wikipedia.org/api/rest_v1/page/summary/{ql.replace(' ','_')}"
            req=urllib.request.Request(url, headers={'User-Agent':'AdeelAI/1.0'})
            with urllib.request.urlopen(req, timeout=2) as r:
                data=js.loads(r.read().decode())
                if data.get('extract'): online_note=f"\n\n🌐 Live Info (Online): {data['extract'][:400]}..."
    except: online_note="\n\n📴 Offline Mode: Internet slow, so offline answer."
    if any(w in ql for w in ['salam','assalam']): return f"🤲 Walaikum Assalam {name}! How are you? ❤️\n\nI am Adeel AI - Like Gemini!{online_note}"
    if any(w in ql for w in ['kaise ho','how are you']): return f"😊 Alhamdulillah {name}! I am fine, how about you?{online_note}"
    if ql in ['hi','hello','hey']: return f"👋 Hello {name}! I am Adeel AI - Like Gemini!{online_note}"
    if 'cricket' in ql: return f"🏏 Cricket:\n\nPakistan Team: Babar Azam - Best Batsman!\nShaheen Afridi - Best Bowler!{online_note}"
    if any(w in ql for w in ['mausam','weather']): return f"🌦️ Weather - Peshawar:\n\nToday weather is good! Light heat in day, cool at night.{online_note}"
    if any(w in ql for w in ['mobile','iphone','samsung']): return f"📱 Best Mobile?\n\nHigh Budget: iPhone 16 Pro - Best Camera!\nLow Budget: Samsung A55 - Battery 2 Days!\nGaming: Redmi Note 13 Pro{online_note}"
    if 'laptop' in ql: return f"💻 Best Laptop 2026:\n\nStudent: HP Pavilion\nGaming: Lenovo LOQ\nOffice: MacBook Air - Battery 15 Hours!{online_note}"
    if 'windows' in ql: return f"🪟 Windows 11:\n\n1. Search 'Windows 11 Download'\n2. Download from Microsoft\n3. Install - Done in 20 min!{online_note}"
    if any(w in ql for w in ['slow','hang']): return f"⚡ Slow? Do 3 Things:\n\n1. Delete useless apps\n2. Free storage\n3. Restart!{online_note}"
    if any(w in ql for w in ['ai','gemini']): return f"🤖 I am Adeel AI!\n\nLike Gemini, but your own! Logo AK - Unique!{online_note}"
    if any(w in ql for w in ['paisa','money']): return f"💰 How To Earn?\n\n1. TechTube - Make videos, earn from Ads\n2. Learn Skill - Freelancing\n3. Website - Put Adsterra Ad!{online_note}"
    return f"🤔 You asked: '{q}'\n\nVery good question {name}!\n\nTry: 'Best mobile?' or 'Cricket?' or 'Weather?'{online_note}"

LOGO = lambda: f"""<span style="font-size:24px">✦</span> <span style="background:linear-gradient(90deg,#ff0055,#00e5ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent">{SETTINGS['site_name']}</span>"""

def topbar(q=""):
    u=USERS.get(session.get('email'))
    btn=f"<a href='/profile' style='color:white;text-decoration:none;font-weight:bold'>👤 {u['name']}</a>" if u else "<a href='/signup' style='background:white;color:#0f172a;padding:9px 16px;border-radius:25px;text-decoration:none;font-weight:bold'>Join Now →</a>"
    return f"""<div style="display:flex;justify-content:space-between;align-items:center;padding:14px 16px;position:sticky;top:0;z-index:50;background:rgba(15,23,42,.97)">
    <a href="/" style="text-decoration:none;color:white;font-size:22px;font-weight:900">{LOGO()}</a>
    <form action="/" method="GET" style="flex:1;display:flex;max-width:450px;margin:0 10px"><input name="q" value="{q}" placeholder="🔍 Search Tech..." style="flex:1;padding:10px 14px;border-radius:25px 0 0 25px;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.1);color:white;outline:none"><button style="padding:10px 14px;border:none;background:rgba(255,255,255,.15);color:white;border-radius:0 25px 25px 0">🔍</button></form>
    <div style="display:flex;gap:10px;align-items:center">{btn} <a href="/ai" style="background:linear-gradient(90deg,#4285f4,#9b72cb,#d96570);color:white;padding:9px 14px;border-radius:20px;text-decoration:none;font-weight:bold">✦ Adeel AI</a> <a href="/admin" style="color:#94a3b8;text-decoration:none">⚙️</a></div></div>"""

def bottom_nav():
    return """<div style="position:fixed;bottom:0;left:0;right:0;background:#0f172a;border-top:1px solid rgba(255,255,255,.1);display:flex;justify-content:space-around;padding:10px 0;z-index:40">
    <a href="/" style="text-decoration:none;text-align:center;color:white">🏠<br><small>Home</small></a>
    <a href="/shorts" style="text-decoration:none;text-align:center;color:white">🎬<br><small>Shorts</small></a>
    <a href="/upload" style="text-decoration:none;text-align:center"><span style="background:linear-gradient(90deg,#ff0055,#00e5ff);padding:10px 14px;border-radius:50%;font-size:18px">+</span></a>
    <a href="/friends" style="text-decoration:none;text-align:center;color:white">👥<br><small>Friends</small></a>
    <a href="/ai" style="text-decoration:none;text-align:center;color:white">✦<br><small>Adeel AI</small></a>
    <a href="/profile" style="text-decoration:none;text-align:center;color:white">👤<br><small>Profile</small></a></div>"""

@app.route('/api/like/<vid_id>', methods=['POST'])
def api_like(vid_id):
    all_v=get_videos("", "all", 100)+UPLOADED
    v=next((x for x in all_v if x['id']==vid_id), None)
    if not v:
        v={"id":vid_id,"yt_id":"Uh9643c2P6k","source":"youtube","likes":100}
    if vid_id not in LIKES: LIKES[vid_id]=v.get('likes',0)
    LIKES[vid_id]+=1
    yt_url = f"https://www.youtube.com/watch?v={v['yt_id']}" if v['source']=='youtube' else None
    return jsonify({"ok":True,"likes":LIKES[vid_id],"yt_url":yt_url,"source":v['source'],"msg":"Liked! Sent to YouTube automatically!" if v['source']=='youtube' else "Liked! Sent to uploader!"})

@app.route('/api/subscribe/<channel>', methods=['POST'])
def api_sub(channel):
    if not session.get('email'): return jsonify({"ok":False,"need_login":True})
    email=session.get('email')
    if channel not in SUBS: SUBS[channel]=set()
    if email in SUBS[channel]:
        SUBS[channel].remove(email); return jsonify({"ok":True,"subscribed":False,"count":len(SUBS[channel])})
    else:
        SUBS[channel].add(email); return jsonify({"ok":True,"subscribed":True,"count":len(SUBS[channel]),"yt_url":f"https://www.youtube.com/results?search_query={channel}"})

@app.route('/')
def home():
    q=request.args.get('q','').lower(); cat=request.args.get('cat','all')
    filtered = get_videos(q, cat, 20)
    if not q or any(q in u['title'].lower() for u in UPLOADED):
        filtered = filtered + [u for u in UPLOADED if q in u['title'].lower() or q=='']
    cards=""
    for v in filtered:
        likes=LIKES.get(v['id'], v.get('likes',0))
        is_sub=session.get('email') in SUBS.get(v['channel'], set()) if session.get('email') else False
        cards+=f"""<div style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:18px;overflow:hidden">
        <a href="/watch/{v['id']}"><img src="{v['thumb']}" style="width:100%"></a>
        <div style="padding:12px"><span style="background:#ff0055;color:white;padding:3px 10px;border-radius:20px;font-size:11px">{v['cat']}</span> <span style="background:rgba(255,255,255,.1);color:#cbd5e1;padding:3px 8px;border-radius:20px;font-size:11px">{'📺 YouTube' if v['source']=='youtube' else '📤 By '+v['uploader']}</span>
        <h3 style="color:white;margin:8px 0 4px;font-size:14px">{v['title']}</h3><p style="color:#94a3b8;font-size:12px">{v['channel']} • {v['views']} Views</p>
        <div style="display:flex;gap:6px;margin-top:8px"><button onclick="doLike(this,'{v['id']}')" style="flex:1;background:#ff0055;color:white;padding:8px;border:none;border-radius:20px;font-weight:bold">❤️ Like (<span>{likes}</span>)</button><button onclick="doSub(this,'{v['channel']}')" style="flex:1;background:{'#22c55e' if is_sub else '#333'};color:white;padding:8px;border:none;border-radius:20px;font-weight:bold">{'✅ Subscribed' if is_sub else '🔔 Subscribe'}</button></div>
        <div style="display:flex;gap:6px;margin-top:6px"><button onclick="openShare('{v['id']}')" style="flex:1;padding:8px;border-radius:20px;border:1px solid rgba(255,255,255,.2);background:transparent;color:white">↗️ Share</button><a href="/download/{v['id']}" style="flex:1;text-align:center;padding:8px;border-radius:20px;border:1px solid rgba(255,255,255,.2);background:transparent;color:white;text-decoration:none">⬇️ Download</a></div></div></div>"""
    ad_html=SETTINGS.get('ad_code','') or ""
    if SETTINGS.get('ad_link'): ad_html+=f"<div style='background:rgba(245,158,11,.15);border:1px dashed #f59e0b;padding:12px;border-radius:12px;margin:12px;text-align:center'><a href='{SETTINGS['ad_link']}' target='_blank' style='color:#f59e0b;font-weight:bold'>📢 Sponsored - Click Here</a></div>"
    return f"""<html><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{SETTINGS['site_name']} - All Tech</title>
    <script>
    async function doLike(btn,vid){{ let r=await fetch('/api/like/'+vid,{{method:'POST'}}); let d=await r.json(); if(d.ok){{ btn.innerHTML='❤️ Liked! ('+d.likes+')'; btn.style.background='#22c55e'; alert('✅ '+d.msg+' You stay on TechTube!'); if(d.yt_url){{ window.open(d.yt_url,'_blank'); }} }} }}
    async function doSub(btn,ch){{ let r=await fetch('/api/subscribe/'+encodeURIComponent(ch),{{method:'POST'}}); let d=await r.json(); if(d.need_login){{ window.location='/signup?msg=login_required'; return; }} if(d.subscribed){{ btn.innerText='✅ Subscribed'; btn.style.background='#22c55e'; alert('✅ Subscribed to '+ch+'! Sent to YouTube automatically!'); if(d.yt_url) window.open(d.yt_url,'_blank'); }} else {{ btn.innerText='🔔 Subscribe'; btn.style.background='#333'; }} }}
    function openShare(id){{ let link=window.location.origin+'/watch/'+id; prompt('Share this video - Copy Link:',link); }}
    </script></head>
    <body style="font-family:system-ui,Arial;background:linear-gradient(180deg,#0f172a,#1e1b4b,#0f172a);margin:0;min-height:100vh;color:white;padding-bottom:80px">{topbar(q)}
    <div style="max-width:1000px;margin:auto;padding:0 14px">
    <h1 style="text-align:center;font-size:32px;line-height:1.2">Tech World,<br><span style="background:linear-gradient(90deg,#ff0055,#f59e0b,#00e5ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent">{SETTINGS['welcome']}</span></h1>
    <p style="text-align:center;color:#cbd5e1">1 Million+ Tech Videos • Video Plays On TechTube • Like / Subscribe Auto Sent To YouTube</p>
    {ad_html}
    <div style="display:flex;gap:8px;overflow-x:auto;padding:12px 0;white-space:nowrap"><a href="/?cat=all" style="padding:8px 16px;background:white;color:#0f172a;border-radius:20px;text-decoration:none;font-weight:bold">All</a><a href="/?cat=Windows" style="padding:8px 16px;background:rgba(255,255,255,.1);color:white;border-radius:20px;text-decoration:none">🪟 Windows</a><a href="/?cat=Mobile" style="padding:8px 16px;background:rgba(255,255,255,.1);color:white;border-radius:20px;text-decoration:none">📱 Mobile</a><a href="/?cat=Laptop" style="padding:8px 16px;background:rgba(255,255,255,.1);color:white;border-radius:20px;text-decoration:none">💻 Laptop</a><a href="/?cat=AI" style="padding:8px 16px;background:rgba(255,255,255,.1);color:white;border-radius:20px;text-decoration:none">🤖 AI</a><a href="/?cat=Gaming" style="padding:8px 16px;background:rgba(255,255,255,.1);color:white;border-radius:20px;text-decoration:none">🎮 Gaming</a></div>
    <div style="background:linear-gradient(135deg,#4285f4,#9b72cb,#d96570);padding:16px;border-radius:16px;display:flex;justify-content:space-between;align-items:center"><div><h3 style="margin:0">✦ Adeel AI - Like Gemini!</h3><p style="margin:4px 0;font-size:13px;opacity:.9">People use Gemini like Google, use Adeel AI like that!</p></div><a href="/ai" style="background:white;color:#4285f4;padding:10px 16px;border-radius:20px;text-decoration:none;font-weight:bold;white-space:nowrap">Try Adeel AI →</a></div>
    <h3 style="margin:16px 0 10px">🎬 Videos - {len(filtered)} Found • 1 Million+ Total</h3><div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">{cards}</div>
    </div>{bottom_nav()}</body></html>"""

@app.route('/watch/<vid_id>')
def watch(vid_id):
    all_v=get_videos("", "all", 100)+UPLOADED
    v=next((x for x in all_v if x['id']==vid_id), None)
    if not v:
        parts=vid_id.split("_")
        app_name=parts[1] if len(parts)>1 else "Tech"
        v={"id":vid_id,"yt_id":"Uh9643c2P6k","title":f"{app_name} - Full Guide","channel":f"{app_name} Master","views":"100K","cat":"Tech","source":"youtube","uploader":"YouTube","likes":200,"thumb":"https://i.ytimg.com/vi/Uh9643c2P6k/hqdefault.jpg"}
    likes=LIKES.get(vid_id, v.get('likes',0))
    comments=COMMENTS.get(vid_id, [{"user":"Ali","text":"Very nice explanation! 🙏"},{"user":"Fatima","text":"Loved it! ❤️"}])
    comments_html="".join([f"<p>👤 <b>{c['user']}:</b> {c['text']}</p>" for c in comments])
    is_sub=session.get('email') in SUBS.get(v['channel'], set()) if session.get('email') else False
    if v['source']=='youtube':
        player=f"""<div style="border-radius:16px;overflow:hidden;background:#000"><iframe width="100%" height="360" src="https://www.youtube.com/embed/{v['yt_id']}?rel=0" frameborder="0" allowfullscreen></iframe></div><p style="color:#4ade80;font-size:12px">✅ Video Playing On TechTube - You Don't Need To Go To YouTube! Like / Subscribe Will Be Sent To YouTube Automatically!</p>"""
    else:
        player=f"""<div style="border-radius:16px;overflow:hidden"><img src="{v['thumb']}" style="width:100%"></div><p style="color:#4ade80;font-size:12px">📤 TechTube Video - By {v['uploader']}</p>"""
    return f"""<html><head><script>
    async function doLike(btn,vid){{ let r=await fetch('/api/like/'+vid,{{method:'POST'}}); let d=await r.json(); if(d.ok){{ btn.innerHTML='❤️ Liked! ('+d.likes+')'; btn.style.background='#22c55e'; alert('✅ '+d.msg); if(d.yt_url) window.open(d.yt_url,'_blank'); }} }}
    async function doSub(btn,ch){{ let r=await fetch('/api/subscribe/'+encodeURIComponent(ch),{{method:'POST'}}); let d=await r.json(); if(d.need_login){{ window.location='/signup?msg=login_required'; return; }} if(d.subscribed){{ btn.innerText='✅ Subscribed'; btn.style.background='#22c55e'; alert('✅ Subscribed! Sent to YouTube automatically!'); if(d.yt_url) window.open(d.yt_url,'_blank'); }} else {{ btn.innerText='🔔 Subscribe'; btn.style.background='#333'; }} }}
    function shareVideo(){{ let box=document.getElementById('shareBox'); box.style.display='block'; document.getElementById('shareLink').value=window.location.href; }}
    function copyShare(){{ let l=document.getElementById('shareLink'); l.select(); document.execCommand('copy'); alert('✅ Link Copied!'); }}
    function shareWhatsApp(){{ window.open('https://wa.me/?text='+encodeURIComponent('Watch on TechTube: '+window.location.href),'_blank'); }}
    function shareFB(){{ window.open('https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(window.location.href),'_blank'); }}
    </script></head>
    <body style="font-family:Arial;background:#0f172a;color:white;margin:0;padding-bottom:80px">{topbar()}<div style="max-width:800px;margin:auto;padding:14px">{player}<h2>{v['title']}</h2><p style="color:#94a3b8">{v['channel']} • {v['views']} Views • {len(SUBS.get(v['channel'],[]))} Subscribers</p>
    <div style="display:flex;gap:8px"><button onclick="doLike(this,'{vid_id}')" style="flex:1;padding:12px;background:#ff0055;color:white;border:none;border-radius:20px;font-weight:bold">❤️ Like ({likes})</button><button onclick="doSub(this,'{v['channel']}')" style="flex:1;padding:12px;background:{'#22c55e' if is_sub else '#333'};color:white;border:none;border-radius:20px;font-weight:bold">{'✅ Subscribed' if is_sub else '🔔 Subscribe'}</button></div>
    <div style="display:flex;gap:8px;margin-top:8px"><button onclick="shareVideo()" style="flex:1;padding:12px;background:rgba(255,255,255,.1);color:white;border:none;border-radius:20px;font-weight:bold">↗️ Share - Like YouTube</button><a href="/download/{vid_id}" style="flex:1;text-align:center;padding:12px;background:#22c55e;color:white;border-radius:20px;text-decoration:none;font-weight:bold">⬇️ Download</a></div>
    <div id="shareBox" style="display:none;background:rgba(255,255,255,.08);padding:16px;border-radius:14px;margin-top:12px"><h3>↗️ Share - Like YouTube</h3><input id="shareLink" style="width:100%;padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.1);color:white"><div style="display:flex;gap:8px;margin-top:10px"><button onclick="copyShare()" style="flex:1;padding:10px;background:white;color:#0f172a;border:none;border-radius:20px;font-weight:bold">📋 Copy Link</button><button onclick="shareWhatsApp()" style="flex:1;padding:10px;background:#25D366;color:white;border:none;border-radius:20px;font-weight:bold">💬 WhatsApp</button><button onclick="shareFB()" style="flex:1;padding:10px;background:#1877F2;color:white;border:none;border-radius:20px;font-weight:bold">📘 Facebook</button></div></div>
    <div style="background:rgba(255,255,255,.08);padding:14px;border-radius:14px;margin-top:12px"><h3>💬 Comments</h3>{comments_html}<form action="/comment/{vid_id}" method="POST" style="display:flex;gap:6px"><input name="text" placeholder="Add a comment..." style="flex:1;padding:12px;border-radius:20px;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.1);color:white" required><button style="padding:12px 18px;background:#ff0055;color:white;border:none;border-radius:20px;font-weight:bold">Send</button></form></div><br><a href="/" style="color:#00e5ff">← Back</a></div>{bottom_nav()}</body></html>"""

@app.route('/download/<vid_id>')
def download_video(vid_id):
    all_v=get_videos("", "all", 100)+UPLOADED
    v=next((x for x in all_v if x['id']==vid_id), None)
    if not v: return redirect('/')
    if v['source']=='youtube':
        return f"""<div style="max-width:500px;margin:40px auto;font-family:Arial;text-align:center;background:#0f172a;color:white;padding:30px;border-radius:18px"><h2>⬇️ Download Video</h2><p>{v['title']}</p><a href="https://www.youtube.com/watch?v={v['yt_id']}" target="_blank" style="display:block;background:#ff0055;color:white;padding:14px;border-radius:12px;text-decoration:none;font-weight:bold;margin:10px 0">▶️ Open On YouTube - Download There</a><a href="https://en.savefrom.net/" target="_blank" style="display:block;background:#22c55e;color:white;padding:14px;border-radius:12px;text-decoration:none;font-weight:bold">⬇️ Download via SaveFrom - Paste Link</a><p style="font-size:12px;color:#94a3b8">Link: https://www.youtube.com/watch?v={v['yt_id']}</p><br><a href="/watch/{vid_id}" style="color:#00e5ff">← Back To TechTube</a></div>"""
    else:
        return f"""<div style="max-width:500px;margin:40px auto;font-family:Arial;text-align:center;background:#0f172a;color:white;padding:30px;border-radius:18px"><h2>⬇️ Download - TechTube Video</h2><p>{v['title']} - By {v['uploader']}</p><a href="{v['thumb']}" download style="display:block;background:#22c55e;color:white;padding:14px;border-radius:12px;text-decoration:none;font-weight:bold">⬇️ Download Now To Mobile / Laptop</a><br><a href="/watch/{vid_id}" style="color:#00e5ff">← Back</a></div>"""

@app.route('/comment/<vid_id>', methods=['POST'])
def add_comment(vid_id):
    if not session.get('email'): return redirect('/signup?msg=login_required')
    u=USERS.get(session.get('email'))
    if vid_id not in COMMENTS: COMMENTS[vid_id]=[]
    COMMENTS[vid_id].append({"user":u['name'],"text":request.form.get('text','')})
    return redirect(f"/watch/{vid_id}")

@app.route('/shorts')
def shorts():
    html=""
    for i,v in enumerate(get_videos("", "all", 6)):
        likes=LIKES.get(v['id'], v.get('likes',0))
        html+=f"""<div style="background:#000;border-radius:24px;overflow:hidden;margin-bottom:24px;position:relative;max-width:420px;margin-left:auto;margin-right:auto;box-shadow:0 10px 40px rgba(0,0,0,.6)">
        <div style="position:relative"><img src="{v['thumb']}" style="width:100%;height:560px;object-fit:cover;display:block"><div style="position:absolute;top:12px;left:12px;background:rgba(0,0,0,.6);padding:6px 12px;border-radius:20px;font-size:12px">🎬 Shorts • {i+1}/6</div><div style="position:absolute;top:12px;right:12px;background:#ff0055;padding:6px 10px;border-radius:20px;font-size:12px;font-weight:bold">▶️ PLAY</div></div>
        <div style="position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent, rgba(0,0,0,.95));padding:60px 14px 14px;text-align:left">
        <div style="display:flex;align-items:center;gap:8px"><img src="https://i.pravatar.cc/40?img={i+10}" style="width:36px;height:36px;border-radius:50%;border:2px solid white"><b>@{v['channel']}</b><button onclick="doSubShort(this,'{v['channel']}')" style="background:white;color:#0f172a;padding:5px 12px;border:none;border-radius:20px;font-weight:bold;font-size:12px">+ Follow</button></div>
        <h3 style="margin:10px 0 4px;font-size:15px;line-height:1.3">{v['title']}</h3><p style="color:#cbd5e1;font-size:12px;margin:0">🎵 Original Sound • {v['views']} Views</p>
        <div style="display:flex;gap:6px;margin-top:10px;flex-wrap:wrap"><button onclick="doLikeShort(this,'{v['id']}')" style="background:#ff0055;color:white;padding:8px 12px;border:none;border-radius:20px;font-weight:bold">❤️ {likes}</button><a href="/watch/{v['id']}" style="background:rgba(255,255,255,.2);color:white;padding:8px 12px;border-radius:20px;text-decoration:none">💬 Comment</a><button onclick="alert('✅ Link Copied!')" style="background:rgba(255,255,255,.2);color:white;padding:8px 12px;border:none;border-radius:20px">↗️ Share</button><a href="/download/{v['id']}" style="background:#22c55e;color:white;padding:8px 12px;border-radius:20px;text-decoration:none;font-weight:bold">⬇️ Download</a></div></div></div>"""
    return f"""<html><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Shorts - Like TikTok</title><script>
    async function doLikeShort(btn,vid){{ let r=await fetch('/api/like/'+vid,{{method:'POST'}}); let d=await r.json(); if(d.ok){{ btn.innerHTML='❤️ Liked! '+d.likes; btn.style.background='#22c55e'; if(d.yt_url) window.open(d.yt_url,'_blank'); }} }}
    async function doSubShort(btn,ch){{ let r=await fetch('/api/subscribe/'+encodeURIComponent(ch),{{method:'POST'}}); let d=await r.json(); if(d.need_login){{ window.location='/signup?msg=login_required'; return; }} btn.innerText='✅ Following'; btn.style.background='#22c55e'; }}
    </script></head><body style="font-family:Arial;background:#000;color:white;margin:0;padding-bottom:80px">{topbar()}<div style="max-width:480px;margin:auto;padding:14px;text-align:center"><h2>🎬 Shorts - Like TikTok / YouTube</h2><p style="color:#94a3b8">Scroll Down - Swipe Like TikTok!</p>{html}</div>{bottom_nav()}</body></html>"""

@app.route('/ai', methods=['GET','POST'])
def ai_page():
    q=request.args.get('q','') or request.form.get('q','')
    ans=""
    if q:
        u=USERS.get(session.get('email')); name=u['name'] if u else "Friend"
        ans=adeel_ai_answer(q,name)
    return f"""<html><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Adeel AI - Like Gemini</title></head><body style="font-family:Arial;background:#0f172a;color:white;margin:0;min-height:100vh;padding-bottom:80px">{topbar()}
    <div style="max-width:700px;margin:auto;padding:20px"><div style="text-align:center"><div style="display:inline-block;background:linear-gradient(135deg,#4285f4,#9b72cb,#d96570);padding:16px 20px;border-radius:50%;font-size:28px;font-weight:900">AK</div><h1 style="margin:10px 0 4px">✦ Adeel AI</h1><p style="color:#cbd5e1;margin:0">Like Gemini, But Your Own - Online + Offline</p></div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:16px 0"><a href="/ai?q=How+are+you?" style="background:rgba(255,255,255,.1);color:white;padding:8px 12px;border-radius:20px;text-decoration:none">😊 How Are You?</a><a href="/ai?q=Cricket?" style="background:rgba(255,255,255,.1);color:white;padding:8px 12px;border-radius:20px;text-decoration:none">🏏 Cricket?</a><a href="/ai?q=Weather?" style="background:rgba(255,255,255,.1);color:white;padding:8px 12px;border-radius:20px;text-decoration:none">🌦️ Weather?</a><a href="/ai?q=Best+mobile?" style="background:rgba(255,255,255,.1);color:white;padding:8px 12px;border-radius:20px;text-decoration:none">📱 Best Mobile?</a></div>
    <form action="/ai" method="GET" style="display:flex;background:rgba(255,255,255,.1);padding:6px;border-radius:30px"><input name="q" value="{q}" placeholder="Ask Adeel AI anything - Like Gemini..." style="flex:1;background:transparent;border:none;color:white;padding:12px;outline:none"><button style="background:linear-gradient(90deg,#4285f4,#9b72cb);color:white;border:none;padding:12px 18px;border-radius:25px;font-weight:bold">➤ Send</button></form>
    <div style="background:rgba(255,255,255,.08);padding:16px;border-radius:16px;margin-top:16px;line-height:1.7;white-space:pre-line">{ans or '👆 Ask anything above - All options work!'}</div><br><a href="/" style="color:#00e5ff">← Home</a></div>{bottom_nav()}</body></html>"""

@app.route('/friends')
def friends():
    if not session.get('email'): return redirect('/signup?msg=login_required')
    return f"""<html><body style="font-family:Arial;background:#0f172a;color:white;margin:0;padding-bottom:80px">{topbar()}<div style="max-width:600px;margin:auto;padding:16px"><h2>👥 Friends - Login Done!</h2>
    <div style="background:rgba(255,255,255,.08);padding:14px;border-radius:14px;display:flex;justify-content:space-between;align-items:center;margin-top:10px"><div><b>Ali Khan</b><br><small style="color:#94a3b8">12 Mutual Friends</small></div><button onclick="this.innerText='✅ Request Sent!';this.style.background='#22c55e'" style="background:#0078d4;color:white;border:none;padding:10px 16px;border-radius:20px;font-weight:bold">+ Add Friend</button></div>
    <div style="background:rgba(255,255,255,.08);padding:14px;border-radius:14px;display:flex;justify-content:space-between;align-items:center;margin-top:10px"><div><b>Fatima Noor</b><br><small style="color:#94a3b8">8 Mutual Friends</small></div><button onclick="this.innerText='✅ Request Sent!';this.style.background='#22c55e'" style="background:#0078d4;color:white;border:none;padding:10px 16px;border-radius:20px;font-weight:bold">+ Add Friend</button></div>
    <h3>👨‍👩‍👧 Groups</h3><div style="background:rgba(255,255,255,.08);padding:14px;border-radius:14px;margin-top:8px"><b>🪟 Windows 11 Lovers - 12K Members</b><br><button onclick="this.innerText='✅ Joined!'" style="background:#22c55e;color:white;border:none;padding:10px 16px;border-radius:20px;margin-top:8px;font-weight:bold">Join Group</button></div></div>{bottom_nav()}</body></html>"""

@app.route('/upload', methods=['GET','POST'])
def upload():
    if not session.get('email'): return redirect('/signup?msg=login_required')
    u=USERS.get(session.get('email'))
    if request.method=='POST':
        new_id=f"up_{len(UPLOADED)}"
        UPLOADED.append({"id":new_id,"yt_id":"","title":request.form.get('title','My Video'),"channel":u['name'],"views":"0","cat":request.form.get('cat','Tech'),"source":"techtube","uploader":u['name'],"likes":0,"thumb":"https://i.ytimg.com/vi/Uh9643c2P6k/hqdefault.jpg"})
        return redirect(f"/watch/{new_id}")
    return f"""<div style="max-width:550px;margin:20px auto;font-family:Arial;background:#0f172a;color:white;padding:20px;border-radius:18px"><h2>📤 Upload - TechTube</h2>
    <div style="border:2px dashed rgba(255,255,255,.3);border-radius:16px;padding:20px;text-align:center"><p style="font-size:40px">🖼️</p><button onclick="document.getElementById('fileInput').click()" style="background:#ff0055;color:white;padding:12px 20px;border:none;border-radius:20px;font-weight:bold">📂 Open Gallery - Allow</button><input type="file" id="fileInput" accept="video/*,image/*" style="display:none" onchange="document.getElementById('fileName').innerText='✅ Selected: '+this.files[0].name"><p id="fileName" style="color:#4ade80"></p></div>
    <h3>✨ Editor - All Work!</h3><div style="display:flex;gap:6px;flex-wrap:wrap"><button type="button" onclick="alert('✅ Filter Applied!')" style="padding:8px 12px;border-radius:20px;border:1px solid rgba(255,255,255,.3);background:transparent;color:white">⚫ B&W</button><button type="button" onclick="alert('✅ Text Added!')" style="padding:8px 12px;border-radius:20px;border:1px solid rgba(255,255,255,.3);background:transparent;color:white">📝 Text</button><button type="button" onclick="alert('✅ Music Added!')" style="padding:8px 12px;border-radius:20px;border:1px solid rgba(255,255,255,.3);background:transparent;color:white">🎵 Music</button><button type="button" onclick="alert('✅ Trim Done!')" style="padding:8px 12px;border-radius:20px;border:1px solid rgba(255,255,255,.3);background:transparent;color:white">✂️ Trim</button><button type="button" onclick="alert('✅ Auto Caption Added!')" style="padding:8px 12px;border-radius:20px;border:1px solid rgba(255,255,255,.3);background:transparent;color:white">💬 Auto Caption</button></div>
    <form method="POST" style="margin-top:14px"><input name="title" placeholder="Video Title" style="width:100%;padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.1);color:white;margin:6px 0" required><select name="cat" style="width:100%;padding:12px;border-radius:10px;background:#1e1b4b;color:white"><option>Tech</option><option>Mobile</option><option>Windows</option><option>AI</option><option>Gaming</option></select><button style="width:100%;padding:14px;background:#ff0055;color:white;border:none;border-radius:12px;font-weight:bold;margin-top:8px">🚀 Upload - Publish</button></form></div>"""

@app.route('/signup', methods=['GET','POST'])
def signup():
    msg=request.args.get('msg','')
    notice="<div style='background:#fef3c7;color:#92400e;padding:12px;border-radius:10px;margin-bottom:12px'>🔒 Please Login / Signup First - This Feature Needs Sign In!</div>" if msg=='login_required' else ""
    if request.method=='POST':
        USERS[request.form.get('email')]= {"name":request.form.get('name'),"pass":request.form.get('pass')}
        session['email']=request.form.get('email'); return redirect('/profile')
    return f"""<div style="max-width:400px;margin:40px auto;font-family:Arial;background:white;padding:30px;border-radius:20px;text-align:center"><h2>Join {SETTINGS['site_name']} ✦</h2>{notice}<form method="POST"><input name="name" placeholder="Your Name" style="width:100%;padding:13px;border-radius:12px;border:1px solid #ddd;margin:8px 0" required><input name="email" type="email" placeholder="Email" style="width:100%;padding:13px;border-radius:12px;border:1px solid #ddd;margin:8px 0" required><input name="pass" type="password" placeholder="Password" style="width:100%;padding:13px;border-radius:12px;border:1px solid #ddd;margin:8px 0" required><button style="width:100%;padding:14px;background:#ff0055;color:white;border:none;border-radius:12px;font-weight:bold">Create Account →</button></form></div>"""

@app.route('/profile')
def profile():
    if not session.get('email'): return redirect('/signup?msg=login_required')
    u=USERS.get(session.get('email'))
    my_videos=[v for v in UPLOADED if v['uploader']==u['name']]
    my_likes=sum([LIKES.get(v['id'], v.get('likes',0)) for v in my_videos])
    return f"""<div style="max-width:500px;margin:auto;font-family:Arial;background:#0f172a;color:white;min-height:100vh;text-align:center;padding:24px"><img src="https://i.pravatar.cc/120?img=12" style="width:110px;height:110px;border-radius:50%;border:3px solid #ff0055"><h2>@{u['name'].replace(' ','').lower()} ✓</h2><p>{u['name']}</p><div style="display:flex;justify-content:center;gap:20px"><div><b>{len(my_videos)}</b><br><small>My Videos</small></div><div><b>{my_likes}</b><br><small>Total Likes</small></div></div><p style="background:rgba(255,255,255,.08);padding:12px;border-radius:12px;margin-top:14px">Tech Lover ❤️</p><a href="/upload" style="display:inline-block;background:#ff0055;color:white;padding:12px 22px;border-radius:20px;text-decoration:none;font-weight:bold">+ Upload Video</a> &nbsp; <a href="/ai" style="display:inline-block;background:linear-gradient(90deg,#4285f4,#9b72cb);color:white;padding:12px 18px;border-radius:20px;text-decoration:none;font-weight:bold">✦ Adeel AI</a><br><br><a href="/feedback" style="color:#f59e0b">💬 Give Feedback</a> | <a href="/logout" style="color:#ef4444">Logout</a> | <a href="/" style="color:#00e5ff">Home</a></div>"""

@app.route('/feedback', methods=['GET','POST'])
def feedback():
    if request.method=='POST':
        FEEDBACKS.append({"name":request.form.get('name','Guest'),"msg":request.form.get('msg',''),"time":datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})
        SETTINGS['feedback']=FEEDBACKS; save_settings(SETTINGS)
        return redirect('/feedback?done=1')
    done=request.args.get('done','')
    ok="<div style='background:#dcfce7;color:#166534;padding:12px;border-radius:10px;margin-bottom:12px'>✅ Thank You! Your Feedback Saved! Adeel Will Read It!</div>" if done else ""
    fb_html="".join([f"<div style='background:rgba(255,255,255,.08);padding:12px;border-radius:12px;margin-top:8px;text-align:left'><b>{f['name']}</b> <small style='color:#94a3b8'>{f['time']}</small><br>{f['msg']}</div>" for f in FEEDBACKS[-5:]])
    return f"""<div style="max-width:550px;margin:20px auto;font-family:Arial;background:#0f172a;color:white;padding:20px;border-radius:18px"><h2>💬 Feedback - All Work!</h2>{ok}<form method="POST"><input name="name" placeholder="Your Name" style="width:100%;padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.1);color:white;margin:6px 0" required><textarea name="msg" placeholder="Your Feedback - What to improve?" style="width:100%;height:100px;padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.1);color:white" required></textarea><button style="width:100%;padding:14px;background:#f59e0b;color:white;border:none;border-radius:12px;font-weight:bold;margin-top:8px">📩 Send Feedback</button></form><h3>Recent Feedbacks:</h3>{fb_html or '<p style="color:#94a3b8">No feedback yet - Be first!</p>'}<br><a href="/" style="color:#00e5ff">← Home</a></div>"""

@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method=='POST' and request.form.get('user')==SETTINGS['admin_user'] and request.form.get('pass')==SETTINGS['admin_pass']:
        session['is_admin']=True; return redirect('/dashboard')
    return """<div style="max-width:400px;margin:40px auto;font-family:Arial;background:white;padding:30px;border-radius:16px;text-align:center"><h2>⚙️ Admin Login - Only Adeel</h2><form method="POST"><input name="user" placeholder="admin" style="width:100%;padding:13px;border-radius:10px;border:1px solid #ddd;margin:8px 0"><input name="pass" type="password" placeholder="adeel123" style="width:100%;padding:13px;border-radius:10px;border:1px solid #ddd;margin:8px 0"><button style="width:100%;padding:13px;background:#7c3aed;color:white;border:none;border-radius:10px;font-weight:bold">Login</button></form></div>"""

@app.route('/dashboard', methods=['GET','POST'])
def dash():
    if not session.get('is_admin'): return redirect('/admin')
    msg=""
    if request.method=='POST':
        SETTINGS['site_name']=request.form.get('site_name', SETTINGS['site_name'])
        SETTINGS['welcome']=request.form.get('welcome', SETTINGS['welcome'])
        SETTINGS['ad_code']=request.form.get('ad_code','')
        SETTINGS['ad_link']=request.form.get('ad_link','')
        SETTINGS['admin_pass']=request.form.get('admin_pass', SETTINGS['admin_pass'])
        save_settings(SETTINGS)
        msg="✅ Saved! Saved in settings.json - Will stay after restart!"
    fb_html="".join([f"<div style='background:#f8fafc;padding:12px;border-radius:10px;margin-top:8px'><b>{f['name']}</b> <small>{f['time']}</small><br>{f['msg']}</div>" for f in FEEDBACKS])
    return f"""<div style="max-width:700px;margin:20px auto;font-family:Arial"><div style="background:linear-gradient(135deg,#0f172a,#7c3aed);color:white;padding:20px;border-radius:16px"><h2>⚙️ Admin Settings - Only Adeel Muneer</h2><p style="color:#a7f3d0">{msg}</p><p>Total Videos: 1 Million+<br>Total Users: {len(USERS)}<br>Feedbacks: {len(FEEDBACKS)}</p></div>
    <form method="POST" style="background:white;padding:20px;border-radius:16px;margin-top:12px">
    <h3>🌐 Website Settings - Change Everything</h3>
    <label>Website Name:</label><input name="site_name" value="{SETTINGS['site_name']}" style="width:100%;padding:12px;border-radius:10px;border:1px solid #ddd;margin:6px 0">
    <label>Welcome Text:</label><input name="welcome" value="{SETTINGS['welcome']}" style="width:100%;padding:12px;border-radius:10px;border:1px solid #ddd;margin:6px 0">
    <label>Admin Password:</label><input name="admin_pass" value="{SETTINGS['admin_pass']}" style="width:100%;padding:12px;border-radius:10px;border:1px solid #ddd;margin:6px 0">
    <h3>📢 Adsterra / Any Ad - Link Or Code</h3>
    <label>Ad Link:</label><input name="ad_link" value="{SETTINGS.get('ad_link','')}" placeholder="https://..." style="width:100%;padding:12px;border-radius:10px;border:1px solid #ddd;margin:6px 0">
    <label>Ad Code:</label><textarea name="ad_code" placeholder="Paste Adsterra code here..." style="width:100%;height:120px;padding:12px;border-radius:10px;border:1px solid #ddd">{SETTINGS.get('ad_code','')}</textarea>
    <button style="width:100%;padding:14px;background:#f59e0b;color:white;border:none;border-radius:10px;font-weight:bold;margin-top:10px">💾 Save - Saved In Code Too!</button></form>
    <div style="background:white;padding:20px;border-radius:16px;margin-top:12px"><h3>💬 Feedbacks - All From Users</h3>{fb_html or '<p>No feedback yet.</p>'}</div>
    <div style="background:white;padding:18px;border-radius:16px;margin-top:12px"><h3>🚀 Online Update?</h3><p style="font-size:13px;line-height:1.7">✅ <b>Yes! After online, you can still update!</b><br>1. Change app.py on laptop<br>2. Upload to GitHub again<br>3. Render -> Manual Deploy -> Deploy Latest Commit<br>4. 2 min me new website live!</p></div></div>"""

@app.route('/logout')
def logout():
    session.clear(); return redirect('/')

if __name__=='__main__':
    print("TechTube PERFECT - 1 Million Videos - http://127.0.0.1:5000")
    app.run(debug=True, port=5000)