# -*- coding: utf-8 -*-


import phonenumbers
from phonenumbers import geocoder , carrier
from opencage.geocoder import OpenCageGeocode
import folium
from colorama import Fore
import string 
import random 
import time






class x :
    number = ''
    for_save = ''

y=x


def logo():
    


    print ('\n\n')
    print(Fore.RED +'______  _______   ______  ')
    print(Fore.RED +'/      \|       \ /      \ ')
    print(Fore.RED +'|  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓')
    print(Fore.RED +'| ▓▓__/ ▓▓ ▓▓__| ▓▓ ▓▓__/ ▓▓')
    print(Fore.RED +' >▓▓    ▓▓ ▓▓    ▓▓\▓▓    ▓▓')
    print(Fore.RED +'|  ▓▓▓▓▓▓| ▓▓▓▓▓▓▓\_\▓▓▓▓▓▓▓')
    print(Fore.RED +'| ▓▓__/ ▓▓ ▓▓  | ▓▓  \__/ ▓▓')
    print(Fore.RED +' \▓▓    ▓▓ ▓▓  | ▓▓\▓▓    ▓▓')
    print(Fore.RED +' \▓▓▓▓▓▓ \▓▓   \▓▓ \▓▓▓▓▓▓ ')
    print ('\n\n\n')
    time.sleep(2)      
                                
                            





    




def loc ():
    inpu = input (Fore.GREEN + 'Enter the number here with + and country code : >> ')
    print ("\n")
    time.sleep(3)
    y.number=(inpu)





    c = (phonenumbers.parse(y.number))
    global locatin
    locatin = geocoder.description_for_number(c,'en')





    global sallocation
    sallocation = phonenumbers.parse(y.number)




    geoc = OpenCageGeocode ('483296bb8365410ca07bb287aa901839')
    qus=str(locatin)
    res = geoc.geocode(qus)




    la = res[0]['geometry']['lat']
    ln = res[0]['geometry']['lng']
    
    
    

    global my_loc
    my_loc = folium.Map(location=[la,ln],zoom_start=8)
    
    folium.Marker([la,ln],popup=locatin).add_to(my_loc)
    


    
def s_and_p():
    print (Fore.RED + 'The country of Target : >>> '+locatin+''+'\n\n')
    forp = carrier.name_for_number(sallocation,'en')
    print (Fore.RED + 'Service Provider : >>>  '+forp + '\n\n')
    
    
    print ('')


    y.for_save = '329476265454254276542234567890987654321354254254527425424'
    ran = random.sample(y.for_save,3)
    map = ''.join(ran)

    my_loc.save(f'map_{map}'+'.html')
    print (Fore.RED + 'The location page has ben saved under name : > map_'+map+'.html' + '\n\n')





logo()
loc()
s_and_p()