#input we need from the user
# total rent
#total food order
# electricity units spend
# charge per unit pre area 
#  
# total amount you have to pay 

rent = int(input("enter your flat rent :"))
food = int(input("enter the ammount of food order"))
electricity_spend = int(input("enter the total of electricity spent"))
area = int(input("enter the charge of your area"))
people = int(input("person in your grp :"))
total_electricity_bill = electricity_spend * area

total_rent = (rent + food + total_electricity_bill) // people
print (total_rent)