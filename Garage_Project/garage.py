import os
spots = {1:"Open",2:"Open",3:"Open",
                4:"Open", 5:"Open",6:"Open",
                7:"Open",8:"Open",9:"Open",10:"Open"}
pay_status = {1:False,2:False,3:False,
                4:False, 5:False,6:False,
                7:False,8:False,9:False,10:False}
class garage():
    def __init__(self, spots, count):
        self.spots = spots
        self.count = count

    



    def take_ticket():
        count = 1
        while True:
            if count == 11:
                os.system('cls')
                print("The Garage is Full, Sorry")
                break
            elif spots[count] == "Taken":
                count += 1
            elif spots[count] == "Open":
                spots[count] = "Taken"
                os.system('cls')
                print(f"You took spot {count}")
                break
        

    def pay_for_parking():
        while True:
            answer = input("What spot are you paying for?")
            if int(answer) > 0 and int(answer) < 11:
                if spots[int(answer)] == "Open":
                    os.system('cls')
                    print("No one is parked in that spot, please try again")
                else:
                    os.system('cls')
                    spots[int(answer)] = "Open"
                    pay_status[int(answer)] = True
                    print("Thanks for paying, you have 15 minutes to leave")
                    break
            else:
                os.system('cls')
                print("That spot does not exist, please try again")

    def leave_garage():
        while True:
            answer = input("Who's leaving?")
            if int(answer) > 0 and int(answer) < 11:
                if pay_status[int(answer)] == True:
                    os.system('cls')
                    pay_status[int(answer)] = False
                    print("You have left the Garage, come again soon!")
                    break
                else:
                    os.system('cls')
                    print("whoops, you forgot to pay")
                    garage.pay_for_parking()
            else:
                os.system('cls')
                print("That spot does not exist, please try again")

    def run_garage():
        while True:
            
            print(spots)
            answer = input("What would you like to do? Park, Pay, Leave, Quit: ")
            if answer.lower() == "quit":
                exit()
            elif answer.lower() == "park":
                garage.take_ticket()
            elif answer.lower() == "pay":
                garage.pay_for_parking()
            elif answer.lower() == "leave":
                garage.leave_garage()
            else:
                os.system('cls')
                print("Invalid response, please try again")

garage.run_garage()    













































