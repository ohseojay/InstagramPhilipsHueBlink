from instaloader import Instaloader, Profile
from phue import Bridge
import time

L = Instaloader()
b = Bridge('Your Bridge IP address') #change this to your philips hue bridge's ip address

profile = Profile.from_username(L.context, "Your Instagram Username") #change this to your instagram username
followersave = (profile.followers)

b.set_light('Your Philips hue light name', 'on', True) #change this to the light's name you chose on the philips hue app
b.set_light('Your Philips hue light name', 'bri', 81) #change this to the light's name you chose on the philips hue app, the number 81 is brightness
b.set_light('Your Philips hue light name', 'on', False) #change this to the light's name you chose on the philips hue app
#this code checks if the code has started successfully

while True:
    time.sleep(5) #choose how many seconds for the delay of the reload
    profile = Profile.from_username(L.context, "Your Instagram Username") #change this to your instagram username

    if (profile.followers) > followersave:
        profile = Profile.from_username(L.context, "Your Instagram Username") #change this to your instagram username
        followersave = (profile.followers)
        b.set_light('Your Philips hue light name', 'on', True) #change this to the light's name you chose on the philips hue app
        b.set_light('Your Philips hue light name', 'bri', 81)  #change this to the light's name you chose on the philips hue app, the number 81 is brightness
        b.set_light('Your Philips hue light name', 'on', False)  #change this to the light's name you chose on the philips hue app
    else:
        followersave = (profile.followers)