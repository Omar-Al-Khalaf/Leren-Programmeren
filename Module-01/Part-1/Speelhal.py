# ==== Start ==== #

Entry_Cost = 7.45  # Entry cost for 1 person.
Vip_Room = 0.37  # Entry Cost for VIP Room for 1 person for 5 min.
Vip_Room_In_min = 5 # that is the 5 min timeing.
Total_vip_room = Vip_Room_In_min / Vip_Room # that is the resume vip room in 1 min.

# Input
Person = int(input("Welcome to Speelhal : Entre amunt of peapol : "))
Amount_of_Time = int(input("Enter amunt of Time u want in the VIP Room in minuten : "))

# logic
# this is the total entry for the person + the VIP room time.
Total_Entry_Vip = round (Amount_of_Time * Total_vip_room + Person * Entry_Cost,2) 

# Output
print(f': you and {Person} people + {Amount_of_Time} minuten in de VIP-VR-GameSeat : your total is : ',Total_Entry_Vip )

