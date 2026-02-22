import base64
import random
import requests
from seleniumbase import SB

# Get geolocation data
geo_data = requests.get("http://ip-api.com/json/").json()
proxy_str = False

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()

# Decode channel name
name = "YnJ1dGFsbGVz"
fulln = base64.b64decode(name).decode("utf-8")
urlt = f"https://www.twitch.tv/{fulln}"

while True:
    with SB(
        uc=True,
        locale="en",
        ad_block=True,
        chromium_arg="--disable-webgl",
        proxy=proxy_str
    ) as sssa:

        rnd = random.randint(450, 800)

        sssa.activate_cdp_mode(
            urlt,
            tzone=timezone_id,
            geoloc=(latitude, longitude)
        )
        sssa.sleep(2)

        if sssa.is_element_present('button:contains("Accept")'):
            sssa.cdp.click('button:contains("Accept")', timeout=4)

        sssa.sleep(2)
        sssa.sleep(12)

        if sssa.is_element_present('button:contains("Start Watching")'):
            sssa.cdp.click('button:contains("Start Watching")', timeout=4)
            sssa.sleep(10)

        if sssa.is_element_present('button:contains("Accept")'):
            sssa.cdp.click('button:contains("Accept")', timeout=4)
        sssa.cdp.get('https://store.steampowered.com/app/1836560/Aether__Iron/?%20utm_source=Influencer&utm_medium=bonus_demo&utm_ca%20mpaign=brutalles')
        if sssa.is_element_present("#live-channel-stream-information"):
          	sssa.cdp.get('https://store.steampowered.com/app/1836560/Aether__Iron/?%20utm_source=Influencer&utm_medium=bonus_demo&utm_ca%20mpaign=brutalles')
          	sssa.sleep(random.randint(5, 60))
          	sssa.cdp.get(urlt)
          	sssa.sleep(12)
            if sssa.is_element_present('button:contains("Accept")'):
                sssa.cdp.click('button:contains("Accept")', timeout=4)

            sssa2 = sssa.get_new_driver(undetectable=True)
            sssa2.activate_cdp_mode(
                urlt,
                tzone=timezone_id,
                geoloc=(latitude, longitude)
            )
            sssa2.sleep(10)

            if sssa2.is_element_present('button:contains("Start Watching")'):
                sssa2.cdp.click('button:contains("Start Watching")', timeout=4)
                sssa2.sleep(10)

            if sssa2.is_element_present('button:contains("Accept")'):
                sssa2.cdp.click('button:contains("Accept")', timeout=4)

            sssa.sleep(10)
            sssa.sleep(rnd)

        else:
            break
