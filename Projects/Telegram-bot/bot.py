import os
from os import environ, sendfile
import requests
import json
import telebot
import csv
from dotenv import load_dotenv
load_dotenv()

# TODO: 1.1 Add Request HTTP URL of the API
NUTRITIONIX_API_KEY = environ.get('NUTRITIONIX_API_KEY')
NUTRITIONIX_APP_ID = environ.get('NUTRITIONIX_APP_ID')
HTTP_API = environ.get('http_api')

headers = {'Content-Type': 'application/json',
           'x-app-id': NUTRITIONIX_APP_ID, 'x-app-key': NUTRITIONIX_API_KEY}
user = {'name': None, 'gender': None,
        'weight': None, 'height': None, 'age': None}
bot = telebot.TeleBot(HTTP_API)


@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    fileN = open('Nutrition_Report.csv', 'w')
    fileE = open('Exercise_Report.csv', 'w')
    fileNwriter = csv.writer(fileN)
    fileEwriter = csv.writer(fileE)
    fileNwriter.writerow(['Food_Name', 'Quantity', 'Calories', 'Fat','Carbohydrates', 'Protiens'])
    fileEwriter.writerow(['Exercise_Name', 'Duration(in mins)', 'Calories Burned'])
    fileE.close()
    fileN.close()
    # TODO: 3.1 Add CSV file creation

    bot.reply_to(
        message, 'Hello! I am TeleFit. Use me to monitor your health'+'\N{grinning face with smiling eyes}'+'\nYou can use the command \"/help\" to know more about me.')


@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nStay Healthy'+'\N{flexed biceps}')


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/nutrition Units Quantity-Type Food-Name\" command to get the nutrients of a particular food. For eg: \"/nutrition 1 piece chapati\"\n\n2.1 For using the bot to get details about an exercise you need to first set the user data using the command \"/user Name, Gender, Weight(in Kg), Height (in cm), Age\". For eg: \"/user Akshat, Male, 70, 6, 19\n\n2.2 Then you can use the command \"/execise Duration-amount Duration-unit Exercise-name\" to get data about an exercise. For eg: \"/exercise 40 minutes push-ups\"\n\n3.0. You can use the command \"/reports Report-name\" to get the reports in CSV Format. For eg: \"/reports nutrition\" to get nutrition report and \"/reports exercise\" to get exercise reports or use the command \"/reports nutrition, exercise\" to get both nutrition and exercise reports\n\n4.0. You can use the command \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['user'])
def setUser(message):
    global user
    usr_input = message.text[6:]
    Name, Gender, Weight, Height, Age = usr_input.split(", ")
    # TODO: 2.1 Set user data
    bot.reply_to(message, 'User set!')
    reply = 'Name: ' + str(Name)+"\n"+"Gender: "+str(Gender)+"\n"+"Weight: "+str(Weight)+"\n"+"Height: "+str(Height)+"\n"+"Age: "+str(Age)
    # TODO: 2.2 Display user details in the telegram chat
    bot.send_message(message.chat.id, reply)

 
@bot.message_handler(func=lambda message: botRunning, commands=['nutrition'])
def getNutrition(message):
    bot.reply_to(message, 'Getting nutrition info...')
    # TODO: 1.2 Get nutrition information from the API
    qinput = message.text[11:]
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    n = requests.request("POST", url, headers=headers, json={"query":qinput})
    for i in n.json():
        for j in (n.json()[i]):
            Nutrinfo = j
    # TODO: 1.3 Display nutrition data in the telegram chat
    itemname = str(Nutrinfo['food_name'])
    quantity = str(Nutrinfo['serving_qty'])
    calories = str(Nutrinfo['nf_calories'])
    fat = str(Nutrinfo['nf_total_fat'])
    carbs = str(Nutrinfo['nf_total_carbohydrate'])
    protiens = str(Nutrinfo['nf_protein'])
    INFo = "Item: "+ itemname +"\n"+"Quantity: " + quantity + "\n"+ "Calories: " + calories+"\n"+ "Carbohydrates: " + carbs + "\n"+ "Protiens: "+protiens+"\n" + "Fat: "+fat+"\n"
    bot.send_message(message.chat.id, INFo)
    # TODO: 3.2 Dump data in a CSV file
    data = []
    for i in [itemname, quantity,calories,fat,carbs,protiens]:
        data.append(i)
    with open('Nutrition_Report.csv', 'a') as n:
        writer = csv.writer(n)
        writer.writerow(data)


   


@bot.message_handler(func=lambda message: botRunning, commands=['exercise', 'Ex', 'ex'])
def getCaloriesBurn(message):
    bot.reply_to(message, 'Estimating calories burned...')
    # TODO: 2.3 Get exercise data from the API
    url = "https://trackapi.nutritionix.com/v2/natural/exercise"
    einput = message.text[10:]
    e = requests.request("POST", url, headers=headers, json={"query":einput })
    # TODO: 2.4 Display exercise data in the telegram chat
    for i in e.json():
        for j in (e.json()[i]):
            Exerinfo = j
    
    exer_name = str(Exerinfo['name'])
    exer_time = str(Exerinfo["duration_min"]) + " minutes"
    calories_burned = str(Exerinfo["nf_calories"])

    messE = f"Exercise: {exer_name} \nWorkout Time: {exer_time} \nCalories Burned : {calories_burned}"
    bot.send_message(message.chat.id, messE)
    # TODO: 3.3 Dump data in a CSV file
    data = []
    for i in [exer_name,exer_time,calories_burned]:
        data.append(i)
    with open('Exercise_Report.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    




@bot.message_handler(func=lambda message: botRunning, commands=['reports'])
def getCaloriesBurn(message):
    bot.reply_to(message, 'Generating report...')
    # TODO: 3.4 Send downlodable CSV file to telegram chat
    repor = (message.text[9:]).split(', ')
    if 'nutrition' in repor:
        nutriCsv = open('Nutrition_Report.csv', 'rb')
        bot.send_document(message.chat.id, nutriCsv)
    if 'exercise' in repor:
        exerCsv = open("Exercise_Report.csv",'rb' )
        bot.send_document(message.chat.id, exerCsv)


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

bot.infinity_polling()
