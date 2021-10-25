# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
DATA_FILE = "socialmedia/titres_clean/TITRES AMAZON RAW.xlsx"
PROXIS_FILE="socialmedia/titres_clean/list_proxis.txt"
GOOGLE_PREFIX = "https://www.google.com/search?q="
DRIVER_DIR = "C:/WebDriver/chromedriver"
BOOK_DIR = "babelio.com/livres"
SEARCH_ENGINE_DATA = {
    "google":{
        "prefix": "https://www.google.com/search?q=",
        "search_pattern": '.yuRUbf > a'
    },
    "yahoo":{
        "prefix": "https://fr.search.yahoo.com/search?p=",
        "search_pattern": '.richAlgo  h3 > a::attr(href)'
    },

}
CONNEXION_DATA = {
    "user1":{
          "usr":"aliali190270",
          "pass":"hello32!"
       },
    
    "user2":{
          "usr":"alicha1713",
          "pass":"hello32!"
       },
       
    "user3":{
          "usr":"achamas452",
          "pass":"Azeqsdwxc-12"
       },
    "user4":{
          "usr":"alichch1",
          "pass":"hello32!"
       },
   
    "user5":{
          "usr" : "chamal33@outlook.com",
          "pass" : "Azeqsdwxc-12345"

      },
    "user6":{
          "usr":"chamsss768@gmail.com",
          "pass":"Azeqsdwxc-123"
       },
    "user7":{
          "usr":"shimla12021@outlook.com",
          "pass":"Azeqsdwxc-12345"  
       },
    "user8":{
          "usr":"snapi37",
          "pass":"hello32!"  
       },

    }
    #chamaas30@outlook.com
    #Ezadsqcxw-321
    #aliali190270
    #hello32!"