# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "young.park"


if __name__ == "__main__":
    print "firebase"

from cgi import escape  # py3
from firebase import firebase
import json
from flask import Flask, render_template
from firebase_token_generator import create_token
auth_payload = {"uid": "1"}
token = create_token("FJxrAdOEo31MWjEAMjgl0c2Y8pEp49siqYL1THg6", auth_payload)

firebase = firebase.FirebaseApplication('https://projecta.firebaseio.com/', None)
def getUsers():  
    users = firebase.get('/users', None)
    jsonUsers = json.dumps(users, ensure_ascii=False)
    return jsonUsers
    if(not users):
        result = 'no users'
    else:
	result = 'type: ' + escape(str(type(users)))
	result += str(users)
	for user in users:
        	result += escape(str(type(user))) + str(user)
    return result

def getMenu():  
    menu = firebase.get('/menu', None)

    if(not menu):
        result = 'no menu'
    else:
        result = str(menu).decode("unicode-escape")
    return result

def getDish():
    dish = firebase.get('/dish', None)

    if(not dish):
        result = 'no dish'
    else:
        jsonDish = json.dumps(dish, ensure_ascii=False)
        ##return render_template('dish.html', obj=str(dish).decode("unicode-escape"))
        return render_template('dish.html', obj=jsonDish)
        return jsonDish
        result = str(dish).decode("unicode-escape")
	for item in dish:
		result += '<br /> ' +   escape(str(type(item))) + ' --   ' +  item 
 
    return result

def getDishDetail(name):
    dish = firebase.get('/dish/'+name, None)
    if(not dish):
        result = 'no dish'
    else:
        jsonDish = json.dumps(dish, ensure_ascii=False)
        ##return render_template('dish.html', obj=str(dish).decode("unicode-escape"))
        
        return render_template('dishDetail.html', obj=jsonDish)
        return jsonDish
        result = str(dish).decode("unicode-escape")

    return result







