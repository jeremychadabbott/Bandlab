#This code vilates BANDLABS TERMS AND CONDITIONS
#it is for educational and demonstration purposes.
#It points out that Bandlab does not require a 'log in' to register a 'play'
#this code adds 'plays' to a 'track', qty is calculated off how many comments and likes there are
#   so that the amount of 'plays' always appears to be in the correct proportion to avoide the 
#   perception of "pay for play"

#Import text analysis tool
import re

#Import timekeeping tool
import time

#Import Selenium for chrome interations
from selenium import webdriver

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


#Variables that I comment out if I'm not using--->
#bandlab_plays = 0
#bandlab_plays = input("Total plays wanted? ")
#bandlab_plays = int(bandlab_plays)

#Begining of the loop, where 't' is the main loop, the uper bound of 50,000 cycles is will never 
#   be achieved so basically you just break the code when you're tired of it running. otherwise it
#   "continuously" checks the links to see if they need additional plays
for t in range(0,50000):
    bandlab_play = 0

    #Second loop, where the track to receive plays is decided.
    #This function is to provide the user the capability to have multiple tracks played in sequence
    for i in range (0,19):
        #Track List:
        TargetURL = ""
        if i == 18:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/psychadelics-fe924b3f?revId=c791966b-db94-ec11-a507-0050f280e91e" #Psychadelics
        if i == 17:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/january-29-8298a952?revId=42c16839-3d81-ec11-94f6-0003ffcd3240" #January 29
        if i == 16:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/more-than-blood-5c0d23a1?revId=0b785e15-7d63-ec11-94f6-a04a5e79a6b8" #More than Blood
        if i == 15:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/pajama-drinking-7b6b379d?revId=40c3f236-cf83-ed11-9d7a-000d3a3eed2a" #Pajama Drinking
        if i == 14:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/cheat-code-157681f5?revId=7f01de4c-bc5b-ec11-94f6-a04a5e79a6b8" #Cheat code
        if i == 13:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/new-project-c5d3a7e2?revId=df2aa411-a721-ed11-9441-000d3a3f83b4" #Focus on the Good SAX VERSION
        if i == 12:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/fallin-0ba6d219?revId=a1af7d27-474a-ed11-819a-000d3a3eefd0" #Fallin
        if i == 11:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/make-my-way-95171031?revId=38399629-4583-eb11-9889-0050f28a50ba" #Make my way
        if i == 10:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/far-from-the-ocean-4c0229b8?revId=0b2f0051-ea45-ed11-b495-000d3a3ee153" #Far from the ocean
        if i == 1:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/focus-on-the-good-107b7f6f?revId=4f2f40e6-8119-ed11-9441-000d3a3f83b4" #Focus on the Good
        if i == 2:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/sad-to-be-so-happy-full-version-d10b5061?revId=5cc05f62-ea61-ed11-819a-000d3a3eefd0" #Sad to be so happy
        if i == 3:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/living-in-a-dreamcwp-77422bc2?revId=f351ae9f-0337-ed11-b494-000d3a3ee5f3" #Living in a dream
        if i == 4:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/the-lonely-11692bf0?revId=dd3a4d56-1d14-ed11-bd6e-281878315d59" #The Lonely (Preview)
        if i == 5:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/where-the-band-plays-6a641622?revId=cdb9f0c1-3d53-ed11-819a-000d3a3eefd0" #Where the Band Plays
        if i == 6:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/the-lesson-7565fe8c?revId=839ace4d-6665-ed11-819a-000d3a3ee86d" #The LEsson
        if i == 7:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/i-get-high-on-my-dreams-d942971c?revId=c86366c4-714b-ed11-819a-000d3a3eefd0" #I get high
        if i == 8:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/postapocalyptic-love-song-a1d93a24?revId=f6918fe5-e762-ed11-819a-000d3a3ee86d" #postapocolypti love song
        if i == 9:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/glutton-for-punishment-efd4d8b7?revId=4f619db4-3348-ed11-b495-000d3a3ee153" #Glutton for Punishment
        if i == 0:
            TargetURL = "https://www.bandlab.com/jeremyabbottmusic/new-project-1938a5b5?revId=89e8de29-2f09-ed11-b47a-281878315d59" #Contact High


        # Open Chrome with our without options (headless) by commenting out the one you don't want
        driver = webdriver.Chrome(chrome_options=options)
        #driver = webdriver.Chrome()

        #Maximize window
        driver.maximize_window()

        #Provide user track info
        print(TargetURL)

        #Open track in bandlab
        driver.get(TargetURL)

        #Wait for bandlab to load
        driver.implicitly_wait(200)

        #Try to click "got it" to remove cookies ribbon that appears at bottom of screen        
        try:
            element = driver.find_element_by_xpath("/html/body/cookie-consent/div/div/a")
            element.click ()
            #give user info that cookie ribbon was dismissed
            print ("dismissed coookie ribbon")
        #It's ok if can't find cookies ribbon
        except:
            time.sleep(.01)

        #Get Track Title on webpage
        track_title = driver.find_element("xpath", '/html/body/main/div/section[1]/div/div/div[2]/div[1]/h1').text
        
        #Give user the track title and where we are in the loop
        print (" ")
        print(" ")
        print ("Track " + str(i) + "/14 -> " + track_title)

        #Try to Find total likes
        try:
            element = driver.find_element_by_xpath('/html/body/main/div/section[2]/div/div/div[1]/span/like')
            Clss = element.get_attribute(Class)
            #Tell user the amount of likes 
            Print (Clss)
        except:
            #likes = driver.find_element_by_xpath('/html/body/main/div/div[2]/div/div/div[1]/div/span/like/span').text
            likes = driver.find_element("xpath",'/html/body/main/div/section[2]/div/div/div[1]/span/like').text
        print ("Likes:" + str(likes))
        if likes[-1] == "K":
            print ("K Exists, modify")
            likes = likes[:-1]
            print ("Dropped K: " + str(likes))
            multiply = 1000
            #print("find chracter:" + str(likes[-3]))
            if len(likes) > 1:

                if likes[-2] == ".":
                    multiply = 100
            if len(likes)>2:

                if likes[-3] == ".":
                    multiply = 10
            likes = re.sub('[.]', '', likes)
            likes = int(likes)
            likes = likes * multiply
            print("Revised:" + str(likes))

        #Find total plays
        try:
            print ("Trying first method")
            plays = driver.find_element_by_css_selector('play-counter').innertext
        except:   
            print ("Trying second method")
            plays = driver.find_element("xpath",'/html/body/main/div/section[2]/div/div/div[1]/div[3]/play-counter').text

        print ("Plays:" + str(plays))
        if plays[-1] == "K":
            #print ("K Exists, modify")
            plays = plays[:-1]
            #print ("Dropped K: " + str(plays))
            multiply = 1000
            #print("find chracter:" + str(plays[-3]))
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

        #Evaluate how many plays should be added to match like ratio

        bandlab_plays = 0
        if int(likes) < 171:
            bandlab_plays = int(likes) * 2
        if int(likes) > 170:
            bandlab_plays = ((int(likes)/10)*(int(likes)/10)*1.2) 


        print("Target Plays: " + str(bandlab_plays)) 
        bandlab_plays = bandlab_plays - int(plays)
        if bandlab_plays < 0:
            bandlab_plays = 0
        print ("Plays to add:   ----------------------------->" + str(bandlab_plays))

        bandlab_play = 0  

        #var = amount of time we're goingt to spend on a song beyond 10 seconds
        var = 1
        if bandlab_plays < 1000:
            var = 5
        if bandlab_plays < 100:
            var  = 30
        if bandlab_plays < 50:
            var = 60
        if bandlab_plays < 20:
            var = 120

        print ("Wait:" + str(var))


        if bandlab_plays > 2:
            for x in range (1, (int(bandlab_plays))):
                driver = webdriver.Chrome(chrome_options=options)
                #driver = webdriver.Chrome()
                driver.get(TargetURL)
                driver.implicitly_wait(10) # seconds
                time.sleep(2) # Load Page
                try:
                    'Find "Play Icon'
                    #/html/body/main/div/section[1]/div/div/div[1]/div/div[1]
                    element = driver.find_element("xpath","/html/body/main/div/section[1]/div/div/div[1]/div")
                    element.click () #try to hit Play Music
                    wait_more = (randrange(var))
                    time.sleep(9 + wait_more) 
                    bandlab_play = bandlab_play + 1
                except NoSuchElementException:
                    #print ("Bandlab No such element (Play Icon) error recorded")
                    time.sleep(.1)
                except ElementClickInterceptedException:
                    #print ("Bandlab click intercepted exception recorded")
                    time.sleep(.1)
                except ElementNotInteractableException:
                    #print ("Bandlab click play not interactable recorded")
                    time.sleep(.1)

                print (track_title + "->" + str(bandlab_play) + "/" + str(bandlab_plays))
                driver.close()
        print ("")
    print ("..............................")
    print ("Cycle " + str(t) + " Complete")
    print (".............................")












