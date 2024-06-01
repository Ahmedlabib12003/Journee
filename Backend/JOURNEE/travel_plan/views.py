from django.shortcuts import render
from gemini import Gemini


# Create your views here.
def program(request):
    cookies = {
        "SID": "g.a000kAjG1XgzY3qfdZCTZB6YMUYoiVgGhdDd2c_NkKZPrFE9OUbKddHhS6gTIekqi6-wEMwwTQACgYKAdYSARASFQHGX2MiCl5rEx8eqARI6QtOz4Wu_xoVAUF8yKoSzfnUnFHjoxxgUCufSDm00076",
        "__Secure-1PSID": "g.a000kAjG1XgzY3qfdZCTZB6YMUYoiVgGhdDd2c_NkKZPrFE9OUbKDTd9zUF0Ee2P0zo8xI3v4gACgYKAcISARASFQHGX2MigeTDm6uuLYvYtTmuIhUaaRoVAUF8yKrKsYXpWrnUc-1fZPItQm__0076",
        "__Secure-3PSID": "g.a000kAjG1XgzY3qfdZCTZB6YMUYoiVgGhdDd2c_NkKZPrFE9OUbKEt5y39celjXw6WIe_QdH5QACgYKAWcSARASFQHGX2MiAKve6259swJCMaGqByIVJxoVAUF8yKos5oArWtJdI3jEoeY-BKJ30076",
        "HSID": "AcOjeMDtiT1ZqZe1d",
        "SSID": "A1v4I9cpSb6Lw-AXi",
        "APISID": "7DvrmjP4yS8itTQc/Ab3L3mVP513pCUH13",
        "SAPISID": "OvdIgsOtMhQcfWnJ/AYve798v-wJ7yoS8P",
        "__Secure-1PAPISID": "OvdIgsOtMhQcfWnJ/AYve798v-wJ7yoS8P",
        "__Secure-3PAPISID": "OvdIgsOtMhQcfWnJ/AYve798v-wJ7yoS8P",
        "SEARCH_SAMESITE": "CgQImZsB",
        "AEC": "AQTF6Hxp5KWHbDLFqqxkmiubt3z3cApHodq-9dsnG_IcOQu6nyA-pxAhGBM",
        "_ga": "GA1.1.943748736.1716402524",
        "1P_JAR": "2024-05-22-22",
        "NID": "514",
        "__Secure-1PSIDTS": "sidts-CjEBLwcBXCQxC41mD5TS68PSn3oORQKEzNObUDY6Gort0IEoij2ULm096lEDtEKBd62pEAA",
        "__Secure-3PSIDTS": "sidts-CjEBLwcBXCQxC41mD5TS68PSn3oORQKEzNObUDY6Gort0IEoij2ULm096lEDtEKBd62pEAA",
        "SIDCC": "AKEyXzV34HLCADiMHTstYAITW5N-fxVOp7_Ax9qWJCpxDvFXd0GUhltw_J0V-Nv2kJwtXvFZFQ",
        "__Secure-1PSIDCC": "AKEyXzWMelrHz1HTGtWjaU7G1yy0HNxUAjsYmEOtB3hEoKvk97y_2hry_jaQRzY9Y6lw6Gxqngg",
        "__Secure-3PSIDCC": "AKEyXzWV_MmyJwvgWM7-nZGfJIEPg8sBm_NVw9_vSrPvr_hXJYdl4LktGcD1uRNjk3AU0BcgxCc",
        "_ga_WC57KJ50ZZ": "GS1.1.1717282675.5.0.1717282679.0.0.0",
    }
    # the following variables are to be inputted by the user
    country = "Germany"
    city = "Berlin"
    duration = 7
    country_of_origin = "Egypt"

    client = Gemini(cookies=cookies)
    test_response = client.generate_content(
        f"hello gemini, I'm traveling to {country} in {city} for {duration} days, and my country of origin is {country_of_origin}. I need you to generate an itinerary for me, giving me a list of activities about what to do each day (format it in bullet points for each day) and how much will i spend for each activity in my home country currency."
    )
    
    return render(request, "travel_plan/program_output.html", {"test_response": test_response})
