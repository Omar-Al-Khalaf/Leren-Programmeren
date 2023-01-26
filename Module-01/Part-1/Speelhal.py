# ==== Start ==== #

Entry_Cost = 7.45  # Entry cost for 1 person.
Vip_Room = 0.37  # Entry Cost for VIP Room for 1 person for 5 min.
Vip_Room_In_min = 5 # that is the 5 min timeing.
Total_vip_room = Vip_Room / Vip_Room_In_min # that is the resume vip room in 1 min.

# Input
Person = int(input("Welcome to Speelhal : Entre amunt of peapol : "))
Amount_of_Time = int(input("Enter amunt of Time u want in the VIP Room in minuten : (Type (pass) if you dont want to enter VIP room : "))

# logic
Total_Entry = Person * Entry_Cost # this is the total entry for just the person.
Total_Entry_Vip = round (Amount_of_Time * Total_vip_room + Person * Entry_Cost,2) # this is the total entry for just the person + the VIP room time.

# Output
if Amount_of_Time == "pass":
    print(f': you and {Person} people Your Total is : ', Total_Entry)
else:
    print(f': you and {Person} people + {Amount_of_Time} minuten in de VIP-VR-GameSeat : your total is : ',Total_Entry_Vip )

