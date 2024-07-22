# Bandlab
Automations for Bandlab
These files VIOLATE BANDLABS TOS. They are for EDUCATION and for Bandlab to see where and how the can be exploited.
 
#   This code violates BANDLABS TERMS AND CONDITIONS by increasing play count
#   it is for educational and demonstration purposes.
#   It points out that Bandlab does not require a 'log in' to register a 'play'
#   this code loops through up to 20 URLs (tracks) you set and adds plays, proportional to the amount of likes
#   so that the amount of 'plays' always appears to be in the correct proportion to avoid the perception of
#   "pay for play". This code works exceptionally well in conjuction with another script which might add likes 

#   1.) Add up to 20 URL's to monitor
#   2.) Amount of plays to add is amutomatically calculated by formula, considering amount of existing likes
#   3.) Amount of time each track is played is determined by calculation
#   4.) the intent of the code is to make adding plays "automatic" and beleivable 
#------------------------------------------------------------------------------------------------------------------------

#Import text analysis tool
import re

#Import timekeeping tool
import time

#Import Selenium for chrome interations
from selenium import webdriver
from selenium.webdriver.common.by import By

#Import chrome options and the ability to run headless (without seeing it)
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True

#import errors library so can use some error handling in the code
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException

#import the ability to generate random numbers
from random import randrange

#----------------------------------------------------------------------------------------------------------
#   Begining of the main loop, where 't' is the main loop, the uper bound of 50,000 cycles is will never 
#   be achieved so basically you just break the code when you're tired of it running. otherwise it
#   "continuously" checks the links to see if they need additional plays
#----------------------------------------------------------------------------------------------------------

for t in range(0,50000):
    #   Second loop start , where the track to receive plays is decided.
    #   This function is to provide the user the capability to have multiple tracks played in sequence
    for i in range (0,19):

        #Track List----------------->Replace my tracks with yours. Empty "" is OK, will tell code to jump back to start
        TargetURL = ""
        if i == 18:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/if-we-had-a-soul-bfb661a3?revId=a4670f89-ad46-ee11-b8f0-000d3a41ec20" #If we had a soul
        if i == 17:
            TargetURL = "https://www.bandlab.com/track/230380b7-1ff1-ee11-aaf0-000d3aa5105b?revId=220380b7-1ff1-ee11-aaf0-000d3aa5105b" #Critcial THought
        if i == 16:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/where-have-all-the-flowers-gone-instrumental-ddd1d951?revId=1d20e017-416c-ee11-9937-000d3a41ec2a" #Flowers Gone
        if i == 15:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/ill-be-there-for-you-final-version-a5d4952c?revId=73f984f5-1d6d-ee11-9937-000d3a41ec2a" #Ill be there for you
        if i == 14:
            TargetURL = "https://www.bandlab.com/track/7a13ea7f-1b04-ef11-aaf0-000d3aa5105b?revId=7713ea7f-1b04-ef11-aaf0-000d3aa5105b" #At least I am Human
        if i == 13:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/new-project-c5d3a7e2?revId=df2aa411-a721-ed11-9441-000d3a3f83b4" #Focus on the Good SAX VERSION
        if i == 12:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/fallin-0ba6d219?revId=a1af7d27-474a-ed11-819a-000d3a3eefd0" #Fallin
        if i == 11:
            TargetURL = "https://www.bandlab.com/track/998ccdd8-92fd-ee11-aaf0-000d3aa5105b?revId=988ccdd8-92fd-ee11-aaf0-000d3aa5105b" #Beach Day
        if i == 10:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/far-from-the-ocean-4c0229b8?revId=0b2f0051-ea45-ed11-b495-000d3a3ee153" #Far from the ocean
        if i == 1:
            TargetURL = "https://www.bandlab.com/track/bc392dc8-1ea5-ee11-8926-000d3a428257?revId=b9392dc8-1ea5-ee11-8926-000d3a428257" #Guns
        if i == 2:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/ill-take-care-of-you-fd754938?revId=98d161c5-025b-ee11-9937-000d3a41ec2a" #Ill take care of you
        if i == 3:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/living-in-a-dreamcwp-77422bc2?revId=f351ae9f-0337-ed11-b494-000d3a3ee5f3" #Living in a dream
        if i == 4:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/the-lonely-11692bf0?revId=dd3a4d56-1d14-ed11-bd6e-281878315d59" #The Lonely (Preview)
        if i == 5:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/where-the-band-plays-6a641622?revId=cdb9f0c1-3d53-ed11-819a-000d3a3eefd0" #Where the Band Plays
        if i == 6:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/sleep-tight-8f298e98?revId=d2ee3726-0a76-ee11-9937-000d3a41ec2a" #SleepTight
        if i == 7:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/i-get-high-on-my-dreams-d942971c?revId=c86366c4-714b-ed11-819a-000d3a3eefd0" #I get high
        if i == 8:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/test-9401297d?revId=f3306aad-e68b-ee11-b75e-000d3a428fff&commentId=60826245" #peel my mind
        if i == 9:
            TargetURL = "https://www.bandlab.com/sjong/blink-of-an-eye-4d2427da-1506a78?revId=d36f2fb2-c68f-ee11-b75e-000d3a428fff" #Blink of an Eye with PIP
        if i == 0:
            TargetURL = "https://www.bandlab.com/track/bc392dc8-1ea5-ee11-8926-000d3a428257?revId=b9392dc8-1ea5-ee11-8926-000d3a428257" #Guns

        #TargetURL = "https://www.bandlab.com/track/24f7ea88-36c1-ee11-b660-000d3a428b97?revId=23f7ea88-36c1-ee11-b660-000d3a428b97" #misery


   
        # Open Chrome with our without options (headless) by commenting this out
        driver = webdriver.Chrome(chrome_options=options)
        #driver = webdriver.Chrome()

        #Maximize window
        driver.maximize_window()

        #Provide user track info in terminal
        print(TargetURL)

        #Open track in bandlab
        driver.get(TargetURL)

        #Wait for bandlab to load
        driver.implicitly_wait(200)

        #Try to click "got it" to remove cookies ribbon that appears at bottom of screen        
        try:
            element = driver.find_element_by_xpath("/html/body/privacy-banner/div/div[2]/button")
            element.click ()
            #give user info that cookie ribbon was dismissed in terminal
            print ("dismissed coookie ribbon")
        #It's ok if can't find cookies ribbon
        except:
            time.sleep(.01)

        #Get Track Title on webpage
        #track_title = driver.find_element("xpath", '/html/body/main/div/section[1]/div/div/div[2]/div[1]/h1').text
        track_title = TargetURL
        #Give user the track title and where we are in the loop in terminal
        print (" ")
        print (" ")
        print ("Track " + str(i) + "/19 -> " + track_title)

        # Find the element by class name
        likes = driver.find_element(By.CLASS_NAME, 'semibold-12').text

        # Get the text content of the element
        #likes_count = int(likes_element.text)

        #likes = str(likes_count)  # Convert integer to string
   
        
        #   Give user qty of likes feedback in terminal
        print ("Likes:" + str(likes))

        #   Convert the amount of likes into a number because somtimes short hand is used, like 1.1k. 
        #   If a "K" is found in the number, remove it and multiply the original number by 1000
        if likes[-1] == "K":
            print ("K Exists, modify")
            likes = likes[:-1]
            #provide user feedback on how the number of likes modification is going
            print ("Dropped K: " + str(likes))
            multiply = 1000
            #If a "." is found in 2nd position in the number, remove it and multiply the original number by 100
            if len(likes) > 1:
                if likes[-2] == ".":
                    multiply = 100
            if len(likes)>2:
            #If a "." is found in 3nd position in the number, remove it and multiply the original number by 10
                if likes[-3] == ".":
                    multiply = 10
            likes = re.sub('[.]', '', likes)
            likes = int(likes)
            likes = likes * multiply
            #Provide feedback to the user on how the number conversion is going
            print("Revised:" + str(likes))

        # Locate the element using XPath
        try:
            print ("trying first plays location")
            plays_element = driver.find_element("xpath", '/html/body/main/div/section[1]/div/div[1]/div/div[2]/div[1]/div/play-counter')
            plays_text = plays_element.text
        except:
            print ("Try second plays location")
            plays_text = "30"

        # Convert text to integer
        plays = str(plays_text)

        #Give user feedback about how many existin gplays were found, and convert number similar to above
        print ("Plays:" + str(plays))
        if plays[-1] == "K":
            plays = plays[:-1]
            multiply = 1000
            if len(plays)>1:
                if plays[-2] == ".":
                    multiply = 100
            if len(plays) > 2:
                if plays[-3] == ".":
                    multiply = 10
            plays = re.sub('[.]', '', plays)
            plays = int(plays)
            plays = plays * multiply
            print("Revised:" + str(plays))
        time.sleep(1)
        driver.close()

        #Calculate how many plays to add considering the amount of likes
        bandlab_plays = 0
        if int(likes) < 171:
            bandlab_plays = int(likes) * 2
        if int(likes) > 170:
            bandlab_plays = ((int(likes)/10)*(int(likes)/10)*1.2) 

        #Give user feedback in terminal, how many plays to add
        print("Target Plays: " + str(bandlab_plays)) 
        bandlab_plays = bandlab_plays - int(plays)
        if bandlab_plays < 0:
            bandlab_plays = 0
        print ("Plays to add:   ------------------->" + str(bandlab_plays))

        bandlab_play = 0  

        #   var = amount of time we're going to spend playing a song beyond 10 seconds. Take our
        #   time if we're only adding a few plays so user gets maximum value, but move quickly if
        #   we need to add a lot of plays so it doesn't take forever
        var = 1
        if bandlab_plays < 1000:
            var = 5
        if bandlab_plays < 100:
            var  = 30
        if bandlab_plays < 50:
            var = 60
        if bandlab_plays < 20:
            var = 120
        #Tell user in terminal, how long we're letting each track play
        print ("Wait:" + str(var))

        #Loop 3, play track if call for additional plays is greater than 2, otherwise, don't bother rn
        if bandlab_plays > 2:
            for x in range (1, (int(bandlab_plays))):
                driver = webdriver.Chrome(chrome_options=options)
                #driver = webdriver.Chrome()
                driver.get(TargetURL)
                driver.implicitly_wait(10) # seconds
                time.sleep(2) # Load Page

                #Try to find and press 'Play Icon'
                try:
                    #/html/body/main/div/section[2]/div/div/div[1]/div/player-audio-button/svg[1]/path
                    element = driver.find_element("xpath","/html/body/main/div/section[1]/div/div[1]/div/div[1]/div")
                    print ("Found Play Button")
                    element.click () 
                    wait_more = (randrange(var))
                    time.sleep(9 + wait_more) 
                    bandlab_play = bandlab_play + 1
                #If there are any errors tryingt o find the play icon, just keep moving on
                except NoSuchElementException:
                    print ("Bandlab No such element (Play Icon) error recorded, trying alternate")
                    try:
                        element = driver.find_element("xpath","/html/body/main/div/section[2]/div/div/div[1]/div/player-audio-button")
                        print ("Found Play Button")
                        element.click () 
                        wait_more = (randrange(var))
                        time.sleep(9 + wait_more) 
                        bandlab_play = bandlab_play + 1
                        time.sleep(.1)
                    except NoSuchElementException:
                        print ("Still failed")
                        time.sleep(.1)
                except ElementClickInterceptedException:
                    print ("Bandlab click intercepted exception recorded")
                    time.sleep(.1)
                except ElementNotInteractableException:
                    print ("Bandlab click play not interactable recorded")
                    time.sleep(.1)
                #Give user some feedback in terminal on progress
                print (track_title + "->" + str(bandlab_play) + "/" + str(bandlab_plays))
                driver.close()
        print ("")
        
    #All tracks have been checked once, tell user in terminal, and start cycle over! 
    print ("..............................")
    print ("Cycle " + str(t) + " Complete")
    print (".............................")












