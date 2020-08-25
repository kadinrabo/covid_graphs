import main_1
import main_2
import main_3
import main_4
import main_5
import main_6

print("""
>
>>
>>>
Welcome to my graphing tool! Let's gather some data first
>>>
>>
>
""")

statistic_choice = input("How many statistics would you like to graph? (1, 2, or 3): ")
if int(statistic_choice) == 1:
	state_choice = input("How many states would you like to graph? (1, 2, or 3): ")
	if int(state_choice) == 1:
		main_1.main()
	elif int(state_choice) == 2:
		main_2.main()
	elif int(state_choice) == 3:
		main_3.main()
elif int(statistic_choice) == 2:
	state_choice = input("How many states would you like to graph? (1, 2, or 3): ")
	if int(state_choice) == 1:
		main_4.main()
	elif int(state_choice) == 2:
		main_6.main()
	elif int(state_choice) == 3:
		print("Functionality not yet available.")
elif int(statistic_choice) == 3:
	state_choice = input("How many states would you like to graph? (1, 2, or 3): ")
	if int(state_choice) == 1:
		main_5.main()
	elif int(state_choice) == 2:
		print("Functionality not yet available.")
	elif int(state_choice) == 3:
		print("Functionality not yet available.")
