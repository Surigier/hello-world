""" numbers=[]
for ranges in range(1,1000000):
    number=ranges
    if(number%3==0):
        numbers.append(number)
print (numbers[-10:]) """
""" 在列表中校验元素是否在列表，可用 if x in y： """
favorite_language={

        'aeibstein':{
                'first': 'albert',
                'last':'einstein',
                'location':'princetion'
              
                 },
        'mucurie':{
                'first': 'maries',
                'last':'curie',
                'location':'parise',
                'character':['long_hair','big_eyes']
        }
         

 }
characters1=[] 
for name,language in favorite_language.items():
        print(name.title())
        for key,vlaue in language.items():
                print(key.title())
                print(vlaue) 
        if(name == 'mucurie'):
                characters=language['character']
                for characterss in characters:
                        characters1.append(characterss)
                print(characters)

unprint_model=['iphone','duck','lianxisheng']
completed_models=[]
def print_model(unprint_model , completed_models):
        while unprint_model:
                current_print=unprint_model.pop()
                completed_models.append(current_print)
                print (current_print+ " is  printing")
print_model(unprint_model,completed_models)


class car():
        def __init__(self,make,model,year):
                self.make=make
                self.model=model
                self.year=year
                self.odometer=0
        def get_descriptive_name(self):
                long_name=str(self.year)+' '+self.make+' '+self.model
                return long_name.title()
        def read_odometer(self):
                print("this car has ran "+str(self.odometer))
        def updata_odometer(self,meter):
                if meter>=self.odometer:
                        self.odometer=meter
                else:
                        print("inpur meter wrong")
        def increase_meter(self,meter):
                self.odometer+=meter
                print("odometer has increase :"+str(self.odometer))
        def decrease_meter(self,meter):
                self.odometer-=meter
                print("odometer has decrease :"+str(self.odometer))

import json
numbers=[1,5,7,9,0]
filename='record.txt'
with open(filename,'w') as f_obj:
        f_obj.write("l love python")

with open (filename) as f_obj:
        lines=f_obj.read()
        print (lines)
with open (filename,'a') as f_obj:
        f_obj.write("\r\n")
        f_obj.write("i love python, too")   
with open (filename) as f_obj:
        word=f_obj.read()
        words=word.split()
        print (words)
        



