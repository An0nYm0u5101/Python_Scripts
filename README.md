# Python-Scripts 

## hitz_top30
Grabs all 30 songs in https://hitz.com.my/charts/hitz-30-chart and downloads it with youtube-dl. 

Install requirements with ``pip install -r requirements.txt``

1. Run the script with ``--debug`` flag to enable debug mode.
2. If the response code is showing 503, it will most likely be Google Captcha limiting the request.
3. The audio will be downloaded in .opus format, if you are using Linux, please consider using Rhythmbox to play it.
4. You can also download any videos into audio format by running ``./app.sh <url>`` after ``chmod +x``
