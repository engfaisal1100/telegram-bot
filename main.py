from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser
import schedule
import time
import os

# بيانات API الخاصة بك
api_id = 22980443
api_hash = 'e2c8582d246ada1e5530c9a94ff7e57b'

client = TelegramClient('my_session', api_id, api_hash)
client.start()  # بدء الاتصال بالبوت تلقائيًا

# قائمة المجموعات
selected_chat_usernames = [
    'onemilion1998', 'code_for_web', 'Upm27266', 'alsharqa1100', 'sultanu1999',
    'AlAmeerSultan', 'yj9028bv2FiNDk', 'yyytttyuiii', 'programmers_sy', 'ajman1100',
    'kPDIxkrMaxjMmI00', 'UQ2023', 'discussions_5', 'hjjhjvvjkgbkohbkkml', 'alorden',
    'Laeringja', 'abudabi1100', 'BOXHILL1', 'kalifa1100', 'dubai11000',
    'gshsbnslkrGwmZ5UtVlZjg0z', 'Riirv1', 'HTML_CSS_ARAB', 'dw_html_css_group',
    'alain11000', 'alsharqa1100', 'CodeProM4', 'programing_gathering',
    'TheUAE1100', 'Elite_Web_Developers', 'zaiiid1100', 'chat_israel_top',
    'sjdhd2024', '8280', 'Work_From_The_Home', 'indianchat_12', 'taifstdents',
    'qLcp9vlkapqNajjimh9', 'fayha_college', 'alsharqa1100',
]

# الرسالة التي سيتم إرسالها
message = """
📢 هل تبحث عن موقع إلكتروني احترافي لأعمالك أو شركتك؟
أنا مطور ويب أقدم لك خدمة تصميم وتطوير مواقع إلكترونية احترافية تشمل:
✅ تصميم جذاب وسهل الاستخدام  
✅ لوحة تحكم كاملة لإدارة المحتوى  
✅ تحسين SEO لظهور موقعك في نتائج Google  
✅ استضافة مدفوعة واسم نطاق خاص بك  
✅ أنظمة مخصصة لإدارة الموظفين والمهام والتقارير

📌 شاهد نماذج من أعمالي على موقعي الشخصي:  
https://engfaisal101.vercel.app

📞 تواصل معي عبر واتساب:  
+967779289621  
https://wa.me/967779289621
"""

# دالة إرسال الرسائل
def send_messages():
    for username in selected_chat_usernames:
        try:
            entity = client.get_entity(username)
            last_message = client.get_messages(entity, limit=1)
            if last_message:
                sender = client.get_entity(last_message[0].sender_id)
                if sender.id == client.get_me().id or sender.username == "Faisalhosin":
                    print(f"Skipping {username} (last message from self)")
                    continue
            client.send_message(entity, message)
            print(f"✅ Sent to {username}")
        except Exception as e:
            print(f"❌ Error sending to {username}: {e}")

# جدولة الإرسال كل 10 دقائق
schedule.every(10).minutes.do(send_messages)

print("✅ Bot started...")
send_messages()  # أول إرسال فوري عند التشغيل

while True:
    schedule.run_pending()
    time.sleep(5)
