temp = int(input("Please enter the current temperature: "))
if temp > 90:
	print("Wear shorts")
elif temp > 70 and temp <= 90:
	print("Short sleeves are fine")
elif temp > 50 and temp <= 70:
	print("Wear a jacket")
elif temp > 32 and temp <= 50:
	print("Wear a heavy coat")
else:
	print("Stay Inside")