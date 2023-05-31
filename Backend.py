#Create a parent class to represent a car.
#Use mutator and setter methods to access the private variable.
#Create a static method that does not receive any reference argument from class itself.
class Vehicle:
    def __init__(self, make, model, year, colour, mileage) -> None:
        self.__make=make
        self.__model=model
        self.__year=year
        self.__colour=colour
        self.__mileage=mileage

    @property
    def odometer(self):
        return self.__mileage

    @odometer.setter
    def odometer(self,new_mileage):
        #Use try method to make sure the inpur is integer.
        try:
            self.__mileage=int(new_mileage) 
        #Raise Error when user input the other type, such as string.     
        except:
            raise TypeError("Only input numbers.")

    @staticmethod
    def car_update_infromation(new_mileage):
        car_update_list=[]
        car_update_list.append(new_mileage)
        return car_update_list

    @staticmethod
    def __repr__(make, model, year, colour,mileage, __mileage) -> str:
        summary ="\n"
        summary+=f"You add {make},model is {model}, built in {year},\n"
        summary+=f"colour is {colour}.\n"
        summary+=f"This car already drove {mileage}KM.\n"
        summary+=f"Now updating to drive {__mileage}KM.\n"
        return summary

    @staticmethod
    def __str__(make, model, year, colour, battery, mileage, __mileage) -> str:
        summary ="\n"
        summary+=f"You add is {make},model is {model}, built in {year},\n"
        summary+=f"colour is {colour}. "+f"batter is {battery} kWh.\n"
        summary+=f"This car already drove {mileage}KM.\n"
        summary+=f"Now updating to drive {__mileage}KM.\n"
        return summary

#Create a child class to represent a petrol car which inherit variable from parent class.
#This class allow user to create a list of stock of petrol cars. Display stock information and display update information.
class PetrolCar(Vehicle):
    def __init__(self, make, model, year, colour, mileage) -> None:
        super().__init__(make, model, year, colour, mileage) 
        self.key ="Petrol car "

    def add_petrol_car(self,make, model, year, colour, mileage):
        self.petrol_car_list=[]
        self.petrol_car_list.append(make)
        self.petrol_car_list.append(model)
        self.petrol_car_list.append(year)
        self.petrol_car_list.append(colour)
        self.petrol_car_list.append(mileage)
        return self.petrol_car_list

    def __repr__(self,make, model, year, colour, mileage) -> str:
        summary ="\n"
        summary+=f"You add {make},model is {model}, built in {year},\n"
        summary+=f"colour is {colour}.\n"
        summary+=f"This car already drive {mileage}KM.\n"
        return summary

    @staticmethod
    def __str__(car_list):
        summary=""
        i=0
        while(i<len(car_list)):
            j=0
            summary+="\nYou add a new car make by "+str(car_list[i][j])+"."+"\n"
            j+=1
            summary+=" "+"Model is  "+str(car_list[i][j])+"."+"\n"
            j+=1
            summary+=" "+"Built in  "+str(car_list[i][j])+"."+"\n"
            j+=1
            summary+=" "+"The colour is  "+str(car_list[i][j])+"."+"\n"
            j+=1
            summary+=" "+"This car already drove  "+str(car_list[i][j])+"KM."+"\n"
            i+=1
        return summary

#Create a child class to represent a electric car which inherit variable from parent class.
#This class allow user to create a list of stock of electric cars. Display stock information and display update information.
class ElectricCar(Vehicle):
    def __init__(self, make, model, year, colour, battery, mileage) -> None:
        super().__init__(make, model, year, colour, mileage)
        self.key ="Electric car "
        self.battery=battery
    
    def add_electric_car_list(self,make, model, year, colour, battery, mileage):
        self.electric_car_list=[]
        self.electric_car_list.append(make)
        self.electric_car_list.append(model)
        self.electric_car_list.append(year)
        self.electric_car_list.append(colour)
        self.electric_car_list.append(battery)
        self.electric_car_list.append(mileage)
        return self.electric_car_list

    def __repr__(self,make, model, year, colour, battery,mileage) -> str:
        summary ="\n"
        summary+=f"You add {make},model is {model}, built in {year},\n"
        summary+=f"battery is {battery} "+"kWh"+f"colour is {colour}.\n"
        summary+=f"This car already drive {mileage}KM.\n"
        return summary
    
    @staticmethod
    def __str__(car_list):
        summary=""
        i=0
        k=0
        while(i<len(car_list)):
            j=0
            summary+="\nYou add a new car make by "+str(car_list[i][j])+"."+"\n"
            j+=1
            summary+=" "+"Model is  "+str(car_list[i][j])+"."+"\n"
            j+=1
            summary+=" "+"Built in  "+str(car_list[i][j])+"."+"\n"
            j+=1
            summary+=" "+"The colour is  "+str(car_list[i][j])+"."+"\n"
            j+=1
            summary+=" "+"The battery is  "+str(car_list[i][j])+"."+"\n"
            j+=1
            summary+=" "+"This car already drove  "+str(car_list[i][j])+"KM."+"\n"
            i+=1
        return summary

#The class stock empty list and try method that can call in frontend without take specific parameters.
class StockList:

    def get_car_list():
        return []
    
    def check_type(input):
        try:
            int(input)            
        except:
            raise TypeError ("Must be a number.")


#The class to open data file and save data to a specific file.
class CarRentalManager():
    #@staticmethod
    def load_data():
        try:
            file_object = open("test.txt","r")
            s_string=file_object.readline()
        except:
            raise ValueError("Unable to open file.")
        s_list=s_string.split()
        if (len(s_list)!=5):
            raise ValueError("Incorrect value.")
        else:
            try:
                make=s_list[0]
                model=s_list[1]
                year=int(s_list[2])
                colour=str(s_list[3])
                mileage=float(s_list[4])
                
            except:
                raise ValueError("Badly formatted data.")
        file_object.close()

    @staticmethod
    def save_data(petrol_car_list):
        data_file=open("data.csv","w")
        summary=PetrolCar.__str__(petrol_car_list)       
        data_file.write(summary)
        data_file.close()
    
    @staticmethod
    def save_data_ele(electric_car_list):
        data_file=open("data.csv","w")
        summary=ElectricCar.__str__(electric_car_list)       
        data_file.write(summary)
        data_file.close()

    @staticmethod
    def save_update_data(make, model, year, colour,mileage, __mileage):
        data_file=open("data.csv","w")
        summary=Vehicle.__repr__(make, model, year, colour,mileage, __mileage)     
        data_file.write(summary)
        data_file.close()

    @staticmethod
    def save_update_data_ele(make, model, year, colour, battery, mileage, __mileage):
        data_file=open("data.csv","w")
        summary=Vehicle.__str__(make, model, year, colour, battery, mileage, __mileage)     
        data_file.write(summary)
        data_file.close()

#String display and ASCII art, it can be called in frontend.
class Display:
    def car_type():
        car_type ="[P]etrol car.\n"
        car_type+="[E]lectric car.\n"
        car_type+="Ei[x]t.\n"
        return car_type

    def car_stock_option():
        car_stock_option ="[A]dd new stock.\n"
        car_stock_option+="[D]isplay the last stock.\n"
        car_stock_option+="Ei[x]t.\n"
        return car_stock_option

    def logo_car():
        logo_car ="   __                 _ _____      _    \n"
        logo_car+="  /__\ ___   __ _  __| /__   \_ __(_)_ __ \n"
        logo_car+=" / \/// _ \ / _` |/ _` | / /\/ '__| | '_ \ \n"
        logo_car+="/ _  \ (_) | (_| | (_| |/ /  | |  | | |_) |\n"
        logo_car+="\/ \_/\___/ \__,_|\__,_|\/   |_|  |_| .__/ \n"
        logo_car+="                                    |_| \n"
        logo_car+="\n"
        logo_car+="   ___ \n"
        logo_car+="  / __\__ _ _ __\n"
        logo_car+=" / /  / _` | '__|\n"
        logo_car+="/ /__| (_| | |\n"
        logo_car+="\____/\__,_|_| \n"
        logo_car+="\n"
        logo_car+="   __            _        _  \n"
        logo_car+="  /__\ ___ _ __ | |_ __ _| |   \n"
        logo_car+=" / \/// _ \ '_ \| __/ _` | | \n"
        logo_car+="/ _  \  __/ | | | || (_| | | \n"
        logo_car+="\/ \_/\___|_| |_|\__\__,_|_|  \n"
        return logo_car

    def petrol_car_logo():
        petrol_car_logo ="   ___     _             _ \n"
        petrol_car_logo+="  / _ \___| |_ _ __ ___ | |\n"
        petrol_car_logo+=" / /_)/ _ \ __| '__/ _ \| |\n"
        petrol_car_logo+="/ ___/  __/ |_| | | (_) | |\n"
        petrol_car_logo+="\/    \___|\__|_|  \___/|_|\n"
        petrol_car_logo+="\n"
        petrol_car_logo+="   ___ \n"
        petrol_car_logo+="  / __\__ _ _ __  \n"
        petrol_car_logo+=" / /  / _` | '__|  \n"
        petrol_car_logo+="/ /__| (_| | |\n"
        petrol_car_logo+="\____/\__,_|_|\n"
        return petrol_car_logo
    
    def electric_car_logo():
        electric_car_logo ="   __ _           _        _   \n"
        electric_car_logo+="  /__\ | ___  ___| |_ _ __(_) ___ \n"
        electric_car_logo+=" /_\ | |/ _ \/ __| __| '__| |/ __|\n"
        electric_car_logo+="//__ | |  __/ (__| |_| |  | | (__ \n"
        electric_car_logo+="\__/ |_|\___|\___|\__|_|  |_|\___|\n"
        electric_car_logo+="\n"
        electric_car_logo+="   ___\n"
        electric_car_logo+="  / __\__ _ _ __ \n"
        electric_car_logo+=" / /  / _` | '__|\n"
        electric_car_logo+="/ /__| (_| | | \n"
        electric_car_logo+="\____/\__,_|_| \n"
        return electric_car_logo

    def good_bye():
        good_bye ="  ________                  .___ \n"
        good_bye+=" /  _____/  ____   ____   __| _/\n"
        good_bye+="/   \  ___ /  _ \ /  _ \ / __ |  \n"
        good_bye+="\    \_\  (  <_> |  <_> ) /_/ |\n"
        good_bye+=" \______  /\____/ \____/\____ | \n"
        good_bye+="        \/                   \/ \n"
        good_bye+="\n"
        good_bye+="__________ \n"
        good_bye+="\______   \___.__. ____ \n"
        good_bye+=" |    |  _<   |  |/ __ \ \n"
        good_bye+=" |    |   \\___  \  ___/\n"
        good_bye+=" |______  // ____|\___  >\n"
        good_bye+="        \/ \/         \/ \n"
        return good_bye

