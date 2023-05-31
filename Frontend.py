import Backend
import sys

#Create a class to take input and display output.
class CarRental:
    @staticmethod
    def get_str(element):
        sys.stdout.write(element)
        sys.stdout.flush()
        return sys.stdin.readline().strip()
    
    @staticmethod
    def output(element):
        return sys.stdout.write(element)

#Create a UI for user to run program. This is the main class to run the whole program.
#This class allow user to interact with computer.
class CarRentalManagerUI:
    def __init__(self, __backend) -> None:
        self.__backend=Backend.CarRentalManager

    def show_ui(__backend):
        Backend.CarRentalManager.load_data()
        display=Backend.Display
        CarRental.output(display.logo_car())
        stock=Backend.StockList
        choice=CarRental.get_str(display.car_type())
        petrol_car_list=stock.get_car_list()
        electric_car_list=stock.get_car_list()
        car_update_list=stock.get_car_list()
        #Use if method to set selection for user who can choose to run program or exit the program.    
        if (choice!="X" or choice=="x"):
            #Use while loop to into petrol car option, it can let user keep adding car stock.
            #Use while loop instead if statment because while loop does the things as long as the condition is true.
            while (choice=="P" or choice=="p"):
                CarRental.output(display.petrol_car_logo())
                stock_option=CarRental.get_str(display.car_stock_option())
                #If statement allows user add new car stock or display stock summary or choose to exit the program.
                if (stock_option=="A" or stock_option=="a"):
                    make=CarRental.get_str("Make:")
                    model=CarRental.get_str("Model:")
                    year=CarRental.get_str("Year(YYYY):")
                    stock.check_type(year)
                    colour=CarRental.get_str("Colour:")
                    mileage=int(CarRental.get_str("Mileage(KM):"))
                    stock.check_type(mileage)
                    vehicle=Backend.Vehicle(make, model, year, colour, mileage)
                    petrol_car=Backend.PetrolCar(make, model, year, colour, mileage)
                    petrol_cars=petrol_car.add_petrol_car(make, model, year, colour, mileage)
                    petrol_car_list.append(petrol_cars)
                    CarRental.output(petrol_car.__repr__(make, model, year, colour, mileage)+"\n")
                    update=CarRental.get_str("Do you want to update mileage? 'y' or 'n':")
                    #User can use if statement to choose update data or not.
                    if (update=="Y" or update=="y"):
                        update_mileage=CarRental.get_str("New Mileage(KM):")
                        vehicle.odometer=int(update_mileage) 
                        update_cars=vehicle.car_update_infromation(update_mileage)
                        car_update_list.append(update_cars)
                        CarRental.output(vehicle.__repr__(make, model, year, colour, mileage,update_mileage)+"\n")
                        Backend.CarRentalManager.save_update_data(make, model, year, colour, mileage, update_mileage)
                    #If/else statement to provide multiple choice for user to update or not update data. 
                    #If user choose not to update data, then stock and display the original data.
                    else:                
                        CarRental.output(petrol_car.__repr__(make, model, year, colour, mileage)+"\n")
                        Backend.CarRentalManager.save_data(petrol_car_list)
                #Elif statement for user who choose display data.
                elif (stock_option=="D" or stock_option=="d"):
                    input=CarRental.get_str("Did you update data? 'y' or 'n':")
                    #Use if statement to confirm user's previous action. Then display the correct information.
                    if (input=="Y" or input=="y"):
                        CarRental.output(vehicle.__repr__(make, model, year, colour, mileage,update_mileage)+"\n")
                    #If/else statement to confirm user's previous action. If user didn't update the data, it will display non-update data.   
                    else:
                        CarRental.output(petrol_car.__repr__(make, model, year, colour, mileage)+"\n")
                #If/else statement to provide multiple choice for user to choose start add new stock or exit the program.       
                else:
                    CarRental.output(display.good_bye()) 
                    choice=CarRental.get_str(display.car_type())
            #Use while loop to into electric car option, it can let user keep adding car stock.
            #Use while loop instead if statment because while loop does the things as long as the condition is true. 
            while (choice=="E" or choice=="e"):
                CarRental.output(display.electric_car_logo())
                stock_option=CarRental.get_str(display.car_stock_option())
                #If statement allows user add new car stock or display stock summary or choose to exit the program.
                if (stock_option=="A" or stock_option=="a"):
                    make=CarRental.get_str("Make:")
                    model=CarRental.get_str("Model:")
                    year=int(CarRental.get_str("Year(YYYY):"))
                    stock.check_type(year)
                    colour=CarRental.get_str("Colour:")
                    battery=int(CarRental.get_str("Battery(kWh):"))
                    stock.check_type(battery)
                    mileage=int(CarRental.get_str("Mileage(KM):"))
                    stock.check_type(mileage)
                    vehicle=Backend.Vehicle(make, model, year, colour, mileage)
                    electric_car=Backend.ElectricCar(make, model, year, colour, battery, mileage)
                    electric_cars=electric_car.add_electric_car_list(make, model, year, colour, battery, mileage)
                    electric_car_list.append(electric_cars)
                    CarRental.output(electric_car.__repr__(make, model, year, colour, battery, mileage)+"\n")
                    update=CarRental.get_str("Do you want to update mileage? 'y' or 'n':")
                    #User can use if statement to choose update data or not.
                    if (update=="Y" or update=="y"):
                        update_mileage=CarRental.get_str("New Mileage(KM):")
                        vehicle.odometer=int(update_mileage) 
                        update_cars=vehicle.car_update_infromation(update_mileage)
                        car_update_list.append(update_cars)
                        CarRental.output(vehicle.__str__(make, model, year, colour, battery, mileage,update_mileage)+"\n")
                        Backend.CarRentalManager.save_update_data_ele(make, model, year, colour, battery, mileage, update_mileage)
                    #If/else statement to provide multiple choice for user to update or not update data. 
                    #If user choose not to update data, then stock and display the original data.
                    else:                
                        CarRental.output(electric_car.__repr__(make, model, year, colour, battery, mileage)+"\n")
                        Backend.CarRentalManager.save_data_ele(electric_car_list)
                #Elif statement for user who choose display data.
                elif (stock_option=="D" or stock_option=="d"):
                    input=CarRental.get_str("Did you update data? 'y' or 'n':")
                    #Use if statement to confirm user's previous action. Then display the correct information.
                    if (input=="Y" or input=="y"):
                        CarRental.output(vehicle.__str__(make, model, year, colour, battery, mileage, update_mileage)+"\n") 
                    #If/else statement to confirm user's previous action. If user didn't update the data, it will display non-update data.          
                    else:
                        CarRental.output(electric_car.__repr__(make, model, year, colour, battery, mileage)+"\n") 
                #If/else statement to provide multiple choice for user to choose start add new stock or exit the program.      
                else:
                    CarRental.output(display.good_bye())  
                    choice=CarRental.get_str(display.car_type())
        #Else statement to provide multiple choice for user to exit the program.  
        else:
            CarRental.output(display.good_bye())  


