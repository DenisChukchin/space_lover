# Telegram channel with photos from space.
This project contains several scripts for downloading photos from space-related sites, as well as scripts for sending these photos by a bot in the Telegram channel.
## Prerequisites:
### Step 1:
For successful script run you will need to get API tokens.
+ [Telegram token](https://telegram.me/BotFather)
+ [NASA token](https://api.nasa.gov)
### Step 2:
You also need to find out ID for your chat-bot. Follow the instructions below.
+ [python-telegram-bot](https://github.com/python-telegram-bot/v13.x-wiki/wiki/Introduction-to-the-API)
## Installation.
Install Python3 latest version. Install PyCharm IDE, if you need it.
> To isolate the project, I'd recommend to use a virtual environment model. [vertualenv/venv](https://docs.python.org/3/library/venv.html).
 ## Preparing to run the script.
+ Create a virtualenv and activate it.
+ Then use pip (or pip3, there is a conflict with Python2) to install the dependencies (use the requirements.txt file):
```bash
% pip install -r requirements.txt
```
> For permanent set, create .env file and add variables in this format:
```python
NASA_TOKEN = "YOUR_TOKEN"
TELEGRAM_TOKEN = "YOUR_TOKEN"
TELEGRAM_CHAT_ID = int(YOUR_ID)
BOT_TIMER = 5
```
__BOT_TIMER__ - Time between sending messages with photos.
The variable is specified in seconds.
## Scripts.
### __fetch_spacex_images.py__
Uploads photos from the launch specified by the user. The photos will be saved to "Images" folder.
> Example: Upload photos from the 88th launch.
``` bash
% python3 fetch_spacex_images.py 88  
```
> If you don't know the launch number, then run the script without it. The script will upload photos of the last shuttle launch by default.
``` bash
% python3 fetch_spacex_images.py
```
### __fetch_apod_nasa_images.py__
The script will upload photos from the NASA website [Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html). The photos will be saved to "Images" folder.
> If you haven't set environment variables, then for a quick test run, export your private "NASA token" by this command:
``` bash
% export NASA_TOKEN="YOUR_TOKEN"
```
> Example: Let's download 12 photos from the NASA website.
``` bash
% python3 fetch_apod_nasa_images.py 12  
```
> If the number of photos is not set, then the script will download 5 photos by default.
``` bash
% python3 fetch_apod_nasa_images.py
```
### __fetch_epic_nasa_images.py__
The script will download photos of Earth from NASA's [EPIC website](https://epic.gsfc.nasa.gov). The photos will be saved to "Images" folder.
> If you haven't set environment variables, then for a quick test run, export your private "NASA token" by this command:
``` bash
% export NASA_TOKEN="YOUR_TOKEN"
```
> Example: Let's download 10 photos from the EPIC website.
> You can download no more than 13 photos tops. This photos taken 2 days ago from today.
``` bash
% python3 fetch_epic_nasa_images.py 10  
```
> If the number of photos is not set, then the script will download 5 photos by default.
``` bash
% python3 fetch_epic_nasa_images.py 
```
### __manual_bot.py__
This script allows the chatbot to send a photo that the user specifies.
> If you haven't set environment variables, then for a quick test run, export your private "Telegram token" and "TELEGRAM_CHAT_ID" by this commands:
``` bash
% export TELEGRAM_TOKEN="YOUR_TOKEN"
% export TELEGRAM_CHAT_ID=int("YOUR_ID_CHAT")
```
> Example: Let's send a specific photo "epic_planet_1.png".
``` bash
% python3 manual_bot.py epic_planet_1.png  
```
> If you don't know what to send,  the chat-bot will send random photo that is in the folder.
> 
``` bash
% python3 manual_bot.py
```
### __auto_bot.py__
The script allows the chatbot to send all the photos __one by one__ after a certain time in an infinite loop.
> If you haven't set environment variables, then for a quick test run, export your private "Telegram token" and "TELEGRAM_CHAT_ID" by this commands:
``` bash
% export TELEGRAM_TOKEN="YOUR_TOKEN"
% export TELEGRAM_CHAT_ID=int("YOUR_ID_CHAT")
```
> Example: Let's send a photo every 10 seconds.
``` bash
% python3 auto_bot.py 10    
```
> The default value is 4 hours (14400 seconds). Activate by this command.
``` bash
% python3 auto_bot.py
```
> If you want to use an environment variable, use the following command.
``` bash
% python3 auto_bot.py -user_timer
```
## Project goals.
*The program was designed by a student from online web development courses for educational purposes [Devman](https://dvmn.org).*
