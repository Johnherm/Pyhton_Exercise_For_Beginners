# import datetime
# current_datetime = datetime.datetime.now()
# print("Current Date and Time is: ")
# print(current_datetime.strftime("%d-%m-%y"))
# # print(current_datetime.strftime("%H:%M:S"))



import datetime
Date = datetime.datetime.now()
print()
print("Today: ",Date.strftime("%d-%m-%y"))
Time = datetime.datetime.now()
print()
print("Time: " ,Time.strftime("%H:%M:%S"))
