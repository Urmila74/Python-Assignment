"""
Q2 : Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a
dictionary of information about each city and include the country that the city is in, its approximate
population, and one fact about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored
about it.
"""
 

cities = {
    "Karachi": {
        "Information":{
           "City":"Karachi",
           "country":"Pakistan",
           "population": "14.91 million",
           "fact": "Karachi is the sixth largest city in the world by city population.",
             }
        },
    
    "Dubai": {
         "Information":{
             "City":"Dubai",
              "country":"the United Arab Emitates",
              "population": "3.137 million",
              "fact": "Dubai's Artificial palm island use Enough Sand to Fill 2.5 Empire State Buildings",
           }
        },
    
    "Paris": {
        "Information":{
            "City":"Paris",
            "country":"France",
            "population": "2.141 million",
            "fact": "Paris was originally a Roman City called “Lutetia.",
           }
        }
}
print("Currently we have 3 cities database which is below mentioned \n")
karachi = cities["Karachi"]
print(karachi)
print("\n--------------------------------\n")
Dubai = cities["Dubai"]
print(Dubai)
print("\n--------------------------------\n")
Paris = cities["Paris"]
print(Paris)
print("\n--------------------------------\n")