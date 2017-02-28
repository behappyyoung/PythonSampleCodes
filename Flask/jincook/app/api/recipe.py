__author__ = 'young'
import pycurl
from StringIO import StringIO
import DBapi
import json

def get_recipe(url):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue()

def search_recipe(name):
    searchData = DBapi.getSearchData()
    noresult = searchData[0]
    searchedWord = searchData[1]
    ##return noresult , searchedWord, searchedWord.find(name)
    if( name in map(str.strip, noresult.split(",")) ):
        result ="no recipe"
    else:
        if( name in map(str.strip, searchedWord.split(",")) ):
            recipe = DBapi.getRecipeFromDB(name)
            result = recipe

        else:
            targetUrl =  'http://food2fork.com/api/search?key=f99ea1cf8741d9c23ee1b3a63542fd96&q='+name
            recipe = get_recipe(targetUrl)
            recipe_obj = json.loads(recipe)
            if(recipe_obj['count']>0):
                result =  save_recipe(name, recipe.replace("'", r"\'"), searchedWord)
            else:
                DBapi.updateNoresult(name, noresult)
                result = "no recipe"
    return result

def save_recipe(search_word, recipe, searchedWord):
    result = DBapi.insertRecipeSearch(search_word, recipe)
    if(result.find("Error")>-1):
        return "input error"
    else:
        return DBapi.updateSearchedWord(search_word, searchedWord)