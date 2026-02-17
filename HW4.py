web_development=["Raj","Sonia","Rohit"]
data_science=["Rahul","Anjali","Sam"]
ui_ux=["Ravi","Sneha","Amit"]

all_participants=[web_development,data_science,ui_ux]

web_development.append("Atul")
data_science.insert(1,"Riya")
ui_ux.pop()

data_science_new=data_science.copy()
data_science.clear()

print(web_development[0:2])

len_name=[len(participant) for participant in data_science_new ]
print(len_name)

if "Asha" in web_development or "Asha" in ui_ux or "Asha" in data_science_new:
    print("Asha is a participant in the workshop.")
else:    print("Asha is not a participant in the workshop.")

tuple_first=(web_development[0],data_science_new[0],ui_ux[0])
print(tuple_first)
    









