import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="/home/bunty/Downloads/chromedriver")
browser.get('https://www.netflix.com/in/browse/genre/839338')



# Printing the heading
columns = shutil.get_terminal_size().columns
print("NETFLIX TRAILER AUTOMATION STARTS".center(columns))


# Getting the movie name and clicking on the movie
movie_name = browser.find_element(By.CLASS_NAME,
"nm-collections-title-name")
Name = movie_name.get_attribute("textContent")
print("The name of the movie is ", Name)
movie_name.click()

#Clicking on the trailer video
element = browser.find_element(By.CLASS_NAME, "additional-video-image-wrapper")
browser.execute_script("var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});",element)
element.click()
video = element.get_attribute("automationTrack")
if video :
  print("Trailer is playing",video)


#Bonus
#Getting the summary
synopsis = browser.find_element(By.CLASS_NAME, "title-info-synopsis")
summary = synopsis.get_attribute("textContent")
print("The summary of the  movie is ", summary)

#getting the actor
actorlist = browser.find_element(By.CLASS_NAME, "title-info-talent")
actorName = actorlist.get_attribute("textContent")
print("The actors are :",actorName )
