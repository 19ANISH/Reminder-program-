#codes for reminder
import pygame
from time import time
import datetime
from plyer import notification
water='water.mp3'
facebook='facebook.mp3'
instagram='instagram.mp3'
youtube='youtube.mp3'
whatsapp='whatsapp.mp3'
user_name=input("Enter your name:\n")
print(f"{user_name.capitalize()} Welcome To Our Application")
user_age=int(input("Enter your age:\n"))
print(f"You Entered {user_age}\n")
with open("reminder_list.txt",'a') as f:
    f.write(f"{datetime.datetime.now()} completed\n")
if __name__ == '__main__':
    init_water=time()
    init_facebook=time()
    init_instagram=time()
    init_youtube=time()
    init_whatsapp=time()
    print("Press 1 to set reminder for drinking water:\n"
          "Press 2 to set reminder for usage of facebook:\n"
          "Press 3 to set reminder for usage of instagram:\n"
          "Press 4 to set reminder for usage of youtube:\n"
          "Press 5 to set reminder for usage of whatsapp:\n")
    user_choice=(input("Enter your choice:\n"))
    if user_choice=='1':
        water_reminder = float(input("Enter time to remind you to drink water:\n"))
        water_mins = water_reminder * 60
        while 1:
            if time() - init_water > water_mins:
                title="WATER"
                message=f"TIME TO DRINK WATER, YOU HAVE NOT DRANK WATER SINCE {water_mins/60} minutes"
                notification.notify(title=title,message=message,app_icon=r"C:\Users\Shrey Shaha\Desktop\Python\water_icon.ico",timeout=3,toast=False)
                pygame.mixer.init()
                pygame.mixer.music.load(water)
                pygame.mixer.music.play()
                input_to_stop = input("Press Y to stop alarm\n")
                if input_to_stop.lower() == 'y':
                    pygame.mixer.music.stop()
                else:
                    print("Reminder Snoozed for more 10 minutes")
                    init_water=time()
                    water_mins=10*60
                    if time()-init_water>water_mins:
                        notification.notify(title=title,message=message,app_icon=r"C:\Users\Shrey Shaha\Desktop\Python\water_icon.ico",timeout=3,toast=False)
                        pygame.mixer.init()
                        pygame.mixer.music.load(water)
                        pygame.mixer.music.play()
                        input_to_stop_= input("Press Y to stop alarm\n")
                        if input_to_stop.lower() == 'y':
                            pygame.mixer.music.stop
                    continue
                init_water = time()
                print(f"Drank at {datetime.datetime.now()}")
                break
    elif user_choice=='2':
        facebook_reminder = float(input("Enter your maximum time to use facebook:\n"))
        facebook_mins = facebook_reminder * 60
        while True:
            if time() - init_facebook > facebook_mins:
                title1 = "FACEBOOK"
                message1 = f"YOUR USING FACEBOOK SINCE {facebook_mins/60} minutes"
                notification.notify(title=title1, message=message1,
                                    app_icon=r"C:\Users\Shrey Shaha\Desktop\Python\facebook_icon.ico", timeout=3,
                                    toast=False)
                print(f"Your screen time for facebook is {(facebook_mins) / 60} minutes, time to turn off facebook")
                pygame.mixer.init()
                pygame.mixer.music.load(facebook)
                pygame.mixer.music.play()
                input_to_stop1 = input("Press Y to stop alarm\n")
                if input_to_stop1.lower() == 'y':
                    pygame.mixer.music.stop()
                else:

                    print("Screen time for facebook is increased by 10 minutes")
                    print(f"Your screen total time for facebook is  {facebook_mins/60 + 10} minutes")
                    init_facebook=time()
                    facebook_mins=10*60
                    continue
                init_facebook = time()
                print(f"Closed at {datetime.datetime.now()}\n")
                break
    elif user_choice=='3':
        instagram_reminder = float(input("Enter your maximum time to use instagram:\n"))
        instagram_mins = instagram_reminder * 60
        while True:
            if time() - init_instagram > instagram_mins:
                title3 = "INSTAGRAM"
                message3 = f"YOUR INSTAGRAM USAGE {instagram_mins/60} minutes"
                notification.notify(title=title3,message=message3,app_icon=r"C:\Users\Shrey Shaha\Desktop\Python\instagram_icon.ico",timeout=3,toast=False)
                print(f"Your screen time for instagram is {(instagram_mins) / 60} minutes, time to turn off instagram")
                pygame.mixer.init()
                pygame.mixer.music.load(instagram)
                pygame.mixer.music.play()
                input_to_stop2 = input("Press Y to stop alarm\n")
                if input_to_stop2.lower() == 'y':
                    pygame.mixer.music.stop()
                else:
                    print("Screen time for instagram is increased by 10 minutes")
                    print(f"Your total screen time for instagram is {((instagram_mins) / 60) + 10} minutes")
                    instagram_mins=time()
                    instagram_mins =10*60
                    continue
                init_instagram = time()
                print(f"Closed at {datetime.datetime.now()}\n")
                break
    elif user_choice=='4':
        youtube_reminder = float(input("Enter your maximum time to use youtube:\n"))
        youtube_mins = youtube_reminder * 60
        while 1:
            if time() - init_youtube > youtube_mins:
                title4="YOUTUBE"
                message4=f"YOU HAVE BEEN USING YOUTUBE FOR {youtube_mins/60} minutes"
                notification.notify(title=title4, message=message4,
                                    app_icon=r"C:\Users\Shrey Shaha\Desktop\Python\youtube_icon.ico", timeout=3,
                                    toast=False)
                print(f"Your screen time for youtube is {(youtube_mins) / 60} minutes, time to turn off youtube")
                pygame.mixer.init()
                pygame.mixer.music.load(youtube)
                pygame.mixer.music.play()
                input_to_stop3 = input("Press Y to stop alarm\n")
                if input_to_stop3.lower() == 'y':
                    pygame.mixer.music.stop()
                else:
                    print("Screen time for youtube is increased by 10 minutes")
                    print(f"Your total screen time for youtube is {((youtube_mins) / 60) + 10} minutes")
                    init_youtube=time()
                    youtube_mins =10*60
                    continue
                init_youtube = time()
                print(f"Closed at {datetime.datetime.now()}\n")
                break
    elif user_choice=='5':
        whatsapp_reminder = float(input("Enter your maximum time to use whatsapp:\n"))
        whatsapp_mins = whatsapp_reminder * 60
        while True:
            if time() - init_whatsapp > whatsapp_mins:
                title5="WHATSAPP"
                message5=f"WHATSAPP IS IN USE FROM LAST {whatsapp_mins/60} minutes"
                notification.notify(title=title5,message=message5,app_icon=r"C:\Users\Shrey Shaha\Desktop\Python\whatsapp_icon.ico",timeout=3,toast=False)
                print(f"Your screen time for whatsapp is {(whatsapp_mins) / 60} minutes, time to turn off whatsapp")
                pygame.mixer.init()
                pygame.mixer.music.load(whatsapp)
                pygame.mixer.music.play()
                input_to_stop4 = input("Press Y to stop alarm\n")
                if input_to_stop4.lower() == 'y':
                    pygame.mixer.music.stop()
                else:
                    print("Screen time for whatsapp is increased by 10 minutes")
                    print(f"Your total screen time for whatsapp is {((whatsapp_mins) / 60) + 10} minutes")
                    init_whatsapp=time()
                    whatsapp_mins = 10* 60
                    continue
                init_whatsapp = time()
                print(f"Closed at {datetime.datetime.now()}\n")
                break
    else:
        print("Invaild Input  :(")

