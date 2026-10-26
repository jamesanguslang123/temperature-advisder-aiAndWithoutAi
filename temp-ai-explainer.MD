ClimateCheck AI 🌡️

Overview

ClimateCheck AI is a Python project that uses an AI model through the Ollama API to analyse a temperature entered by the user. It asks the user for their country and the current temperature in degrees Celsius, then generates an explanation of whether the temperature is cold, mild, warm, or hot and whether it may be unusual for that country at this time of year.

Features

Asks the user to enter their country.

Accepts temperatures in degrees Celsius.

Uses an AI model through the Ollama API to analyse the information.

Generates a natural-language explanation of the temperature.

Handles invalid temperature input.

Handles connection errors and HTTP errors.

Processes the AI's JSON response.

Technologies Used

Python

Ollama API

JSON

HTTP requests

Python exception handling

How to Run

Install Python.

Install and set up Ollama.

Make sure the model configured in the program is available.

Save the program as temp_ai_analyser.py.

Run the program from your terminal:

python temp_ai_analyser.py

Enter your country and the current temperature when prompted.

What I Learned

Collecting and validating user input in Python.

Using environment variables to configure a program.

Sending HTTP requests to an API.

Converting JSON responses into Python data.

Handling exceptions such as invalid input and connection errors.

Using an AI model to generate a response from user-provided information.

Limitations

The analysis depends on the AI model's knowledge and response.

The program does not currently retrieve live weather or historical climate data.

Temperature classifications and claims about unusual weather may not always be accurate.

Future Improvements

Connect to a live weather API.

Compare current temperatures against historical climate data.

Build a graphical user interface.

Add more detailed location and seasonal analysis.

Improve response validation and testing.

Project Status

First working prototype.
