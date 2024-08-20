import win32com.client
speaker = win32com.client.Dispatch("SAPY.SpVoice")

print("welcome for shoutout")
list = ['nominath']

for l in list:
    speaker.Speak(f"shout our for {l}")

# https://replit.com/@NominathKuwar/text-to-speak#main.py
