from datetime import date
print("Welcome to ROYAL_BENGAL,".center(130))
print("ITC, Kolkata,sector-09.".center(133))
print("Email_ID:www.itc_ROYAL_BENGAL_Hotels@gmail.com".center(110))
roomno=0
no=0
bill=0
payment={}
li=[]
room={}
for i in range (10):
    room[i]="Not Booked"
f=0
details=dict()
cname=0
cphno=0
caddress=0
def home():
    print("===============================================")
    print("Enter 1 for check availability of rooms.")
    print("Enter 2 for booking.")
    print("Enter 3 for booking report.")
    print("Enter 4 for bill payment.")
    print("Enter 5 for booking cancelation")
    print("Enter 6 to exit.")
    choice=int(input("Enter your choice :"))
    print("===============================================")
    if(choice == 1):
        available()
    elif(choice == 2):
        booking()
    elif(choice ==3):
        report()
    elif(choice ==4):
        bill()
    elif(choice ==5):
        cancel()
    elif(choice ==6):
        print("Thank you.\nPlease visit again")
    else:
        print("Wrong choice.")
        home()
def booking():
    f=0
    roomno=int(input("enter the room number for booking(1-10)"))
    if(roomno > 10):
        print("Room not available.")
        booking()
    elif(room[roomno-1] == "Booked"):
        f=1
    elif(f == 1):       
        print("This room is already booked.")
        print("Try another room please.")
        booking()
    else:
        name=input("Enter your name :")
        phno=eval(input("Enter your phone number :"))
        if(phno < 1000000000 or phno > 9999999999):
            print("Wrong phone number")
            print("Try again please")
        else:
            details[phno]=name
            address=input("Enter your address :")
            cidate=int(input("Enter check in date :"))
            cim=int(input("Enter check in month :"))
            cidate=date(2020,cim,cidate)
            codate=int(input("Enter check out date :"))
            com=int(input("Enter check out month :"))
            codate=date(2020,com,codate)
            details[roomno]=[name,phno,address,cidate,codate]
            no=codate-cidate
            bill=no.days*2099
            payment[roomno]=[no.days,bill]
            room[roomno-1]="Booked"
            print("Room Number",roomno," -- Booked Successfully")
        home()
def available():
    print("Available Rooms:")
    l=len(room)
    for i in range(l):
        if(room[i]=="Not Booked"):
            print("Room Number --",i+1)
    home()
def report():
    l=len(room)
    print("Room Number ",'\t',"Name")
    for i in range(l):
        if(room[i] == "Booked"):
            print((i+1),'\t\t',details[i+1][0])
    home()
def bill():
    numb=int(input("Enter room Number :"))
    if(room[numb-1] == "Not Booked"):
        print("Wrong Input !!\nPlease try again.")
        bill()
    else:
        print("Number of days stayed:",payment[numb][0]," days")
        print("Total payable amount  Rs:",payment[numb][1])
        room[numb-1]="Not Booked"
        print("Thank You.\nHope you liked our service.\nPlease visit again.")
def cancel():
    numb=int(input("Enter room number :"))
    if(room[numb-1] == "Not Booked"):
        print("This room not booked.")
        cancel()
    room[numb-1]="Not Booked"
    print("Sorry to see you go.\nPlease visit again.")
home()


