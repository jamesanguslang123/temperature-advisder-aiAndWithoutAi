import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OLLAMA_URL = os.environ.get(
    "OLLAMA_HOST", "http://localhost:11434"
).rstrip("/")

OLLAMA_MODEL = os.environ.get(
    "OLLAMA_MODEL", "gpt-oss:20b-cloud"
)

userCountry = input("What country are you from? ")

try:
    userTemperature = float(
        input("What is the current temperature in Celsius? ")
    )
except ValueError:
    print("Please enter a valid number for the temperature.")
    raise SystemExit

prompt = f"""
Analyse the temperature entered by the user.

Country: {userCountry}
Temperature: {userTemperature} degrees Celsius
Month: {input("What month is it? ")}
Explain whether the temperature is cold, mild, warm, or hot.
Discuss whether it is typical or unusual for that country
at this time of year . Be clear if you are uncertain.
Do not invent climate statistics.
"""

data = {
    "model": OLLAMA_MODEL,
    "prompt": prompt,
    "stream": False
}

request = Request(
    f"{OLLAMA_URL}/api/generate",
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    with urlopen(request, timeout=120) as response:
        response_text = response.read().decode("utf-8")

    # First try to parse the complete response as one JSON object.
    try:
        result = json.loads(response_text)

    except json.JSONDecodeError:
        # If there are multiple JSON objects, parse each line.
        result = None

        for line in response_text.splitlines():
            if line.strip():
                result = json.loads(line)

    if result and "response" in result:
        print("\n--- ClimateCheck AI Analysis ---\n")
        print(result["response"])
    else:
        print("The AI response did not contain the expected answer.")
        print(response_text)

except HTTPError as error:
    print(f"HTTP error: {error.code} - {error.reason}")

except URLError as error:
    print(f"Could not connect to Ollama: {error.reason}")

except json.JSONDecodeError:
    print("Could not understand Ollama's response. Please try again.")