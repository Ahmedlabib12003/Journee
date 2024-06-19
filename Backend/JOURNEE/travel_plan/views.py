from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from gemini import Gemini
import re


# Create your views here.
def booking (request):
    # Cookies placed here
    if request.method == "POST":
        budget = int(request.POST.get("budget"))
        travel_style = request.POST.get("travel_style")
        travel_group = request.POST.get("travel_group")
        destination = request.POST.get("destination")
        coo = request.POST.get("coo")
        date_start = request.POST.get("date_start")
        date_end = request.POST.get("date_end")

        #A_budget = budget // 2
        #F_budget = round(budget * 0.2)
        #H_budget = round(budget * 0.3)

        urls_to_remove = [
            r"http://googleusercontent\.com/tool_disclaimer_content/1",
            r"http://googleusercontent\.com/hotel_content/0",
            r"http://googleusercontent.com/flight_content/0",
            r"\[Image of [^]]+\]"
        ]
        url_pattern = r"|".join(urls_to_remove)

        # cookie inserted here
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
            "NID": "515",
            "_ga_WC57KJ50ZZ": "GS1.1.1718586273.9.1.1718586280.0.0.0",
            "__Secure-1PSIDTS": "sidts-CjEB3EgAEgLWaxapMaBMT36q-pD_h1lXA1cJJnAjppYrHTfDSGC9gmfjNVaYhC7Ww8lFEAA",
            "__Secure-3PSIDTS": "sidts-CjEB3EgAEgLWaxapMaBMT36q-pD_h1lXA1cJJnAjppYrHTfDSGC9gmfjNVaYhC7Ww8lFEAA",
            "SIDCC": "AKEyXzUXr8zxJDudWvfUCq3FVH_eM-5whhbOb_2UvdW361VOehuXbKNLGPht13MN19REbZaIYA",
            "__Secure-1PSIDCC": "AKEyXzUsw-f6fpa-uFGVSKYt1_nsnvk3jvdLL8gtS-B85Esum8SHE8e3vrsa0szlK03TJwnwzKs",
            "__Secure-3PSIDCC": "AKEyXzU7YBLL0BPMOKf7ciEFVsQb0H_SLNg2huG4AUo3zbsU4S7AXehZp3PQRWPkeHOdZKvhhQ8",
        }

        client = Gemini(cookies=cookies)
        Activities = client.generate_content(
            f"""hello gemini, I'm travelling to {destination},
            from {date_start} to {date_end}. my country of origin is {coo}(use it to conclude the currency and show the current exchange rate) and my budget is {budget}.
            my travel group is {travel_group}, and my travel style is {travel_style}. I need you to act as a travel advisor and reply only
            with an itenerary that contains a list of activities about what to do each day and how much will be spent per activity
            (include internal mode of trasnportation and its costs)
            witout giving additional tips or anything in the end. just a plain itinerary with no intros or outros.
            (format it in bullet points for each day e.g day1:... day2:... etc) also exclude flight and accommodation expenses,
            taking in consideration the data I told you about above"""
        )
        
        activities = re.sub(url_pattern, "", Activities.text)

        Flights = client.generate_content(
            f"""hello gemini, I'm travelling to {destination} from {date_start} to {date_end}.
            my country of origin is {coo}.can you show me a list of all available flights (in bullet points).
            Reply only in bullet points with no intros or outros"""
        )

        flight = re.sub(url_pattern, "", Flights.text)

        Accommodation = client.generate_content(
            f"""hello gemini, I'm travelling to {destination} from {date_start} to {date_end} with a budget of {budget}.
            my country of origin is {coo}(use it to conclude the currency).I need you to reply with a list of hotels and the price per night in bullet points.
            (No intro or outro)"""
        )

        accommodation = re.sub(url_pattern, "", Accommodation.text)

        return render(
            request,
            "travel_plan/program_output.html",
            {
                "activities": activities,
                "flight": flight,
                "accommodation": accommodation,
            },
        )
    else:
        return render(request, "travel_plan/booking.html")