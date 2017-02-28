# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "young.park"


if __name__ == "__main__":
    print "DB APis"

import db

def showResult(obj):
    for row in obj:
        column = ""
        for col in row:
            column +=  str(col) + ","
        print column + "\n"


def getUsers():
    users = db.getQuery("select * from users ;")
    ##showResult(users)
    ##listusers = list(users)
    dictUsers =[]
    for user in users:
        dictUser ={}
        dictUser['iduser'] = user[0]
        dictUser['name'] = user[1]
        dictUser['type'] = user[2]
        dictUsers.append(dictUser)

    print dictUsers, "\n listusers\n", listusers
    return dictUsers


def insertUser(name, type):
    result = db.commitQuery("""insert into users(name, type) values ('"""+ name +"""', '"""+type+"""');""")
    return result

def updateUser(userid, name, type ):
    result = db.commitQuery("""update users set name= '"""+ name +"""', type = '"""+type+"""' where idusers = '"""+userid+"""';""")
    return result



def getDishes():
    dishes = db.getQuery("select * from dish ;")
    print dishes, type(dishes), (dishes == None), len(dishes)
    
    result = ""
    for row in dishes:
        column = ""
        for col in row:
            column +=  str(col) + ","
        result += column + "\n"
    
    print result


##listDishes = list(dishes)
    dictDishes =[]
    for dish in dishes:
        dictDish ={}
        dictDish['iddish'] = dish[0]
        dictDish['name'] = dish[1]
        dictDish['recipe'] = dish[2]
        dictDish['star'] = dish[3]
        dictDish['image'] = dish[4]
        dictDish['imageurl'] = dish[5]
        dictDishes.append(dictDish)
    return dictDishes

def getRecipeFromDB(searchWord):
    dbResult = db.getQuery("""select recipe_detail from open_recipe_search WHERE search_word='"""+searchWord+"""'""")
    if(len(dbResult)):
        return dbResult[0][0]
    else:
        return "no data"

def insertRecipeSearch(searchWord, recipe):
    result = db.commitQuery("""insert into open_recipe_search(search_word, recipe_detail) values ('"""+ searchWord +"""', '"""+recipe+"""');""")
    return result

def getNoresult():
    noresults = db.getQuery("select noresult from search_words;")
    noresultString=""
    for noresult in noresults:
        print noresult
        noresultString += noresultString.join(noresult) + ","
    return noresultString[:-1]

def getSearchData():
    dbResult = db.getQuery("select noresult, searched_word from search_words;")
    return dbResult[0]

def updateNoresult(addword, currentresult):
    newnoresult = currentresult + ", " + addword
    result = db.commitQuery("""UPDATE search_words SET noresult = '"""+newnoresult+"""';""")
    return result

def updateSearchedWord(addword, currentresult):
    newSearched = currentresult + ", " + addword
    result = db.commitQuery("""UPDATE search_words SET searched_word = '"""+newSearched+"""';""")
    return result

