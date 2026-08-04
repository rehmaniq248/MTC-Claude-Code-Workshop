"""Prayer Times MCP server — wraps the free Aladhan API.

One tool: given a city/country, returns today's five prayer times plus
the Gregorian->Hijri date conversion, in a single call.
"""

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("prayer-times")

ALADHAN_URL = "https://api.aladhan.com/v1/timingsByCity"

# Method 2 = Islamic Society of North America (ISNA) — sensible default for
# a US demo. Asr madhab: 0 = Shafi'i/Maliki/Hanbali (standard shadow ratio).
DEFAULT_METHOD = 2
DEFAULT_SCHOOL = 0


@mcp.tool()
def get_prayer_times(city: str = "San Diego", country: str = "USA") -> dict:
    """Get today's prayer times and Hijri date for a city.

    Returns Fajr, Dhuhr, Asr, Maghrib, Isha (24h "HH:MM"), the Gregorian
    date, and the corresponding Hijri date (day/month name/year).
    """
    resp = httpx.get(
        ALADHAN_URL,
        params={
            "city": city,
            "country": country,
            "method": DEFAULT_METHOD,
            "school": DEFAULT_SCHOOL,
        },
        timeout=10,
        follow_redirects=True,
    )
    resp.raise_for_status()
    data = resp.json()["data"]
    timings = data["timings"]
    hijri = data["date"]["hijri"]

    return {
        "city": city,
        "country": country,
        "gregorian_date": data["date"]["gregorian"]["date"],
        "hijri_date": f"{hijri['day']} {hijri['month']['en']} {hijri['year']} AH",
        "prayers": {
            "fajr": timings["Fajr"],
            "dhuhr": timings["Dhuhr"],
            "asr": timings["Asr"],
            "maghrib": timings["Maghrib"],
            "isha": timings["Isha"],
        },
    }


if __name__ == "__main__":
    mcp.run()
