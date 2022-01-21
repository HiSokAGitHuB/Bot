import requests
import telebot 
from telebot import types

def login(email,password):
        url = 'https://api2.musical.ly/passport/user/login/?mix_mode=1&username=1&email=&mobile=&account=&password=hg&captcha=&ts=&app_type=normal&app_language=en&manifest_version_code=2018073102&_rticket=1633593458298&iid=7011916372695598854&channel=googleplay&language=en&fp=&device_type=SM-G955F&resolution=1440*2792&openudid=91cac57ba8ef12b6&update_version_code=2018073102&sys_region=AS&os_api=28&is_my_cn=0&timezone_name=Asia/Muscat&dpi=560&carrier_region=OM&ac=wifi&device_id=6785177577851504133&mcc_mnc=42203&timezone_offset=14400&os_version=9&version_code=800&carrier_region_v2=422&app_name=musical_ly&version_name=8.0.0&device_brand=samsung&ssmix=a&build_number=8.0.0&device_platform=android&region=US&aid=&as=&cp=Qm&mas='
        head = {
          'User-Agent': 'Connectionzucom.zhiliaoapp.musically/2018073102 (Linux; U; Android 9; en_AS; SM-G955F; Build/PPR1.180610.011; Cronet/58.0.2991.0)z',
          'Host': 'api2.musical.ly',
          'Connection': 'keep-alive' }
        data = {'email': email,'password': password}
        resp = requests.post(url, headers=head,data=data)
        if 'user_id' in resp.text:
                session_key = resp.json()['data']['session_key']
                return True,session_key
        else:
                return False,False

bot = telebot.TeleBot(BOT_TOKEN)
N = types.InlineKeyboardButton(text ="- New Frome - HeSoka : ", url = 't.me/Hisoka2i')
m = types.InlineKeyboardButton(text ="- New Frome - Developer :", url = 't.me/OOC5C')		
	
@bot.message_handler(content_types=["text"])
def start(message):
        text = (message.text)
        if text == '/start':
                
                Moj = types.InlineKeyboardMarkup()
                Moj.row_width = 1
                Moj.add(N,m)
                w = 'https://siasky.net/MADgOOd5zXV2wPn1GOHrc5G6oGSr7eLj4ynIAh4oXuUNJA'
                bot.send_photo(message.chat.id,w,'✺ - Welcome  - Bot\n✺ - NeW , Bot Get  : Session - iD\n✺ - System Bot\n✺ - Sind , Email:Password : 🧠✅\n✺ - ProgrAm Ch : [ @Hisoka2i ]',parse_mode='markdown', reply_markup=Moj)               
        if ':' in text:
                email , password = text.split(':')
                resp_l = login(email,password)
                if resp_l[0] == True:
                        bot.send_message(message.chat.id, text=" - Login , iN YeS ✅")   
                        bot.send_message(message.chat.id, text=f"✺ - Done Session - iD : ✅\n✺ - Session - iD : {resp_l[1]}\n✺ - ProgrAm Ch : [ @Hisoka2i ]")
                else:
                        bot.send_message(message.chat.id, text=' - Login , iN No ❌ : ')

bot.polling()
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://bottelgramhis.herokuapp.com/"+str(BOT_TOKEN))