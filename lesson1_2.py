time = int(input("Enter time in sec"))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Time: hh:mm:ss   {hours} : {minutes} : {seconds}"


