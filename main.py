#project data

# Flights
flights = [

    {
        "id": 1,"date": "20-08-2026","from": "Cairo","to": "Dubai",
        "economy_price": 500, "business_price": 800,
        "firstclass_price": 1200
    },

    {
        "id": 2,"date": "22-08-2026","from": "Cairo","to": "Riyadh",
        "economy_price": 400,"business_price": 700,"firstclass_price": 1000
    }
]
# Seats
seats = {
    1: {
     "A1": {
            "class": "economy",
            "status": "available"
        },

        "A2": {
            "class": "economy",
            "status": "available"
        },

        "B1": {
            "class": "business",
            "status": "available"
        },

        "B2": {
            "class": "business",
            "status": "booked"
        },

        "C1": {
            "class": "firstclass",
            "status": "available"
        }
    },


    2: {

        "A1": {
            "class": "economy",
            "status": "available"
        },

        "A2": {
            "class": "economy",
            "status": "booked"
        },

        "B1": {
            "class": "business",
            "status": "available"
        },

        "B2": {
            "class": "business",
            "status": "available"
        },

        "C1": {
            "class": "firstclass",
            "status": "available"
        }
    }
}
Admins=[ {"username":"Ahmed","pass":1234},
    {"username":"Ali","pass":1111}
    ]


users=[{"username":"Salma","pass":12345},
    {"username":"Amin","pass":15987},
    {"username":"AbdelAziz","pass":00000}
    ]

 #=========================================================================================================================================================================
from tabulate import tabulate


#
from tabulate import tabulate
#==============================
# Bookings
# ==============================

Bookings = []
next_booking_id = 1


# ==============================
# Book Ticket Function
# ==============================

def book_tickets(flights, username):

    global next_booking_id

    while True:

        print("\n==============================")
        print("Available Flights")
        print("==============================")

        if len(flights) == 0:
            print("No flights available.")
            return

        for flight in flights:
            print(
                "Flight ID:", flight.get_flight_id(),
                "| Date:", flight.get_departure_date(),
                "| From:", flight.get_departure_city(),
                "| To:", flight.get_arrival_city()
            )

        # ==============================
        # Choose Flight
        # ==============================

        flight_id = input("\nChoose Flight ID: ").strip()

        selected_flight = None

        for flight in flights:

            if flight.get_flight_id() == flight_id:
                selected_flight = flight
                break

        if selected_flight is None:
            print("Invalid flight ID.")
            continue

        # ==============================
        # Find Related Plane
        # ==============================

        selected_plane = selected_flight.get_related_plane()

        if selected_plane is None:
            print("The plane related to this flight was not found.")
            continue

        # ==============================
        # Choose Class
        # ==============================

        while True:

            print("\nChoose class:")
            print("1. Economy")
            print("2. Business")
            print("3. First Class")

            class_choice = input("Enter your choice: ").strip()

            if not class_choice.isdigit():
                print("Please enter a number.")
                continue

            class_choice = int(class_choice)

            if class_choice == 1:

                travelclass = "economy"
                price = selected_flight.get_economy_price()

                break

            elif class_choice == 2:

                travelclass = "business"
                price = selected_flight.get_business_price()

                break

            elif class_choice == 3:

                travelclass = "first class"
                price = selected_flight.get_firstclass_price()

                break

            else:

                print("Invalid choice.")

        # ==============================
        # Choose Seat
        # ==============================

        while True:

            # ==============================
            # Choose Row
            # ==============================

            row = input("\nEnter row number: ").strip()

            if not row.isdigit():
                print("Please enter a valid row number.")
                continue

            row = int(row)

            # ==============================
            # Check Row
            # ==============================

            if row not in selected_plane.seat:

                print("This row does not exist.")
                continue

            # ==============================
            # Choose Seat Letter
            # ==============================

            letter = input("Enter seat letter: ").strip().upper()

            # ==============================
            # Check Seat Letter
            # ==============================

            if letter not in selected_plane.seat[row]:

                print("This seat letter does not exist.")
                continue

            # ==============================
            # Get Seat Class
            # ==============================

            row_class = selected_plane.seat[row][letter]["class"]

            if row_class != travelclass:

                print(
                    "This seat is not in your selected class."
                )

                continue

            # ==============================
            # Check Availability
            # ==============================

            if selected_plane.seat[row][letter]["status"] == "available":

                selected_plane.seat[row][letter]["status"] = "booked"

                print(
                    "\nRow", row,
                    "Seat", letter,
                    "booked successfully!"
                )

                break

            else:

                print("This seat is not available.")

        # ==============================
        # Create Booking
        # ==============================

        booking = {

            "booking_id": next_booking_id,

            # Username of the person who made the booking
            "username": username,

            "flight_id": selected_flight.get_flight_id(),

            # Store Plane Object
            "plane": selected_plane,

            # Store Plane Code
            "plane_code": selected_plane.get_code(),

            "class": travelclass,

            "row": row,

            "seat": letter,

            "price": price
        }

        Bookings.append(booking)

        next_booking_id += 1

        # ==============================
        # Display Booking
        # ==============================

        print("\n==============================")
        print("Booking Successful!")
        print("==============================")

        print("Username:", booking["username"])

        print("Booking ID:", booking["booking_id"])

        print(
            "Flight:",
            selected_flight.get_departure_city(),
            "to",
            selected_flight.get_arrival_city()
        )

        print("Flight ID:", booking["flight_id"])

        print("Plane Code:", booking["plane_code"])

        print("Class:", booking["class"])

        print("Row:", booking["row"])

        print("Seat:", booking["seat"])

        print("Price:", booking["price"])

        # ==============================
        # Another Ticket
        # ==============================

        while True:

            another = input(
                "\nDo you want to book another ticket?"
                "\n1. Yes"
                "\n2. No"
                "\nEnter your choice: "
            ).strip()

            if another == "1":

                break

            elif another == "2":

                return

            else:

                print("Invalid choice. Please enter 1 or 2.")


# ==============================
# Cancel Booking Function
# ==============================

def cancel_booking(username):

    # ==============================
    # Get Current User Bookings
    # ==============================

    my_bookings = []

    for booking in Bookings:

        if booking["username"] == username:
            my_bookings.append(booking)

    # ==============================
    # Check if User Has Bookings
    # ==============================

    if len(my_bookings) == 0:

        print("\nYou have no bookings.")
        return

    # ==============================
    # Display User Bookings
    # ==============================

    print("\n==============================")
    print("Your Bookings")
    print("==============================")

    for booking in my_bookings:

        print("\nBooking ID:", booking["booking_id"])

        print("Flight ID:", booking["flight_id"])

        print("Plane Code:", booking["plane_code"])

        print("Class:", booking["class"])

        print("Row:", booking["row"])

        print("Seat:", booking["seat"])

        print("Price:", booking["price"])

    # ==============================
    # Choose Booking
    # ==============================

    booking_id = input(
        "\nEnter Booking ID to cancel: "
    ).strip()

    if not booking_id.isdigit():

        print("Invalid Booking ID.")
        return

    booking_id = int(booking_id)

    # ==============================
    # Find Booking
    # ==============================

    for booking in Bookings:

        # IMPORTANT:
        # Booking must belong to current user

        if (
            booking["booking_id"] == booking_id
            and booking["username"] == username
        ):

            row = booking["row"]

            letter = booking["seat"]

            # ==============================
            # Get Plane Object
            # ==============================

            selected_plane = booking["plane"]

            # ==============================
            # Make Seat Available
            # ==============================

            if row in selected_plane.seat:

                if letter in selected_plane.seat[row]:

                    selected_plane.seat[row][letter]["status"] = "available"

            # ==============================
            # Delete Booking
            # ==============================

            Bookings.remove(booking)

            print("\nBooking cancelled successfully!")

            print("Booking ID:", booking_id)

            print(
                "Row", row,
                "Seat", letter,
                "is now available again."
            )

            return

    # ==============================
    # Booking Not Found
    # ==============================

    print("\nBooking ID not found or this booking does not belong to you.")


# ==============================
# Display My Bookings
# ==============================

def display_bookings(username):

    print("\n==============================")
    print("My Bookings")
    print("==============================")

    # ==============================
    # Get Current User Bookings
    # ==============================

    my_bookings = []

    for booking in Bookings:

        if booking["username"] == username:

            my_bookings.append(booking)

    # ==============================
    # No Bookings
    # ==============================

    if len(my_bookings) == 0:

        print("You have no bookings.")
        return

    # ==============================
    # Create Table
    # ==============================

    table = []

    for booking in my_bookings:

        table.append([
            booking["booking_id"],
            booking["flight_id"],
            booking["plane_code"],
            booking["class"],
            booking["row"],
            booking["seat"],
            booking["price"]
        ])

    print(
        tabulate(
            table,
            headers=[
                "Booking ID",
                "Flight ID",
                "Plane Code",
                "Class",
                "Row",
                "Seat",
                "Price"
            ],
            tablefmt="grid"
        )
    )


# ==============================
# Booking Menu
# ==============================

def booking_menu(flights, username):

    while True:

        print("\n==============================")
        print("Flight Booking System")
        print("==============================")

        print("Logged in as:", username)

        print("\n1. Book Ticket")
        print("2. Cancel Booking")
        print("3. Display My Bookings")
        print("4. Exit")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            book_tickets(flights, username)

        elif choice == "2":

            cancel_booking(username)

        elif choice == "3":

            display_bookings(username)

        elif choice == "4":

            print("Goodbye!")
            break

        else:

            print("Invalid choice.")
###################################################################


class Planes:
  def __init__(self,model,code,num_of_rows,seat_leaters_per_row,max_weight):
    self.model=model
    self.__code=code
    self.__num_of_rows=num_of_rows
    self.__seat_leaters_per_row=seat_leaters_per_row
    self.__max_weight=max_weight
    self.seat=self.create_seat()
 #create seat
  def create_seat(self):
    seat={}
    for row in range(1,self.__num_of_rows+1):
     seat[row]={}
     for letter in self.__seat_leaters_per_row:
      if row<=5:
        seat[row][letter]={"status":"available","class":"first class"}
      elif 5<row<=8:
        seat[row][letter]={"status":"available","class":"business"}
      else:
        seat[row][letter]={"status":"available","class":"economy"}
    return seat
 #getter function
  def get_code(self):
    return self.__code
  def get_num_of_rows(self):
    return self.__num_of_rows
  def  get_seat_leaters_per_row(self):
    return self.__seat_leaters_per_row
  def get_max_weight(self):
    return self.__max_weight
  #setter functions
  def set_model(self,model):
    self.model=model
  def set_code(self,code):
    self.__code=code
  def set_num_of_rows(self,rows):
    self.__num_of_rows=rows
  def  set_seat_leaters_per_row(self,leaters):
    self.__seat_leaters_per_row=leaters
  def set_max_weight(self,weight):
    self.__max_weight=weight
  #display method
  """def display_info(self,planes):
   # my_code=int(input("enter the code of the plane you want to display its iformation: "))
    for plane in planes:
      if plane.get_code()==my_code:
       return(plane.model,
       plane.get_code(),
       plane.get_num_of_rows(),
       plane.get_seat_leaters_per_row(),
       plane.get_max_weight())"""
  def get_info(self):
   return(self.model,
       self.get_code(),
       self.get_num_of_rows(),
       self.get_seat_leaters_per_row(),
       self.get_max_weight())
def generate_code(planes):
  while True:
    code=random.randint(100,500)
    if all(plane.get_code() != code for plane in planes):
       return code
import time
import random
import os
planes=[]
plane_1=Planes("Airbus A320",random.randint(100,500),20,["A","B","C","D","E"],10000)
planes.append(plane_1)
#add new plane
def add_plane(planes):
  plane_model=input("enter the new plane's moodel please: ")
  plane_code=generate_code(planes)
  plane_rows=int(input("enter the new plane's number of rows please: "))
  plane_leaters=list(input("enter the new plane's seat_leaters_per_row please(without spaces): "))
  plane_weight=int(input("enter the new plane's max weight please: "))
  new_plane=Planes(plane_model,plane_code,plane_rows,plane_leaters,plane_weight)
  planes.append(new_plane)
  with open("planes.txt","a")as file:
    file.write(f"{plane_model}\n"
               f"{plane_code}\n"
               f"{plane_rows}\n"
               f"{plane_leaters}\n"
               f"{plane_weight}\n")
    print("congrats!")
    print("the new plane added successfuly!")
#update exist plane
def update_info(planes):

  print ("The all of codes with planes informations :")
  for plane in planes:
    print( plane.get_code() ,plane.get_info())
  plane_code=int(input("enter the code of the plane you wanna update its information: "))
  found=False
  for plane in planes:
    if plane_code==plane.get_code():
      print("you entered a valid code!")
      print("please now choose a choice from updating menu -->")
      updating_plane=plane
      before_updating=plane.get_info()
      found=True
      break
  if not found:
      print(f"this code {plane_code} is invalid!")
      return
      #plane_code=int(input("please enter a valid plane code this time"))
  print("___updating menu___")
  while True:
    print("1. the plane's model")
    print("2. the plane's code")
    print("3. the plane's max weight")
    print("4. exit")
    choice=int(input("enter your choice number please: "))
    if choice==1:
      new_model=input("enter the plane's new model: ")
      updating_plane.set_model(new_model)
      print("great! the updates have been saved.")
    elif choice==2:
      new_code=generate_code(planes)
      updating_plane.set_code(new_code)
      print(f"your updated code is : {updating_plane.get_code()}")
    elif choice==3:
      new_weight=int(input("enter the plane's new max weight: "))
      updating_plane.set_max_weight(new_weight)
      print("great! the updates have been saved.")
    elif choice==4:
      answer=input("you have choosed to exit and close this site: (yes or no) ")
      if answer.lower()=="yes":
        print("wish you have found what you want!")
        break
      else:
        choice=int(input("enter your choice number again please: "))
    else:
      print("you entered an invalid choice!")
      choice=int(input("enter your choice number again please: "))
  after_updating=updating_plane.get_info()
  print(f"the plane before updating the data: ")
  print("\n")
  print(before_updating)
  print("_____________")
  print(f"the plane after updating the data: ")
  print("\n")
  print(after_updating)
def search_plane(planes):
  plane_code=int(input("enter the code of the plane you wanna find its information: "))
  found=False
  for plane in planes:
    if plane.get_code()==plane_code:
      print("found this plane info!")
      print(plane.get_info())
      found=True
      break
  if found==False:
      print("no plane found for this code:(")
def delete_plane(planes):
  not_needed_plane_code=int(input("enter the plane code you want to delete its information from the system: "))
  for plane in planes:
    if plane.get_code()==not_needed_plane_code:
      planes.remove(plane)
      break
  else:
    print(f"this code {not_needed_plane_code} is invalid")

# #############################################
def solving_complainant():
 if os.path.exists("complainant.txt"):
  with open("complainant.txt","r")as file:
    complainant=file.readlines()
    if len(complainant)==0:
       print("you haven't received any complaint yet")
    else:
       
        with open("solution.txt","a")as file:
          for complain in complainant:
            complain=complain.strip()
            print(f"complaing from : {complain} ")
            solving=input("enter a logical solving depending on last complainant: ")
            file.write(f"complaing from : {complain} ")
            file.write(f"admin's suggested solution : {solving}")

     
def complainant():
  print("___complaining from___")
  while True:
    print("1.plane lateness (q to quit)")
    print("2.staff attitude (q to quit)")
    print("3.bags lost (q to quit)")
    print("4.stealing (q to quit)")
    print("5.bad landing (q to quit)")
    print("6.else (q to quit)")
    choice=input("enter your coplainant number please: ")
    if choice.lower()=="q":
       print("thanks for using our airline booking system\n")
       print("wait until loading please....")
       time.sleep(3)
       break
    elif choice=="1":
       print("sorry for your disruption we already working on increasing our flieghts and vary planes so you won't be disrupted again")
    elif choice=="2":
       print("we are sorry for you to make you face such a bad experience we will increase staff trainig time so they will be ready to serve you well")
    elif choice=="3":
       print("please go straight to losted section to find it")
    elif choice=="4":
       print("please go straight to security section to reshow the camera video and your complainant will be handeled there")
    elif choice=="5":
      print("sorry for you to face such a scary or bad experience but it may be a weather problem so we ask you understanding")
    elif choice=="6":
     complain=input("enter your coplainant here and the admin will respond you: ")
     with open("complainant.txt","a")as file:
       file.write(complain )
       file.write("\n")
     print("your complaint had sent to the admin successfuly so you will get the respond soon")
     return
def show_solution():
  if os.path.exists("solution.txt"):
   with open("solution.txt","r")as file:
    print(file.read())
    print("wish you have found what you whant!")
  else:
    print("you haven't received a solution yet.")
#========================================================================
import uuid
def unique_id():
    return "FL-" + str(uuid.uuid4())[:8].upper()

# Flight Class

class Flight:

    def __init__(
        self,
        departure_city,
        arrival_city,
        departure_date,
        arrival_date,
        departure_time,
        arrival_time,
        related_plane,
        economy_price,
        business_price,
        firstclass_price
    ):

        self.__flight_id = unique_id()

        self.__departure_city = departure_city
        self.__arrival_city = arrival_city

        self.__departure_date = departure_date
        self.__arrival_date = arrival_date

        self.__departure_time = departure_time
        self.__arrival_time = arrival_time

        # Plane Object
        self.__related_plane = related_plane

        # Prices
        self.__economy_price = economy_price
        self.__business_price = business_price
        self.__firstclass_price = firstclass_price

    # =====================================================
    # Getters

    def get_flight_id(self):
        return self.__flight_id

    def get_departure_city(self):
        return self.__departure_city

    def get_arrival_city(self):
        return self.__arrival_city

    def get_departure_date(self):
        return self.__departure_date

    def get_arrival_date(self):
        return self.__arrival_date

    def get_departure_time(self):
        return self.__departure_time

    def get_arrival_time(self):
        return self.__arrival_time

    def get_related_plane(self):
        return self.__related_plane

    def get_economy_price(self):
        return self.__economy_price

    def get_business_price(self):
        return self.__business_price

    def get_firstclass_price(self):
        return self.__firstclass_price

    # =====================================================
    # Setters
    # =====================================================

    def set_departure_city(self, new_city):
        self.__departure_city = new_city

    def set_arrival_city(self, new_city):
        self.__arrival_city = new_city

    def set_departure_date(self, new_date):
        self.__departure_date = new_date

    def set_arrival_date(self, new_date):
        self.__arrival_date = new_date

    def set_departure_time(self, new_time):
        self.__departure_time = new_time

    def set_arrival_time(self, new_time):
        self.__arrival_time = new_time

    def set_related_plane(self, new_plane):
        self.__related_plane = new_plane

    def set_economy_price(self, new_price):
        self.__economy_price = new_price

    def set_business_price(self, new_price):
        self.__business_price = new_price

    def set_firstclass_price(self, new_price):
        self.__firstclass_price = new_price

    # =====================================================
    # Display Flight Information

    def display_flight_info(self):

        print("\n================================")
        print("        FLIGHT DETAILS")
        print("================================")

        print("Flight ID       :", self.get_flight_id())
        print("From            :", self.get_departure_city())
        print("To              :", self.get_arrival_city())
        print("Departure Date  :", self.get_departure_date())
        print("Arrival Date    :", self.get_arrival_date())
        print("Departure Time  :", self.get_departure_time())
        print("Arrival Time    :", self.get_arrival_time())

        if self.get_related_plane() is not None:
            print(
                "Plane Code      :",
                self.get_related_plane().get_code()
            )
        print("Economy Price   :", self.get_economy_price())
        print("Business Price  :", self.get_business_price())
        print("First Class     :", self.get_firstclass_price())

        print("================================")


# =========================================================
# Flight Data
# =========================================================

flights = []

# =========================================================
# Add Flight

def add_flight(flights, planes):

    print("\n================================")
    print("          ADD NEW FLIGHT")
    print("================================")

    departure_city = input("Departure City: ").strip()
    arrival_city = input("Arrival City: ").strip()

    departure_date = input("Departure Date: ").strip()
    arrival_date = input("Arrival Date: ").strip()

    departure_time = input("Departure Time: ").strip()
    arrival_time = input("Arrival Time: ").strip()

    # -----------------------------------------
    # Prices
    # -----------------------------------------

    try:
        economy_price = float(input("Economy Price: "))
        business_price = float(input("Business Price: "))
        firstclass_price = float(input("First Class Price: "))
    except ValueError:
        print("Invalid price!")
        return
    # -----------------------------------------
    # Display Available Planes
  
    if len(planes) == 0:
        print("No planes available!")
        return

    print("\nAvailable Planes:")

    for plane in planes:
        print(
            "Code:",
            plane.get_code(),
            "| Model:",
            plane.model
        )
    # -----------------------------------------
    # Choose Plane
    try:
        plane_code = int(input("Enter Plane Code: "))
    except ValueError:
        print("Invalid plane code!")
        return

    selected_plane = None

    for plane in planes:

        if plane.get_code() == plane_code:
            selected_plane = plane
            break

    if selected_plane is None:
        print("Plane code not found!")
        return
    # -----------------------------------------
    # Create Flight

    new_flight = Flight(
        departure_city,
        arrival_city,
        departure_date,
        arrival_date,
        departure_time,
        arrival_time,
        selected_plane,
        economy_price,
        business_price,
        firstclass_price
    )

    # Add object to flights list
    flights.append(new_flight)

    print("\nFlight added successfully!")

    print("Flight ID:", new_flight.get_flight_id())

# =========================================================
# Update Flight

def update_flight(flights):

    print("\n================================")
    print("          UPDATE FLIGHT")
    print("================================")

    if len(flights) == 0:
        print("No flights available!")
        return

    search_id = input("Enter Flight ID: ").strip()

    selected_flight = None

    # -----------------------------------------
    # Find Flight
  
    for flight in flights:

        if flight.get_flight_id() == search_id:
            selected_flight = flight
            break

    if selected_flight is None:
        print("Flight ID not found!")
        return

    print("\nFlight Found!")

    while True:

        print("\n----------- Update List -----------")

        print("1. Departure City")
        print("2. Arrival City")
        print("3. Departure Date")
        print("4. Arrival Date")
        print("5. Departure Time")
        print("6. Arrival Time")
        print("7. Economy Price")
        print("8. Business Price")
        print("9. First Class Price")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()
        
        if choice == "1":

            new_city = input(
                "Enter New Departure City: "
            ).strip()

            if new_city:
                selected_flight.set_departure_city(new_city)
                print("Departure city updated!")

        elif choice == "2":

            new_city = input(
                "Enter New Arrival City: "
            ).strip()

            if new_city:
                selected_flight.set_arrival_city(new_city)
                print("Arrival city updated!")

        elif choice == "3":

            new_date = input(
                "Enter New Departure Date: "
            ).strip()

            if new_date:
                selected_flight.set_departure_date(new_date)
                print("Departure date updated!")

        elif choice == "4":

            new_date = input(
                "Enter New Arrival Date: "
            ).strip()

            if new_date:
                selected_flight.set_arrival_date(new_date)
                print("Arrival date updated!")

        elif choice == "5":

            new_time = input(
                "Enter New Departure Time: "
            ).strip()

            if new_time:
                selected_flight.set_departure_time(new_time)
                print("Departure time updated!")

        elif choice == "6":

            new_time = input(
                "Enter New Arrival Time: "
            ).strip()

            if new_time:
                selected_flight.set_arrival_time(new_time)
                print("Arrival time updated!")

        elif choice == "7":

            try:
                new_price = float(
                    input("Enter New Economy Price: ")
                )

                selected_flight.set_economy_price(new_price)

                print("Economy price updated!")

            except ValueError:
                print("Invalid price!")

        elif choice == "8":

            try:
                new_price = float(
                    input("Enter New Business Price: ")
                )

                selected_flight.set_business_price(new_price)

                print("Business price updated!")

            except ValueError:
                print("Invalid price!")

        elif choice == "9":

            try:
                new_price = float(
                    input("Enter New First Class Price: ")
                )

                selected_flight.set_firstclass_price(new_price)

                print("First class price updated!")

            except ValueError:
                print("Invalid price!")

        elif choice == "10":

            print("\nFlight information updated successfully!")
            break

        else:

            print("Invalid choice!")
# =========================================================
# Search For Flight

def search_for_flight(flights):

    print("\n================================")
    print("          SEARCH FLIGHT")
    print("================================")

    if len(flights) == 0:
        print("No flights available!")
        return

    search_city = input(
        "Enter Departure or Arrival City: "
    ).strip().lower()

    found = False

    for flight in flights:

        departure = flight.get_departure_city().strip().lower()
        arrival = flight.get_arrival_city().strip().lower()

        if departure == search_city or arrival == search_city:

            print("\n-----------------------------")

            print(
                "Flight ID:",
                flight.get_flight_id()
            )

            print(
                "From:",
                flight.get_departure_city()
            )

            print(
                "To:",
                flight.get_arrival_city()
            )

            print(
                "Date:",
                flight.get_departure_date()
            )

            print(
                "Time:",
                flight.get_departure_time()
            )

            print(
                "Economy:",
                flight.get_economy_price()
            )

            print(
                "Business:",
                flight.get_business_price()
            )

            print(
                "First Class:",
                flight.get_firstclass_price()
            )

            found = True

    if not found:
        print("\nNo flights found for this city!")
        
# =========================================================
# View Flight Details

def view_flight_details(flights):

    print("\n================================")
    print("       VIEW FLIGHT DETAILS")
    print("================================")

    if len(flights) == 0:
        print("No flights available!")
        return

    search_id = input(
        "Enter Flight ID: "
    ).strip()

    for flight in flights:

        if flight.get_flight_id() ==search_id:

            flight.display_flight_info()
            return
            print("\nNo flight found with this ID!")

# =========================================================
# Search By Flight ID / Plane

def search_about_trip_or_plane(flights):

    print("\n================================")
    print("      SEARCH TRIP / PLANE")
    print("================================")

    if len(flights) == 0:
        print("No flights available!")
        return

    search_id = input(            
        "Enter Flight ID: "
    ).strip()

    for flight in flights:

        if flight.get_flight_id() == search_id:

            print("\nFlight Found!")

            flight.display_flight_info()

            return

    print("\nNo trip or flight found!")
################################################################################

def check_Admin(Admins, pass_1):
    for i in range(len(Admins)):
        if Admins[i]["pass"] == pass_1:
            return True
    return False

def login_admin(Admins, pass_1):
    for i in range(len(Admins)):
        if Admins[i]["pass"] == pass_1:
            return i
    return None


def check_user(users, pass_user):
    for i in range(len(users)):
        if users[i]["pass"] == pass_user:
            return True
    return False

def login_user(users, pass_user):
    for i in range(len(users)):
        if users[i]["pass"] == pass_user:
            return i
    return None

def signup_user(users, name, pass_9, pass_10):
    while True:
        if pass_9 == pass_10:
            users.append({"username": name, "pass": pass_9})
            print("User created successfully.")
            print("=============================================================================================================")
            break
        else:
            print("Passwords do not match, try again.")
            pass_9 = int(input("Enter your password : "))
            pass_10 = int(input("Enter your password again: "))
            

print ("\n\n================================================================================================================================")
print ("                                                  AIRLINES TICKETS SYSTEM                                                        ")
print( "================================================================================================================================\n\n")
while True:
    print ("press 1. for Admin . ")
    print ("----------------------")
    print ("press 2. for user . ")
    print ("----------------------")

    print ("press 3. to exit . ")
    print ("----------------------")

    choice = int (input("Enter you choice : "))
    if choice==1:
        print("=============================================================================================================")
        pass_1 = int(input("Enter your password : "))
        flag_1 = check_Admin(Admins, pass_1)
        id = login_admin(Admins, pass_1)
        if flag_1 and id is not None:
            print("--------------------------------")
            print ( "HELLO " , Admins[id]["username"])
            while True:
                print ("\nchoose operation: ")
                print ("press 1. to Add new planes .")
                print( "press 2. to update plane information.")
                print ("press 3. to Add new flights.")
                print ("press 4  to update flight information.")
                print ("press 5. to search about a trip or plan . ")
                print ("press 6. to respond about complainant ")
                print ("press 7. to exit . ")
                choice_2=int (input ("Enter your choice :"))
                if choice_2==1:
                    add_plane(planes)
                    time.sleep(2)
                elif choice_2==2:
                    update_info(planes)
                    time.sleep(2)
                elif choice_2==3:
                    add_flight(flights,planes)
                    time.sleep(2)
                elif choice_2==4:
                    update_flight(flights)
                    time.sleep(2)
                elif choice_2==5:
                    search_about_trip_or_plane(flights)
                    time.sleep(2)
                elif choice_2==6:
                    solving_complainant()
                    time.sleep(2)
                elif choice_2==7:
                    print ("\nsee you soon ", Admins[id]["username"])
                    print("\n\n")
                    break

                else:
                    print ("invalid number")
        else:
            print("take careful your password is wrong !")                                       
    elif choice==2:
        print("=============================================================================================================")
        print ( "press 1. to sign up. ")
        print("\npress 2. to log in.")
       
        choose=int(input("\nEnter your choice : "))
        if choose ==1:
            name = input("Enter your name : ")
            pass_9 = int(input("Enter your password : "))
            pass_10 = int(input("Enter your password again: "))
                
            signup_user(users ,name,pass_9,pass_10)
        elif choose ==2:
            pass_user = int(input("Enter your password : "))
            flag_user = check_user(users, pass_user)
            id = login_user(users, pass_user)
            if flag_user and id is not None:
                print("=============================================================================================================")
                print ("welcome back ",users[id]["username"])
            
              
                while True:
                    print("=============================================================================================================")
                    print ("\nchoose operation: ")
                    print("press 1. to search for flight . ")
                    print("press 2. to view flight details .")
                    print("press 3. to book available seats.")
                    print("press 4. to cancel booking .")
                    print("press 5. to show your booked flights.")
                    print("press 6. to complainant .")
                    print("press 7. to show the solution.")
                    print("press 8. to exit")
                    choice_user=int (input ("enter your choice : "))
                    if choice_user==1:
                       search_for_flight(flights)
                       time.sleep(2)
                    elif choice_user==2:
                       view_flight_details(flights)
                       time.sleep(2)
                    elif choice_user==3:
                        book_tickets(flights,users[id]["username"])
                        time.sleep(2)
                    elif choice_user ==4:
                       cancel_booking(users[id]["username"])
                       time.sleep(2)
                    elif choice_user ==5:
                       display_bookings(users[id]["username"])
                       time.sleep(2)
                   
                    elif choice_user==6:
                       complainant()
                       time.sleep(2)
                    elif choice_user==7:
                       show_solution()
                       time.sleep(2)
                    elif choice_user==8:
                        print ("\nSee you soon ",users[id]["username"],"\n")
                        break
                    else:
                        print ("invalid number .")  
            else :
                print("take careful your password is wrong !")
        else:
           print ("invalid number.")
          

    elif choice ==3:
        print ("----------------------------------------------------------")
        print ("thanks for using our airlines APP . ")
        
        break
    else :
        print ("invalid number .")
