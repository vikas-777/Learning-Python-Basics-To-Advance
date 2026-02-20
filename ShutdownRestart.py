import os
# os.system("shutdown /r /t 50")
# os.system("shutdown /s /t 50")


# print("Enter the time in seconds to restart at that sheduled time")
# time1 = int(input("Time in seconds"))
# time2 = "shutdown /r /t "
# time3 = str(time1)
# time4 = time2 + time3
# os.system(time4)





print("Enter the option to perform operation")
print("Enter 1 to shutdown immediately")
print("Enter 2 to restart immediately")
print("Enter 3 to shutdown after given time")
print("Enter 4 to restart after given time")
print("Press any other key to exit from this operations")
Num = int(input("Enter the Number : "))
if Num == 1:
    os.system("Shutdown /s ")
elif Num == 2:
    os.system("Shutdown /r ")
elif Num == 3:
    shut_time = int(input("Enter the time in seconds : "))
    shut_1 = "shutdown /s /t "
    shut_2 = str(shut_time)
    shut3 = shut_1 + shut_2
    os.system(shut3)
elif Num == 4:
    Shut_time1 = int(input("Enter the time in seconds : "))
    time1 = "shutdown /r /t "
    time2 = str(Shut_time1)
    time3 = time1 + time2
    os.system(time3)
else:
    print("You have entered wrong key")
    print("Thank You")


















